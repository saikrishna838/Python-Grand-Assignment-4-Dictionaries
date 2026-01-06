n = int(input())
m = int(input())
new_list = []
while n <= m:
    for i in range(n):
        if i * i == n:
            new_list.append(n)
            
    n = n + 1
if len(new_list) >= 1:
    print(new_list[0])
else:
    print("No Perfect Square")
        
        