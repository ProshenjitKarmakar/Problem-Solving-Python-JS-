n = int(input())
arr = list(map(int, input().split()))

unique_arr = list(set(arr))

for i in range(len(unique_arr)):
    for j in range(0, len(unique_arr) - 1 - i):
        if unique_arr[j] > unique_arr[j + 1]:
            unique_arr[j], unique_arr[j + 1] = unique_arr[j + 1], unique_arr[j]

if len(unique_arr) >= 2:
    print(unique_arr[len(unique_arr) - 2])
else:
    print("There is no second highest unique value.")
