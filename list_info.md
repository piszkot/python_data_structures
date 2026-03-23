# 💡 List

#### A list is a mutable, dynamic sequence that stores references to its elements. Unlike `range`, it materializes every item in memory at once — and allocates extra space in advance to make future appends cheaper.

Every Python object carries a fixed overhead (`ob_refcnt`, `ob_type`), followed by the actual payload.
For `list`, the payload consists of its length, a pointer to the data buffer, and the allocated capacity — hence 5 × 8 = 40 bytes for the list object itself, plus 8 bytes per stored element.

64 bits = 8 bytes — the size of one memory slot on a modern computer. Every pointer and every basic integer in CPython is aligned to this size.

| Field          | Size         | Description                                      |
|----------------|--------------|--------------------------------------------------|
| `ob_refcnt`    | 8 bytes      | reference counter used by GC                     |
| `ob_type`      | 8 bytes      | pointer to the type object (`list`)              |
| `ob_size`      | 8 bytes      | current number of elements                       |
| `ob_item`      | 8 bytes      | pointer to the array of element references       |
| `allocated`    | 8 bytes      | number of slots allocated (capacity)             |
| **Object**     | **40 bytes** | always, for any `list` object                    |
| **Elements**   | **n × 8 bytes** | one pointer per element (n = current length) |
| **Total**      | **40 + (n × 8 bytes**) | grows linearly with the number of items  |