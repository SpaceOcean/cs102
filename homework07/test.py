import unittest
from process_pool import ProcessPool, heavy_computation
import random


class MyTestCase(unittest.TestCase):
    def generate_data(self, len_list):
        big_data = [random.randint(1, 10) for _ in range(len_list)]
        return big_data
 
    def test_memory(self):
        worker = ProcessPool()
        self.assertGreaterEqual(int(worker.map(heavy_computation(), [11])[1]),
        		int(worker.map(heavy_computation(), self.generate_data(5))[1]))

    def test_count_worker(self):
        worker = ProcessPool()
        self.assertEqual(10, worker.map(heavy_computation(), self.generate_data(1))[0])


    def test_count_worker_max(self):
        worker = ProcessPool(1, 2, 512)
        self.assertEqual(2, worker.map(heavy_computation(), self.generate_data(5))[0])

    def test_count_worker_min(self):
        worker = ProcessPool(5, 10, 50)
        self.assertRaisesRegexp(MemoryError,"Недостаточно воркеров",
        	worker.map, heavy_computation() , self.generate_data(1))

if __name__ == '__main__':
    unittest.main()