# ResourceAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resource Assignment id | [optional] 
**task_id** | **int** | Task id | [optional] 
**resource_id** | **int** | Resource id | [optional] 
**schedule_attributes** | **Dict[str, str]** | When a schedule is imported from an external system, any attributes which are not otherwise represented in this object will appear as key-value pairs here. Note that the set of keys present in this object will depend on the application from which the schedule was obtained. | [optional] 

## Example

```python
from procore_sdk.models.resource_assignment import ResourceAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAssignment from a JSON string
resource_assignment_instance = ResourceAssignment.from_json(json)
# print the JSON string representation of the object
print(ResourceAssignment.to_json())

# convert the object into a dict
resource_assignment_dict = resource_assignment_instance.to_dict()
# create an instance of ResourceAssignment from a dict
resource_assignment_from_dict = ResourceAssignment.from_dict(resource_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


