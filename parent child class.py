#Inheritance

class pet:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def information(self):
        print(self.name+" is "+str(self.age))

class cat(pet):
    def __init__(self,name ,age , type, sound):
        self.type = type
        self.sound = sound

        pet.__init__(self, name, age)

    def show(self):
        print(self.name+" is "+str(self.age)+". And it is a "+self.type+". Sound like "+self.sound)

if __name__ == '__main__':
    kitty = cat("kitty", 8, "cat", "meonmeon")
    kitty.information()
    kitty.show()

    muffy = cat("muffy", 2, "cat", "nono")
    muffy.information()
    muffy.show()

