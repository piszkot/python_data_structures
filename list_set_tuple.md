# 📝 Python Data Structures: List, Set & Tuple

Python has several built-in collection types for storing groups of values.
Each one has different rules around ordering, mutability, and uniqueness —
choosing the right one depends on what you need to do with your data.

- Use a **list** when order matters and you need to change the contents.
- Use a **set** when you only care about unique values and order doesn't matter.
- Use a **tuple** when the data should stay fixed and not be changed.

---

## ── LIST ──
Ordered, mutable, allows duplicates. Defined with `[]`.

## ── SET ──
Unordered, mutable, NO duplicates. Defined with `{}`.

## ── TUPLE ──
Ordered, immutable, allows duplicates. Defined with `()`.

---

#### ── QUICK COMPARISON ──

| Feature    | List  | Set   | Tuple |
|------------|-------|-------|-------|
| Ordered    | Yes   | No    | Yes   |
| Mutable    | Yes   | Yes   | No    |
| Duplicates | Yes   | No    | Yes   |
| Syntax     | `[ ]` | `{ }` | `( )` |


## 💾 Memory usage 

In Python, memory usage differs between list, set, and tuple because each is designed for a different purpose and stores data in a different way.

##### 📊 Which uses the most memory?
From most to least (generally): set > list > tuple
##### 🔍 Why?
1. set – uses the most

Implemented as a hash table
Must store:

the elements themselves
their hash values
extra empty slots to handle collisions and enable fast lookups


The hash table is also kept partially empty on purpose (load factor ~⅔), which wastes space but keeps operations fast
Trade-off: high memory overhead, but x in set runs in O(1) on average

2. list – middle ground

Implemented as a dynamic array
Stores pointers to elements (not the elements directly)
Allocates extra capacity in advance so that append() doesn't trigger a reallocation every time (over-allocation strategy)
Trade-off: uses more memory than a tuple, but adding elements is fast — amortized O(1)

3. tuple – uses the least

Also a fixed-size array of pointers, but immutable
No extra capacity needed — size is fixed at creation
CPython also caches small tuples (length 0–20) and reuses them, which can save memory and speed up creation
Best choice when data doesn't need to change


