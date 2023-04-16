#dict를 이용한 해시
table = {} #dict()
table["key"] = 100
table["key2"] = "Hello"
print(table["key"]) #100
table["key"] = 349
print(table["key"]) #349
del table["key"]
print(table["key"]) #에러 발생

#set()을 이용한 해시
table1 = set()
table1.add("key")
table1.add("Hello")
print(table1) #{"Hello", "key"}

table2 = set()
table2.add(100)
table2.add("key")
print(table1 & table2) #교집합, {"key"}
print(table1 | table2) #합집합, {100, "key", "Hello"}
print(table1 - table2) #차집합, {"Hello"}