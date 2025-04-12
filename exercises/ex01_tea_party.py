"""Practice writing functions and decomposing a program"""

__author__: str = "730705563"


def main_planner(guests: int) -> None:
    """Printed output of the three numbered outputs below"""
    print("A Cozy Tea Party for " + str(int(guests)) + " People!")
    print("Tea Bags: " + str(int(tea_bags(guests))))
    print("Treats: " + str(int(treats(guests))))
    print("Cost: $" + str(float(cost(treat_count(guests)))))


def tea_bags(people: int) -> int:
    """Number of tea bags needed for all of the guests attending the tea party"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed for the guests at the tea party to have with their tea"""
    return tea_bags(int(float(1.5) * people))


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of treats and tea together for everyone at the tea party"""
    return (tea_bags(tea_count) * 0.50) + (treats(treat_count) * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
