# ChecklistResponseBody1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Response1**](Response1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_response_body1 import ChecklistResponseBody1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponseBody1 from a JSON string
checklist_response_body1_instance = ChecklistResponseBody1.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponseBody1.to_json())

# convert the object into a dict
checklist_response_body1_dict = checklist_response_body1_instance.to_dict()
# create an instance of ChecklistResponseBody1 from a dict
checklist_response_body1_from_dict = ChecklistResponseBody1.from_dict(checklist_response_body1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


