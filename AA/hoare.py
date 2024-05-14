import random
import time

def hoare_partition_low_pivot(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare_low_pivot(arr, low, high):
    if low < high:
        pivot_index = hoare_partition_low_pivot(arr, low, high)

        quick_sort_hoare_low_pivot(arr, low, pivot_index)
        quick_sort_hoare_low_pivot(arr, pivot_index + 1, high)

def hoare_partition_randomized_pivot(arr, low, high):
    # Randomly select pivot index
    pivot_index = random.randint(low, high)

    # Move pivot to the beginning
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]

    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare_randomized_pivot(arr, low, high):
    if low < high:
        pivot_index = hoare_partition_randomized_pivot(arr, low, high)

        quick_sort_hoare_randomized_pivot(arr, low, pivot_index)
        quick_sort_hoare_randomized_pivot(arr, pivot_index + 1, high)

# Example usage
array_size = 100000
fixed_input = [random.randint(0, 1000000) for _ in range(array_size)]

# Duplicate the input for both versions
input_copy_low_pivot = fixed_input.copy()
input_copy_randomized_pivot = fixed_input.copy()

# Measure time for Hoare partition with low pivot
start_time_low_pivot = time.time()
quick_sort_hoare_low_pivot(input_copy_low_pivot, 0, array_size - 1)
end_time_low_pivot = time.time()

# Measure time for Randomized Hoare partition
start_time_randomized_pivot = time.time()
quick_sort_hoare_randomized_pivot(input_copy_randomized_pivot, 0, array_size - 1)
end_time_randomized_pivot = time.time()

# Calculate time differences
time_difference_low_pivot = end_time_low_pivot - start_time_low_pivot
time_difference_randomized_pivot = end_time_randomized_pivot - start_time_randomized_pivot

# Print time-related information
print(f"Hoare Partition with Low Pivot Time: {time_difference_low_pivot} seconds")
print(f"Randomized Hoare Partition Time: {time_difference_randomized_pivot} seconds")
print(f"Time Difference: {time_difference_low_pivot - time_difference_randomized_pivot} seconds")
