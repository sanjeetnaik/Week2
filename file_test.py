from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

database = connection['test_file']

import gridfs

fs = gridfs.GridFS(database=database)

# file = 'example.pdf'

# with open(file, 'rb') as f:
#     contents = f.read()

# fs.put(contents, filename = 'example.pdf')

pdfs = fs.find()

print(pdfs[0].filename)
print(pdfs[1].filename)