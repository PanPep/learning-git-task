print("Hello :)")
shopping_list={
    "warzywniak" : ["marchew", "seler", "rukola"],
    "piekarnia" : ["bułka", "chleb", "pączek"]
    }
print(shopping_list)

for keys in shopping_list:
    print(f"Wchodzę do ", keys.capitalize() , " i kupuję tam: " , shopping_list[keys])

print('\n')

suma_p=(len(shopping_list["piekarnia"]))
suma_w=(len(shopping_list["warzywniak"]))
suma=(suma_p+suma_w)
print(f"W sumie kupuję ",suma, " produktów")