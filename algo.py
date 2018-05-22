# Number algorithms

import math

def ExtendedEuclid(a,b):
    if b == 0:
        return a,1,0
    dt,xt,yt = ExtendedEuclid(b,a % b)
    d,x,y = dt,yt,xt-math.floor(a/b)*yt
    return d,x,y

def Linear_Congruence_Solver(a,b,n):
    d,u,v = ExtendedEuclid(a,n)
    if not b/d:
        return []
    x0 = u*(b/d) % n
    sols = []
    k = n/d
    for i in range(d):
        sols.append((x0+i*k)%n)
    return sols        

def MultInverse(a,n):
    d,u,v = ExtendedEuclid(a,n)
    if d == 1:
        while u<0:
            u += n
        return u
    else:
        return None

def Linear_Congruence_System_Solver(arrA,arrM):
    m = 1
    for x in arrM:
        m *= x    
    res = 0
    for i in range(len(arrM)):
        M = m/arrM[i]
        S = MultInverse(M,arrM[i])
        E = S*M
        res += arrA[i]*E    
    return res%m 

res = 0
for line in open('in.txt'):
    ss = line.strip().split(';')
    if len(ss) > 1:
        A,M =[],[]
        for x in ss:
            nums = x.split(',')
            A.append(int(nums[0]))
            M.append(int(nums[1]))
        res += Linear_Congruence_System_Solver(A,M)
    else:
        nums = line.split(',')
        sols = Linear_Congruence_Solver(int(nums[0]),int(nums[1]),int(nums[2]))
        for x in sols:
            res += x
    
print(res)
