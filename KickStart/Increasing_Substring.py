# Round B 2021 - Kick Start 2021 - Increasing Substring
import string 

chars = { v:k for k, v in enumerate(string.ascii_uppercase)}
def fn(out, n):
    print(f"Case #{n+1}: {out}")

z = int(input())
for j in range(z):
    len1 = int(input())
    arr = input()
    arr1 = []
    count = 1
    
    for i in range(len1-1):
        arr1.append(count)    
        if chars[arr[i]] < chars[arr[i+1]]:
            count += 1
        else:
            count = 1
    arr1.append(count)    
    arr1 = list(map(str, arr1))
    fn(str(' '.join(arr1)),j)


    
    

            
