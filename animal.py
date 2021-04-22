class Dog:
    def make_sound(self):
        print("woof")
class Duck:
    def make_sound(self):
        print("quack")

def main():
    dog = Dog()
    dog.make_sound()
    duck = Duck()
    duck.make_sound()

if __name__ == "__main__":
    main()