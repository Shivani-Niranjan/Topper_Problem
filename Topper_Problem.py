register_num = int(input())
register_num = str(register_num)
sumOdd = 0
sumEven = 0
for i in range(len(register_num)):
    if(i % 2 == 0):
        sumOdd = sumOdd+int(register_num[i])
    else:
        sumEven = sumEven+int(register_num[i])

print(True if sumEven==sumOdd else False)