import re

sentence = input()
numbers = list(map(int, re.findall(r'\d+', sentence)))

total = sum(numbers)
    
if numbers:
    average = round(total / len(numbers), 2)
else: 
    average = 0.0
    
print(total)
print(average)
        
