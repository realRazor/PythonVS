def organizer(** data):
    names = [i for i in data.keys()]
    age = [i for i in data.values()]
    
    print(names)
    print(age)

organizer(john = 19, robert = 22,anna = 33,ada = 38)