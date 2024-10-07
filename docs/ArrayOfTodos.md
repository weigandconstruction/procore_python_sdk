# ArrayOfTodos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[ToDo1]**](ToDo1.md) |  | [optional] 
**errors** | [**List[ArrayOfTodosErrorsInner]**](ArrayOfTodosErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_todos import ArrayOfTodos

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTodos from a JSON string
array_of_todos_instance = ArrayOfTodos.from_json(json)
# print the JSON string representation of the object
print(ArrayOfTodos.to_json())

# convert the object into a dict
array_of_todos_dict = array_of_todos_instance.to_dict()
# create an instance of ArrayOfTodos from a dict
array_of_todos_from_dict = ArrayOfTodos.from_dict(array_of_todos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


