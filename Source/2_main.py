import os
from multiAGVscene.Layout import Layout  # layout
from multiAGVscene.Explorer_taskAssign import Explorer  # explorer

# from multiAGVscene.Explorer_test import Explorer  # explorer
from multiAGVscene.Scene_test import Scene  # Scene
from algorithm.MADQN_structure.Controller import MADQNAgentController as modelController
# from task_app.task_assignment import task_assignment, get_info_values 
import numpy as np

def main():
    dim = 7
    ss_x_width, ss_y_width, ss_x_num, ss_y_num, ps_num = 1, 1, 4, 4, 4
    layout_lists = [layout_5_2.MatrixLayout]  # Add your layouts here
    # task_list = None
    task_list =[(24, 16, 14, 34, 'veh1'), (2, 6, 24, 34, 'veh2'), (12, 28, 6, 34, 'veh3'), (28, 20, 6, 34, 'veh4'), (30, 2, 16, 34, 'veh5'), (12, 6, 26, 34, 'veh6'), (18, 28, 8, 34, 'veh7'), (16, 16, 26, 34, 'veh8'), (20, 24, 10, 34, 'veh9'), (6, 16, 24, 34, 'veh10'), (2, 10, 10, 34, 'veh11'), (22, 4, 8, 34, 'veh12'), (18, 16, 28, 34, 'veh13'), (26, 28, 20, 34, 'veh14'), (4, 2, 30, 34, 'veh15'), (4, 6, 28, 34, 'veh16'), (28, 4, 24, 34, 'veh17'), (2, 22, 16, 34, 'veh18'), (16, 18, 10, 34, 'veh19'), (20, 28, 8, 34, 'veh20'), (24, 14, 18, 34, 'veh1'), (2, 4, 20, 34, 'veh2'), (12, 26, 6, 34, 'veh3'), (28, 18, 24, 34, 'veh4'), (28, 2, 2, 34, 'veh5'), (12, 4, 2, 34, 'veh6'), (18, 26, 10, 34, 'veh7'), (16, 14, 30, 34, 'veh8'), (20, 22, 4, 34, 'veh9'), (6, 14, 16, 34, 'veh10'), (2, 8, 10, 34, 'veh11'), (22, 2, 26, 34, 'veh12'), (18, 14, 22, 34, 'veh13'), (26, 26, 18, 34, 'veh14'), (2, 2, 24, 34, 'veh15'), (4, 4, 6, 34, 'veh16'), (26, 4, 10, 34, 'veh17'), (2, 20, 12, 34, 'veh18'), (14, 18, 24, 34, 'veh19'), (20, 26, 10, 34, 'veh20'), (24, 12, 30, 34, 'veh1'), (6, 4, 16, 34, 'veh2'), (12, 24, 26, 34, 'veh3'), (28, 16, 22, 34, 'veh4'), (26, 2, 18, 34, 'veh5'), (12, 2, 26, 34, 'veh6'), (18, 24, 28, 34, 'veh7'), (16, 12, 26, 34, 'veh8'), (20, 20, 4, 34, 'veh9'), (6, 12, 12, 34, 'veh10'), (4, 8, 26, 34, 'veh11'), (20, 2, 18, 34, 'veh12'), (18, 12, 24, 34, 'veh13'), (26, 24, 20, 34, 'veh14'), (6, 2, 28, 34, 'veh15'), (8, 4, 30, 34, 'veh16'), (24, 4, 26, 34, 'veh17'), (2, 18, 8, 34, 'veh18'), (14, 16, 24, 34, 'veh19'), (22, 26, 24, 34, 'veh20'), (24, 10, 8, 34, 'veh1'), (6, 6, 26, 34, 'veh2'), (12, 22, 20, 34, 'veh3'), (28, 14, 4, 34, 'veh4'), (24, 2, 12, 34, 'veh5'), (10, 2, 4, 34, 'veh6'), (18, 22, 2, 34, 'veh7'), (16, 10, 22, 34, 'veh8'), (20, 18, 4, 34, 'veh9'), (6, 10, 24, 34, 'veh10'), (6, 8, 24, 34, 'veh11'), (18, 2, 24, 34, 'veh12'), (18, 10, 26, 34, 'veh13'), (26, 22, 8, 34, 'veh14'), (8, 2, 20, 34, 'veh15'), (10, 4, 22, 34, 'veh16'), (24, 6, 26, 34, 'veh17'), (2, 16, 14, 34, 'veh18'), (14, 14, 16, 34, 'veh19'), (22, 24, 10, 34, 'veh20'), (24, 8, 26, 34, 'veh1'), (8, 6, 20, 34, 'veh2'), (12, 20, 6, 34, 'veh3'), (28, 12, 28, 34, 'veh4'), (20, 4, 4, 34, 'veh5'), (14, 2, 8, 34, 'veh6'), (18, 20, 4, 34, 'veh7'), (16, 8, 16, 34, 'veh8'), (20, 16, 30, 34, 'veh9'), (4, 10, 20, 34, 'veh10'), (8, 8, 10, 34, 'veh11'), (16, 2, 14, 34, 'veh12'), (18, 8, 10, 34, 'veh13'), (26, 20, 10, 34, 'veh14'), (10, 6, 30, 34, 'veh15'), (14, 4, 26, 34, 'veh16'), (22, 6, 16, 34, 'veh17'), (2, 14, 24, 34, 'veh18'), (14, 12, 20, 34, 'veh19'), (22, 22, 30, 34, 'veh20'), (22, 8, 20, 34, 'veh1'), (10, 8, 30, 34, 'veh2'), (12, 18, 8, 34, 'veh3'), (28, 10, 12, 34, 'veh4'), (18, 4, 24, 34, 'veh5'), (14, 6, 22, 34, 'veh6'), (18, 18, 22, 34, 'veh7'), (16, 6, 30, 34, 'veh8'), (20, 14, 24, 34, 'veh9'), (4, 12, 16, 34, 'veh10'), (8, 10, 28, 34, 'veh11'), (16, 4, 14, 34, 'veh12'), (18, 6, 18, 34, 'veh13'), (26, 18, 28, 34, 'veh14'), (12, 8, 24, 34, 'veh15'), (14, 8, 4, 34, 'veh16'), (20, 6, 26, 34, 'veh17'), (2, 12, 12, 34, 'veh18'), (14, 10, 2, 34, 'veh19'), (22, 20, 18, 34, 'veh20'), (22, 10, 10, 34, 'veh1'), (10, 10, 14, 34, 'veh2'), (12, 16, 6, 34, 'veh3'), (28, 8, 20, 34, 'veh4'), (20, 8, 26, 34, 'veh5'), (12, 10, 12, 34, 'veh6'), (22, 18, 30, 34, 'veh7'), (20, 10, 30, 34, 'veh8'), (22, 14, 10, 34, 'veh9'), (4, 14, 12, 34, 'veh10'), (8, 12, 8, 34, 'veh11'), (26, 6, 16, 34, 'veh12'), (20, 12, 14, 34, 'veh13'), (26, 16, 30, 34, 'veh14'), (12, 12, 18, 34, 'veh15'), (10, 12, 28, 34, 'veh16'), (26, 8, 2, 34, 'veh17'), (4, 16, 26, 34, 'veh18'), (12, 14, 28, 34, 'veh19'), (24, 20, 20, 34, 'veh20'), (22, 12, 16, 34, 'veh1'), (10, 14, 10, 34, 'veh2'), (10, 16, 26, 34, 'veh3'), (30, 8, 28, 34, 'veh4'), (30, 10, 16, 34, 'veh5'), (8, 14, 4, 34, 'veh6'), (24, 18, 28, 34, 'veh7'), (26, 10, 26, 34, 'veh8'), (22, 16, 14, 34, 'veh9'), (4, 18, 12, 34, 'veh10'), (8, 16, 18, 34, 'veh11'), (28, 6, 14, 34, 'veh12'), (26, 12, 24, 34, 'veh13'), (26, 14, 22, 34, 'veh14'), (10, 18, 2, 34, 'veh15'), (8, 18, 2, 34, 'veh16'), (30, 6, 16, 34, 'veh17'), (6, 18, 16, 34, 'veh18'), (10, 20, 28, 34, 'veh19'), (24, 22, 24, 34, 'veh20'), (16, 22, 12, 34, 'veh1'), (14, 20, 20, 34, 'veh2'), (10, 22, 18, 34, 'veh3'), (30, 18, 8, 34, 'veh4'), (30, 14, 22, 34, 'veh5'), (6, 20, 22, 34, 'veh6'), (24, 24, 10, 34, 'veh7'), (30, 16, 20, 34, 'veh8'), (16, 20, 6, 34, 'veh9'), (4, 20, 10, 34, 'veh10'), (8, 22, 16, 34, 'veh11'), (28, 22, 24, 34, 'veh12'), (30, 12, 24, 34, 'veh13'), (30, 20, 20, 34, 'veh14'), (10, 24, 6, 34, 'veh15'), (8, 20, 28, 34, 'veh16'), (30, 4, 6, 34, 'veh17'), (6, 22, 20, 34, 'veh18'), (14, 22, 12, 34, 'veh19'), (24, 26, 18, 34, 'veh20'), (16, 24, 30, 34, 'veh1'), (14, 24, 26, 34, 'veh2'), (10, 26, 18, 34, 'veh3'), (30, 22, 24, 34, 'veh4'), (30, 24, 8, 34, 'veh5'), (6, 24, 22, 34, 'veh6'), (24, 28, 12, 34, 'veh7'), (30, 26, 6, 34, 'veh8'), (16, 26, 20, 34, 'veh9'), (4, 22, 8, 34, 'veh10'), (8, 24, 20, 34, 'veh11'), (28, 24, 26, 34, 'veh12'), (28, 26, 22, 34, 'veh13'), (30, 28, 24, 34, 'veh14'), (10, 28, 6, 34, 'veh15'), (8, 26, 24, 34, 'veh16'), (28, 28, 8, 34, 'veh17'), (4, 24, 20, 34, 'veh18'), (14, 26, 26, 34, 'veh19'), (22, 28, 26, 34, 'veh20'), (4, 26, 20, 34, 'veh1'), (14, 28, 12, 34, 'veh2'), (6, 26, 22, 34, 'veh3'), (8, 28, 2, 34, 'veh4'), (6, 28, 8, 34, 'veh5'), (2, 24, 20, 34, 'veh6'), (16, 28, 4, 34, 'veh7'), (4, 28, 30, 34, 'veh8'), (2, 26, 18, 34, 'veh9'), (2, 28, 14, 34, 'veh10')]

    case_num = [20]
    k = 1
    agent_locations = [(16, 25), (7, 3), (28, 13), (20, 29), (1, 30), (7, 13), (29, 19), (17, 17), (25, 21), (17, 6), (10, 3), (5, 22), (17, 18), (30, 26), (2, 5), (6, 3), (5, 28), (23, 2), (18, 17), (31, 19)]

    for explorer_num in case_num:
        for layout_list in layout_lists:
            
            print("Case: ", explorer_num)
            print("truong hop: ", k)
            k += 1
            layout = Layout(storage_station_x_width=ss_x_width, storage_station_y_width=ss_y_width,
                            storage_station_x_num=ss_x_num, storage_station_y_num=ss_y_num,
                            picking_station_number=ps_num, layout_list=layout_list, task_list=task_list)
            explorer_group = []
            for i in range(explorer_num):
                start_position = agent_locations[i]
                veh_name = "veh" + str(i + 1)
                explorer = Explorer(layout, veh_name=veh_name, icon_name=veh_name, start_position=start_position)
                explorer_group.append(explorer)
            """ 3. create scene """
            multi_agv_scene = Scene(layout, explorer_group)

            control_type = {0: "train_NN", 1: "use_NN", 2: "A_star", 3:"Manual"}
            control_mode = 1

            if control_mode in [2, 3]:
                multi_agv_scene.run_game(control_pattern=control_type[control_mode])
            if control_mode in [0, 1]:
                map_xdim = layout.scene_x_width
                map_ydim = layout.scene_y_width
                print(map_xdim)
                print(map_ydim)
                max_task = len(layout.storage_station_list)
                agent = modelController(multi_agv_scene, map_xdim = dim, map_ydim = dim, max_task=max_task,
                                        control_mode=control_type[control_mode], state_number=3)
                agent.model_run()

