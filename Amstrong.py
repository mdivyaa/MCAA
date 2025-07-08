# Armstrong Numbers from 1 to 10000
for num in range(1, 10001):
    power = len(str(num))
    total = sum(int(d)**power for d in str(num))
    if total == num:
        print(num)
