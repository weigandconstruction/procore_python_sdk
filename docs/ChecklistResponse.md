# ChecklistResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the Response | [optional] 
**corresponding_status** | **str** | Corresponding Checklist Item status | [optional] 

## Example

```python
from procore_sdk.models.checklist_response import ChecklistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponse from a JSON string
checklist_response_instance = ChecklistResponse.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponse.to_json())

# convert the object into a dict
checklist_response_dict = checklist_response_instance.to_dict()
# create an instance of ChecklistResponse from a dict
checklist_response_from_dict = ChecklistResponse.from_dict(checklist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


