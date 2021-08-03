from MysqlClass import Mysql


class checking:
    def checkmain(self):
        self.x = Mysql()
        self.x.drop_database("Tanay")
        return
 
k = checking()
k.checkmain()