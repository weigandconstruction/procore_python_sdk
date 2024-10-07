# ChecklistResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the Response | [optional] 
**corresponding_status** | **str** | Corresponding Checklist Item status | [optional] 
**item_status_id** | **int** | Checklist Item Status ID | [optional] 

## Example

```python
from procore_sdk.models.checklist_response2 import ChecklistResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponse2 from a JSON string
checklist_response2_instance = ChecklistResponse2.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponse2.to_json())

# convert the object into a dict
checklist_response2_dict = checklist_response2_instance.to_dict()
# create an instance of ChecklistResponse2 from a dict
checklist_response2_from_dict = ChecklistResponse2.from_dict(checklist_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


