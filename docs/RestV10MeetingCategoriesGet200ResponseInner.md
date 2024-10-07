# RestV10MeetingCategoriesGet200ResponseInner

Meeting category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Meeting category id | [optional] 
**title** | **str** | Meeting category topic | [optional] 
**position** | **int** | Meeting category position | [optional] 
**created_by** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meeting_categories_get200_response_inner import RestV10MeetingCategoriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingCategoriesGet200ResponseInner from a JSON string
rest_v10_meeting_categories_get200_response_inner_instance = RestV10MeetingCategoriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingCategoriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_meeting_categories_get200_response_inner_dict = rest_v10_meeting_categories_get200_response_inner_instance.to_dict()
# create an instance of RestV10MeetingCategoriesGet200ResponseInner from a dict
rest_v10_meeting_categories_get200_response_inner_from_dict = RestV10MeetingCategoriesGet200ResponseInner.from_dict(rest_v10_meeting_categories_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


