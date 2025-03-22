class Base:
    def who_am_i(self):
        print("I am Base")
        
class Left(Base):
    def who_am_i(self):
        print("I am Left")
            
class Right(Base):
    def who_am_i(self):
        print("I am Right")

class Bottom(Left, Right):
    pass
        
bootom = Bottom()
bootom.who_am_i()
        
            