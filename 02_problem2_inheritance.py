# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog".
class Aminals:
    pass


class Pets(Aminals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("bow bow!")
d=Dog()
d.bark()

