class Parent(object):
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        super(Child, self).show_info()
        print("Number of toys - "+self.number_of_toys)

king_david = Parent("David", "blue")
king_solomon = Child("David", "green", "100000")
# print(king_david.eye_color)
# print(king_solomon.eye_color, king_solomon.number_of_toys)
king_solomon.show_info()

