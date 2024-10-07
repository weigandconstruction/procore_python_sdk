# RestV10ChangeEventsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_event** | [**ChangeEvent**](ChangeEvent.md) |  | 
**attachments** | **List[str]** | Change Event Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_post_request import RestV10ChangeEventsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsPostRequest from a JSON string
rest_v10_change_events_post_request_instance = RestV10ChangeEventsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsPostRequest.to_json())

# convert the object into a dict
rest_v10_change_events_post_request_dict = rest_v10_change_events_post_request_instance.to_dict()
# create an instance of RestV10ChangeEventsPostRequest from a dict
rest_v10_change_events_post_request_from_dict = RestV10ChangeEventsPostRequest.from_dict(rest_v10_change_events_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


