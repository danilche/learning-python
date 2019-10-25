def sastojci(*sastojci):
    recept = input("Upisite listu sastojaka odvojenu zarezom: ").split(",")
    for j in range(len(recept)):
    
        print("-{}".format(recept[j]))
    
def main():
#    recept = input("Upisite listu sastojaka odvojenu zarezom: ").split(",")
#    for j in range(len(recept)):
#    
#        print("-{}".format(recept[j]))
#    
    sastojci(sastojci)
    
main()
	