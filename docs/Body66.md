# Body66


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Meeting Topic belongs to | 
**meeting_id** | **int** | The ID of the Meeting the Meeting Topic belongs to | 
**meeting_topic** | [**MeetingTopic**](MeetingTopic.md) |  | 
**attachments** | **List[str]** | An array of the Attachments of the Meeting Topic. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

## Example

```python
from procore_sdk.models.body66 import Body66

# TODO update the JSON string below
json = "{}"
# create an instance of Body66 from a JSON string
body66_instance = Body66.from_json(json)
# print the JSON string representation of the object
print(Body66.to_json())

# convert the object into a dict
body66_dict = body66_instance.to_dict()
# create an instance of Body66 from a dict
body66_from_dict = Body66.from_dict(body66_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


