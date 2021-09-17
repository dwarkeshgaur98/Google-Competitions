# Qualification Round 2020 - Code Jam 2020 - Vestigium

def trace(arr, n):
  
    return sum([arr[i][i] for i in range(n)])

def check_row(arr,n):
    count1 = 0
    for i in range(n):

        set1 = {arr[i][j] for j in range(n)} 
        if len(set1) < n:
            count1 += 1
    return count1

def check_column(arr,n):
    count1 = 0
    for i in range(n):

        set1 = {arr[j][i] for j in range(n)}
        if len(set1) < n:
            count1 += 1
    return count1

z = int(input())

for i in range(z):
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]  
    trace1 = trace(arr,n)
    rows1 = check_row(arr,n)
    column1 = check_column(arr,n)
    print(f"Case #{i+1}: {trace1} {rows1} {column1}") 



