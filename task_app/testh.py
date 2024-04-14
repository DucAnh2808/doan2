import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist


class Task_allocation:
    
    def __init__(self):
        self.agent_locations = [(16, 25), (7, 3), (28, 13), (20, 29), (1, 30), (7, 13), (29, 19), (17, 17), (25, 21), (17, 6), (10, 3), (5, 22), (17, 18), (30, 26), (2, 5), (6, 3), (5, 28), (23, 2), (18, 17), (31, 19)]
        self.task_lists = [((2, 2), (34, 24)), ((2, 4), (34, 30)), ((2, 6), (34, 28)), ((2, 8), (34, 20)), ((2, 10), (34, 4)), ((2, 12), (34, 26)), ((2, 14), (34, 8)), ((2, 16), (34, 14)), ((2, 18), (34, 24)), ((2, 20), (34, 18)), ((2, 22), (34, 26)), ((2, 24), (34, 12)), ((2, 26), (34, 18)), ((2, 28), (34, 2)), ((2, 30), (34, 16)), ((4, 2), (34, 20)), ((4, 4), (34, 6)), ((4, 6), (34, 16)), ((4, 8), (34, 30)), ((4, 10), (34, 22)), ((4, 12), (34, 2)), ((4, 14), (34, 26)), ((4, 16), (34, 14)), ((4, 18), (34, 24)), ((4, 20), (34, 4)), ((4, 22), (34, 8)), ((4, 24), (34, 26)), ((4, 26), (34, 10)), ((4, 28), (34, 24)), ((4, 30), (34, 6)), ((6, 2), (34, 24)), ((6, 4), (34, 28)), ((6, 6), (34, 26)), ((6, 8), (34, 20)), ((6, 10), (34, 30)), ((6, 12), (34, 26)), ((6, 14), (34, 22)), ((6, 16), (34, 30)), ((6, 18), (34, 18)), ((6, 20), (34, 26)), ((6, 22), (34, 16)), ((6, 24), (34, 26)), ((6, 26), (34, 16)), ((6, 28), (34, 14)), ((6, 30), (34, 16)), ((8, 2), (34, 10)), ((8, 4), (34, 26)), ((8, 6), (34, 24)), ((8, 8), (34, 10)), ((8, 10), (34, 30)), ((8, 12), (34, 24)), ((8, 14), (34, 4)), ((8, 16), (34, 16)), ((8, 18), (34, 10)), ((8, 20), (34, 26)), ((8, 22), (34, 20)), ((8, 24), (34, 26)), ((8, 26), (34, 2)), ((8, 28), (34, 20)), ((8, 30), (34, 28)), ((10, 2), (34, 10)), ((10, 4), (34, 20)), ((10, 6), (34, 24)), ((10, 8), (34, 28)), ((10, 10), (34, 14)), ((10, 12), (34, 12)), ((10, 14), (34, 2)), ((10, 16), (34, 22)), ((10, 18), (34, 26)), ((10, 20), (34, 30)), ((10, 22), (34, 10)), ((10, 24), (34, 8)), ((10, 26), (34, 26)), ((10, 28), (34, 12)), ((10, 30), (34, 16)), ((12, 2), (34, 12)), ((12, 4), (34, 16)), ((12, 6), (34, 12)), ((12, 8), (34, 8)), ((12, 10), (34, 28)), ((12, 12), (34, 18)), ((12, 14), (34, 20)), ((12, 16), (34, 26)), ((12, 18), (34, 24)), ((12, 20), (34, 14)), ((12, 22), (34, 16)), ((12, 24), (34, 30)), ((12, 26), (34, 24)), ((12, 28), (34, 28)), ((12, 30), (34, 24)), ((14, 2), (34, 24)), ((14, 4), (34, 12)), ((14, 6), (34, 16)), ((14, 8), (34, 4)), ((14, 10), (34, 10)), ((14, 12), (34, 28)), ((14, 14), (34, 16)), ((14, 16), (34, 30)), ((14, 18), (34, 22)), ((14, 20), (34, 24)), ((14, 22), (34, 10)), ((14, 24), (34, 18)), ((14, 26), (34, 22)), ((14, 28), (34, 4)), ((14, 30), (34, 22)), ((16, 2), (34, 14)), ((16, 4), (34, 26)), ((16, 6), (34, 24)), ((16, 8), (34, 18)), ((16, 10), (34, 26)), ((16, 12), (34, 6)), ((16, 14), (34, 24)), ((16, 16), (34, 26)), ((16, 18), (34, 28)), ((16, 20), (34, 30)), ((16, 22), (34, 14)), ((16, 24), (34, 14)), ((16, 26), (34, 30)), ((16, 28), (34, 22)), ((16, 30), (34, 20)), ((18, 2), (34, 8)), ((18, 4), (34, 12)), ((18, 6), (34, 16)), ((18, 8), (34, 2)), ((18, 10), (34, 2)), ((18, 12), (34, 8)), ((18, 14), (34, 24)), ((18, 16), (34, 10)), ((18, 18), (34, 22)), ((18, 20), (34, 4)), ((18, 22), (34, 30)), ((18, 24), (34, 28)), ((18, 26), (34, 28)), ((18, 28), (34, 24)), ((18, 30), (34, 8)), ((20, 2), (34, 12)), ((20, 4), (34, 10)), ((20, 6), (34, 22)), ((20, 8), (34, 28)), ((20, 10), (34, 28)), ((20, 12), (34, 6)), ((20, 14), (34, 20)), ((20, 16), (34, 6)), ((20, 18), (34, 4)), ((20, 20), (34, 4)), ((20, 22), (34, 18)), ((20, 24), (34, 20)), ((20, 26), (34, 10)), ((20, 28), (34, 6)), ((20, 30), (34, 20)), ((22, 2), (34, 16)), ((22, 4), (34, 8)), ((22, 6), (34, 20)), ((22, 8), (34, 16)), ((22, 10), (34, 18)), ((22, 12), (34, 20)), ((22, 14), (34, 12)), ((22, 16), (34, 12)), ((22, 18), (34, 2)), ((22, 20), (34, 4)), ((22, 22), (34, 30)), ((22, 24), (34, 24)), ((22, 26), (34, 8)), ((22, 28), (34, 24)), ((22, 30), (34, 24)), ((24, 2), (34, 20)), ((24, 4), (34, 20)), ((24, 6), (34, 22)), ((24, 8), (34, 20)), ((24, 10), (34, 6)), ((24, 12), (34, 26)), ((24, 14), (34, 26)), ((24, 16), (34, 30)), ((24, 18), (34, 28)), ((24, 20), (34, 10)), ((24, 22), (34, 10)), ((24, 24), (34, 10)), ((24, 26), (34, 20)), ((24, 28), (34, 26)), ((24, 30), (34, 8)), ((26, 2), (34, 18)), ((26, 4), (34, 20)), ((26, 6), (34, 22)), ((26, 8), (34, 24)), ((26, 10), (34, 18)), ((26, 12), (34, 6)), ((26, 14), (34, 26)), ((26, 16), (34, 20)), ((26, 18), (34, 10)), ((26, 20), (34, 10)), ((26, 22), (34, 24)), ((26, 24), (34, 18)), ((26, 26), (34, 18)), ((26, 28), (34, 22)), ((26, 30), (34, 6)), ((28, 2), (34, 14)), ((28, 4), (34, 30)), ((28, 6), (34, 8)), ((28, 8), (34, 2)), ((28, 10), (34, 6)), ((28, 12), (34, 6)), ((28, 14), (34, 12)), ((28, 16), (34, 4)), ((28, 18), (34, 8)), ((28, 20), (34, 8)), ((28, 22), (34, 26)), ((28, 24), (34, 12)), ((28, 26), (34, 20)), ((28, 28), (34, 8)), ((28, 30), (34, 24))]
        
