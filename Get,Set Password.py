class Password:
    def __init__(self):
        self.__password = "" 

    def set_password(self, pwd):
        self.__password = pwd  

    def get_password(self):
        return self.__password  


p = Password()
p.set_password("mySecret123")
print(p.get_password())  
