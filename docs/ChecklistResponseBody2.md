# ChecklistResponseBody2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Response2**](Response2.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_response_body2 import ChecklistResponseBody2

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponseBody2 from a JSON string
checklist_response_body2_instance = ChecklistResponseBody2.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponseBody2.to_json())

# convert the object into a dict
checklist_response_body2_dict = checklist_response_body2_instance.to_dict()
# create an instance of ChecklistResponseBody2 from a dict
checklist_response_body2_from_dict = ChecklistResponseBody2.from_dict(checklist_response_body2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


