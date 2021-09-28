def getFactors(n):
    factors = [ ]
    for num in range(1, n+1):# num is a possible factor
        if n % num == 0:
            factors.append(num)
    return factors