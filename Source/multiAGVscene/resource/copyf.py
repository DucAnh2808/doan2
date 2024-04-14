import shutil

# Đường dẫn của tệp cần sao chép và đổi tên
duong_dan_goc = 'veh11_2.png'

# Đường dẫn mới của tệp sao chép và đổi tên
for i in range (1, 10):
    duong_dan_moi = f'veh{i}_2.png'
    print(duong_dan_moi)
    shutil.copy(duong_dan_goc, duong_dan_moi)