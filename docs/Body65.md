# Body65


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meeting_id** | **int** | The ID of the Meeting the Meeting Topic belongs to | 
**meeting_topic** | [**MeetingTopic**](MeetingTopic.md) |  | 
**attachments** | **List[str]** | An array of the Attachments of the Meeting Topic. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.body65 import Body65

# TODO update the JSON string below
json = "{}"
# create an instance of Body65 from a JSON string
body65_instance = Body65.from_json(json)
# print the JSON string representation of the object
print(Body65.to_json())

# convert the object into a dict
body65_dict = body65_instance.to_dict()
# create an instance of Body65 from a dict
body65_from_dict = Body65.from_dict(body65_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


