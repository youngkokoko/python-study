## 딕셔너리 생성
# 첫 번째 방법
person={
    "name" : 'Alice',
    "age" : 25
}
print(person["name"]) 

# 두 번째 방법
person =dict(name="Alice",age=25)

# key 로 정수를 사용가능
num_dict={1:'one',2:'two'}

# key 로 튜플 사용가능
coord_dict={(0,0):"origin",(1,2):"point A"}
print(coord_dict[(0,0)])

# key 로 리스트 사용은 불가능. 리스트는 변경이 가능한 객체이므로.
my_dict={
    [1,2,3]:"value"
}


product=dict(name="keyboard", price=30000, in_stock=True)

pairs=[('name','Bob'),('age',22),('city','Busan')]
person=dict(pairs)

keys=['name','age','city']
values=['Charlie',28,'Incheon']
info=dict(zip(keys,values))
# {'name':'Charlie','age':28,'city':'Incheon'}

person = {
    'name':'Alice',
    'age':30,
    'city':'Seoul'
}

## 데이터 접근

# 첫 번째 방법
print(person['name']) # Alice
print(person['email']) # KeyError: 'email' 은 존재하지 않는 key

# 두 번째 방법 (get 은 KeyError를 방지 가능함)
print(person.get('name')) # Alice
print(person.get('email')) # None.  오류가 아님
print(person.get('email'), "없음")  # 없음 출력