# Tính toán khoảng cách giữa tất cả các AGV và tất cả các nhiệm vụ
    # Áp dụng thuật toán Hungarian để tối ưu hóa gán nhiệm vụ cho các AGV
    def assign_tasks(self,agents, tasks):
        first_elements = [task[0] for task in tasks]
        cost_matrix = self.compute_cost_matrix(agents, first_elements)
        row_indices, col_indices = linear_sum_assignment(cost_matrix)
        return row_indices, col_indices

    def compute_cost_matrix(self,agents, tasks):
        return cdist(agents, tasks, 'cityblock')

    def allocation(self):
    # Gán nhiệm vụ cho các AGV
        self.task_assign = []
        print(len(self.task_lists))
        
        while len(self.task_lists) > 0:
            if len(self.agent_locations) < len(self.task_lists):
                # số nhiệm vụ lớn hơn số robot có thể nhận lệnh tại thời điểm t
                assigned_agents, assigned_tasks = self.assign_tasks(self.agent_locations, self.task_lists)
                for i in range(len(assigned_agents)):
                    # self.task_assign.append((assigned_agents[i], self.task_lists[assigned_tasks[i]]))
                    self.agent_locations[assigned_agents[i]] = self.task_lists[assigned_tasks[i]][0]
                    
                    ###
                    task = self.task_lists[assigned_tasks[i]]
                    flat_task = (task[0][1], task[0][0], task[1][1], task[1][0], "veh" + str(assigned_agents[i] + 1))
                    self.task_assign.append(flat_task)
                    
                self.task_lists = [task for i, task in enumerate(self.task_lists) if i not in assigned_tasks]
                
                
            elif len(self.agent_locations) == len(self.task_lists):
                # Số nhiệm vụ bằng số agent 
                assigned_agents, assigned_tasks = self.assign_tasks(self.agent_locations, self.task_lists)
                for i in range(len(assigned_agents)):
                    # self.task_assign.append((assigned_agents[i], self.task_lists[assigned_tasks[i]]))
                    self.agent_locations[assigned_agents[i]] = self.task_lists[assigned_tasks[i]][0]
                    
                    ###
                    task = self.task_lists[assigned_tasks[i]]
                    flat_task = (task[0][1], task[0][0], task[1][1], task[1][0], "veh" + str(assigned_agents[i] + 1))
                    self.task_assign.append(flat_task)
                    
                self.task_lists = [task for i, task in enumerate(self.task_lists) if i not in assigned_tasks]
                

            else:
                # số nhiệm vụ nhỏ hơn số robot có thể nhận lệnh tại thời điểm t
                assigned_agents, assigned_tasks = self.assign_tasks(self.agent_locations[:len(self.task_lists)], self.task_lists)
                for i in assigned_agents:
                    # self.task_assign.append((assigned_agents[i], self.task_lists[assigned_tasks[i]]))
                    self.agent_locations[assigned_agents[i]] = self.task_lists[assigned_tasks[i]][0]
                    ###
                    task = self.task_lists[assigned_tasks[i]]
                    flat_task = (task[0][1], task[0][0], task[1][1], task[1][0], "veh" + str(assigned_agents[i] + 1))
                    self.task_assign.append(flat_task)
                    
                self.task_lists = []
            
        
        # print(len(self.task_assign))
        print(self.task_assign)

    def convert(self):
        self.test = []
        for i in range(len(self.task_lists)):
            task = self.task_lists[i]
            flat_task = (task[0][1], task[0][0], task[1][1], task[1][0])
            self.test.append(flat_task)
        print(self.test)

if __name__ == "__main__":
    t = Task_allocation()
    t.allocation()