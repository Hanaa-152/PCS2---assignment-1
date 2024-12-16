def rabbit_pairs(n, k):
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    
    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)


n = 29
k = 2
result = rabbit_pairs(n, k)
print(result)  
