# Function for selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current index is the minimum

        # Find the actual minimum in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only once after finding the minimum
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Step {i+1}: {arr}")

# Input and execution
input_str = input("Enter numbers separated by space: ")
arr = list(map(int, input_str.split()))

print("\nOriginal array:", arr)
selection_sort(arr)
print("\nSorted array:", arr)

#input dalo ye wala
#64 25 12 22 11