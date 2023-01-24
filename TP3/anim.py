#encoding : UTF8

# class having the information of the parents
class Parents():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.children = []

    # function to print the information for parents
    def __str__(self) -> str:
        return self.name + " " + str(self.age)

# class having the information for the children


class Children(Parents):
    def __init__(self, name, age, mother, father) -> None:
        super().__init__(name, age)
        self.mother = mother
        self.father = father
        self.parents = [mother, father]

    def __str__(self) -> str:
        return self.name + " " + str(self.age) + \
            " " + self.mother + " " + self.father

# Function to add children to the descendent


def add_children(child) -> None:
    descendants = children.append(child)
    return descendants

# Function to remove children from the descendent


def remove_children(child) -> None:
    descendants = children.remove(child)
    return descendants


# test
if __name__ == "__main__":
    children = []
    child1 = Children("Lynn", 23, "Maguy", "Jean")
    Parent1 = Parents("Maguy", 58)
    add_children(child1)
    print(child1)
    print(Parent1)
