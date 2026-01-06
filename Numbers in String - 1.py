string = input().split()

sum_of_numbers = 0
count = 0
new_string = ''
for i in string:
    new_string += i
    
for i in new_string:
    if i.isdigit():
        sum_of_numbers += int(i)
        count += 1
print(sum_of_numbers)
average = round(sum_of_numbers / count, 2)
print(average)