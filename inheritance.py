class Animal():
    def __init__(self,age=0,name=""):
        self.age = age
        self.name=name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,new_age=0):
        self.age=new_age
    def set_name(self,new_name=""):
        self.name=new_name

class Cat(Animal):
    def speal(self):
        print("Meow!")
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self,age,name):
        Animal.__init__(self,age,name)
        self.friends = []
    # Override speak method
    def speak(self):
        print("Hello")
    def add_friend(self,new_friend):
        self.friends.append(new_friend)
    def age_diff(self,other):
        diff-self.age - other.age
        print(abs(diff),"year difference")
    def __str__(self):
        return "Person:"+str(self.name)+":"+str(self.age)+":"+str(len(self.friends))

class Student(Person):
    def __init__(self,age,name,major=None):
        Person.__init__(self,age,name)
        self.major=major
    def change_major(self,new_major):
        self.major=new_major
    def speak(self):
        print("Hey there, fella!")
    def __str__(self):
        return "Student:"+str(self.name)+":"+str(self.age)+":"+str(len(self.friends))+":"+str(self.major)

basic_animal=Animal(3,"Teddy")
cat = Cat(3,"Springles")
person =Person(30,"John von Neumann")
student = Student(24,"Nick","Computer Engineering")

basic_animal.set_age(1)
cat.set_age(1)
person.set_age(1)
student.set_age(1)

person.add_friend("Richard")
student.add_friend("Linus")

student.change_major("Computer Science")
print(basic_animal)
print(cat)
print(person)
print(student)

