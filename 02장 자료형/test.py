name = input("이름를 입력하세요: ")
kor = input("국어 점수를 입력하세요: ")
eng = input("영어 점수를 입력하세요: ")
math = input("수학 점수를 입력하세요: ")

total = int(kor) + int(eng) + int(math)
avg = total /3

print(name, "님의 총점=" , total, "평균=" , avg, "입니다." )
#print(name)