list_a = ['a', 'b', 'c']
# output=['a,b,c']
res = []
res.append(','.join(list_a))
print(res)


#sort the number::
l=[1,2,3,5,4,2,6,7]
n=len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
print(l)

#factoraial:
num=int(input('Enter the number::'))
if num==0:
    print(f'The factorial of {num} is 1')
else:
    res=1
    for no in range(1,num+1):
        res*=no
    print(f'The factorial of {num} is {res}')


#1)pp for identity matrix----->
for i in range(5):
    for j in range(5):
        if i==j:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()

l = []
for i in range(5):
    l.append([1 if i == j else 0 for j in range(5)]) #---->here in case of append

for i in l:
    print(i)

#2) find max and min number

l=[1,3,5,3,6,8,9,5,7]  #----->for min number
min_no=l[0]
for i in l:
    if i<min_no:
        min_no=i
print(min_no)

l=[1,3,5,3,6,8,9,5,7]
for i in l:
    for j in l:
        if i<=j:     #----->i>=j for max number
            continue
        else:
            break
    else:
        print(i)

#3)pp for nth largest number:
def large(l,x):
    if 0<x<=len(l):
        l=list(l)
        l.sort()
        return l[-x]
    else:
        return 'choice out of range'

l = [2, 3, 4, 5, 3, 4, 5, 6, 7]
choice=int(input('Enter the number::'))
print(large(l,choice))    #------>for unique numbers only.

def func(l, x):
    global d
    d = {i: {j for j in l if j >= i} for i in l}  ### important step
    return [i[0] for i in d.items() if len(i[1]) == x]
l=[1,2,3,2,6,7,4,3]
print(func(l,2))

l=[1,2,3,2,6,7,4,3]
d = {i: {j for j in l if j <= i} for i in l}
for i in d.items():
    if len(i[1])==2:
        print(i[0])

number=int(input('Enter the number:'))

l=[11,11,34,23,56,32,67,43,54]
for i in l:
    l1=set({})
    for j in l:
        if i>=j:
            l1.add(j)

    if number==len(l1):
        print(i,l1)
        break

#4)reversed the integer
no=12345
print(''.join(list(reversed(str(no)))))
print(str(no)[::-1])

result=''
for i in str(no)[::-1]:
    result=result+i
print(int(result))

def reverse_no(no):
    res=''
    while no>0:
        x=no%10
        no=no//10
        res+=str(x)
    return res
print(reverse_no(12345))

res=0
while no>0:
    x=no%10
    no=no//10
    res*=10
    res+=x
print(type(res))

inp=input('Enter no to reverse:',) ### we ge string
s=''
for i in range(len(inp)):
 s+=inp[-i-1]
print(s)

#5)find the sum of digits in number
no=122343
sum=0
for i in str(no):
    sum+=int(i)
print(sum)

sum1=0
while no!=0:
    sum1+=no%10
    no=no//10
print(sum1)

from functools import reduce
no=[1,2,3,4,5]
res=reduce(lambda x,y:x+y,no)   #------------->to add number in sequence only
print(res)

#6)find the LCM:
def lcm(n1,n2):
    min_no=min(n1,n2)
    no=min(n1,n2)
    while True:
        if no%n1==0 and no%n2==0:
            return no

        else:
            no+=min_no
def main():
    n1 = int(input('Enter the nmber:'))
    n2 = int(input('Enter the nmber:'))
    result=lcm(n1,n2)
    print(result)
if __name__=='__main__':
    main()

#7)pp for GCD
n1 = int(input('Enter the nmber:'))
n2 = int(input('Enter the nmber:'))
min_no=min(n1,n2)
result=0
for i in range(1,min_no+1):
    if n1%i==0 and n2%i==0:
        result=i

print(result)

#8)pp to check for anagram
a='silent'
b='Lis ten'
if list(a.lower()).sort()==list(b.lower().replace(' ','')).sort():
    print('Yes')
else:
    print('no')

