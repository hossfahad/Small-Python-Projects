# Pythagorean Theorem Checker for Triangles
# Verifies the pythagorean theory for triangles based on the length of each side.

# By Fahad Hossain

def pythagorean_triples(x)
    side_1 = int(input("Length of Side 1: ")) ** 2
    side_2 = int(input("Length of Side 2: ")) ** 2
    side_3 = int(input("Length of Side 3: ")) ** 2

    if (side_1 + side_2) == side_3:
        print("Hoorah! This is a Pythogorean Triple ")
    else:
        print("Sorry, this is not a Pythogorean Triple ")
