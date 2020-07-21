#Method overriding
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print('This is ', +self.name, 'He is ', +self.age, 'years old')

class Student(Person):
    def __init__(self, roll_no, grade, result):
        super().__init__(name='John', age=13)
        self.roll_no = roll_no
        self.grade = grade
        self.result = result

    def details(self):
        return 'This is '  +self.name, 'His roll no is: ',   self.roll_no,  self.grade, 'his result is '  +self.result


John=Student(113, '6B','pass' )

print(John.details())


'''class Student():
    def __init__(self, f_name, l_name, age, math ,chem, phy):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.math = math
        self.chem = chem
        self.phy = phy

    def details(self):
        return 'details of ' + self.f_name + ' ' + self.l_name + ' SHe is:',self.age, 'of years old'

    def avg(self):
        return (self.math+self.chem+self.phy)/3

    #def set_f_name(self, f_name):
        #self.f_name=f_name

    def set_f_name(self, f_name, l_name= ''):
        if l_name:
            self.l_name = l_name
        
        self.f_name = f_name

Neha = Student('neha','joshi', 22, 34, 45, 23)
print(Neha.details())
print('Average of her marks are: ', Neha.avg())
Neha.set_f_name ('Priya', 'Modi')
print(Neha.details())'''







