from moodul import *

ikood=""
arvud=[]
ikoodid=[]
while True:
    ikood=input("Sisesta isikukood: ")
    if ikood=="-":
        break
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
        arvud.append(ikood)
    else:
        s=sugu(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
            arvud.append(ikood)
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on vead")
                arvud.append(ikood)
            else:
                lause(ikood)
                if kontrollnr(ikood)==int(ikood[-1]):
                    print("OK")
                    ikoodid.append(ikood)
                else:
                    print("!!!")
print()
ikoodid=naised_mehed(ikoodid)
print(ikoodid)
arvud=arvud_sorted(arvud)
print(arvud)
