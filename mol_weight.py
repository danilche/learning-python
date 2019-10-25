# this program calculates molecular weight of a carbohydrate


def mol_weight():

	h = int(input("Enter the number of hydrogen atoms: "))
	o = int(input("Enter the number of oxygen atoms: "))
	c = int(input("Enter the number of carbon atoms: "))
	hw, cw, ow = 1.00794, 12.0107, 15.9994
	m_weight = h * hw + o * ow + c * cw
	print()
	print("-----------")
	print("Molecular weight is", m_weight)

	input("Press <Enter> to exit")

mol_weight()