# ToDo2

ToDo object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **int** | The ID of the Assignment of the ToDo | [optional] 
**color** | **str** | The Color of the ToDo | [optional] 
**finish_datetime** | **datetime** | The Finish date-time of the ToDo | [optional] 
**name** | **str** | The Name of the ToDo | [optional] 
**description** | **str** | The Description of the ToDo | [optional] 
**percentage** | **int** | The Percentage of the ToDo | [optional] 
**private** | **bool** | The Private status of the ToDo | [optional] 
**start_datetime** | **datetime** | The Start date-time of the ToDo | [optional] 

## Example

```python
from procore_sdk.models.to_do2 import ToDo2

# TODO update the JSON string below
json = "{}"
# create an instance of ToDo2 from a JSON string
to_do2_instance = ToDo2.from_json(json)
# print the JSON string representation of the object
print(ToDo2.to_json())

# convert the object into a dict
to_do2_dict = to_do2_instance.to_dict()
# create an instance of ToDo2 from a dict
to_do2_from_dict = ToDo2.from_dict(to_do2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


