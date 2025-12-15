"""
row_list = [init_time, duration, task_id, finish_time]
task_in_progress = [finish_time, worker_id] # Minheap to manage tasks in progress
worker_queue = [worker_id] # Minheap to manage worker availability and always send the lowest id available
"""
from heapq import heapify, heappush, heappop

def finish_time_calculator(init_time: str, duration: str) -> str:
    """
    Calculate the finish time for a task.
    """
    hrs = int(init_time[0:2])
    mins = int(init_time[2:4])
    mins += int(duration)
    while mins >= 60:
        mins -= 60
        hrs += 1

    finish_time = str(hrs).zfill(2) + str(mins).zfill(2)
    return finish_time    

def define_tasks(main_task_list) -> None:
    """
    Define the tasks to be created.
    """
    tasks=input("How many tasks would you like to create? ")
    for i in range(int(tasks)):
        task_row=input(f"Enter init time and duration for task {i + 1}: ").split()
        finish_time = finish_time_calculator(task_row[0], task_row[1])
        task_row.append(i)
        task_row.append(finish_time)
        main_task_list.append(task_row)    
    

def free_workers(current_time: str, worker_queue:list) -> None:
    """
    Free up workers based on the current time.
    """
    while task_in_progress and task_in_progress[0][0] <= current_time:
        finish_time, worker_id = heappop(task_in_progress)
        heappush(worker_queue, worker_id)

def assign_worker(task_row:list, worker_queue:list, task_in_progress:list) -> None:
    """
    Assign a worker to a task.
    """
    global workers
    finish_time = task_row[3]
    free_workers(task_row[0], worker_queue)     # Free up workers based on the current time
    if worker_queue:
        worker_id = heappop(worker_queue)
    else:
        worker_id = workers
        workers += 1
    heappush(task_in_progress, [finish_time, worker_id])
    task_row.append(worker_id)

def print_task_details(task_list:list) -> None:
    """
    Print the task details.
    """
    print("Total workers used:", workers)
    print("Task ID | Init Time | Duration | Finish Time | Worker ID")
    for task in task_list:
        print(f"{task[2]}       | {task[0]}      | {task[1]}      | {task[3]}       | {task[4]}")


worker_queue = [0]  # Minheap to manage worker availability inits worker 0
heapify(worker_queue)
workers = 1     # Number of workers used

task_in_progress = []  # Minheap to manage tasks in progress
heapify(task_in_progress)


main_task_list=[]
define_tasks(main_task_list)
#sort tasks by init time 
main_task_list.sort(key=lambda x: x[0])
for task_row in main_task_list:
    assign_worker(task_row, worker_queue, task_in_progress)

#sort by task id
main_task_list.sort(key=lambda x: x[2])

print_task_details(main_task_list)