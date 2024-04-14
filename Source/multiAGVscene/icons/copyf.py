import shutil

# Đường dẫn của tệp cần sao chép và đổi tên
duong_dan_goc = 'ccc.png'

# Đường dẫn mới của tệp sao chép và đổi tên
for i in range (1, 100):
    duong_dan_moi = f'veh{i}_1.png'
    print(duong_dan_moi)
    shutil.copy(duong_dan_goc, duong_dan_moi)