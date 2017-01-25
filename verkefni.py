#Liður 3
print("#Liður 3")
texti = input("Settu inn random texta")
telhast = 0
tellagst = 0
telefthst = 0
sidastur = False
for i in range(len(texti)):
    if texti[i].isupper() and texti[i]:
        telhast += 1
        sidastur = True
    elif texti[i].islower() and sidastur == True:
        telefthst += 1
        sidastur = True
    if texti[i].islower():
        tellagst += 1
        sidastur = False
print("í þessum texta eru ", telhast," hástafir", tellagst, "Lágstafir", telefthst," lágstafir sem koma strax eftir hástöfum")
