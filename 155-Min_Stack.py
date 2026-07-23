class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.minstack or self.minstack[-1] >= value:
            self.minstack.append(value)
        return self.stack.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
