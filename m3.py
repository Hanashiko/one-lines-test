from typing import Callable, Any

flatten = lambda target: sum((flatten(sub) if isinstance(sub, list) else [sub] for sub in target), [])

nested_list: list[Any] = [1, [2, [3, 4], 5, "F"], [6, 7], 8, "S", [[[[[[9, 10], 11]]]]]]
print(flatten(nested_list))