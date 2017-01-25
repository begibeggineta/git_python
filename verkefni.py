#verkefni python
print("#Liður 1")
#Liður 1
tala1 = int(input("Sláðu inn tölu"))
tala2 = int(input("Sláðu inn aðra tölu"))
marg = tala1 + tala2
bla = tala1 * tala2
print("tölurnar plúsaðar",tala1,"+", tala2, marg)
print("tölurnar sinnumaðar",tala1,"*", tala2, bla)

#liður 2
print("#Liður 2")
ta1 = input("gefðu mér Fornafnið þitt")
ta2 = input("gefðu mér eftirnafnið þitt")
print("hello", ta1, ta2)

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
        t

