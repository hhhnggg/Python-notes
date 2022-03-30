class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name+" is "+str(self.age))

if __name__ == '__main__':
    kitty = cat("kitty", 8)
    muffy = cat("muffy", 2)
    kitty.show()
    muffy.show()