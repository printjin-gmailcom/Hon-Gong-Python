def print_3_times():

    print("안녕하세요")

    print("안녕하세요")

    print("안녕하세요")

print_3_times()

def print_n_times(value, n):

    for i in range(n):

        print(value)

print_n_times("안녕하세요", 5)

def print_n_times(n, *values):

    for i in range(n):

        for value in values:

            print(value)

        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

def print_n_times(value, n=2):

    for i in range(n):

        print(value)

print_n_times("안녕하세요")

def print_n_times(*values, n=2):

    for i in range(n):

        for value in values:

            print(value)

        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

def test(a, b=10, c=100):

    print(a + b + c)



test(10, 20, 30)

test(a=10, b=100, c=200)

test(c=10, a=100, b=200)

test(10, c=200)

def return_test():

    print("A 위치입니다.")

    return # 리턴합니다.

    print("B 위치입니다.")

return_test()

def return_test():

    return 100



value = return_test()

print(value)

def sum_all(start, end):

    output = 0

    for i in range(start, end + 1):

        output += i

    return output



print("0 to 100:", sum_all(0, 100))

print("0 to 1000:", sum_all(0, 1000))

print("50 to 100:", sum_all(50, 100))

print("500 to 1000:", sum_all(500, 1000))

def sum_all(start=0, end=100, step=1):

    output = 0

    for i in range(start, end + 1, step):

        output += i

    return output



print("A.", sum_all(0, 100, 10))

print("B.", sum_all(end=100))

print("C.", sum_all(end=100, step=2))

def factorial(n):

    output = 1

    for i in range(1, n + 1):

        output *= i

    return output



print("1!:", factorial(1))

print("2!:", factorial(2))

print("3!:", factorial(3))

print("4!:", factorial(4))

print("5!:", factorial(5))

def factorial(n):

    if n == 0:

        return 1

    else:

        return n * factorial(n - 1)



print("1!:", factorial(1))

print("2!:", factorial(2))

print("3!:", factorial(3))

print("4!:", factorial(4))

print("5!:", factorial(5))

def fibonacci(n):

    if n == 1:

        return 1

    if n == 2:

        return 1

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)



print("fibonacci(1):", fibonacci(1))

print("fibonacci(2):", fibonacci(2))

print("fibonacci(3):", fibonacci(3))

print("fibonacci(4):", fibonacci(4))

print("fibonacci(5):", fibonacci(5))

counter = 0

def fibonacci(n):

    print("fibonacci({})를 구합니다.".format(n))

    global counter

    counter += 1

    if n == 1:

        return 1

    if n == 2:

        return 1

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)

print("---")

print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

counter = 0

def fibonacci(n):

    counter += 1

    if n == 1:

        return 1

    if n == 2:

        return 1

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

dictionary = {

    1: 1,

    2: 2

}



def fibonacci(n):

    if n in dictionary:

        return dictionary[n]

    else:

        output = fibonacci(n - 1) + fibonacci(n - 2)

        dictionary[n] = output

        return output



print("fibonacci(10):", fibonacci(10))

print("fibonacci(20):", fibonacci(20))

print("fibonacci(30):", fibonacci(30))

print("fibonacci(40):", fibonacci(40))

print("fibonacci(50):", fibonacci(50))

[a, b] = [10, 20]

(c, d) = (10, 20)

print("a:", a)

print("b:", b)

print("c:", c)

print("d:", d)

tuple_test = 10, 20, 30, 40

print("# 괄호가 없는 튜플의 값과 자료형 출력")

print("tuple_test:", tuple_test)

print("type(tuple_test):", type(tuple_test))

print()

a, b, c = 10, 20, 30

print("# 괄호가 없는 튜플을 활용한 할당")

print("a:", a)

print("b:", b)

print("c:", c)

a, b = 10, 20

print("# 교환 전 값")

print("a:", a)

print("b:", b)

print()

a, b = b, a

print("# 교환 후 값")

print("a:", a)

print("b:", b)

print()

def test():

    return (10, 20)

a, b = test()

print("a:", a)

print("b:", b)

def call_10_times(func):

    for i in range(10):

        func()



def print_hello():

    print("안녕하세요")



call_10_times(print_hello)

def power(item):

    return item * item

def under_3(item):

    return item < 3



list_input_a = [1, 2, 3, 4, 5]



output_a = map(power, list_input_a)

print("# map() 함수의 실행 결과")

print("map(power, list_input_a):", output_a)

print("map(power, list_input_a):", list(output_a))

print()



output_b = filter(under_3, list_input_a)

print("# filter() 함수의 실행 결과")

print("filter(under_3, list_input_a):", output_b)

print("filter(under_3, list_input_a):", list(output_b))

power = lambda x: x * x

under_3 = lambda x: x < 3



list_input_a = [1, 2, 3, 4, 5]



output_a = map(power, list_input_a)

print("# map() 함수의 실행 결과")

print("map(power, list_input_a):", output_a)

print("map(power, list_input_a):", list(output_a))

print()



output_b = filter(under_3, list_input_a)

print("# filter() 함수의 실행 결과")

print("filter(under_3, list_input_a):", output_b)

print("filter(under_3, list_input_a):", list(output_b))

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)

print("# map() 함수의 실행 결과")

print("map(power, list_input_a):", output_a)

print("map(power, list_input_a):", list(output_a))

print()





output_b = filter(lambda x: x < 3, list_input_a)

print("# filter() 함수의 실행 결과")

print("filter(under_3, list_input_a):", output_b)

print("filter(under_3, list_input_a):", list(output_b))

file = open("basic.txt", "w")

file.write("Hello Python Programming...!")


file.close()

with open("basic.txt", "r") as file:

    contents = file.read()

print(contents)

import random

hanguls = list("가나다라마바사아자차카타파하")



with open("info.txt", "w") as file:

    for i in range(1000):

        name = random.choice(hanguls) + random.choice(hanguls)

        weight = random.randrange(40, 100)

        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))


with open("info.txt", "r") as file:

    for line in file:

        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):

            continue

        bmi = int(weight) / ((int(height) / 100) **2)

        result = ""

        if 25 <= bmi:

            result = "과체중"

        elif 18.5 <= bmi:

            result = "정상 체중"

        else:

            result = "저체중"

        print('\n'.join([

            "이름: {}",

            "몸무게: {}",

            "키: {}",

            "BMI: {}",

            "결과: {}"

        ]).format(name, weight, height, bmi, result))

        print()

def test():

    print("함수가 호출되었습니다.")

    yield test

print("A 지점 통과")

test()

print("B 지점 통과")

test()

print(test())



def test():

    print("A 지점 통과")

    yield 1

    print("B 지점 통과")

    yield 2

    print("C 지점 통과")

output = test()



print("D 지점 통과")

a = next(output)

print(a)



print("E 지점 통과")

b = next(output)

print(b)



print("F 지점 통과")

c = next(output)

print(c)



next(output)

