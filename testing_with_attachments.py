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
            ls_of_messages= []
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
                structured_message['attachment'] = 'None'
                structured_message['body'] = temp
                structured_message['date'] = message.date
                
                ls_of_messages.append(structured_message)

            print(ls_of_messages[len(ls_of_messages)-2])
            last_ele = ls_of_messages[len(ls_of_messages)-1]

            
            # print(ls_of_messages)

check_mail()

