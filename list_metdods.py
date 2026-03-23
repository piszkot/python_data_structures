# Common Python list methods

fruits = ["banana", "apple", "cherry", "mango", "kiwi"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
words = ["banana", "apple", "fig", "cherry"]
print()

# --- Adding items ---
print("--- ADDING ITEMS ---")
fruits.append("orange")           # add item to the end
fruits.insert(1, "mango")         # insert item at given index
fruits.extend(["lime", "peach"])  # add multiple items from iterable
print(fruits)

# --- Removing items ---
print()
print("--- REMOVING ITEMS ---")
fruits.remove("apple")            # remove first occurrence of value
popped_last = fruits.pop()        # remove and return last item
popped_idx = fruits.pop(2)        # remove and return item at given index
print(f"fruits before fruits.clear(): {fruits!r:>61}")
fruits.clear()                    # remove all items
print(f"fruits after fruits.clear(): {fruits!r:>10}")

# --- Searching ---
print()
print("--- SEARCHING ---")
fruits = ["banana", "apple", "cherry", "banana"]
idx = fruits.index("apple")      # find index of first occurrence
print(idx)
count = fruits.count("banana")   # count occurrences of value
print(count)

# --- Sorting ---
print()
print("--- SORTING ---")
numbers.sort()                           # sort in ascending order (in place)
print(numbers)
numbers.sort(reverse=True)               # sort in descending order (in place)
print(numbers)
numbers.sort(key=lambda x: -x)           # sort with custom key (desc)
print(numbers)
words.sort(key=len)                      # sort by string length
print(words)
words.sort(key=lambda s: s[-1])          # sort by last character
print(words)

sorted_numbers = sorted(numbers)         # returns new sorted list (ascending)
# returns new sorted list (descending)
sorted_desc = sorted(numbers, reverse=True)

# --- Other ---
print()
print("--- OTHER ---")
fruits = ["banana", "apple", "cherry"]
fruits.reverse()                        # reverse the order in place
reversed_list = list(reversed(fruits))  # reverse without modifying original
fruits2 = fruits.copy()                 # create a shallow copy

print(f"numbers: {numbers!r:>32}")
print(f"words: {words!r:>46}")
print(f"fruits2: {fruits2!r:>37}")
print()
