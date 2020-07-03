# # python3
# class thread:
#     def __init__(self,id):
#         self.val=-1
#         self.id=id
#
# def min_heap(data):
#     while True :
#         count=0
#         for i in range(len(data)-1,-1,-1):
#             L= (2*i) +1
#             R= (2*i) +2
#             # print(data," i ",i,"  Left: ",L," Right: ",R)
#             if L < len(data) and R<len(data):
#                 if data[L].val< data[R].val:k=L
#                 else: k=R
#                 if data[k].val<data[i].val:
#                     data[i],data[k]=data[k],data[i]
#                     count=1
#             elif L < len(data):
#                 if data[L].val<data[i].val:
#                     data[i],data[L]=data[L],data[i]
#                     count=1
#             elif R < len(data):
#                 if data[R].val<data[i].val:
#                     data[i],data[R]=data[R],data[i]
#                     count=1
#         if count==0:
#             break
#     return
#
# def assign(jobs,T):
#     cache=[]
#     tim=0
#     job=0
#     # print("INIT",[T[i].val for i in range(len(T))])
#     while job<len(jobs) :
#         while T[0].val<=tim and job<len(jobs):
#             T[0].val=tim + jobs[job]
#             cache.append([T[0].id,tim])
#             job+=1
#             # print("assign",[T[i].val for i in range(len(T))])
#             min_heap(T)
#             # print("heapify",[T[i].val for i in range(len(T))])
#         tim+=1
#         # for i in range(len(T)):
#         #     T[i].val-=1
#         # print("time ",[T[i].val for i in range(len(T))])
#     return cache
#
# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs
#     T=[thread(i) for i in range(n_workers)]
#     # print([T[i].id for i in range(len(T))])
#     # print([T[i].val for i in range(len(T))])
#
#     assigned_jobs = assign(jobs,T)
#
#     for th,ti in assigned_jobs:
#         print(th, ti)
#
#
# if __name__ == "__main__":
#     main()
# python3
class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])
    def CompareWorker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]
    def SiftDown(self,i):
        minIndex, left = i, 2 * i + 1
        if left < self.num_workers and self.CompareWorker(next_free_time[left], next_free_time[minIndex]):
            minIndex = left
        right = 2 * i + 2
        if right < self.num_workers and self.CompareWorker(next_free_time[right], next_free_time[minIndex]):
            minIndex = right
        if i != minIndex:
            next_free_time[i], next_free_time[minIndex] = next_free_time[minIndex], next_free_time[i]
            self.SiftDown(minIndex)
    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        global next_free_time
        next_free_time = [[i, 0] for i in range(self.num_workers)]
        for i in range(len(self.jobs)):
          self.assigned_workers[i] = next_free_time[0][0]
          self.start_times[i] = next_free_time[0][1]
          next_free_time[0][1] += self.jobs[i]
          self.SiftDown(0)
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()
if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
