def perfect_number(num: int):
    sum = 0
    result = []
    for i in range(1, int(num / 2) + 1):    
        if num % i == 0:
            result.append(i)
    for i in range(len(result)):
        sum += result[i]
    if sum == num:
        return True
    return False


num = int(input())
print(f'result = {perfect_number(num)}')
