"""
Python Data Structures: List, Set, and Tuple
=============================================

A quick overview of three core Python collection types.
"""

# ── LIST ──────────────────────────────────────────────
# Ordered, mutable, allows duplicates. Defined with [].

fruits = ["apple", "banana", "cherry", "banana"]

fruits.append("mango")        # add to end
fruits.remove("banana")       # removes first occurrence
fruits[0] = "avocado"         # change element by index

print()
print("List:", fruits)
print("First item:", fruits[0])
print("Sliced[1:3]:", fruits[1:3])


# ── SET ───────────────────────────────────────────────
# Unordered, mutable, NO duplicates. Defined with {}.

numbers = {1, 2, 3, 3, 4, 4, 5}   # duplicates auto-removed

numbers.add(6)
numbers.discard(1)

print("\nSet:", numbers)            # order not guaranteed

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)             # {1, 2, 3, 4, 5}
print("Intersection:", a & b)      # {3}
print("Difference:", a - b)        # {1, 2}


# ── TUPLE ─────────────────────────────────────────────
# Ordered, immutable, allows duplicates. Defined with ().

coordinates = (51.5, -0.1, 35.0)

print("\nTuple:", coordinates)
print("Latitude:", coordinates[0])
print("Length:", len(coordinates))

# Unpacking
lat, lon, alt = coordinates
print(f"lat={lat}, lon={lon}, alt={alt}")
print()

# Tuples are immutable — this would raise a TypeError:
# coordinates[0] = 99.9


# ── QUICK COMPARISON ──────────────────────────────────
#
#  Feature       │ List   │ Set    │ Tuple
# ───────────────┼────────┼────────┼───────
#  Ordered       │  Yes   │  No    │  Yes
#  Mutable       │  Yes   │  Yes   │  No
#  Duplicates    │  Yes   │  No    │  Yes
#  Syntax        │  [ ]   │  { }   │  ( )
