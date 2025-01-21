
if __name__ == '__main__':
    record = []
    numbers = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
        numbers.append(score)

    nums = list(set(numbers))
    print(f'nums {nums}')
    second_highest = nums[len(nums) -2]
    print(f'second_highest {second_highest}')

    for item in record:
        if item[1] == second_highest:
            names.append(item[0])

    names = names.sort()
    
    for name in names:
        print(name)


