print("Quadratic Formula Calculator")
print("\nSolving ax^2 + bx + c = 0")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

x_1 = (-b + math.sqrt((math.pow(b,2)) - (4 * a * c))) / 2 *a
x_2 = (-b - math.sqrt((math.pow(b,2)) - 4 * a * c)) / 2 *a

print("\nROOTS OF GIVEN QUADRATIC EQUATION ARE:")
print("x_1: ", x_1)
print("x_2: ", x_2)