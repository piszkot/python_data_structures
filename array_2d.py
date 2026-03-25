# A 2D array is a collection of elements arranged in rows and columns,
# forming a grid-like structure. It can be thought of as a list of lists (or in Python, a tuple of tuples),
# where each inner sequence represents a single row of data.

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

print()
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

print("\n-----\n")
print("num_pad[1][2]: ", num_pad[1][2], "\n")
