# Remove Duplicates Problem

## Problem Statement

Given a list of elements, implement a function `remove_duplicates` that removes duplicate elements from the list while preserving the original order. The function should return a new list without any duplicates.

## Function Signature

```python
def remove_duplicates(input_list: List) -> List:
    """
    Removes duplicates from the input list.

    Args:
    - input_list: A list of elements.

    Returns:
    - A new list with duplicates removed, preserving the original order.
    """
    # Your implementation goes here
```

## Examples
### Example One:
```python
input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print(result)
```
#### Expected Output:
```csharp
[1, 2, 3, 4, 5]
```
### Example Two:
```python
input_list = [1, "apple", "orange", 2, 1, "apple"]
result = remove_duplicates(input_list)
print(result)
```
#### Expected Output:
```csharp 
[1, "apple", "orange", 2]
```
## Constraints
- The input list may contain elements of any data type.
- The input list may be empty.
- The order of elements in the output list should be the same as the original order in the input list.

## Explanation
The remove_duplicates function should iterate through the input list and build a new list, adding elements to it only if they haven't been encountered before. This ensures that the output list contains unique elements while preserving the order.
