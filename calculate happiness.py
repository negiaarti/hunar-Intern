def calculate_happiness(array, set_a, set_b):
    happiness = 0
    for element in array:
        if element in set_a:
            happiness += 1
        elif element in set_b:
            happiness -= 1
    return happiness

def main():
    print("Calculate Your Happiness")

    # Input array elements
    array = input("Enter array elements separated by space: ").strip().split()

    # Input Set A elements
    set_a = set(input("Enter Set A elements separated by space: ").strip().split())

    # Input Set B elements
    set_b = set(input("Enter Set B elements separated by space: ").strip().split())

    # Calculate happiness
    happiness = calculate_happiness(array, set_a, set_b)

    print(f"Happiness: {happiness}")

if __name__ == "__main__":
    main()
