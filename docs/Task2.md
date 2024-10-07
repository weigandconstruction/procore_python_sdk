# Task2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task ID | [optional] 
**name** | **str** | Task name | [optional] 
**key** | **str** | A deprecated value which was originally used to uniquely identify tasks. This value will be removed in a later version of the API. | [optional] 

## Example

```python
from procore_sdk.models.task2 import Task2

# TODO update the JSON string below
json = "{}"
# create an instance of Task2 from a JSON string
task2_instance = Task2.from_json(json)
# print the JSON string representation of the object
print(Task2.to_json())

# convert the object into a dict
task2_dict = task2_instance.to_dict()
# create an instance of Task2 from a dict
task2_from_dict = Task2.from_dict(task2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


