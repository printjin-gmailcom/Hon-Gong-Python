def create_student(name, korean, math, english, science):

    return {

        "name": name,

        "korean": korean,

        "math": math,

        "english": english,

        "science": science

    }



students = [
    create_student("윤인성", 87, 98, 88, 95),

    create_student("연하진", 92, 98, 96, 98),

    create_student("구지연", 76, 96, 94, 90),

    create_student("나선주", 98, 92, 96, 92),

    create_student("윤아린", 95, 98, 98, 98),

    create_student("윤명월", 64, 88, 92, 92)
]



print("이름", "총점", "평균", sep="\t")

for student in students:

    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]

    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")

def create_student(name, korean, math, english, science):

    return {

        "name": name,

        "korean": korean,

        "math": math,

        "english": english,

        "science": science

    }



def student_get_sum(student):

    return student["korean"] + student["math"] + student["english"] + student["science"]



def student_get_average(student):

    return student_get_sum(student) / 4



def student_to_string(student):

    return "{}\t{}\t{}".format(

        student["name"],

        student_get_sum(student),

        student_get_average(student))



students = [

    create_student("윤인성", 87, 98, 88, 95),

    create_student("연하진", 92, 98, 96, 98),

    create_student("구지연", 76, 96, 94, 90),

    create_student("나선주", 98, 92, 96, 92),

    create_student("윤아린", 95, 98, 98, 98),

    create_student("윤명월", 64, 88, 92, 92)

]



print("이름", "총점", "평균", sep="\t")

for student in students:

    # 출력합니다.

    print(student_to_string(student))

class Student:

    def __init__(self, name, korean, math, english, science):

        self.name = name

        self.korean = korean

        self.math = math

        self.english = english

        self.science = science



    def get_sum(self):

        return self.korean + self.math +  self.english + self.science



    def get_average(self):

        return self.get_sum() / 4



    def to_string(self):

        return "{}\t{}\t{}".format(\

            self.name,\

            self.get_sum(),\

            self.get_average())



students = [

    Student("윤인성", 87, 98, 88, 95),

    Student("연하진", 92, 98, 96, 98),

    Student("구지연", 76, 96, 94, 90),

    Student("나선주", 98, 92, 96, 92),

    Student("윤아린", 95, 98, 98, 98),

    Student("윤명월", 64, 88, 92, 92)

]



print("이름", "총점", "평균", sep="\t")

for student in students:

    print(student.to_string())

class Student:

    def study(self):

        print("공부를 합니다.")



class Teacher:

    def teach(self):

        print("학생을 가르칩니다.")



classroom = [Student(), Student(), Teacher(), Student(), Student()]



for person in classroom:

    if isinstance(person, Student):

        person.study()

    elif isinstance(person, Teacher):

        person.teach()

class Student:

    def __init__(self, name, korean, math, english, science):

        self.name = name

        self.korean = korean

        self.math = math

        self.english = english

        self.science = science



    def get_sum(self):

        return self.korean + self.math + self.english + self.science



    def get_average(self):

        return self.get_sum() / 4



    def __str__(self):

        return "{}\t{}\t{}".format(

            self.name,

            self.get_sum(),

            self.get_average())



students = [

    Student("윤인성", 87, 98, 88, 95),

    Student("연하진", 92, 98, 96, 98),

    Student("구지연", 76, 96, 94, 90),

    Student("나선주", 98, 92, 96, 92),

    Student("윤아린", 95, 98, 98, 98),

    Student("윤명월", 64, 88, 92, 92)

]



print("이름", "총점", "평균", sep="\t")

for student in students:

    print(str(student))

class Student:

    count = 0



    def __init__(self, name, korean, math, english, science):

        self.name = name

        self.korean = korean

        self.math = math

        self.english = english

        self.science = science



        Student.count += 1

        print("{}번째 학생이 생성되었습니다.".format(Student.count))





students = [

    Student("윤인성", 87, 98, 88, 95),

    Student("연하진", 92, 98, 96, 98),

    Student("구지연", 76, 96, 94, 90),

    Student("나선주", 98, 92, 96, 92),

    Student("윤아린", 95, 98, 98, 98),

    Student("윤명월", 64, 88, 92, 92)

]



print()

print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))

class Test:

    def __init__(self, name):

        self.name = name

        print("{} - 생성되었습니다".format(self.name))

    def __del__(self):

        print("{} - 파괴되었습니다".format(self.name))



a = Test("A")

b = Test("B")

c = Test("C")

import math



class Circle:

    def __init__(self, radius):

        self.__radius = radius

    def get_circumference(self):

        return 2 * math.pi *  self.__radius

    def get_area(self):

        return math.pi * (self.__radius ** 2)



circle = Circle(10)

print("# 원의 둘레와 넓이를 구합니다.")

print("원의 둘레:", circle.get_circumference())

print("원의 넓이:", circle.get_area())

print()



print("# __radius에 접근합니다.")

print(circle.__radius)

import math



class Circle:

    def __init__(self, radius):

        self.__radius = radius

    def get_circumference(self):

        return 2 * math.pi *  self.__radius

    def get_area(self):

        return math.pi * (self.__radius ** 2)



    def get_radius(self):

        return self.__radius

    def set_radius(self, value):

        self.__radius = value



circle = Circle(10)

print("# 원의 둘레와 넓이를 구합니다.")

print("원의 둘레:", circle.get_circumference())

print("원의 넓이:", circle.get_area())

print()



print("# __radius에 접근합니다.")

print(circle.get_radius())

print()



circle.set_radius(2)

print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")

print("원의 둘레:", circle.get_circumference())

print("원의 넓이:", circle.get_area())

class Parent:

    def __init__(self):

        self.value = "테스트"

        print("Parent 클래스의 __init()__ 메서드가 호출되었습니다.")

    def test(self):

        print("Parent 클래스의 test() 메서드입니다.")



class Child(Parent):

    def __init__(self):

        Parent.__init__(self)

        print("Child 클래스의 __init()__ 메서드가 호출되었습니다.")



child = Child()

child.test()

print(child.value)

class CustomException(Exception):

    def __init__(self):

        Exception.__init__(self)



raise CustomException

class CustomException(Exception):

    def __init__(self):

        Exception.__init__(self)

        print("##### 내가 만든 오류가 생성되었어요! #####")

    def __str__(self):

        return "오류가 발생했어요"



raise CustomException

class CustomException(Exception):

    def __init__(self, message, value):

        Exception.__init__(self)

        self.message = message

        self.value = value



    def __str__(self):

        return self.message



    def print(self):

        print("###### 오류 정보 ######")

        print("메시지:", self.message)

        print("값:", self.value)



try:

    raise CustomException("딱히 이유 없음", 273)

except CustomException as e:

    e.print()

