for i in range(int(input())):
    n=int(input())
    arr = []
    matrix = [list(map(int, input().split())) for j in range(n)]
    for x in range(n):
        arr[x].append(x+1)
    arr.sort()
    # print(matrix)
    # [[360, 480], [420, 540], [600, 660]]
    # d= {k:v for k,v in enumerate(matrix,start=1)}
    # d1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    # print(d1)
    # Pattern = ''
    # J =[0,0]
    # C =[0,0]
    # intial = [0,0]
    # for p,q in d1.values():
    #         if intial[1] <= p or intial[0] >= q:
    #             Pattern += 'J'
    #         else:
    #             Pattern += 'C'
                
    





      #T1 T2  100 - 500
      #T1' T2' 0 - 99
       
      #t2<=t1' or t2'<t1 (if true not overlapping )


    #   Solution 
    # def f(raw_arr):
#     arr = []
#     for i in range(len(raw_arr)):
#         arr.append((raw_arr[i][0], raw_arr[i][1], i))
#     arr.sort()
#     c_end = 0
#     j_end = 0
#     res_arr = []
#     for start, end, idx in arr:
#         if start < c_end and start < j_end:
#             return "IMPOSSIBLE"
#         if start >= c_end:
#             res_arr.append(('C', idx))
#             c_end = end
#         else:
#             res_arr.append(('J', idx))
#             j_end = end
#     res = ''
#     for c, idx in sorted(res_arr, key=lambda x: x[1]):
#         res += c
#     return res
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         interval = [int(s) for s in input().split(" ")]
#         arr.append(interval)
#     res = f(arr)
#     print("Case #{}: {}".format(t, res))