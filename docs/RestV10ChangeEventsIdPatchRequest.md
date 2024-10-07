# RestV10ChangeEventsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**change_event** | [**ChangeEvent1**](ChangeEvent1.md) |  | 
**attachments** | **List[str]** | Change Event Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_id_patch_request import RestV10ChangeEventsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsIdPatchRequest from a JSON string
rest_v10_change_events_id_patch_request_instance = RestV10ChangeEventsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_change_events_id_patch_request_dict = rest_v10_change_events_id_patch_request_instance.to_dict()
# create an instance of RestV10ChangeEventsIdPatchRequest from a dict
rest_v10_change_events_id_patch_request_from_dict = RestV10ChangeEventsIdPatchRequest.from_dict(rest_v10_change_events_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


