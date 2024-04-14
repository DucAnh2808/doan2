from pymongo import MongoClient
import random
# Tạo kết nối đến MongoDB Atlas
client = MongoClient("mongodb+srv://ldanh35:587268@warehouse.nujy3i9.mongodb.net/")

# Chọn cơ sở dữ liệu và bảng
db = client['Warehouse_1']
collection_picking = db['Picking_info']
collection_storage = db['Storage_info']
collection_Tasklist = db['Task_list']
collection_Tasklist_2  = db['task_testapp']

def task_assignment():


    picking_document = collection_picking.find_one({'ID': 0})
    storage_document = collection_storage.find_one({'ID': 0})
    
    a, b = storage_document['C_x'], storage_document['C_y']
    c, d = picking_document['C_x'], picking_document['C_y']
    #     print(doc)
    task = (a, b, c, d)
    doc = {
        "ID": 0,
        "Name": "Task_0",
        "Info": task,
        "Prioritize": 0,
        "Status": 0
    }
    
    collection_Tasklist.insert_one(doc)
    
def create_random_100():
    storage_documents = list(collection_storage.find({"Name": {"$regex": "^Str_"}}))
    picking_documents = list(collection_picking.find({"Name": {"$regex": "^Pic_"}}))
    tasks = []
    k = 1
    for _ in range(100):
        storage_document = random.choice(storage_documents)
        picking_document = random.choice(picking_documents)

        # Extract the values
        a, b = storage_document['C_x'], storage_document['C_y']
        c, d = picking_document['C_x'], picking_document['C_y']
        # Create the task
        task = (a, b, c, d)
        doc = {
            "ID": k,
            "Name": "Task_" + str(k),
            "Info": task,
            "Prioritize": 0,
            "Status": 0
        }
        collection_Tasklist.insert_one(doc)
        print("Inserted: ", k)
        k = k + 1
    
def get_task():
    task = collection_Tasklist.find_one({'Name': "Task_0"})
    return task['Info']
    
def get_info_values(collection):
    docs = collection.find()

    info_values = []

    for doc in docs:
        info_values.append(doc['Info'])

    return info_values

    
def end_task(s_x,s_y,p_x,p_y):
    info_value = (s_x,s_y,p_x,p_y)
    print(info_value)
    docs = collection_Tasklist.find({'Info': info_value})
    for doc in docs:
        collection_Tasklist.update_one({'_id': doc['_id']}, {'$set': {'Status': 1}})
    
def main():
    create_random_100()
    
if __name__ == '__main__':
    main()
