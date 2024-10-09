list_a = [1, 2, 3]

list_b = [4, 5, 6]



print("# 리스트")

print("list_a = ", list_a)

print("list_b = ", list_b)

print()



print("# 리스트 기본 연산자")

print("list_a + list_b =", list_a + list_b)

print("list_a * 3 =", list_a * 3)

print()



print("# 길이 구하기")

print("len(list_a) = ", len(list_a))

list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")

list_a.append(4)

list_a.append(5)

print(list_a)

print()

print("# 리스트 중간에 요소 추가하기")

list_a.insert(0, 10)

print(list_a)

list_a = [0, 1, 2, 3, 4, 5]

print("# 리스트의 요소 하나 제거하기")

del list_a[1]

print("del list_a[1]:", list_a)

list_a.pop(2)

print("pop(2):", list_a)

array = [273, 32, 103, 57, 52]

for element in array:

    print(element)

dictionary = {

    "name": "7D 건조 망고",

    "type": "당절임",

    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],

    "origin": "필리핀"

}

print("name:", dictionary["name"])

print("type:", dictionary["type"])

print("ingredient:", dictionary["ingredient"])

print("origin:", dictionary["origin"])

print()

dictionary["name"] = "8D 건조 망고"

print("name:", dictionary["name"])

dictionary = {}

print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"

dictionary["head"] = "새로운 정신"

dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

dictionary = {

    "name": "7D 건조 망고",

    "type": "당절임"

    }

print("요소 제거 이전:", dictionary)

del dictionary["name"]

del dictionary["type"]

print("요소 제거 이후:", dictionary)

dictionary = {

    "name": "7D 건조 망고",

    "type": "당절임",

    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],

    "origin": "필리핀"

}

key = input("> 접근하고자 하는 키: ")

if key in dictionary:

    print(dictionary[key])

else:

    print("존재하지 않는 키에 접근하고 있습니다.")

dictionary = {

    "name": "7D 건조 망고",

    "type": "당절임",

    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],

    "origin": "필리핀"

}



value = dictionary.get("존재하지 않는 키")

print("값:", value)



if value == None:

    print("존재하지 않는 키에 접근했었습니다.")

dictionary = {

    "name": "7D 건조 망고",

    "type": "당절임",

    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],

    "origin": "필리핀"

    }
for key in dictionary:

    print(key, ":", dictionary[key])

for i in range(5):

    print(str(i) + "= 반복 변수")

print()

for i in range(5, 10):

    print(str(i) + "= 반복 변수")

print()

for i in range(0, 10, 3):

    print(str(i) + "= 반복 변수")

print()

array = [273, 32, 103, 57, 52]

for element in array:

    print(element)

array = [273, 32, 103, 57, 52]

for i in range(len(array)):

    print("{}번째 반복: {}".format(i, array[i]))

for i in range(4, 0 - 1, -1):

    print("현재 반복 변수: {}".format(i))

for i in reversed(range(5)):

    print("현재 반복 변수: {}".format(i))

while True:

    print(".", end="")

i = 0

while i < 10:

    print("{}번째 반복입니다.".format(i))

    i += 1

list_test = [1, 2, 1, 2]

value = 2

while value in list_test:

    list_test.remove(value)

print(list_test)

import time

number = 0

target_tick = time.time() + 5

while time.time() < target_tick:

    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))

i = 0

while True:

    print("{}번째 반복문입니다.".format(i))

    i = i + 1

    input_text = input("> 종료하시겠습니까?(y): ")

    if input_text in ["y", "Y"]:

        print("반복을 종료합니다.")

        break

numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:

    if number < 10:

        continue

    print(number)

example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")

print(example_list)

print()



print("# enumberate() 함수 적용 출력")

print(enumerate(example_list))

print()



print("# list() 함수로 강제 변환 출력")

print(list(enumerate(example_list)))

print()



print("# 반복문과 조합하기")

for i, value in enumerate(example_list):

    print("{}번째 요소는 {}입니다.".format(i, value))

list_a = [1, 2, 3, 4, 5]

list_reversed = reversed(list_a)

print("# reversed() 함수")

print("reversed([1, 2, 3, 4, 5]):", list_reversed)

print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))

print()



print("# reversed() 함수와 반복문")

print("for i in reversed([1, 2, 3, 4, 5]):")

for i in reversed(list_a):

    print("-", i)

example_dictionary = {

    "키A": "값A",

    "키B": "값B",

    "키C": "값C",

    }

print("# 딕셔너리의 items() 함수")

print("items():", example_dictionary.items())

print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():

    print("dictionary[{}] = {}".format(key, element))

array = []

for i in range(0, 20, 2):

    array.append(i * i)

print(array)

array = [i * i for i in range(0, 20, 2)]

print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]

output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)

number = int(input("정수 입력> "))

if number % 2 == 0:

    print("""\

        입력한 문자열은 {}입니다.

        {}는(은) 짝수입니다.""".format(number, number))

else:

    print("""\

        입력한 문자열은 {}입니다.

        {}는(은) 홀수입니다.""".format(number, number))

number = int(input("정수 입력> "))



if number % 2 == 0:

    print("""입력한 문자열은 {}입니다.

{}는(은) 짝수입니다.""".format(number, number))

else:

    print("""입력한 문자열은 {}입니다.

{}는(은) 홀수입니다.""".format(number, number))

number = int(input("정수 입력> "))



if number % 2 == 0:

    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))

else:

    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))

test = (

    "이렇게 입력해도 "

    "하나의 문자열로 연결 "

    "생성됩니다."

)

print("test:", test)

print("type(test):", type(test))

number = int(input("정수 입력> "))



if number % 2 == 0:

    print((

        "입력한 문자열은 {}입니다.\n"

        "{}는(은) 짝수입니다."

    ).format(number, number))

else:

    print((

        "입력한 문자열은 {}입니다.\n"

        "{}는(은) 홀수입니다."

    ).format(number, number))




number = int(input("정수 입력> "))

if number % 2 == 0:

    print("\n".join([

        "입력한 문자열은 {}입니다.",

        "{}는(은) 짝수입니다."

    ]).format(number, number))

else:

    print("\n".join([

        "입력한 문자열은 {}입니다.",

        "{}는(은) 홀수입니다."

    ]).format(number, number))

numbers = [1, 2, 3, 4, 5, 6]

r_num = reversed(numbers)


print("reversed_numbers :", r_num)

print(next(r_num))

print(next(r_num))

print(next(r_num))

print(next(r_num))

print(next(r_num))

