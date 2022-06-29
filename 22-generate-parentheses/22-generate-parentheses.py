class Solution:
    def generateParenthesis(self, n):
        result = []
        self.dfs(n,result,'',0,0)
        return result

    def dfs(self,n,result,path,left,right):
        # check if the current path is valid
        if not self.isValid(left,right,n):
            return
        # check we are at the right length
        if len(path) == n*2:
            result.append(path)
            return
        self.dfs(n,result,path+'(',left+1,right)
        self.dfs(n,result,path+')',left,right+1)
    
    def isValid(self,left,right,n):
        # left paren <= right paren
        # left paren <= n
        # right paren >= n
        return left >= right and left <= n and right <= n