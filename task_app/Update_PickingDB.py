from pymongo import MongoClient

# Tạo kết nối đến MongoDB Atlas
client = MongoClient("mongodb+srv://ldanh35:587268@warehouse.nujy3i9.mongodb.net/")

# Chọn cơ sở dữ liệu và bảng
db = client['Warehouse_1']
collection_picking = db['Picking_info']

def create_pick_warehouse_1():
    
    for i in range (1,20): 
        new_data = {
            "ID": i,
            "Name": "Pic_" + str(i),
            "C_x": i*2,
            "C_y": 46,
            "Supply" : [],
            "Status": 0
        }
        collection_picking.insert_one(new_data)
        print("Inserted: ", i)

def update_db():
    collection_picking.update_one({'ID': 0}, {'$push': {'Supply': 'item5'}})
    
def main():
    create_pick_warehouse_1()
    
if __name__ == '__main__':
    main()
