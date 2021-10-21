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
                structured_message['attachments'] = message.attachments
                
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