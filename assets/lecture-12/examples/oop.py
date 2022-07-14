from inspect import cleandoc


class Person:
    # class attribute
    origin = 'Earth'

    def __init__(self, fn, ln):
        '''
        Constructor method
        '''
        self.first_name = fn        # instance attribute
        self.last_name = ln         # instance attribute

    @classmethod
    def from_full_name(cls, name):
        '''
        A class/factory method
        that creates a Person object
        from it's full name
        '''
        return cls(*name.split(' '))

    @staticmethod
    def get_definition():
        '''
        A static method. i.e a method that does not refer to any specific Person object
        '''
        return cleandoc(
            '''
            A person (plural people or persons) is a being that has certain capacities or attributes
            such as reason, morality, consciousness or self-consciousness,
            and being a part of a culturally established form of social relations
            such as kinship, ownership of property, or legal responsibility.
            The defining features of personhood and, consequently, what makes a person count as a person,
            differ widely among cultures and contexts.
            '''
        )

    def say_hello(self):
        '''
        An instance method
        '''
        print(f"Hi, I'm {self.first_name} {self.last_name} from {self.origin}!")

    def __repr__(self):
        '''
        Defining the representation of the Person objects
        '''
        return f'<Person {self.first_name=}, {self.last_name=}>'


class Student(Person):
    '''
    Student inherits from Person
    '''

    def __init__(self, fn, ln, rn):
        '''
        Constructor method
        '''
        super().__init__(fn, ln)    # Calling Person's constructor

        self.registration_number = rn
        self.__grades = []

    @property
    def grades(self):
        '''
        A getter for the _grades attribute
        '''
        return self.__grades

    @grades.setter
    def grades(self, new_grades):
        '''
        A setter for the _grades attribute
        '''
        if len(self.__grades) == 0:
            self.__grades = new_grades
        else:
            raise AttributeError('You cannot re-set the grades')

    def __repr__(self):
        '''
        Defining the representation of the Students objects
        '''
        return f'<Student {self.registration_number=}, {self.first_name=}, {self.last_name=}>'


p1 = Person('Guido', 'van Rossum')
p1.origin = 'awesomeland'
p1.say_hello()
print(repr(p1))

print('-' * 100)

p2 = Person('Ryan', 'Dahl')
p2.origin = 'your nightmares'
p2.say_hello()
print(repr(p2))

print('-' * 100)

p3 = Person.from_full_name('Jane Doe')
p3.say_hello()
print(repr(p3))

print('-' * 100)

s1 = Student('John', 'Doe', 12345)
s1.say_hello()
print(repr(s1))

print('-' * 100)

print(isinstance(p1, Person))
print(isinstance(p1, Student))
print(isinstance(s1, Person))
print(isinstance(s1, Student))

print('-' * 100)

print(Person.get_definition())
print(p1.get_definition())

print('-' * 100)

print(repr(s1.grades))
s1.grades = [9, 9, 9]
print(repr(s1.grades))
s1.grades = [10, 10, 10]
print(repr(s1.grades))
