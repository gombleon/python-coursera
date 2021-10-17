def primes(n):
    def sieve(myList):
        if myList == []:
            return []
        else: 
            head, *tail = myList
            return [head] + sieve([x for x in myList if x % head])
    return sieve(range(2, n))

print(primes(30))
