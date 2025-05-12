def find_and_filter_squares(start, end):
    all_squares = []
    even_squares = []
    odd_squares = []
    for num in range(start, end + 1):
        square = num**2
        all_squares.append(square)
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
        print("All squares :", all_squares)
        print("Even squares :", even_squares)
        print("Odd squares :", odd_squares)
print("This program calculates the square values and separates odd/even values.")
start = int(input("Enter the starting number :"))
end = int(input("Enter the ending number :"))
find_and_filter_squares(start, end)