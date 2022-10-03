mylist = ["a","b",1,23,"razor"]
iterator = iter(mylist)

while True:
    try:
        print(next(iterator))
                           
    except StopIteration:
        break
