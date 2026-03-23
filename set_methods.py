# Common Python set methods

animals = {"cat", "dog", "fish", "bird"}
other = {"dog", "rabbit", "hamster"}

# --- Adding items ---
print()
print("--- ADDING ITEMS ---")
animals.add("parrot")              # add a single item
animals.update(["snake", "frog"])  # add multiple items from iterable
print(animals)

# --- Removing items ---
print()
print("--- REMOVING ITEMS ---")
animals.remove("fish")             # remove item, raises KeyError if not found
animals.discard("shark")           # remove item, no error if not found
popped = animals.pop()             # remove and return an arbitrary item
print(f"animals before animals.clear(): {animals}")
animals.clear()                    # remove all items
print(f"animals after animals.clear(): {animals}")

# --- Set operations ---
print()
print("--- SET OPERATIONS ---")
animals = {"cat", "dog", "fish", "bird"}
union = animals | other             # all items from both sets
intersection = animals & other      # only items present in both
difference = animals - other        # items in animals but not in other
sym_diff = animals ^ other          # items in either set, but not both

print(f"union: {union}")
print(f"intersection: {intersection}")
print(f"difference: {difference}")
print(f"symmetric difference: {sym_diff}")

# --- Same operations as methods ---
union2 = animals.union(other)
intersection2 = animals.intersection(other)
difference2 = animals.difference(other)
sym_diff2 = animals.symmetric_difference(other)

# --- Searching / checking ---
print()
print("--- SEARCHING / CHECKING ---")
print("dog" in animals)              # check if item exists
print(animals.issubset(other))       # True if animals is subset of other
print(animals.issuperset(other))     # # True if animals is superset of other
print(animals.isdisjoint(other))     # True if no common items