for i in a.lower().replace(' ','' ):
    if i in b.lower().replace(' ','' ):
        continue
    else:
        print('Not anagram')
        break
else:
    print('Yes its anagram')

#9)pp for [1,22,333,4444,55555,......]
l=[str(i)*i for i in range(1,6)]
result=list(map(lambda x:int(x),l))
print(result)

l=[]
for i in range(1,6):
    num=i
    for j in range(i-1):
        num*=10
        num+=i
    l.append(num)
print(l)

#10) pp for avg of elements in iterable:
l=[1,3,4,5,6,3,4,5,6,78,5]
from functools import reduce   #------->The reduce() function from functool module which takes two arguments: a function and an iterable.
                                # It repeatedly applies the function to the elements of the iterable,
                                #  accumulating a single result.
s=reduce(lambda x,y:x+y,l)
print(s/len(l))


#11)python program to a read number n and compute n+nn+nnn+nnnn::
result='+'.join([str(i)*i for i in range(1,6)])
print(result) #----->1+22+333+4444+55555

no=int(input('Enter the number:'))
l=[]
num=0
for i in range(1,no+1):
    num*=10
    num+=no
    l.append(num)
print(l)
res='+'.join([str(i) for i in l])
print(res)   #------------->6+66+666+6666+66666+666666

#12)pp to count the digits in  number:
no=123454
sum=0
for i in str(no):
    sum+=1

print(sum)

result=0
while no>0:
    no=no//10
    result += 1
print(result)
#---------------------------------------------------------------------------
#13) PP to print palindrome numbers in range 100 -500

list_no=[i for i in range(101,201) if str(i)==str(i)[::-1]]
print(list_no)

fil_no=list(filter(lambda x:str(x)==str(x)[::-1], [x for x in range(101,201)]))
print(fil_no)

def reverse(no):
    res=0
    while no:
        num=no%10
        no=no//10
        res*=10                #---------->most important..
        res+=num
    return res

for i in range(100,210):
    if i==reverse(i):
        print(i)
def reve_no(no):
    if str(i)==str(i)[::-1]:
        return i
for i in range(101,210):
    if reve_no(i):
        print(i)

def rev_no(no):
    rev=''
    while no>0:
        rev+=str(no%10)
        no=no//10
    return int(rev)
for i in range(101,210):     #------->imp here used other functionn(upper)
    if i==rev_no(i):
        print(i)


def rever_no(no):
     l=[]
     while no>0:
         l.append(str(no%10))    #------>by using join method
         no=no//10
     return  int(''.join(l))

for i in range(100,200):
    if i==rever_no(i):
        print(i)

#14) check palindrome
m = ["geeks", "geeg", "keek", "practice", "aa"]
result=list(filter(lambda x: x==x[::-1],m))
print(result)

