class father:
    def work(self):
        print("working")
    def eat(self):
        print("eating")
class mother:
    def work(self):
        print("working")
    def cooking(self):
        print("cooking")
class child(father,mother):
    pass
c=child()     
c.work()   
class sibling(father,mother):
    def study(self):
        print(" is a student")
s = sibling()
s.study()                   