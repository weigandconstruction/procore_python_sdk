# MeetingCategory

Meeting Category object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | The Position of the Meeting Category | [optional] 
**title** | **str** | The Title of the Meeting Category | [optional] 

## Example

```python
from procore_sdk.models.meeting_category import MeetingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingCategory from a JSON string
meeting_category_instance = MeetingCategory.from_json(json)
# print the JSON string representation of the object
print(MeetingCategory.to_json())

# convert the object into a dict
meeting_category_dict = meeting_category_instance.to_dict()
# create an instance of MeetingCategory from a dict
meeting_category_from_dict = MeetingCategory.from_dict(meeting_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


