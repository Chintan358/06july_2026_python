class Sample:
    
    __id = 20
    
    def set(self,id):
        self.__id=id
        
    def get(self):
        print(self.__id)
        
        
s = Sample()
s.set(100)
s.get()