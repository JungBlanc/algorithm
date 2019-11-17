a = "안녕하세요 포멧팅 예제입니다."


print("안녕하세요 포멧팅 %10d 문제입니다." % 5)
print("i eat {a} apples".format(a=3))

#왼쪽정렬 :<
#오른쪽 정렬 :>
#가운데 정렬 :^
print("{0:=^10}".format("hi")) #========

#간단하게
print(f'{"hi":>10}')

