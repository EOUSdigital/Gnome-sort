def gnome_sort(arr):
    index = 0
    n = len(arr)

    while index < n:
        if index == 0:
            index += 1
        elif arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

data = [34, 2, 10, -9, 7, 5]
sorted_data = gnome_sort(data)
print("Sorted list:", sorted_data)