def prime_sieve(M,N):
    
    arr =[True for i in range(N+1)]
    arr[0], arr[1]=False, False
    for i in range(2,N+1):
        if arr[i]==True:
            j=2
            while i*j<N+1:
                arr[i*j]=False
                j+=1
    return arr  