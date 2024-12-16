def dominant_prob(k, m, n):
    total = k + m + n
    
    total_pairs = total * (total - 1)
    
    dominant_probab = (
        k * (k - 1) +               # AA × AA
        2 * k * m +                 # AA × Aa
        2 * k * n +                 # AA × aa
        m * (m - 1) * 0.75 +        # Aa × Aa
        2 * m * n * 0.5             # Aa × aa
    ) / total_pairs
    
    return dominant_probab

k = 18
m = 16
n = 22
result = dominant_prob(k, m, n)
print(result)  
