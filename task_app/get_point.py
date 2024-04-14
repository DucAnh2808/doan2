import random
from pymongo import MongoClient
dim_5 = 31
dim_6 = 15

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

    def get_random_agent_points(self, num_agents):
        agent_points = []
        zero_points = [(i, j) for i, row in enumerate(self.MatrixLayout) for j, point in enumerate(row) if point == 0]
        while len(agent_points) < num_agents:
            random_point = random.choice(zero_points)
            zero_points.remove(random_point)
            # Increase the value of i and j by 1
            agent_points.append((random_point[0] + 1, random_point[1] + 1))
        return agent_points
    
    def get_all_one_points(self):
        one_points = [(i + 1, j + 1) for i, row in enumerate(self.MatrixLayout) for j, point in enumerate(row) if point == 1.000]
        return one_points
    

storage_locations = [(2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (2, 12), (2, 14), (2, 16), (2, 18), (2, 20), (2, 22), (2, 24), (2, 26), (2, 28), (2, 30), (4, 2), (4, 4), (4, 6), (4, 8), (4, 10), (4, 12), (4, 14), (4, 16), (4, 18), (4, 20), (4, 22), (4, 24), (4, 26), (4, 28), (4, 30), (6, 2), (6, 4), (6, 6), (6, 8), (6, 10), (6, 12), (6, 14), (6, 16), (6, 18), (6, 20), (6, 22), (6, 24), (6, 26), (6, 28), (6, 30), (8, 2), (8, 4), (8, 6), (8, 8), (8, 10), (8, 12), (8, 14), (8, 16), (8, 18), (8, 20), (8, 22), (8, 24), (8, 26), (8, 28), (8, 30), (10, 2), (10, 4), (10, 6), (10, 8), (10, 10), (10, 12), (10, 14), (10, 16), (10, 18), (10, 20), (10, 22), (10, 24), (10, 26), (10, 28), (10, 30), (12, 2), (12, 4), (12, 6), (12, 8), (12, 10), (12, 12), (12, 14), (12, 16), (12, 18), (12, 20), (12, 22), (12, 24), (12, 26), (12, 28), (12, 30), (14, 2), (14, 4), (14, 6), (14, 8), (14, 10), (14, 12), (14, 14), (14, 16), (14, 18), (14, 20), (14, 22), (14, 24), (14, 26), (14, 28), (14, 30), (16, 2), (16, 4), (16, 6), (16, 8), (16, 10), (16, 12), (16, 14), (16, 16), (16, 18), (16, 20), (16, 22), (16, 24), (16, 26), (16, 28), (16, 30), (18, 2), (18, 4), (18, 6), (18, 8), (18, 10), (18, 12), (18, 14), (18, 16), (18, 18), (18, 20), (18, 22), (18, 24), (18, 26), (18, 28), (18, 30), (20, 2), (20, 4), (20, 6), (20, 8), (20, 10), (20, 12), (20, 14), (20, 16), (20, 18), (20, 20), (20, 22), (20, 24), (20, 26), (20, 28), (20, 30), (22, 2), (22, 4), (22, 6), (22, 8), (22, 10), (22, 12), (22, 14), (22, 16), (22, 18), (22, 20), (22, 22), (22, 24), (22, 26), (22, 28), (22, 30), (24, 2), (24, 4), (24, 6), (24, 8), (24, 10), (24, 12), (24, 14), (24, 16), (24, 18), (24, 20), (24, 22), (24, 24), (24, 26), (24, 28), (24, 30), (26, 2), (26, 4), (26, 6), (26, 8), (26, 10), (26, 12), (26, 14), (26, 16), (26, 18), (26, 20), (26, 22), (26, 24), (26, 26), (26, 28), (26, 30), (28, 2), (28, 4), (28, 6), (28, 8), (28, 10), (28, 12), (28, 14), (28, 16), (28, 18), (28, 20), (28, 22), (28, 24), (28, 26), (28, 28), (28, 30)]
picking_locations = [(34, 2), (34, 4), (34, 6), (34, 8), (34, 10), (34, 12), (34, 14), (34, 16), (34, 18), (34, 20), (34, 22), (34, 24), (34, 26), (34, 28), (34, 30)]

def create_tasks_for_all_storage_locations(storage_locations, picking_locations):
    tasks = []
    for storage_location in storage_locations:
        picking_location = random.choice(picking_locations)
        tasks.append((storage_location, picking_location))
    return tasks

def main():
    layout = layout_5()
    print(layout.get_random_agent_points(20))
    # agent_points = layout.get_all_one_points()
    # print(create_tasks_for_all_storage_locations(storage_locations, picking_locations))

if __name__ == "__main__":
    main()