s='Avinash'
n=len(s)
x=0
for i in range(n//2):
    if s[i]==s[-i-1]:
        continue
    else:
        break
else:
    print('yes it palinrome')


#15)pp to check prime number:

choice=int(input('Enter the number:'))
no=2
while no<choice:
    if choice%no==0:
        print('not prime')
        break

    no+=1

else:
    print('prime number')

#16) input=['123456789']
    #output=['12','34','56','78','9']

s='123456789'
result=[]
while s:
    a = ''
    for i in s[:2]:       #------->['12', '34', '56', '78', '9']
        a+=i
    result.append(a)
    s=s[2:]
print(result)


s='123456789'
s1=[]
for i in range(len(s)):      #------->['91', '12', '23', '34', '45', '56', '67', '78', '89']
    s1.append(s[i-1]+s[i])
print(s1)

l=[]
s='123456789'
while s:
    l.append(s[:2])        #------->['12', '34', '56', '78', '9']
    s=s[2:]
print(l)

#17) pp for finding the missing number in list of continuos number::.
l=[1,2,4,5,7,8,9,10]
for i in range(len(l)-1):   #---->to avoid index out of rangge focus on range()
    if l[i+1]-1!=l[i]:      # here backwors to forward
        print(l[i]+1)

for i in range(len(l)-1):
    if l[i]!=l[i+1]-1:     # here forward to backward
        print(l[i+1]-1)

for i in range(len(l)-1):
    if l[i+1]-l[i]!=0:       # by difference
        print(l[i]+1)

l=[1,2,4,5,7,8,9,10]
for i in range(1,len(l)-1):
    if l[i]-l[i-1]!=1:
        print('Misiing number is:',l[i]-1)

#------in case if diff etween number is greater than 1::
for i in range(len(l)-1):
    if l[i+1]-l[i]!=1:
        l.insert(l.index(l[i])+1,l[i]+1)
print(l)

res=[l.insert(l.index(l[i])+1,l[i]+1) for i in range(len(l)-1) if l[i+1]-l[i]!=1]
print(l)


#18)P to read N numbers and print the series 1+2+.....+N

no=int(input('enter the number:'))
res='+'.join((str(i) for i in range(1,no+1)))
print(res)

#19) pp for identity matrix
no=int(input('Enter the number:'))
for i in range(no):
    for j in range(no):
        if i==j:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()

#20)pp to find the prime number:
l1=[i for i in range(1,101)]
for i in l1:
    for j in range(2,i):
        if i%j==0:
          break
    else:
        print(i)

#21)pp to create a directory:

import os
def make_dir(name):
    os.mkdir(name)
    return 'yes'

def main():
    dir_name=input('Enter the file name:')
    respose=make_dir(dir_name)
    if respose:
        print('Directory created')
    else:
        print('Try again')

if __name__=='__main__':
    main()

#22)PP to accept target value and print the combination two no whose addition leads to the target:::

l=[1,3,2,4,5,7,6,8,6,9]
target = int(input('Enter the number::'))
no=0
for i,j in enumerate(l):
    for k in l[i+1:]:
        if j+k==target:
            print((j,k))
            no+=1
print(no)

#------importanat::  l[i+1:]--->in slicing it does not show out of range error
#---->l[i+1]-----> in such case it will show if that indexed element not present

result=[(i,j ) for i in range(1,tg) for j in range(1,tg) if i+j==tg] #-------> is single condition --->at last
print(result)

#23)Generate a dictionary from a list ,Where value of key would be it's just next element
l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
d={}
while l:
    if len(l)==1:
        d[l[0]]=0
        l=None
    else:
        d[l[0]]=l[1]
    l=l[2:]
print(d)

l=[1,2,3,4,5]
d1={}
for i in range(0,len(l),2):           #------------->new one very interesting ---> too handle index out of range
    if i+1<len(l):
        d1[l[i]]=l[i+1]
    else:
        d1[l[i]]=0
print(d1)


l = [1, 2, 3, 4, 5]  # Replace this list with your own data
d = {l[i]: (l[i + 1] if i + 1 < len(l) else 0) for i in range(0, len(l), 2)}
print(d)

#--------------------------------------------------------------------------------------------------------
'''imp note::: Wnenever solving problems if there is chance of index out of 
                range always handle with range()-->take only required iterationn'''
#--------------------------------------------------------------------------------------------------------


#24)28-----[[1,2,3],[3,4,5],(6,7,8,9)]=[1,2,3,3,4,5,6,7,8,9]
l=[[1,2,3],[3,4,5],(6,7,8,9)]
res=[]
for i in l:
    for j in i:
        res.append(j)
print(res)

res=[j for i in l for j in i]
print(res)

'''25)Write a Python program which accepts a sequence of comma separated numbers from user and 
      generate a list and a tuple with those numbers'''

input=input('Enter the numbers:')
l=input.split(',')
print(l)

l1=[i for i in input if i.isnumeric()]
print(l1)


#25)  output=['1:a','2:b','3:c']
l=[1,2,3,4]
a=['a','b','c','d']

l1=[]
for i,j in enumerate(l):
    l1.append(f'{j}:{a[i]}')    #-----------> best way to concatt string and integer
print(l1)

res=[f'{j}:{a[i]}' for i,j in enumerate(l)]
print(res)

res_dict=[]
for i in zip(l,a):
    res_dict.append(f'{i[0]}:{i[1]}')
print(res_dict)

res1=list(map(lambda x,y:str(x)+':'+y,l,a)) #-------->most important concept
print(res1)

result1=[f'{k}:{a[i]}' for i,k in enumerate(l) ]
print(result1)

#26) remove 30 from below list::
l=[10,20,30,30,60,20]
l1=[]
for i in l:
    if i!=30:
        l1.append(i)
print(l1)

res=list(filter(lambda x: x!=30,l))
print(res)

print([i for i in l if i!=30])

#27)convert name into ascii number
name='Ajay'
no=str(ord(name[0]))      #-------->65-106-97-121
                           # to avoid   -65-106-97-121
for i in name[1:]:
    no=no+'-'+str(ord(i))
print(no)


#28)Roman-->number

roman=['II','IV','VII','XI','XXX']
d={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
res=[]
for i in roman:
    if i in d:
        res.append(d[i])
    else:
        no=0
        for j in i:
            no+=d[j]
        res.append(no)
print(res)

#29)
l='Avinash kute' #-----output=  A.kute
l1=l.split(' ')
print(l1[0][0]+'.'+l1[-1])

#30)l=['123123123','123123123','123123124']---->['123-123-123', '123-123-123', '123-123-124']
l1=[]
for i in l:
    res=i[:3]+'-'+i[3:6]+'-'+i[6:]
    l1.append(res)
print(l1)

l3=['987654321','987654321','987654321']
l4=[]
for item in l3:
    res='-'.join([item[i:i+3] for i in range(0,len(item),3)])
    l4.append(res)
print(l4)

print([f'{i[:n]}-{i[n:n+n]}-{i[n+n:]}' for i in l])

n=int(input('Enter the number::'))
re=[]
for i in l:
    l1 = []
    for j in range(0,len(i),n):  #------------>more dynamic
        l1.append(i[j:j+n])
    re.append('-'.join(l1))
print(re)

# find below output::
"""1 2 3 4 5
1 2 3 4
1 2 3
1 2
1"""

for i in range(1,7):
    for k in range(1,-i+7):
        print(k,end=' ')
    print()
#print diamond stars::
row=int(input('Enter the number::'))
for i in range(1,row+1):
    space=' '*(row-i)
    stars='* '*i
    print(space + stars.rstrip( ))
for k in range(1,row):
    space=' '*k
    stars='* '*(-k+row)
    print(space + stars.rstrip( ))



'''l2=['Adelia Clooney Zeidler(Sibling)','Monsita Ferrer(Cousin)','Rafael Ferrer(Cousin)',
    'Miguel Ferrer(Cousin)','Tessa Ferrer(Cousin)','Betty Clooney(Aunt or Uncle)','Rosemary Clooney(Aunt or Uncle)']'''
#output={'Adelia': 'Sibling', 'Monsita': 'Cousin', 'Rafael': 'Cousin', 'Miguel': 'Cousin', 'Tessa': 'Cousin', 'Betty': 'Uncle', 'Rosemary': 'Uncle'}
d={}
for i in l2:
    res=i.split(' ')
    d[res[0]]=res[-1].split('(')[-1][:-1]
print(d)

d1={i.split(' ')[0]:i.split(' ')[-1].split('(')[-1][:-1] for i in l2}
print(d1)

#output=Monsita Ferrer(Cousin) ----->having only cousin:
for k in l2:
    if k.endswith('(Cousin)'):
        print(k)

res=[i for i in l2 if i.endswith('(Cousin)')]
print(res)

#max function::
res=max(files,key=(lambda f:os.path.getctime(os.path.join(r'C:\Users\Admin\Desktop\practice',f)))))










