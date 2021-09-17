# Qualification Round 2020 - Code Jam 2020 - Nesting Depth

def brackets(arr):
    arr.append(0)
    arr.insert(0,0)
    out1 = ''
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i] 
        if arr[i] < arr[i+1]:
            
            out1 += str(arr[i]) + diff*"("
        
        elif arr[i] > arr[i+1]:
            
            out1 += str(arr[i]) + (-diff)*")"
        elif arr[i] == arr[i+1]:
            out1 += str(arr[i])
    out2 = out1[1:] 
    print(out2)

        



z = int(input())
for i in range(z):
    int1 = list(map(int, input()))
    brackets(int1)