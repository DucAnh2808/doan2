from pymongo import MongoClient

# Tạo kết nối đến MongoDB Atlas
client = MongoClient("mongodb+srv://ldanh35:587268@warehouse.nujy3i9.mongodb.net/")

# Chọn cơ sở dữ liệu và bảng
db = client['Warehouse_1']
collection_picking = db['Picking_info']
collection_storage = db['Storage_info']

def create_str_warehouse_1():
    k = 1
    for i in range (1,21): 
        for j in range (1,21):
            new_data = {
                "ID": k,
                "Name": "Str_" + str(k),
                "C_x": i*2,
                "C_y": j*2,
                "Supply" : [],
                "Status": 0
            }
            collection_storage.insert_one(new_data)
            print("vi tri", k)
            k  = k + 1

    # Thêm dữ liệu vào bảng
def update_db():
    collection_storage.update_many({'ID': 0}, {'$push': {'Supply': 'HANG_8'}, '$inc': {'Number supplies': 1}})    #'$inc' làm tăng giá trị trường Number supplies lên 1

def main():
    create_str_warehouse_1()
    
if __name__ == '__main__':
    main()
