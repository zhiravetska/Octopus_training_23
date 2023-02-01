# class Car():
# ... def exclaim(self):
# ... print("I'm a Car!")

# car = Car()
# car.exclaim()
# I'm a Car!

# class Person():
#     def __init__(self, name):
#         self.name = name


# hunter = Person('Elmer Fudd')
# hunter.name
# print('The mighty hunter: ', hunter.name)


# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name


# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"


# person = Person('Fudd')
# doctor = MDPerson('Fudd')
# lawyer = JDPerson('Fudd')
# print(person.name)

# print(doctor.name)

# print(lawyer.name)


# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email


# bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
# bob.name
# bob.email

# print(bob.name)
# print(bob.email)

class Circle():
    # radius - eto atribut
    def __init__(self, radius):
        self.raduis = radius
#  diameter - eto svoistvo atributa
    def diameter(self):
        return 2*self.raduis
radius = 5

diameter = Circle(diameter.self)

print(diameter)

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name

#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name

#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#         # zdesj metodi get_name i set_name
#         # ukazivajutsja kak svojstva atributa name
#     name = property(get_name, set_name)


# fowl = Duck('Howard')
# fowl.name
# print(fowl.name)
