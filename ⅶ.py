import random

print("# random 모듈")



print("- random():", random.random())

print("- uniform(10, 20):", random.uniform(10, 20))

print("- randrange(10)", random.randrange(10))

print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))

import sys

print(sys.argv)

print("---")



print("getwindowsversion:()", sys.getwindowsversion())

print("---")

print("copyright:", sys.copyright)

print("---")

print("version:", sys.version)



sys.exit()

import os



print("현재 운영체제:", os.name)

print("현재 폴더:", os.getcwd())

print("현재 폴더 내부의 요소:", os.listdir())



os.mkdir("hello")

os.rmdir("hello")



with open("original.txt", "w") as file:

    file.write("hello")

os.rename("original.txt", "new.txt")



os.remove("new.txt")

# os.unlink("new.txt")



os.system("dir")

import datetime



print("# 현재 시각 출력하기")

now = datetime.datetime.now()

print(now.year, "년")

print(now.month, "월")

print(now.day, "일")

print(now.hour, "시")

print(now.minute, "분")

print(now.second, "초")

print()



print("# 시간을 포맷에 맞춰 출력하기")

output_a = now.strftime("%Y.%m.%d %H:%M:%S")

output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\

now.month,\

now.day,\

now.hour,\

now.minute,\

now.second)

output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")

print(output_a)

print(output_b)

print(output_c)

print()

import datetime

now = datetime.datetime.now()



print("# datetime.timedelta로 시간 더하기")

after = now + datetime.timedelta(\

weeks=1,\

days=1,\

hours=1,\

minutes=1,\

seconds=1)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

print()



print("# now.replace()로 1년 더하기")

output = now.replace(year=(now.year + 1))

print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

from urllib import request



target = request.urlopen("https://google.com")

output = target.read()



print(output)

from urllib import request

from bs4 import BeautifulSoup



target = request.urlopen("https://www.weather.go.kr/m/nation/current.jsp?ele=3")



soup = BeautifulSoup(target, "html.parser")



for location in soup.select("location"):

    print("도시:", location.select_one("city").string)

    print("날씨:", location.select_one("wf").string)

    print("최저기온:", location.select_one("tmn").string)

    print("최고기온:", location.select_one("tmx").string)

    print()

module:

