# ChecklistTemplate4Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location ID | [optional] 
**name** | **str** | Location name | [optional] 
**node_name** | **str** | Location node name | [optional] 
**parent_id** | **int** | Location parent id | [optional] 
**created_at** | **datetime** | Timestamp of Location creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update to Location | [optional] 

## Example

```python
from procore_sdk.models.checklist_template4_location import ChecklistTemplate4Location

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplate4Location from a JSON string
checklist_template4_location_instance = ChecklistTemplate4Location.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplate4Location.to_json())

# convert the object into a dict
checklist_template4_location_dict = checklist_template4_location_instance.to_dict()
# create an instance of ChecklistTemplate4Location from a dict
checklist_template4_location_from_dict = ChecklistTemplate4Location.from_dict(checklist_template4_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


