import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Sanjeet1402",
  database = 'orders_clients'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM clients_info")

myresult = mycursor.fetchall()

ls_of_clients = []

for i in myresult:
    ls_of_clients.append(i[1])


def add_client():
    tclient_email = 'sanjeet.naik@somaiya.edu'
    tclient_phone = '9930974085'
    tclient_address = '177A Bleecker Street'
    tclient_company =  'Nekay'

    if(tclient_email in ls_of_clients):
        print("Client Already Exists !!!!")
    
    else:
        sql = "INSERT INTO clients_info (client_email, client_phone, client_address, client_company) VALUES (%s, %s, %s, %s)"
        val = (tclient_email, tclient_phone, tclient_address, tclient_company)
        mycursor.execute(sql, val)

        print(mycursor.rowcount, "was inserted.")

        mydb.commit()

def see_clients():
    count =1
    for i in myresult:
        print("Client "+str(count), end = " : ")
        print(i)
        count+=1

add_client()
# see_clients()

