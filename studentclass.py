class Student:
    def __init__(self, name, age, gender, level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
    def setName(self, name):
        print(name)
    def setAge(self, age):
        print(age)
    def setGender(self, gender):
        print(gender)
    def setLevel(self, level):
        print(level)

obj = Student("Aarav", 14, "male", "100")
print(obj.gender)
print(obj.setAge(2))