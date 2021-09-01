shopping_list={
    "warzywniak" : ["marchew", "seler", "rukola"],
    "piekarnia" : ["bułka", "chleb", "pączek"]
    }
print(shopping_list)

for keys in shopping_list:
    print(f"Wchodzę do ", keys , " i kupuję tam: " , shopping_list[keys])