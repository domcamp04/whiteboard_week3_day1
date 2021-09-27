# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
 
def fizz(n):
    lst = []
    for i in range (1, n + 1):
        if i % 3  == 0 and i % 5 == 0:
            lst.append('FizzBuzz')
        elif i % 3 == 0:
            lst.append('Fizz')
        elif i % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(str(i))
    print(lst)

    

print(fizz(15))

    
        
#         else i /= 3
#         i == 'fizz'






# ex1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# ex2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# ex3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]