import ray
import random

ray.init()

@ray.remote
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        # self.n += 1
        import time
        time.sleep(10)
        self.n = random.randint(1, 50)

    def read(self):
        return self.n

# 桁を大きくしたら大量にワーカーができてエラーが多発したので、これくらいまでで
for j in range(4, 10):
    counters = [Counter.remote() for i in range(j)]
    [c.increment.remote() for c in counters]
    futures = [c.read.remote() for c in counters]
    print(ray.get(futures))

