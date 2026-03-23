#Method Overriding
#--> OOP concept in which a function which is already defined in a superclass (Parent class) is redefiend within the subclass so that it gives a different output
#This method is used when we want to inherit certain properties from the superclass but also want to have a different output for certain functions for the subclass

class Vehicle:

    def move(self):
        print("The Vehicle is moving")

class Car(Vehicle):

    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):

    def move(self):
        print("Pedaling on the road")


Car1 = Car()
Bike1 = Bicycle()

Car1.move()
Bike1.move()


#Method Overloading

#--> OOP concept in which a class has a function / method which can behave differently based on the amount of parameters passed
#i.e, a class where a method with the same name can perform multiple operations


class Calculator:

    def add(self,n1,n2,n3=0,n4=0):
        self.n1=n1
        self.n2=n2

        print(n1+n2+n3+n4)

if __name__ == "__main__":

    calc = Calculator()

    calc.add(1,2)
    calc.add(1,2,3)
    calc.add(1,2,3,4)
