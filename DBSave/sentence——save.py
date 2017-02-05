import time

from DataAnalyse.valueProcessing.propertyValueModify import PropertyValueModify
from Lib.Currency.ThreadingPool import ThreadingPool
from Lib.DBConnection.OracleConnection import OracleConnection


class SentenceSave(OracleConnection):
    def __init__(self):
        super().__init__()

    def get_component(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "select cc_code,cc_b2c_brid,cc_b2c_kiid from product$component_crawl where cc_task=7777777 and cc_b2c_brid is not null and cc_b2c_kiid is not null and cc_uuid is null")
        i = 0
        while True:
            i += 1
            if i % 100 == 0:
                self.conn.commit()
            print(i)
            row = cursor.fetchone()
            if row is None:
                break
            cc_code = row[0]
            cc_b2c_brid = row[1]
            cc_b2c_kiid = row[2]
            component = self.find_component(cc_b2c_brid, cc_code)
            if component:
                uuid = component[-1]
                self.update_crawl_uuid(uuid=uuid, code=cc_code)
                continue
            else:
                uuid = self.make_uuid(cc_b2c_kiid)
            component_id = self.save_to_component(cc_code, cc_b2c_kiid, cc_b2c_brid, uuid)
            self.update_crawl_uuid(uuid=uuid, code=cc_code)

    def get_component2(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "select cc_code,cc_b2c_brid,cc_b2c_kiid from product$component_crawl where cc_task=7777777 and cc_b2c_brid is not null and cc_b2c_kiid is not null and cc_uuid is null and rownum<10000")
        i = 0
        rows = cursor.fetchall()
        cursor.close()
        return rows

        self.conn.commit()


    def thread_go(self, row):
        conn = super().conn
        cc_code = row[0]
        cc_b2c_brid = row[1]
        cc_b2c_kiid = row[2]
        print("go")
        component = self.find_component(cc_b2c_brid, cc_code)
        if component:
            uuid = self.make_uuid(cc_b2c_kiid)
            self.update_crawl_uuid(uuid=uuid, code=cc_code)
            return
        else:
            uuid = self.make_uuid(cc_b2c_kiid)
        component_id = self.save_to_component(cc_code, cc_b2c_kiid, cc_b2c_brid, uuid)
        self.update_crawl_uuid(uuid=uuid, code=cc_code)

    # 更新爬虫表的uuid
    def update_crawl_uuid(self, uuid, code, taskid=7777777):
        cursor = self.conn.cursor()
        cursor.execute(
            "update product$component_crawl set cc_uuid='{}' where cc_task={} and cc_code='{}'".format(
                uuid, taskid, code))
        cursor.close()

    # 查询正式数据库中是否存在同品牌同型号器件
    def find_component(self, brid, code):
        cursor = self.conn.cursor()
        cursor.execute("select * from product$component where cmp_brid={} and cmp_code='{}'".format(brid, code))
        component = cursor.fetchone()
        cursor.close()
        return component

    # 如果不存在，则重新生成uuid
    def make_uuid(self, kiid):
        cursor = self.conn.cursor()
        cursor.execute("select ki_cmpprefix,ki_cmpsuffix from product$kind where ki_id={}".format(kiid))
        data = cursor.fetchone()
        cursor.execute(
            "update product$kind k set ki_count=(k.ki_count+1),ki_cmpsuffix=(k.ki_cmpsuffix+1) where ki_id={}".format(
                kiid))
        cursor.close()
        cmpprefix = data[0]
        cmpsuffix = data[1]
        lenth = 16 - len(cmpprefix) - len(str(cmpsuffix))
        uuid = cmpprefix + '0' * lenth + str(cmpsuffix)
        return uuid

    # 将新器件信息存入正式数据库
    def save_to_component(self, code, kiid, brid, cmp_uuid, version=1):
        cursor = self.conn.cursor()
        cursor.execute(
            "select to_timestamp(to_char(sysdate, 'yyyy-mm-dd hh24:mi:ss'),'YYYY-MM-DD HH24:MI:SS')  from dual")
        modify_time = cursor.fetchone()[0]

        define_time = modify_time
        cursor = self.conn.cursor()
        cursor.execute("select product$component_seq.nextval from dual")
        component_id = cursor.fetchone()[0]
        cursor.execute(
            "insert into product$component(cmp_id, cmp_code,cmp_unit,cmp_version,cmp_kiid,cmp_brid,cmp_uuid,cmp_createtime,cmp_modifytime) values({},'{}','PCS',{},{},{},'{}',to_timestamp('{}','YYYY-MM-DD HH24:MI:SS'),to_timestamp('{}','YYYY-MM-DD HH24:MI:SS'))".format(
                component_id, code, version, kiid, brid, cmp_uuid, define_time, modify_time))
        cursor.close()
        return component_id

if __name__ == "__main__":
    while True:
        sentence_save = SentenceSave()
        rows = sentence_save.get_component()
        # if len(rows) == 0:
        #     break
        # threadingpool = ThreadingPool()
        # threadingpool.multi_process(sentence_save.thread_go, rows)
        # sentence_save.conn.commit()