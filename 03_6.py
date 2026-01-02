# user_data={
#     "username":'student01',
#     "email" : 'student@example.com'
# }
# # 사용자가 요청한 키
# key=input("확인할 정보를 입력하세요 (username, email, phone): ")

# # 안전하게 접근
# value=user_data.get(key,"해당 정보 없음")
# print(value)

# # 딕셔너리 수정 혹은 추가
# # 이미 있는 key 라면 value를 수정, 없는 key 라면 추가
# user_data['username'] ='tiger'
# print(user_data)


person={
    "name":"Alice",
    "age":25
}

# person.update({"age":26,"city":"Seoul"})   # 있던 key 는 value 수정, 없던 key 는 추가
# print(person)
# person.update({'job':'student'})
# print(person)
# person.update(age=28,hobby="game") # update 를 쓰면 여러가지를 한꺼번에 변경 가능
# print(person)

# del person["age"] # 해당 key:value 삭제. 없는 key 삭제시 에러.
# print(person)

age=person.pop('age')  # 해당 key의 value를 반환하고, 원본 딕셔너리에서 해당 key를 삭제
print(age)
print(person)