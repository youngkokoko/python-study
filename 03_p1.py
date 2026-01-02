# step 1
user=("minji", 25, "Seoul")
temp=list(user)
temp[0]='eunji'
restored_user=tuple(temp)

print(f'step 1 : {restored_user}')

# step 2
name, age, city = restored_user
print(f'step 2 : {name}, {age}, {city}')

# step 3
print('step 3')
if city=="Seoul":
    print('서울 지역 보안 정책 적용 대상입니다.')
else :
    print('일반 지역 보안 정책 적용 대상입니다.')
    
# step 4
users=("minji","eunji","soojin","minji","minji")
print('step 4')
print(f'minji 등장 횟수 : {users.count("minji")}')
print(f'soojin 처음 등장하는 위치 : {users.index("soojin")}')

# step 5
print('step 5')
temp_list=sorted(users)
print(temp_list)
sorted_users=tuple(temp_list)
print(sorted_users)
