"""
    날짜 : 2020/06/22
    이름 : 김보미
    내용 : 리스트 자료형 실습하기 교재 p72
"""
# 리스트
ls1 = [1, 2, 3, 4, 5]
print('ls1[0] :', ls1[0])
print('ls1[2] :', ls1[2])
print('ls1[4] :', ls1[4])

ls2 = [1, 3.14, True, '홍길동']
print('ls2[1] :', ls2[1])
print('ls2[2] :', ls2[2])
print('ls2[3] :', ls2[3])

ls3 = [[1, 2, 3], [True, False, True], ['Apple', 'Banana', 'Grape']]

print('ls3[1] :', ls3[1])
print('ls3[2] :', ls3[2])
print('ls3[0][1] :', ls3[0][1])
print('ls3[2][1] :', ls3[2][1])

# 리스트 더하기
fr1 = ['사과', '오렌지']
fr2 = ['바나나', '포도', '수박']
fr3 = fr1 + fr2
print('fr3 :', fr3)
print('fr3[2] :', fr3[2])

# 리스트 수정,변경,삭제
numbers = [1, 2, 3, 4, 5]

numbers[1] = 7
print('numbers :', numbers)

numbers[2:3] = [8, 9]
print('numbers :', numbers)

numbers[1:3] = []
print('numbers :', numbers)

del numbers[1]
print('numbers :', numbers)

# 리스트 관련 함수 교재 p80 ~ 84
a = [1, 2, 3]
a.append(4)

print(a)

a.append([5, 6])
a

print(a)

#리스트 정렬
a = [1, 4, 3, 2]
a.sort()
a
print(a)

a = ['a', 'c', 'b']
a.sort()
a
print(a)

#리스트 뒤집기
a = ['a', 'c', 'b']
a.reverse()

print(a)


#위치 반환
a = [1, 2, 3]
a.index(3)

print(a.index(3))

2
a.index(1)
print(a.index(1))
0

#a.index(0)
#print(a.index(0)) 오류 메시지 0 is not in list

#리스트에 요소 삽입
a = [1, 2, 3]
a.insert(0, 4) #0위치에 4 삽입

print(a)

[4, 1, 2, 3]

a.insert(3, 5)

print(a)
[4, 1, 2, 5, 3]

#리스트 요소 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)

print(a)
[1, 2, 1, 2, 3]

a.remove(3)
print(a)

[1, 2, 1, 2,]

#리스트 요소 끄집어내기
a = [1, 2, 3]
a.pop()
3
a
print(a)

[1, 2]

a = [1, 2, 3]
a.pop(1)
2
print(a)

#리스트에 포함된 요소 x의 개수 세기
a = [1, 2, 3, 1]
a.count(1)

print(a.count(1))

#리스트 확장
a = [1, 2, 3]
a.extend([4, 5])

print(a)
b = [6, 7]
a.extend(b)

print(a)