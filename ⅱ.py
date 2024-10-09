print("이름\t나이\t지역")

print("윤인성\t25\t강서구")

print("윤아린\t24\t강서구")

print("구름\t3\t강서구")

print("문자 선택 연산자에 대해 알아볼까요?")

print("안녕하세요"[0])

print("안녕하세요"[1])

print("안녕하세요"[2])

print("안녕하세요"[3])

print("안녕하세요"[4])

print("문자 선택 연산자에 대해 알아볼까요?")

print("안녕하세요"[-1])

print("안녕하세요"[-2])

print("안녕하세요"[-3])

print("안녕하세요"[-4])

print("안녕하세요"[-5])

pi=3.14159265

r=10

print("원주율 =", pi)

print("반지름 =", r)

print("원의 둘레 =", 2*pi*r)

print("원의 넓이 =", pi*r*r)

string=input("입력> ")

print("자료:", string)

print("자료형:", type(string))

string = input("입력> ")

print("입력 + 100:", string + 100)

string_a=input("입력A> ")

int_a=int(string_a)

string_b=input("입력B> ")

int_b=int(string_b)



print("문자열 자료:", string_a+string_b)

print("숫자 자료:", int_a+int_b)

output_a=int("52")

output_b=float("52.273")

print(type(output_a), output_a)

print(type(output_b), output_b)

input_a=float(input("첫 번째 숫자> "))

input_b=float(input("두 번째 숫자> "))



print("덧셈 결과:", input_a + input_b)

print("뺄셈 결과:", input_a - input_b)

print("곱셈 결과:", input_a * input_b)

print("나눗셈 결과:", input_a / input_b)

output_a = str(52)

output_b = str(52.273)

print(type(output_a), output_a)

print(type(output_b), output_b)

string_a = "{}".format(10)

print(string_a)

print(type(string_a))

format_a="{}만 원".format(5000)

format_b="파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)

format_c="{} {} {}".format(3000, 4000, 5000)

format_d="{} {} {}".format(1, "문자열", True)



print(format_a)

print(format_b)

print(format_c)

print(format_d)

output_a="{:d}".format(52)

output_b="{:5d}".format(52)

output_c="{:10d}".format(52)

output_d="{:05d}".format(52)

output_e="{:05d}".format(-52)

print("# 기본")

print(output_a)

print("# 특정 칸에 출력하기")

print(output_b)

print(output_c)

print("# 빈 칸을 0으로 채우기")

print(output_d)

print(output_e)

output_f="{:+d}".format(52)

output_g="{:+d}".format(-52)

output_h="{: d}".format(52)

output_i="{: d}".format(-52)



print("# 기호와 함께 출력하기")

print(output_f)

print(output_g)

print(output_h)

print(output_i)

output_h="{:+5d}".format(52)

output_i="{:+5d}".format(-52)

output_j="{:=+5d}".format(52)

output_k="{:=+5d}".format(-52)

output_l="{:+05d}".format(52)

output_m="{:+05d}".format(-52)

print("# 조합하기")

print(output_h)

print(output_i)

print(output_j)

print(output_k)

print(output_l)

print(output_m)

output_a="{:f}".format(52.273)

output_b="{:15f}".format(52.273)

output_c="{:+15f}".format(52.273)

output_d="{:+015f}".format(52.273)

print(output_a)

print(output_b)

print(output_c)

print(output_d)

output_a="{:15.3f}".format(52.273)

output_b="{:15.2f}".format(52.273)

output_c="{:15.1f}".format(52.273)



print(output_a)

print(output_b)

print(output_c)

output_a = 52.0

output_b = "{:g}".format(output_a)

print(output_a)

print(output_b)

