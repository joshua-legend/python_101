#quiz
# userYear = int(input("몇년생이십니까:"))
# print(f"귀하의 나이는 만 {2023 - userYear }입니다.")
#
# a = float(input("첫 번째:"))
# b = float(input("두 번째:"))
# c = float(input("세 번째:"))
# sum = a+b+c
# avg = sum/3
# print(f"총합: {sum},평균:{avg}")

#3)섭씨 온도를 입력받아 화씨 온도로 변환을 출력하는 프로그램 만들기
# F=C×5.9+32입니다.
cel = float(input("섭씨 온도 입력:"))
fah = cel * 5.9 + 32
# 변수[실수]:.2f 둘째 자리 출력
print(f"화씨 온도는 {fah:.2f}")

weight = float(input("몸무게 입력:"))
height = float(input("키 입력:"))
bmi = weight / (height ** 2)
print(f"귀하의 bmi는 {bmi:.2f} 입니다.")

#5) 반지름 입력시 원의 넓이와 둘레를 구하는 프로그램 📏🔵
radius = int(input("반지름 길이 입력:"))
width = 3.14 * radius ** 2
round = 2 * 3.14 * radius
print(f"원의 넓이:{width} 원의 둘레:{round}")

# print() - 출력
# input() - 입력[결과:문자 타입]
# 변수 - 임시 저장하는 곳
# int() / float() / str()
# 사칙연산 - +,-,*, /(나누기), %(나머지), //(몫), **(제곱)









