# money_init = 300000
# money_init -=80000
# money_init -=9000*5
# money_init +=120000
# money_init *=1.2
# money_init *=(2/3)

# print(int(money_init))

# intro = "둠칫"
# drop = "두둠칫"

# rythm = intro + drop*3

# print(rythm)


# x= input('아무 숫자나 입력하세요 : ')
# print(type(x))
# x=int(x)
# print(type(x))

# name = input('이름을 입력하세요 : ')
# print(f'입력한 이름은 {name}입니다.')


# a = int(input('첫 번째 값 : '))
# b = int(input('두 번째 값 : '))
# # input 에 입력한 값은 str 임을 주의해야 함
# print(a+b)


# fruit = '사과 참외 수박'.split()
# print(fruit, type(fruit))

# name=input('이름을 입력하세요 : ')
# age=input('나이를 입력하세요 : ')

# print(f'안녕하세요. 저는 {name}이고, {age}살입니다.')


# width = int(input('너비를 입력하세요 : '))
# height = int(input('높이를 입력하세요 : '))
# print(f"넓이 : {width*height}, 둘레 : {2*(height+width)}")

# number=input('네 자릿수 정수를 입력하세요 : ')
# digits=list(number)

# print(f"""천의 자리 : {digits[0]}
# 백의 자리 : {digits[1]}
# 십의 자리 : {digits[2]}
# 일의 자리 : {digits[3]}""")


# ymd = input('년,월,일을 입력해주세요(.으로 구분) : ')
# hms = input('시,분,초를 입력해주세요(:으로 구분) : ')

# ymd = ymd.split('.')
# hms = hms.split(':')

# print(f"""RE3의 개강일은 {ymd[0]}년 {ymd[1]}월 {ymd[2]}일
# 시작 시간은 {hms[0]}시 {hms[1]}분 {hms[2]}초입니다.""")

# list1= list()
# # 문자열을 리스트로
# list_str=list("codingOn")

# print(list1, '첫번째 확인')
# print(list_str, '데이터 값 들어온거 확인용')

# sample =[1,25,2666,19999,584848484,1212165465465,15,151,5,8,4,84,4,555556598,54551212548,1,15,4]
# # 리스트의 인덱스를 -1로 하면 제일 뒤
# print(sample[-2], type(len(sample)))


# nums=[10,20,30,40,50,60,70,80,90]
# nums_1=nums[::2]
# print(nums_1)

print('문제 1')
nums=[10,20,30,40,50]
print('첫 번째 : ',nums[0], '마지막 : ',nums[-1])

print('문제 2')
nums=[100,200,300,400,500,600,700]
nums_2=nums[int(len(nums)/2 - 1) : int(len(nums)/2 + 2)]
print(nums_2)

print('문제 3')
nums=[1,2,3,4,5]
for i in range(len(nums)):
    nums[i]*=2
print(nums)

print('문제 4')
items=["a","b","c","d","e"]
print(items[::-1])

print('문제 5')
data=['zero','one','two','three','four','five']
print(data[::2])

print('문제 6')
movies=['인셉션','인터스텔라','어벤져스','라라랜드','기생충']
movies[2:4]=['매트릭스','타이타닉']
print(movies)

print('문제 7')
subjects=['국어','수학','영어','물리','화학','생물','역사','지구과학','윤리']
#물리, 생물, 지구과학만 순서대로 뽑아내기
subjects_new=subjects[3::2]
print(subjects_new)

print('문제 8')
data=['A','B','C','D','E','F','G','H','I']
data_1=data[0:3]
data_2=data[3:6]
data_3=data[6:9]
print(data_1[::-1],data_2[::-1],data_3[::-1])