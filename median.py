def stednja():
	glavnica = eval(input("Unesite iznos glavnice: "))
	kamata = eval(input("Unesite iznos kamate: "))
	for i in range(5):
		glavnica = glavnica * (1 + kamata)

	print (glavnica)

	input("press <Enter> to quit")
stednja()