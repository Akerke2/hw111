# Бүгінгі тақырып
# set - дубликаттар болмайтын колекция, дубликаттарды сеттің ішіне сақтай алмаймыз екі рет қайталанбайды {}
# set те индекс жок, ретсіз орналасқан,
# екеуіне де ортақ intersection

# string (строка) - это неизменяемая последовательность символов.
# list (список) - это изменяемая последовательность объектов, которые могут быть разных типов.
# tuple (кортеж) - это неизменяемая последовательность объектов, которые могут быть разных типов.
# set (набор) - это неупорядоченная коллекция уникальных элементов, которая не допускает дублирования.

# Сеттің ұзындығын анықтау
# st = {'item1', 'item2', 'item3', 'item4'}
# print(len(st))

# # in ішінде элемент бар ма жоқ па соны айтады true or false қайтарады
# st = {'item1', 'item2', 'item3', 'item4'}
# print("item5" in st)
# # print("ggg", item1 in переменный )
# st = {'item1', 'item2', 'item3', 'item4'}
# st.add("item5")
# print(st)

# # егер көп элемент қосу керек керек болса "update"
# st.update("item5",'item1', 'item2', 'item3', 'item4')
# print(st)

# # remove сеттің ішіндегіні удалить ету үшін
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove("item5")

# # pop()  рандомный элентті алып өшіре салады
# st = {'item1', 'item2', 'item3', 'item4'}
# st.pop()

# #  сетті тазалау үшін clear()
# st = {'item1', 'item2', 'item3', 'item4'}
# st.clear()

# cities= {"almaty", "Astana", "Karaganda", "Aktau", "Transelvania"}
# print(len(cities))
# cities.add("Milan")
# print((cities))
# cit = input("City")
# cities.add(cit)
# print(cities)

# cit = input("remove a City")
# cities= {"almaty", "Astana", "Karaganda", "Aktau", "Transelvania"}
# if cit in cities:
#     cities.remove(cit)
#     print(f'{cit} remove')
# else:
#     cities.add(cit)
#     print(f'{cit} kosuldu')
# print(cities)

# cities= {"almaty", "Astana", "Karaganda", "Aktau", "Transelvania"}
# cit = input("City")
# x = cit.split()
# cities.update(x)
# print(cities)


# # Маствті сетке айналдырдық
# lst = ["nfrn", "forjfr", "nrfk"]
# st = set(lst)
# # сетті қосу екі сеттен жаңа сет пайда болуы
# st1 = {"nnff", "fjjf", "fjjfjf"}
# st2 = {"nnff", "fjjf", "fjjfjf"}
# st3 = {"nnff", "fjjf", "fjjfjf"}
# st
 


# differnce айырмашылық табады
# isdisjoint ортақ элементтер бар ма жоқ па соны қайтарады


# HW
# Level 1
# 1
# it_companies = {"Css", "Html", "JV"}
# print(len(it_companies))
# # 2
# it_companies.add( "Twitter")
# print(it_companies)
# # 3
# it_companies.update(["Facebook", "Instagram", "Tiktok"])
# print(it_companies)
# 4
# it_companies.remove("Twitter")
# print(it_companies)
# 5
# Дискард удалить етеді. Егер көрсетілген элемент жиынтықта болмаса ошибка бермей сол қалпы қала берді. дискард пен ремув бірдей жұмыс істейді бірақ әр түрлі зат қайтарады
# Ал ремув көрсетілген элемент жиынтықта жоқ болса қате деп шығады
# it_companies = {"Css", "Html", "JV"}
# it_companies.remove("JV")
# it_companies.discard("Css")

# # LEVEL2
A = {"d", "z", "a"}
B = {3, 4, 5}

#1
inter = A.intersection(B)
print(" B", inter)

# 2
isasubset = A.issubset(B)
print("A and B", isasubset)

#3
isdisjoint = A.isdisjoint(B)
print("A B ", isdisjoint)

# 4
unionAB = A.union(B)
unionBA = B.union(A)
print("A and B union", unionAB)
print("union B and A:", unionBA)

#5
symmetric_difference = A.symmetric_difference(B)
print("symetric A and B", symmetric_difference)

#6
del A
del B
# LEVEL3
# 1
age = [25, 30, 35, 40]
agesset = set(age)

# 1a
if len(age) > len(agesset):
    print("сптсоктын длинасы набордан улкен")
else:
    print("набордын длинасы списоктан улкен")

# 2
konspekt = """
string - дегеніміз таңбалары өзгермейтін тізбек, текст
list - әртүрлі бола алады, және өзгереді
tuple - жазған элементтер өзгертілмейді! Тьюплға ештеңе қосылмайды және алынбайды. Бір элемент қосу үшін жаңа Тьюплға қосамыз
set - дубликаттар болмайтын колекция, дубликаттарды сеттің ішіне сақтай алмаймыз екі рет қайталанбайды set те индекс жок, ретсіз орналасқан,
"""
print("айырмашылықтары \n", konspekt)

# 3
sentenc = " I am a teacher and I like to inspire and teach people. "
don = set(sentenc.split())
lili = len(don)
print("уникальные слово", lili)