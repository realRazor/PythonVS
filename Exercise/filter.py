a = "ben size ders anlatırken huzur buluyorum. Dertlerimi unutüyorum"
sesliler = ["a","e","ı","i","o","ö","u","ü"]
def sesli(str):
    for i in str:
        if i in sesliler:
            return True
        else:
            return False 
b = filter(sesli,a)
print(set(list(b)))

