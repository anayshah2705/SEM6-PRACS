import math
import random
import time

def lumoto_partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def lumoto_qs(arr,low,high):
    if low < high:
        pi = lumoto_partition(arr,low,high)
        lumoto_qs(arr,low,pi-1)
        lumoto_qs(arr,pi+1,high)

def randomised_partition(arr,low,high):
    pivot_index = random.randint(low,high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    return lumoto_partition(arr,low,high)

def randomised_qs(arr,low,high):
    if low < high:
        pi = randomised_partition(arr,low,high)
        randomised_qs(arr,low,pi-1)
        randomised_qs(arr,pi+1,high)

array_size = 10000
fixed_input = [random.randint(0, 100000) for _ in range(array_size)]

input_lumuto = fixed_input.copy()
input_random = fixed_input.copy()

start_time = time.time()
lumoto_qs(input_lumuto,0,array_size-1)
end_time = time.time()

lumoto_time = end_time-start_time

start_time = time.time()
randomised_qs(input_random,0,array_size-1)
end_time = time.time()

random_time = end_time-start_time

print(f"Time taken by Lumoto: {lumoto_time}")
print(f"Time taken by Randomised: {random_time}")



