from concurrent.futures import ThreadPoolExecutor

from data_async import f1, g1

print(ThreadPoolExecutor().submit(max, *[f1(2), g1(3)]).result())
