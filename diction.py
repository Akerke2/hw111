# dct = {"key":"f1"}



# popitem() - соңғы жұпты элементтерді удалить етеді
# items() - әрбір жұпты тьюплға айналдырады, масивв қайтарады барлығын
# clear () ішіндегі барлық жұпты өшіреді
# copy() - коптровать етеді новый дикшенариға қояды
# values - тек мәндерді қайтарады
# keys() - ключын алады, қайтарады

# hw
dog = {}
dog = {
    "name": "Princ",
    "color": "golden",
    "breed": "Pomeranian",
    "legs": "Standart",
    "age": "2"
}
stydents = {
    "first_name": "Akerke",
    "last_name": "Adikyzy",
    "gender": "Women",
    "age": "17",
    " marital status": "Not married",
    "skils": ["IT specialist Number 1"],
    "contry": "Kazakhsyan",
    "city": "Almaty",
    "adress": "Almaty",
}
print(len(stydents))
print("IT specialist Number 1" in stydents ["skils"])
stydents["skils"].append("archery")
print(stydents)
print(stydents.keys())
print(stydents.values())
print(stydents.items())
print(stydents.pop("age"))
del dog