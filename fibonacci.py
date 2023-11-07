#0,1,1,2,3,5,8
#without recursion:
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#recursion
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return (self.fib(n-1)+self.fib(n-2))
#----------------------------------------------------------------
#Python program to find nth Fibonacci number
f = [0,1]
print(len(f))
def fibonacci(n):
   if n < len(f):
       return f[n]
   else:
       f.append(fibonacci(n-1) + fibonacci(n-2))
       return(f[n])
   
nterms = int(input("n value = "))
print(fibonacci(nterms))

#without recursion
class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        count = 0
        if n <= 1:
            return n
        else:
            while count < n:
                nnext = n1+n2
                n1 = n2
                n2 = nnext
                count +=1
            return n1
