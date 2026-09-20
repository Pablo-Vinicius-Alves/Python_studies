quadrados = []
for n in range(10):
    quadrados.append(n ** 2)
    
 
quadrados = [n ** 2 for n in range(10)]  
quadrados = [n ** 2 for n in range(10) if n % 2 == 0]
print(quadrados) 

quadrados_dict = {n: n ** 2 for n in range(5)}
print(quadrados_dict)