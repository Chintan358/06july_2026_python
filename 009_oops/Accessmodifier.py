class Demo:
    
    name = "test"
    _email = "test@gmial.com"
    __age = 30
    
    def test(self):
        print(self.name,self._email,self.__age)
        
d = Demo()
d.name="xyz"
d._email="xyz@gmial.com"
d._Demo__age=100
d.test()