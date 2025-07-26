'''
given two integers n and k return all possible combinations of k numbers chosen from the range[1,n]
youn may return the answer in any order.
input: n=4,k=2
output:[[1,2],[1,3],[1,4],[2,3][2,4][3,4]]

def combine(n,k):
    result=[]
    def backtrack(start,path):
        
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(start,n+1):
            path.append(i)
            backtrack(i+1,path)
            path.pop()
    backtrack(1,[])
    return result
n=4
k=2
print(combine(n,k))


given an integer array nums of unique elements,return all possible subsets(the power set) 
the solution set must not contain duplicate.
input: nums=[1,2,3]
output;
input:nums=[0]
output:[[],[0]]

def combine(n):
    result=[]
    def backtrack(start,path):
        
        result.append(path[:])
    
        for i in range(start,len(n)):
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()
    backtrack(0,[])
    return result
n=[1,2,3]

print(combine(n))

given an integer array nums that may contain duplicates,return all possible subsets
the solution set must not contain duplicates subsets. return the solution in any order.
nums=[1,2,2]


def combine(n):
    result=[]
    n.sort()
    def backtrack(start,path):
        result.append(path[:])
    
        for i in range(start,len(n)):
            if i>start and n[i]==n[i-1]:
                continue
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()
        
    backtrack(0,[])
    return result
    #for i in result:
        #if i in ans:
            #continue
        #else:
            #ans.append[i]
    #return ans

n=[1,2,2]
print(combine(n))


def combine(n):
    result=[]
    def backtrack(start,path):
        result.append(path[:])
        for i in range(start,len(n)):    
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()  
    backtrack(0,[])

    ans = []
    for i in result:
        if i not in ans:
            ans.append(i)
    return ans
n=[1,2,2]
print(combine(n))

def combine(n):
    result=[]
    def backtrack(start,path):
        result.append(path[:])
        for i in range(start,len(n)):    
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()  
    backtrack(0,[])
    ans=set(tuple(subset) for subset in result)
    ans = [list(tup) for tup in ans]
    return ans
n=[1,2,2]
print(combine(n))

given a collection of candidate numbers(candidates) and a target number(target),find all unique sum to target.
each number in candidates may only be used once in the combination. 
note: the solution set must not contain duplicate combinations.


def combine(n,target):
    result=[]
    def backtrack(start,path):
        #if sum(path)==target and path not in result:
        result.append(path[:])
        for i in range(start,len(n)):    
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()  
    backtrack(0,[])
    ans = []
    for i in result:
        if i not in ans:
            ans.append(i)
    r=[]
    for i  in ans:
        if sum(i)==target:
            r.append(i)
    return r
n=[1,2,5,4,8,10,5]
target=8
print(combine(n,target))

given a string s, which may contain duplicate characters your task is to generate and 
return an array of all unique permutations of the string you can return your answer in any order.
input="ABC"

def combine(n):
    s=set(s)
    result=[]
    def backtrack(start,path,s):
        #if sum(path)==target and path not in result:
        result.append(path[:])
        for i in range(start,len(n)):    
            path.append(n[i])
            backtrack(i+1,path)
            path.pop()  
    backtrack([],s,resu)
    
    ans = []
    for i in result:
        if i not in ans:
            ans.append(i)
    return ans
n="ABC"
print(combine(n))
'''
def gen(i,s,used,curr,st):
    if i==len(s):
        st.add("".join(curr))
        return
    seen=set()
    for j in range (len(s)):
        if not used[j] and s[j] not in seen:
            seen.add(s[j])
            used[j]=True
            curr.append(s[j])
            gen(i+1,s,used,curr,st)
            used[j]=False
            curr.pop()

    used=[False]*len(s)
    st=set()
    curr=[]
    s=sorted(s)
    gen(0,s,used,curr,st)
    return list(st)
