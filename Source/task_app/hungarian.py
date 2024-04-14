import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def hungarian_algorithm(agent_locations, target_locations):
    num_agents = len(agent_locations)
    num_targets = len(target_locations)

    assignments = []
    total_cost = 0

    # Danh sách các target chưa được gán
    unassigned_targets = list(range(num_targets))

    for agent_index, agent_loc in enumerate(agent_locations):
        min_cost = float('inf')
        min_target_index = None

        # Tìm target gần nhất với agent hiện tại
        for target_index in unassigned_targets:
            cost = euclidean_distance(agent_loc, target_locations[target_index])
            if cost < min_cost:
                min_cost = cost
                min_target_index = target_index

        # Gán target cho agent
        target_loc = target_locations[min_target_index]
        assignments.append((agent_loc, target_loc, min_cost))
        total_cost += min_cost

        # Loại bỏ target đã được gán khỏi danh sách
        unassigned_targets.remove(min_target_index)

    return assignments, total_cost

# Đầu vào
agent_locations = [(5, 6), (2, 2), (25,25)]
target_locations = [(1, 1), (1, 3), (2, 4), (3, 2), (4, 4), (10,10), (20,20), (30,30), (40,40)]

# Áp dụng thuật toán Hungarian và in kết quả
assignments, total_cost = hungarian_algorithm(agent_locations, target_locations)
print("Assignments:")
for assignment in assignments:
    print("Agent at", assignment[0], "is assigned to target at", assignment[1], "with cost", assignment[2])
print("Total cost:", total_cost)
