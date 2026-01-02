#1
submissions=['kim','lee','kim','park','choi','lee','lee']
set=set(submissions)
number=len(set)

#2
user1={'SF','Action','Drama'}
user2={'Drama','Romance','Action'}

intersecton=user1.intersection(user2)
s_difference=user1.symmetric_difference(user2)
union=user1.union(user2)

#3
my_certificates={'SQL','Python','Linux'}
job_required={'SQL','Python'}

fulfill=job_required.issubset(my_certificates)

print('문제 1')
print('제출한 학생 수: ', number )
print('제출자 명단: ', set)

print('문제 2')
print('공통 관심 장르: ', intersecton)
print('서로 다른 장르: ', s_difference)
print('전체 장르: ', union)

print('문제 3')
print('지원 자격 충족 여부: ', fulfill)