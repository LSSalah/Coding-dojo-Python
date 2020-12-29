class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for i in nums:
            self.result = self.result + i
        return self

    def subtract(self, *nums):
        for i in nums:
            self.result = self.result - i
        return self


x = MathDojo().add(2).add(2,5,1).subtract(3,2).result
print(x)