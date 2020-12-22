import ray
ray.init(num_cpus=8)

@ray.remote
def f(x):
    return x * x

for j in range(100):
    futures = [f.remote(i) for i in range(j ** 2)]
    print(j, ray.get(futures))