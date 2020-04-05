from pymongo import MongoClient

from random import randint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db=db.messages ##тут пока не разобарлся до конца
#Step 2: Create sample data
name = ['','','', '', '','','', '','', '','','', '']
text = ['','','','']
time = ['', '', '', '', '', '', '', '']
for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(name)-1))] + ' ' + name[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'text' : randint(1, 5),
        'time' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=db.messages.insert_one() #открытый вопрос
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')
