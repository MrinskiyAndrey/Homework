
array = [1,2,3,4,2,5,1,2,6,3]



def unique(N=[]):
    array2 =[]
    k = 1
    for i in N:
        K = 0
        for q in array :
            k+1
            if i == q:
                K += 1
        if K < 2:
            array2.append(i)
                    
                    
    return array2
            

print(unique(array))
