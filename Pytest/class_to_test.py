

class SomeClassToTest():

    def __init__(self,value):
        self.value = value


    def sum(self,a,b):
        print('Returning sum of 2 numbers'+str(a+b+self.value))
        return a+b+self.value