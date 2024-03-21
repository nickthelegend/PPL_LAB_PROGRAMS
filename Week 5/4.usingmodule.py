import geometry

def print_menu():
    print("\nGeometry Calculator")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Parallelogram")
    print("6. Trapezoid")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "1":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Area:", geometry.rectangle_area(length, width))
            print("Perimeter:", geometry.rectangle_perimeter(length, width))
        elif choice == "2":
            side = float(input("Enter the side length of the square: "))
            print("Area:", geometry.square_area(side))
            print("Perimeter:", geometry.square_perimeter(side))
        elif choice == "3":
            radius = float(input("Enter the radius of the circle: "))
            print("Area:", geometry.circle_area(radius))
            print("Circumference:", geometry.circle_circumference(radius))
        elif choice == "4":
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Area:", geometry.triangle_area(base, height))
            # Assuming it's an equilateral triangle for simplicity
            print("Perimeter:", geometry.triangle_perimeter(base, base, base))
        elif choice == "5":
            base = float(input("Enter the base length of the parallelogram: "))
            height = float(input("Enter the height of the parallelogram: "))
            print("Area:", geometry.parallelogram_area(base, height))
            # Assuming all angles are 90 degrees for simplicity
            print("Perimeter:", geometry.parallelogram_perimeter(base, base))
        elif choice == "6":
            base1 = float(input("Enter the length of the first base of the trapezoid: "))
            base2 = float(input("Enter the length of the second base of the trapezoid: "))
            height = float(input("Enter the height of the trapezoid: "))
            print("Area:", geometry.trapezoid_area(base1, base2, height))
            # Assuming all sides are equal for simplicity
            print("Perimeter:", geometry.trapezoid_perimeter(base1, base2, base1, base2))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
