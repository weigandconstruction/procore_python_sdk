# Body68


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meeting_attendee_record** | [**Body68MeetingAttendeeRecord**](Body68MeetingAttendeeRecord.md) |  | 

## Example

```python
from procore_sdk.models.body68 import Body68

# TODO update the JSON string below
json = "{}"
# create an instance of Body68 from a JSON string
body68_instance = Body68.from_json(json)
# print the JSON string representation of the object
print(Body68.to_json())

# convert the object into a dict
body68_dict = body68_instance.to_dict()
# create an instance of Body68 from a dict
body68_from_dict = Body68.from_dict(body68_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


