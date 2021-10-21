from email import message
from imbox import Imbox
import pymongo
from pymongo import MongoClient 
import pandas as pd

ls_of_messages = []

def check_mail():
    with Imbox(
            'imap.gmail.com',
            username='sanjeetnaik11@gmail.com',
            password='password',
            ssl=True,
            ssl_context=None,
            starttls=False) as imbox:
            sent = 'sanjeet.naik@somaiya.edu'
            inbox_messages_from = imbox.messages(sent_from=sent)

            for uid, message in inbox_messages_from:
                structured_message= {}
                # print(message.body['plain'])
                temp = message.body['plain'][0]
                date = message.date
                temp = temp.replace('\r\n','')
                find = temp.rindex('-- DisclaimerThe')
                temp = temp[:find]
                structured_message['emailid'] = sent
                structured_message['uid'] = str(uid)
                structured_message['subject'] = message.subject
                structured_message['body'] = temp
                structured_message['date'] = message.date
                
                ls_of_messages.append(structured_message)

            # print(ls_of_messages)


def check_database():
    # print('hello')
    connection = MongoClient('localhost',27017)
    conn = connection.Client_Orders
    db = conn.Client_Orders
    data = db.find()
    for item in data:
        pass
        # print(item)

def add_order( order ):
    connection = MongoClient('localhost',27017)
    conn = connection.Client_Orders
    for i in order:
        conn.Client_Orders.insert_one(i)

def check_new_orders():
    ls_of_uids= []
    with Imbox(
            'imap.gmail.com',
            username='sanjeetnaik11@gmail.com',
            password='password',
            ssl=True,
            ssl_context=None,
            starttls=False) as imbox:
            sent = 'sanjeet.naik@somaiya.edu'
            inbox_messages_from = imbox.messages(sent_from=sent)

            for uid, message in inbox_messages_from:
                ls_of_uids.append(str(uid))
            
            # print(ls_of_uids)
            # print('------') 

            existing_uids = []

            connection = MongoClient('localhost',27017)
            conn = connection.Client_Orders
            db = conn.Client_Orders
            data = db.find()
            for item in data:
                # print(item['uid'])
                existing_uids.append(item['uid'])

            # print('------') 
            
            to_add_uid=[]

            for i in ls_of_uids:
                if (str(i) not in existing_uids):
                    to_add_uid.append(i)

            # print(to_add_uid)
            
            # print('------') 
            
            orders = []

            for uid, message in inbox_messages_from:
                if(str(uid) in to_add_uid):
                    structured_message= {}
                    temp = message.body['plain'][0]
                    date = message.date
                    temp = temp.replace('\r\n','')
                    find = temp.rindex('-- DisclaimerThe')
                    temp = temp[:find]
                    structured_message['emailid'] = sent
                    structured_message['uid'] = str(uid)
                    structured_message['subject'] = message.subject
                    structured_message['body'] = temp
                    structured_message['date'] = message.date
                    orders.append(structured_message)
            
            if(len(orders)!=0):
                add_order(orders)
            
            else:
                print('nothing to add')

def check_new_orders_with_user(client_email, password):
    ls_of_uids= []
    with Imbox(
            'imap.gmail.com',
            username=client_email,
            password=password,
            ssl=True,
            ssl_context=None,
            starttls=False) as imbox:
            sent = client_email
            inbox_messages_from = imbox.messages(sent_from=sent)

            for uid, message in inbox_messages_from:
                ls_of_uids.append(str(uid))
            
            # print(ls_of_uids)
            # print('------') 

            existing_uids = []

            connection = MongoClient('localhost',27017)
            conn = connection.Client_Orders
            db = conn.Client_Orders
            data = db.find()
            for item in data:
                # print(item['uid'])
                existing_uids.append(item['uid'])

            # print('------') 
            
            to_add_uid=[]

            for i in ls_of_uids:
                if (str(i) not in existing_uids):
                    to_add_uid.append(i)

            # print(to_add_uid)
            
            # print('------') 
            
            orders = []

            for uid, message in inbox_messages_from:
                if(str(uid) in to_add_uid):
                    structured_message= {}
                    temp = message.body['plain'][0]
                    date = message.date
                    temp = temp.replace('\r\n','')
                    find = temp.rindex('-- DisclaimerThe')
                    temp = temp[:find]
                    structured_message['emailid'] = sent
                    structured_message['uid'] = str(uid)
                    structured_message['subject'] = message.subject
                    structured_message['body'] = temp
                    structured_message['date'] = message.date
                    orders.append(structured_message)
            
            if(len(orders)!=0):
                add_order(orders)
            
            else:
                print('nothing to add')



            # if(len(existing_uids)!=0):
            #     add_order(existing_uids)               

check_new_orders()
    

            