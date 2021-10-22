import gridfs
from email import message
from imbox import Imbox
import pymongo
from pymongo import MongoClient 
import pandas as pd

ls_of_messages = []
download_folder = "C:/Users/sanje/Desktop/Apache Beam/attachment_folders"

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
                # structured_message['attachment'] = message.attachments
                # print(message.attachments)
                if(len(message.attachments) != 0):
                    
                    dwd_path = ''
                    for idx, attachment in enumerate(message.attachments):
                        print('here')
                        att_fn = attachment.get('filename')
                        print(att_fn)
                        download_path = f"{download_folder}/{att_fn}"
                        dwd_path = download_path
                        # print(download_path)
                        with open(download_path, "wb") as fp:
                            fp.write(attachment.get('content').read())
                        
                    connection = MongoClient('localhost', 27017)
                    database = connection['test_file']
                    fs = gridfs.GridFS(database=database)
                    with open(dwd_path, 'rb') as f:
                        contents = f.read()
                        fs.put(contents, filename = str(uid))
                structured_message['body'] = temp
                structured_message['date'] = message.date
                
                ls_of_messages.append(structured_message)

            # print(ls_of_messages[len(ls_of_messages)-1])
            last_ele = ls_of_messages[len(ls_of_messages)-1]
            
            pdfs = fs.find({'filename' : str(b'8424')})

            print(pdfs[0].filename)

            
            # print(ls_of_messages)

check_mail()