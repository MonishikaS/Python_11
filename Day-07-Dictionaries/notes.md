# Python Dictionaries — Theory Notes

## 1. Introduction to Dictionaries

A dictionary is a built-in Python data type used to store data in the form of **key-value pairs**.

Each item in a dictionary contains:
- **Key:** Identifies an item.
- **Value:** The data associated with that key.

Dictionaries are useful for storing related information, such as student details, employee records, phone numbers, and product prices.

## 2. Features of Dictionaries

- Dictionaries store data as key-value pairs.
- Dictionaries are **mutable**, which means their contents can be changed after creation.
- Dictionary keys must be unique.
- Values can be duplicated.
- Keys must be immutable types, such as strings, integers, or tuples containing only immutable elements.
- Values can be of different data types.
- Dictionaries preserve insertion order in modern Python.
- Dictionaries are created using curly brackets `{}`.

## 3. Creating a Dictionary

A dictionary is created by placing key-value pairs inside curly brackets. Each key and its value are separated by a colon, while different pairs are separated by commas.

An empty dictionary can also be created and populated later.

## 4. Accessing Dictionary Elements

Dictionary values are accessed using their keys rather than numerical positions.

If a key does not exist, accessing it directly raises a `KeyError`.

The `get()` method can be used to retrieve a value safely. If the requested key is absent, it returns `None` by default or a specified default value.

## 5. Adding and Modifying Elements

Dictionaries are mutable, so elements can be added or modified after creation.

- **Adding:** Assigning a value to a new key creates a new key-value pair.
- **Modifying:** Assigning a value to an existing key replaces its previous value.

## 6. Deleting Dictionary Elements

Dictionary elements can be removed in different ways:

- `del` removes a specified key-value pair.
- `pop()` removes a specified key and returns its value.
- `popitem()` removes and returns the most recently inserted key-value pair.
- `clear()` removes all elements from the dictionary.

## 7. Membership Operators

The `in` and `not in` operators check whether a key exists in a dictionary.

By default, membership testing checks **keys, not values**.

## 8. Traversing a Dictionary

Traversing means visiting the dictionary's elements one by one.

Python provides several dictionary methods for traversal:

- `keys()` returns a view of all keys.
- `values()` returns a view of all values.
- `items()` returns a view of the key-value pairs.

These methods are useful when processing dictionary data using loops.

## 9. Important Dictionary Functions and Methods

| Function or Method | Purpose |
|---|---|
| `len()` | Returns the number of key-value pairs. |
| `dict()` | Creates a dictionary. |
| `keys()` | Provides a view of the keys. |
| `values()` | Provides a view of the values. |
| `items()` | Provides a view of key-value pairs. |
| `get()` | Retrieves a value for a specified key. |
| `update()` | Adds new pairs or updates existing ones. |
| `pop()` | Removes a specified key and returns its value. |
| `popitem()` | Removes and returns the last inserted pair. |
| `clear()` | Removes all pairs. |

## 10. Nested Dictionaries

A nested dictionary is a dictionary that contains another dictionary as a value.

Nested dictionaries are useful for representing structured information, such as multiple students' records, employee details, or product information.

Values inside a nested dictionary are accessed by following the required keys at each level.

## 11. Dictionary Keys and Values

Keys and values have different roles:

- Keys are used to identify and retrieve data.
- Values contain the information associated with the keys.
- Keys must be unique within a dictionary.
- Multiple keys may have the same value.
- Changing the value associated with a key does not change the key itself.

## 12. Common Mistakes to Avoid

- Using a key that does not exist when accessing a value.
- Assuming dictionary elements can be accessed by numerical position like list elements.
- Forgetting that membership operators check keys by default.
- Using duplicate keys and expecting both entries to remain separate.
- Confusing `pop()` with `popitem()`.
- Assuming dictionaries are immutable.

## 13. Applications of Dictionaries

Dictionaries are commonly used for:

- Storing student names and marks.
- Maintaining employee details and salaries.
- Creating phone books and contact lists.
- Storing product names and prices.
- Counting the frequency of words or characters.
- Representing structured records using nested dictionaries.

## 14. Summary

A dictionary is a mutable Python collection that stores information as unique keys paired with values. It allows efficient access, addition, modification, deletion, and traversal of data using keys and built-in methods.