dim_x3 = 10
dim_4 = 4
dim_5 = 31
dim_6 = 15
# dim_5 = 51
# dim_6 = 20  

class layout_4():
    MatrixPicking = []
    for i in range(0, dim_x3):
        if i % 4 == 1 or i % 4 == 2:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_x3):
        if i % 4 == 1:
            MatrixStorage.append(1.000)
        elif i%4 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)

    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0, dim_x3 - 1):
        MatrixZ.append(0.000)

    MatrixStorage2 = []
    for i in range (0, 3):
        MatrixStorage2.append(MatrixStorage)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    
    MatrixLayout = MatrixLayout + MatrixStorage2
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)    
    MatrixLayout.append(MatrixPicking)

class layout_5():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_5_2():
    dim_5 = 31
    dim_6 = 15
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    


class layout_6():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 3 == 1:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 3 == 0:
            MatrixStorage.append(0.000)
        else:
            MatrixStorage.append(1.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)
        
    MatrixLayout = []
    MatrixLayout.append(MatrixPicking)    
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)

    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_7():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 3 == 1 or i % 3 == 2:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 3 == 1 or i % 3 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)
        
    # MatrixStorage2 = []
    # for i in range (0, 5):
    #     MatrixStorage2.append(MatrixStorage)
    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_8():
    MatrixPicking = []
    for i in range(0, dim_x3):
        if i % 3 == 0:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_x3):
        if i % 3 == 1 or i % 3 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)

    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0, dim_x3 - 1):
        MatrixZ.append(0.000)

    MatrixStorage2 = []
    for i in range (0, 2):
        MatrixStorage2.append(MatrixStorage)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    
    for i in range (1, dim_4):
        MatrixLayout = MatrixLayout + MatrixStorage2
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)    
    MatrixLayout.append(MatrixPicking)
    print("x: ",len(MatrixLayout[0]))
    print("y: ",len(MatrixLayout))


