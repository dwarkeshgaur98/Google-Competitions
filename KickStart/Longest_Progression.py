z =  int(input())
arr = list(map(int, input().split()))
diff = []
for i in range(len(arr)-1):
    diff.append(arr[i] - arr[i+1])
print(diff)
#z-3
arr1 = []
print(max(diff))
for i in diff:
    



# for i in range(z-3):
#     if diff[i] == (-diff[i+1]) and diff[i]!=0:

#         arr1.append([arr[i+1],i+1])
#     if arr[0] - arr[1] != 0 

# print(arr1)
# 5 5 5 5 4* 5 5 5 4* 5 6
# 12 9 7 5 3  
# 3 2 2 2 
# 15 14 12 9 7 5 3

