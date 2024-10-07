# ArrayOfTasks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[Task]**](Task.md) |  | [optional] 
**errors** | [**List[ArrayOfTasksErrorsInner]**](ArrayOfTasksErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_tasks import ArrayOfTasks

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTasks from a JSON string
array_of_tasks_instance = ArrayOfTasks.from_json(json)
# print the JSON string representation of the object
print(ArrayOfTasks.to_json())

# convert the object into a dict
array_of_tasks_dict = array_of_tasks_instance.to_dict()
# create an instance of ArrayOfTasks from a dict
array_of_tasks_from_dict = ArrayOfTasks.from_dict(array_of_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


