from multiprocessing import Process, cpu_count
import psutil
import time
from time import sleep
import math
import random


class ProcessPool:
    def __init__(self, min_workers=1, max_workers=10, mem_usage=500):
        self.min_workers = min_workers
        self.max_workers = max_workers
        self.mem_usage = mem_usage


    def map(self, func, args):
        procs = []
        mem_count = []
        proc = Process(target=func, args=(args[0],))
        proc.start()
        while proc.is_alive():
            proc_info = psutil.Process()
            mem_count.append(proc_info.memory_info().rss / 1000 / 1000)
            sleep(0.0001)
        self.memory = max(mem_count)
        self.worker_count = int(self.mem_usage / self.memory)

        
        if self.worker_count == 0: self.worker_count = 1
        if self.worker_count > self.max_workers: self.worker_count = self.max_workers
        if self.worker_count < self.min_workers:
            raise MemoryError('Недостаточно воркеров')
        proc.join()
        if self.memory > self.mem_usage:
            raise Exception('Для выполнения процесса недостаточно памяти')

        print(self.worker_count)
        print(self.memory)
        self.worker_process = 0
        
        for i in range(self.worker_count):
            if args == []:
                break
            proc = Process(target=func, args=(args[0],))
            procs.append(proc)
            proc.start()
            self.worker_process += 1
            print(self.worker_process)
            del args[0]
            print(proc)
        while not args==[]:
            for idx, proc in enumerate(procs):
                if self.worker_process < self.worker_count:
                    if args==[]: break
                    if not proc.is_alive():
                        new_proc = Process(target=func, args=(args[0],))
                        procs[idx] = new_proc
                        new_proc.start()
                        self.worker_process += 1
                        del args[0]
                        print(new_proc)
                else:
                    for proc in procs:
                        if proc.is_alive():
                            proc.join()
                            self.worker_process -= 1
                            print(proc)
                            break
        for proc in procs:
            proc.join()
            self.worker_process -= 1
            print(proc)

        return self.worker_count, self.memory

def heavy_computation(data_chunk=1):
    for i in range(23):
        data_chunk = (data_chunk + i) * data_chunk
        print(i)
    return data_chunk

if __name__ == '__main__':
    pool = ProcessPool(min_workers=1, max_workers=5, mem_usage=1000)
    big_data = [1,2,3,4,5,1,2,3,4,5]
    result = pool.map(heavy_computation, big_data)
