import mysql.connector
from uagents import Model, Agent, Context
from uagents.setup import fund_agent_if_low
class Activee(Model):
    count: int
    source: str
    dest: str
storag = Agent(
    name="storage agent",
    port=8003,
    seed="storage modification agent",
    endpoint=["http://127.0.0.1:8003/submit"],
)
@storag.on_event("startup")
async def greet(ctx: Context):
    ctx.logger.info("Enter user type : \n1.USER \n2.EMPLOYEE \n3.ADMIN")

db = "testing"
mydb=mysql.connector.connect(host='localhost',user='root',passwd='sahil9087')
mycursor=mydb.cursor()
mycursor = mydb.cursor()
mycursor.execute('use '+db)
xyz=int(input("Enter user type : \n1.USER \n2.EMPLOYEE \n3.ADMIN:"))
if xyz==1:
    tablename2="user"
    from qrtools import QR 
    my_QR = QR(filename = input("enter file path:"))
    my_QR.decode()
    print (my_QR.data)
elif xyz==2:
    tablename2="Bus_count"
elif xyz==3:
    tablename2="Bus_data"
else:
    print("INVALID CHOICE !!!")
