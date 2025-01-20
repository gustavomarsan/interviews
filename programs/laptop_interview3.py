"""
jobs = [[init, dur, end_time, worker, index ]
workers = int
avail_workers = heap
finishing_time = heap
finish_dict = {"finish_time" : [worker1, worker2] , "finish_worker" : [worker 3] }

"""

from collections import deque
from heapq import heapify, heappop, heappush
from operator import itemgetter

class JobSchedule :

    def __init__(self) :
        self.finishing_times = []
        heapify(self.finishing_times)
        self.job_num = int(input())
        self.jobs = [] 
        for i in range(self.job_num) :
            key = input().split()
            finish = self.finish_time(key[0], int(key[1]))   # aks finish time
            my_list = []                        # create new list
            my_list.append(key[0])              # init time     index 0
            my_list.append(int(key[1]))         # duration      index 1
            my_list.append(finish)              # finish time   index 2
            my_list.append(0)                   # worker        index 3
            my_list.append(i)                   # job index     index 4
            self.jobs.append(list(my_list))          # append the list to jobs list
            heappush(self.finishing_times, finish)          

        self.jobs.sort()                             # sort by init time
        self.workers = 1                             # set init worker
        self.avail_workers = [0]                     # worker index 0
        heapify(self.avail_workers)

        self.finish_dict = {}

    # returns time to finished the job
    def finish_time(self, init: str, duration: int) -> str :      
        init_hours = int(init[0:2])
        init_mins = int(init[2:4])
        final_mins = duration % 60 + init_mins
        final_hour = duration // 60 + init_hours
        if final_mins  > 59 :
            final_mins -= 60
            final_hour += 1
        # convert to strt
        #hours
        if final_hour == 0 :
            hour_res = "00"
        elif final_hour < 10 :
            hour_res = "0"+str(final_hour)
        else :
            hour_res = str(final_hour)
        #mins
        if final_mins == 0 :
            min_res = "00"
        elif final_mins < 10 :
            min_res = "0"+str(final_mins)
        else :
            min_res = str(final_mins)
        return  hour_res+min_res

    def free_workers(self, init: int) -> None :       # check init time if jobs finished free workers
        while len(self.finishing_times) > 0 and self.finishing_times[0] < init :
            time = heappop(self.finishing_times)               # job finished
            worker = self.finish_dict[time].pop()        # free worker used
            heappush(self.avail_workers, worker)         # add worker to the available workers heap

a = JobSchedule()
# input and fill jobs list and finish times
for job in a.jobs :                       # this loop is for asign workwer to every job
    a.free_workers(job[0])                # check finished_times to free workers
            
    if len(a.avail_workers) == 0 :        # choose available worker or get new one
        job[3] = a.workers
        a.workers += 1
    else :
        job[3] = heappop(a.avail_workers)
            
    # set "finished time" :  worker used,  in finish_dict to know who is the free worker
    if job[2] in a.finish_dict :
        a.finish_dict[job[2]].append(job[3])        
    else :
        a.finish_dict[job[2]] = [job[3]]

# ending print
a.jobs.sort(key=itemgetter(4))        # sort by job index
print(a.workers)
for i in range(len(a.jobs)) :
    print("J"+str(i), "W"+str(a.jobs[i][3]))
            



    
    

    
    


