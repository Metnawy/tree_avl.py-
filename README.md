
# AVL Tree and Sorted List Array Implementation

This repository contains Python implementations of an **AVL Tree** and a **Sorted List Array**. These data structures are designed to handle various operations such as insertion, deletion, searching, and traversal, while maintaining balance (in the case of the AVL Tree) and order (in the case of the Sorted List Array).

## Classes and Methods

### `tree_avl` (AVL Tree)

- **`insert(data)`**: Inserts a numeric value into the AVL Tree.
- **`delete(data)`**: Deletes a numeric value from the AVL Tree.
- **`search(data)`**: Searches for a numeric value in the AVL Tree and returns the node if found.
- **`in_order_traversal(node)`**: Performs an in-order traversal of the tree starting from the given node.
- **`pre_order_traversal(node)`**: Performs a pre-order traversal of the tree starting from the given node.
- **`post_order_traversal(node)`**: Performs a post-order traversal of the tree starting from the given node.
- **`level_traversal(node)`**: Performs a level-order (breadth-first) traversal of the tree starting from the given node.
- **`min()`**: Returns the minimum value in the tree.
- **`max()`**: Returns the maximum value in the tree.
- **`size()`**: Returns the number of nodes in the tree.
- **`is_empty()`**: Checks if the tree is empty.
- **`__iter__()`**: Allows iteration over the tree in level-order.
- **`__repr__()`**: Provides a string representation of the tree structure.

### `sorted_list_array` (Sorted List Array)

- **`insert_first(data)`**: Inserts a numeric value at the beginning of the list.
- **`insert_last(data)`**: Inserts a numeric value at the end of the list.
- **`insert_index(data, index)`**: Inserts a numeric value at a specific index.
- **`insert_before_data(data, new_data)`**: Inserts a new value before a specific value in the list.
- **`insert_after_data(data, new_data)`**: Inserts a new value after a specific value in the list.
- **`delete_index(index)`**: Deletes the value at a specific index.
- **`delete_data(data)`**: Deletes the first occurrence of a specific value.
- **`delete_before_data(data)`**: Deletes the value before a specific value.
- **`delete_after_data(data)`**: Deletes the value after a specific value.
- **`search(data)`**: Searches for a value and returns its index if found.
- **`search_by_index(index)`**: Returns the value at a specific index.
- **`merge_without_change(second)`**: Merges two sorted lists without modifying the original lists.
- **`merge_with_changes(second)`**: Merges two sorted lists, modifying the original list.
- **`swap_elements_by_index(index1, index2)`**: Swaps two elements in the list by their indices.
- **`sort_ascending()`**: Sorts the list in ascending order.
- **`sort_descending()`**: Sorts the list in descending order.
- **`reverse_with_changes()`**: Reverses the list in place.
- **`reverse_no_changes()`**: Returns a reversed copy of the list without modifying the original.
- **`no_elements_existance()`**: Returns a dictionary with the count of each element in the list.
- **`sort_ascending_recursive()`**: Sorts the list in ascending order using a recursive approach.
- **`sort_descending_recursive()`**: Sorts the list in descending order using a recursive approach.
- **`is_empty()`**: Checks if the list is empty.
- **`__len__()`**: Returns the number of elements in the list.
- **`__iter__()`**: Allows iteration over the list.
- **`__repr__()`**: Provides a string representation of the list.
- **`first()`**: Returns the first element in the list.
- **`last()`**: Returns the last element in the list.
- **`max()`**: Returns the maximum value in the list.
- **`min()`**: Returns the minimum value in the list.
- **`sum()`**: Returns the sum of all elements in the list.
- **`mean()`**: Returns the mean of the elements in the list.
- **`median()`**: Returns the median of the elements in the list.
- **`mood()`**: Returns the mode(s) of the elements in the list.

## Usage

To use the classes and methods, simply import the script and create instances of the desired classes. Here is an example:

```python
from tree_avl import tree_avl, sorted_list_array

# Example usage of AVL Tree
avl_tree = tree_avl()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(5)
print(avl_tree.in_order_traversal(avl_tree.root))  # Output: [5, 10, 20]

# Example usage of Sorted List Array
sorted_list = sorted_list_array()
sorted_list.insert_last(10)
sorted_list.insert_last(5)
sorted_list.insert_last(20)
sorted_list.sort_ascending()
print(sorted_list)  # Output: [5, 10, 20]
```

## Notes

- The **AVL Tree** is a self-balancing binary search tree, ensuring that the tree remains balanced after each insertion or deletion, which guarantees O(log n) time complexity for search, insert, and delete operations.
- The **Sorted List Array** is a dynamic array that supports various operations for maintaining and manipulating a sorted list of numeric values.

