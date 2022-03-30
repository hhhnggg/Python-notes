class cat:
    name = "kitty"
    age = 8

def main():
    muffy = cat()
    print(muffy.name + " is " + str(muffy.age))

def other():
    muffy = cat()
    muffy.name = "muffy"
    muffy.age = 2
    print(muffy.name + " is " + str(muffy.age))

if __name__ == '__main__':
    main()
    other()