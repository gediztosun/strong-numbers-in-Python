num = input()

addition = 0

for i in range(0, len(num)):
    fact = 1
    
    for j in range(int(num[i]), 1, -1):
        fact *= j
    
    
    addition += fact
    
print(addition)