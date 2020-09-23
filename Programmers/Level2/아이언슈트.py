def solution(n):
    ans = 0
    def dp(n):

        if(n==1):
            return 1

        elif(n%2==1):
            return dp(n//2) + 1

        else:
            return dp(n//2)
    
    
    ans = dp(n)
    return ans