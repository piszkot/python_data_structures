# Common Python tuple methods and operations

coords = (10, 20, 30, 20, 50, 20)
mixed = (1, "hello", 3.14, True)

# --- Only two built-in methods ---
print()
print("--- Only two built-in methods - count & index: ---")
count = coords.count(20)         # count occurrences of value -> 3
idx = coords.index(30)           # find index of first occurrence -> 2
print(count)
print(idx)

# --- Tuple is immutable - no add/remove methods ---
# coords.append(99)   # AttributeError
# coords.remove(10)   # AttributeError

# --- Creating tuples ---
empty = ()                       # empty tuple
single = (42,)                   # single item (comma required!)
from_list = tuple([1, 2, 3])     # convert list to tuple
from_range = tuple(range(5))     # convert range to tuple

# --- Accessing items ---
first = coords[0]                # indexing
last = coords[-1]                # negative indexing
sliced = coords[1:4]             # slicing -> (20, 30, 20)

# --- Unpacking ---
x, y, z, *rest = coords          # unpack with wildcard
a, b = (1, 2)                    # simple unpack

# --- Checking ---
print()
print("--- Checking: ---")
print(f"Empty tuple: {empty}")
print(20 in coords)              # check if item exists -> True
print(len(coords))               # number of items -> 6
print(min(coords), max(coords))  # min and max value

# --- Concatenation ---
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2               # -> (1, 2, 3, 4, 5, 6)
repeated = t1 * 3                # -> (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(coords)
print(combined)
print()
