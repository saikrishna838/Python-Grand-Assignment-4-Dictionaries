def convert_str_to_int(list_a):
    new_list = []
    for i in list_a:
        num = int(i)
        new_list.append(num)
    return new_list
    
m, n = input().split()
m, n = int(m), int(n)

num_list = []
for i in range(m):
    list_a = input().split()
    list_a = convert_str_to_int(list_a)
    num_list.extend(list_a)
    
num_list.sort()

result_matrix = []

x = 0
for i in range(m):
    t = []
    for j in range(n):
        t.append(num_list[x])
        x += 1
    result_matrix.append(t)
    
for i in result_matrix:
    print(" ".join(map(str, i)) + " ")
    
    