def task():
    task_list = [(9, 2, 4, 13), (4, 3, 10, 13), (11, 8, 4, 13), (12, 2, 4, 13), (2, 2, 10, 13), (8, 6, 10, 13), (
    11, 11, 10, 13), (12, 9, 4, 13), (3, 8, 4, 13), (3, 11, 4, 13), (9, 10, 4, 13), (10, 3, 4, 13), (6, 11, 10, 13), (
                    3, 9, 10, 13), (12, 6, 10, 13), (9, 8, 4, 13), (2, 3, 10, 13), (12, 5, 4, 13), (9, 11, 4, 13), (
                    8, 11, 4, 13), (5, 2, 10, 13), (2, 6, 10, 13), (11, 5, 10, 13), (2, 5, 4, 13), (5, 10, 4, 13), (
                    11, 9, 4, 13), (5, 8, 4, 13), (10, 2, 4, 13), (4, 2, 4, 13), (5, 3, 4, 13), (2, 9, 10, 13), (
                    11, 3, 10, 13), (11, 2, 4, 13), (3, 5, 4, 13), (6, 2, 4, 13), (3, 2, 4, 13), (8, 8, 10, 13), (
                    2, 8, 4, 13), (6, 8, 4, 13), (5, 7, 4, 13), (8, 7, 4, 13), (6, 6, 10, 13), (8, 2, 4, 13), (
                    6, 9, 4, 13), (5, 11, 10, 13), (12, 3, 4, 13), (6, 10, 4, 13), (12, 8, 10, 13), (8, 10, 10, 13), (
                    9, 9, 4, 13), (4, 5, 10, 13), (11, 6, 4, 13), (3, 6, 4, 13), (10, 5, 10, 13), (8, 9, 10, 13), (
                    5, 9, 4, 13), (3, 3, 10, 13), (9, 7, 4, 13), (2, 11, 10, 13), (6, 7, 4, 13), (9, 3, 4, 13), (
                    12, 11, 4, 13)]
    return task_list
if __name__ == '__main__':
    main()