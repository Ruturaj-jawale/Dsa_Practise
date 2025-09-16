def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def replaceNonCoprimes(self, nums):
        stack = []
    
        for num in nums:
            stack.append(num)
            
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)   # custom gcd
                
                if g > 1:
                    lcm = a * b // g
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        
        return stack
