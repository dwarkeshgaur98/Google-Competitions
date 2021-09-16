# Round A 2021 - Kick Start 2021 - K - Goodness String
z = int(input())
for y in range(z):
    length , exp_good = map(int, input().split(' '))
    arr = input()
    acc_good = 0
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[-i-1]:
            acc_good += 1
    
    diff = exp_good - acc_good  
    print(f"Case #{y+1}: {diff}")
    
    