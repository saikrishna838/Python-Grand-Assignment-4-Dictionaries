def count_right_rotations(s1, s2):
    if len(s1) != len(s2):
        return "No Match"
        
    n = len(s1)
    rotated = s1 
    for i in range(n):
        if rotated == s2:
            return i
        rotated = rotated[-1] + rotated[:-1]
    return "No Match"
    
s1 = input().strip()
s2 = input().strip()

print(count_right_rotations(s1, s2))
    
    