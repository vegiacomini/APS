def expn(x, j):
    total = x
    for i in range(1, j):
        total = total*x
    return total

def fatorial(n):
    total = n
    for i in range(1,n):
        total = total*(n-1)
        n = n-1
    return total

def cos(x, n):
    r = 1
    for k in range(1, n):
        r = r + expn(-1,k)*expn(x, 2*k)/fatorial(2*k)
    return r    
    
print cos(float(2), 10)
print cos(float(3.1415), 10)
print cos(float(0.1), 10)

def sin(x, n):
    r = x
    for k in range(1, n):
        r = r + expn(-1,k)*expn(x, 2*k+1)/fatorial(2*k+1)
    return r  
    
    
print sin(float(2), 10)
print sin(float(3.1415), 10)
print sin(float(0.1), 10)    
    