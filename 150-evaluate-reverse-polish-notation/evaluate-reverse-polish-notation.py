class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result=[]
        for t in tokens:
            if t in ['+','-','*','/']:
                num1=int(result[len(result)-1])
                result.pop()
                num2=int(result[len(result)-1])
                result.pop()
                res=0
                match t:
                    case '+':
                        res=num1+num2
                    case '-':
                        res=num2-num1
                    case '*':
                        res=num1*num2
                    case '/':
                        res=int(num2/num1)
                result.append(res)

            else:
                result.append(t)

        return int(result[0])