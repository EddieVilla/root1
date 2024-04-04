import clearing
import winter_map

def main1():
    cle = clearing.clearing()
    cle2 = clearing.clearing()
    clearing.clearing.connect(cle, cle2)
    print(cle.get_neighbors())
    print(cle2.get_neighbors())

def main2():
    win = winter_map.winter_map()
    print(win)

if __name__=="__main__":
    # main1()
    main2()
    print("hi")


"""
river neighbors
    give edges a type
        normal
        river
        mountain covered (changes to normal)
forest
"""