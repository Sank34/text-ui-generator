import texts
print("Salut,bun venit la configurarea propriului tau design,te rugam sa alegi din tip-urile noastre variate:")
print("1.-------")
print("2.+++++++")
print("3.✄✄✄✄✄✄✄")
print("4.♠ si ✑")
sel = input("Scrie numarul variantei dorite: ")

if sel != "1" and sel != "2" and sel != "3" and sel != "4":
    print("EROARE-argumente invalide")
    sel = input("Scrie numarul variantei dorite: ")


#def print statement---mh(input("Alegeti ip-ul"), input("alegeti store ul:"), input("alegeti portalul"))
if sel == "1":
    texts.mh1(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "2":
    texts.mh2(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "3":
    texts.mh3(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "4":
    texts.mh4(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))

print("Iti place acest design?(da/nu)")
var = input()

if var != "da" and var != "nu":
    print("EROARE-argumente invalide,scrie da/nu")
    print("Iti place acest design?(da/nu)")
    var = input()

if var == "da":
    print("Multumim,nu uita sa dai star la proiect!:D")
elif var == "nu":
    print("Ce pacat...\nDaca mai ai sugestii de UI-uri,nu uita sa contactezi dezvoltatorul pe discord.\nDiscord: Sanke#4704")

