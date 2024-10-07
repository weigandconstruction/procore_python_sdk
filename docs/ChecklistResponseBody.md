# ChecklistResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Response**](Response.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_response_body import ChecklistResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistResponseBody from a JSON string
checklist_response_body_instance = ChecklistResponseBody.from_json(json)
# print the JSON string representation of the object
print(ChecklistResponseBody.to_json())

# convert the object into a dict
checklist_response_body_dict = checklist_response_body_instance.to_dict()
# create an instance of ChecklistResponseBody from a dict
checklist_response_body_from_dict = ChecklistResponseBody.from_dict(checklist_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


