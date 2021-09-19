# Round F 2021 - Kick Start 2021 - Trash Bins
#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
#for z in range(int(input())):
N = int(input())
S = list(map(int,input()))
total = 0
for i in range(N):
    r_count = 0
    l_count = 0
    if S[i] == 0:
        #right
        for j in range(N-i-1):
            print('i=',i,'j=',j)
            if S[i+j] == 0:
                r_count +=1 
                print('right',r_count) 
            elif i == N-1:
                r_count = 5* (10**5)

            else:
                break
                 
        #left
        for k in range(i):
            print('i=',i,'k=',k)
            if S[i-k] == 0:
                l_count += 1
                print('left',l_count)

            elif i== 0:
                l_count = 5* (10**5)
            else:
                break
                
        # j=0
        # k=0
        # while S[i+j] <= 0:
        #     r_count +=1
        #     j += 1
        # while S[i-k] <= 0:
        #     l_count += 1
        #     k += 1
 
        if r_count < l_count:
            total += r_count

        elif r_count > l_count:
            total += l_count
        else:
            total += l_count
        print(total)


print(total)
