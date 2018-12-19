class A():
    def __init__(self, a=0, b=0):
        self._a = 0
        self.__b = 0
    def zz(self):
        print("123460")

c = A()
# print(c._a)
print(c._A__b)
print('hehe')

print('today is good day')
c.zz()
