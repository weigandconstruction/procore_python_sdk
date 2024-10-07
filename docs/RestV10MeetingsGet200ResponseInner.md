# RestV10MeetingsGet200ResponseInner

Group of meetings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_title** | **str** | Meeting group title | [optional] 
**meetings** | [**List[RestV10MeetingsGet200ResponseInnerMeetingsInner]**](RestV10MeetingsGet200ResponseInnerMeetingsInner.md) | Meetings | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meetings_get200_response_inner import RestV10MeetingsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingsGet200ResponseInner from a JSON string
rest_v10_meetings_get200_response_inner_instance = RestV10MeetingsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_meetings_get200_response_inner_dict = rest_v10_meetings_get200_response_inner_instance.to_dict()
# create an instance of RestV10MeetingsGet200ResponseInner from a dict
rest_v10_meetings_get200_response_inner_from_dict = RestV10MeetingsGet200ResponseInner.from_dict(rest_v10_meetings_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


