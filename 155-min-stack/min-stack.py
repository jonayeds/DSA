class MinStack(object):
    stack=[]
    minimum={}
    def __init__(self):
        self.stack=[]
        self.minimum={}
        pass

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        length=len(self.stack)
        min_val=val if length==1 or self.minimum[length-1]>val else self.minimum[length-1]
        self.minimum[length]=min_val

    def pop(self):
        """
        :rtype: None
        """
        length = len(self.stack)
        self.stack.pop()
        self.minimum[length]=None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[len(self.stack)]