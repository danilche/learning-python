animal = [
    "duck", "turkey", "pig", "cow", 
    "cat", "mule", "dog", "turtle"
    ]

voice = [
    "quack", "gobble", "oink", "moo", 
    "meow", "heehaw", "woof", "nerp"
    ]

def title():
    print("Old MacDonald had a farm".upper())
    print()

def verse_1_5():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    
def verse_2(j):
    print("And on that farm he had a {}, Ee-igh, Ee-igh, Oh!".format(animal[j]))
    
def verse_3_4(j):
    print("With a {0}, {0} here and a {0}, {0} there.\nHere a {0}, \
there a {0}, everywhere a {0}, {0}.".format(voice[j]))
    
def main():
    
    title() 
    for j in range(len(animal)):
        verse_1_5()
        verse_2(j)
        verse_3_4(j)
        verse_1_5()
        print()

main()
    
