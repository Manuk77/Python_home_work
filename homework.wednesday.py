def dividers(num: int):
    
    result = []                             
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result 


num = int(input())
print(f'result = {dividers(num)}')
