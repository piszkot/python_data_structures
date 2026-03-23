# Why does strings have .index() and .find() but list only has .index()?
#
# str.find() was designed for text searching — it's common to check
# whether a substring exists without raising an error.
# Returning -1 on failure is a classic C-style convention (e.g. strstr()).
#
# list.index() raises ValueError when item is not found — this follows
# Python's philosophy: if something goes wrong, raise an exception
# rather than returning a magic number like -1.
# Lists are general-purpose containers, so a silent -1 could be misleading.

# --- str has both find() and index() ---
print()
print("--- STR: ---")
text = "hello world"
print(text.find("world"))       # -> 6  (returns -1 if not found)
print(text.find("python"))      # -> -1 (no exception)
print(text.index("world"))      # -> 6  (same result)
# print(text.index("python"))   # -> ValueError (raises exception)

# --- list only has index() ---
print()
print("--- LIST: ---")
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))   # -> 1
# print(fruits.index("mango"))  # -> ValueError (no find() alternative)

# --- custom find() for lists ---

print()
print("--- CUSTOM FIND() FOR LISTS: ---")


def find(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1


print(find(fruits, "cherry"))   # -> 2
print(find(fruits, "mango"))    # -> -1  (no exception, just -1)
print()
