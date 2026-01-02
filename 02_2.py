# 실습2


print('문제 1')
fruits=['apple','banana', 'cherry', 'grape','watermelon','strawberry']
del fruits[1:4]
print(fruits)

print('문제 2')

letters=['A','B']
letters_1=letters*3
first_a=letters_1.index('A')
second_a=letters_1.index('A',first_a + 1)

del letters_1[second_a]
print(letters_1)
