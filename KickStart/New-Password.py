# Round C 2022 - Kick Start 2022 - New Password
def tests(arr):
        arr = list(arr)
        arr1 = arr.copy()
        arr = sorted(arr)
        arr1 = list(arr1) 
        numbers = 0
        symbols = 0 
        u_al = 0
        l_al = 0
        all_symbols =['@','#',"*","&"]
        for j in range(len(arr)):
                if arr[j] in all_symbols and symbols == 0:
                        symbols = 1
                
                

                if arr[j].isnumeric() and numbers == 0:
                        numbers = 1
                if arr[j].isalpha() and l_al == 0:
                        if arr[j].islower() and l_al == 0:
                                l_al = 1
                if arr[j].isalpha() and u_al == 0:
                        if arr[j].isupper() and u_al == 0:
                                u_al  = 1
                        
        if symbols == 0:
                arr1.append('@')
        if numbers == 0:
                arr1.append('1')
        if u_al == 0:
                arr1.append('A')
        if l_al == 0:
                arr1.append('a')

        if len(arr1)<7:
                arr1 += list("a"*(7-len(arr1)))
                
        return arr1

a = int(input())
output = []
for i in range(a):
    
    len1 = int(input())
    arr = input()
    
    
    abc = "".join(tests(arr))
    
    output.append(f"Case #{i+1}: {abc}")
for j in range(len(output)):
    print(output[j])
    
    
