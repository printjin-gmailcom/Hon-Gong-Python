user_input_a = input("정수 입력> ")



if user_input_a.isdigit():

    number_input_a = int(user_input_a)

    print("원의 반지름:", number_input_a)

    print("원의 둘레:", 2 * 3.14 * number_input_a)

    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

else:

    print("정수를 입력하지 않았습니다.")

try:

    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)

    print("원의 둘레:", 2 * 3.14 * number_input_a)

    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except:

    print("무언가 잘못되었습니다.")

list_input_a = ["52", "273", "32", "스파이", "103"]



list_number = []

for item in list_input_a:

    try:

        float(item)

        list_number.append(item)

    except:

        pass



print("{} 내부에 있는 숫자는".format(list_input_a))

print("{}입니다.".format(list_number))

try:

    number_input_a = int(input("정수 입력> "))

except:

    print("정수를 입력하지 않았습니다.")

else:

    print("원의 반지름:", number_input_a)

    print("원의 둘레:", 2 * 3.14 * number_input_a)

    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

try:

    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)

    print("원의 둘레:", 2 * 3.14 * number_input_a)

    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except:

    print("정수를 입력하지 않았습니다.")

else:

    print("예외가 발생하지 않았습니다.")

finally:

    print("일단 프로그램이 어떻게든 끝났습니다.")

try:

    # 파일을 엽니다.

    file = open("info.txt", "w")

    file.close()

except Exception as e:

    print(e)



print("# 파일이 제대로 닫혔는지 확인하기")

print("file.closed:", file.closed)

try:

    file = open("info.txt", "w")

    file.close()

    예외.발생해라()

except Exception as e:

    print(e)



print("# 파일이 제대로 닫혔는지 확인하기")

print("file.closed:", file.closed)

try:

    file = open("info.txt", "w")

    예외.발생해라()

except Exception as e:

    print(e)

finally:

    file.close()



print("# 파일이 제대로 닫혔는지 확인하기")

print("file.closed:", file.closed)

try:

    file = open("info.txt", "w")

    예외.발생해라()

except Exception as e:

    print(e)



file.close()

print("# 파일이 제대로 닫혔는지 확인하기")

print("file.closed:", file.closed)

def test():

    print("test() 함수의 첫 줄입니다.")

    try:

        print("try 구문이 실행되었습니다.")

        return

        print("try 구문의 return 키워드 뒤입니다.")

    except:

        print("except 구문이 실행되었습니다.")

    else:

        print("else 구문이 실행되었습니다.")

    finally:

        print("finally 구문이 실행되었습니다.")

    print("test() 함수의 마지막 줄입니다.")



test()

def write_text_file(filename, text):

    try:

        file = open(filename, "w")

        return

        file.write(text)

    except Exception as e:

        print(e)

    finally:

        file.close()



write_text_file("test.txt", "안녕하세요!")

print("프로그램이 시작되었습니다.")



while True:

    try:

        print("try 구문이 실행되었습니다.")

        break

        print("try 구문의 break 키워드 뒤입니다.")

    except:

        print("except 구문이 실행되었습니다.")

    finally:

        print("finally 구문이 실행되었습니다.")

    print("while 반복문의 마지막 줄입니다.")

print("프로그램이 종료되었습니다.")

try:

    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)

    print("원의 둘레:", 2 * 3.14 * number_input_a)

    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

except Exception as exception:

    print("type(exception):", type(exception))

    print("exception:", exception)

list_number = [52, 273, 32, 72, 100]



try:

    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

except Exception as exception:

    print("type(exception):", type(exception))

    print("exception:", exception)

list_number = [52, 273, 32, 72, 100]



try:

    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

except ValueError:

    print("정수를 입력해 주세요!")

except IndexError:

    print("리스트의 인덱스를 벗어났어요!")

list_number = [52, 273, 32, 72, 100]



try:

    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

except ValueError as exception:

    print("정수를 입력해 주세요!")

    print("exception:", exception)

except IndexError as exception:

    print("리스트의 인덱스를 벗어났어요!")

    print("exception:", exception)

list_number = [52, 273, 32, 72, 100]



try:

    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

    예외.발생해주세요()

except ValueError as exception:

    print("정수를 입력해 주세요!")

    print(type(exception), exception)

except IndexError as exception:

    print("리스트의 인덱스를 벗어났어요!")

    print(type(exception), exception)

list_number = [52, 273, 32, 72, 100]



try:

    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

    예외.발생해주세요()

except ValueError as exception:

    print("정수를 입력해 주세요!")

    print(type(exception), exception)

except IndexError as exception:

    print("리스트의 인덱스를 벗어났어요!")

    print(type(exception), exception)

except Exception as exception:

    print("미리 파악하지 못한 예외가 발생했습니다.")

    print(type(exception), exception)

