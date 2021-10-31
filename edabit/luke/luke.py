def relation_to_luke(name):
    try:
        return "Luke, I am your {}.".format({
            "darth vader"   : "father",
            "leia"          : "sister",
            "han"           : "bother in law",
            "r2d2"          : "droid"
            }[str.lower(name)])
    except:
        return "I don't know you."

print(relation_to_luke("Darth Vader"))
print(relation_to_luke("LEIA"))
print(relation_to_luke("Han"))
print(relation_to_luke("R2D2"))
print(relation_to_luke("Dimas"))