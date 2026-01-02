# 문제 1
# user={
#     "username":"skywalker",
#     "email":"sky@example.com",
#     "level":5
# }
# email_value=user["email"]
# print("email value: ",email_value)
# user["level"]=6
# print("level: ", user["level"])
# print(user.get('phone',"미입력"))
# user.update(nickname="sky")
# del user["email"]
# user.setdefault("signup_date","2025-07-10")
# print(user)

# 문제 2
students={}
students.update(Alice=85,Bob=90,Charlie=95)
students["David"]=80
students["Alice"]=88
del students["Bob"]
print(students)