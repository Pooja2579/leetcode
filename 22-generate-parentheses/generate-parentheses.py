class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      res = []

      def backtrack(current, openN, closedN):
        if len(current) == 2*n:
            res.append(current)
            return
        if openN<n:
            backtrack(current +'(', openN+1, closedN)
        if closedN < openN:
            backtrack(current+')', openN, closedN+1)
      backtrack("", 0, 0)
      return res
