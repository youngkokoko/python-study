A={1,2,3}
B={3,4,5}

# 합집합
print(A|B)  # 중복된 원소는 제거   {1,2,3,4,5}
print(A.union(B))

# 교집합 : 두 집합에 공통으로 들어있는 원소만 모은 것
print(A&B) # {3}
print(A.intersection(B))

# 차집합
print(A-B)  # {1,2}
print(A.difference(B))

# 대칭 차집합
print(A^B) # {1,2,4,5}
print(A.symmetric_difference(B))