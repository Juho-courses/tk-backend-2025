def moikkaa(name: str, age: int = 23) -> int:
    print(f"moi {name}. Sun nimi on {age}!")
    return age * 2


moikkaa("leena")
age = moikkaa("leena", age=34)
print(age)
