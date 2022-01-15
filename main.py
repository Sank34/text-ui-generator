print("Salut,bun venit la configurarea propriului tau design,te rugam sa alegi din tip-urile noastre variate:")
print("1.-------")
print("2.+++++++")
print("3.✄✄✄✄✄✄✄")
print("4.♠ si ✑")
sel = input("Scrie numarul variantei dorite: ")

if sel != "1" and sel != "2" and sel != "3" and sel != "4":
    print("EROARE-argumente invalide")
    sel = input("Scrie numarul variantei dorite: ")

#default funct
def mh1(x, y, z):
    print("-----------------")
    print("IP:", x)
    print("Store:", y)
    print("Portal:", z)
    print("-----------------")
def mh2(a, b, c):
    print("+++++++++++++++++")
    print("IP:", a)
    print("Store:", b)
    print("Portal:", c)
    print("+++++++++++++++++")
def mh3(d, e, v):
    print("✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄")
    print("IP:", d, "|")
    print("Store:", e, "|")
    print("Portal:", v, "|")
    print("✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄✄")

def mh4(l, m, n):
    print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
    print("✑ IP:", l, "|")
    print("✑ Store:", m, "|")
    print("✑ Portal:", n, "|")
    print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")


#def print statement---mh(input("Alegeti ip-ul"), input("alegeti store ul:"), input("alegeti portalul"))
if sel == "1":
    mh1(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "2":
    mh2(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "3":
    mh3(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))
elif sel == "4":
    mh4(input("Alegeti ip-ul: "), input("alegeti store ul: "), input("alegeti portalul: "))

print("Iti place acest design?(da/nu)")
var = input()

if var != "da" and var != "nu":
    print("EROARE-argumente invalide,scrie da/nu")
    print("Iti place acest design?(da/nu)")
    var = input()

if var == "da":
    print("Multumim,nu uita sa dai star la proiect")
elif var == "nu":
    print("Ce pacat...")
    print("Daca mai ai sugestii de ui-uri,nu uita sa contactezi dezvoltatorul pe discord.")
    print("Discord: Sanke</>#4704")

