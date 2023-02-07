from mysql.connector import Error
from stored_proc_demo import MysqlDatabaseConnection
class HclStoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata=('pizza',)
            self.cursor.callproc("get_cust_dtls",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj=HclStoredProcedure();
connect_obj.connect("localhost","root","bhagi318","hcl_vij")
connect_obj.execute_str_procedure()
