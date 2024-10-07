# RestV10MeetingCategoriesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**id** | **int** | Meeting category id | [optional] 
**title** | **str** | Meeting category topic | [optional] 
**position** | **int** | Meeting category position | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_meeting_categories_post201_response import RestV10MeetingCategoriesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeetingCategoriesPost201Response from a JSON string
rest_v10_meeting_categories_post201_response_instance = RestV10MeetingCategoriesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10MeetingCategoriesPost201Response.to_json())

# convert the object into a dict
rest_v10_meeting_categories_post201_response_dict = rest_v10_meeting_categories_post201_response_instance.to_dict()
# create an instance of RestV10MeetingCategoriesPost201Response from a dict
rest_v10_meeting_categories_post201_response_from_dict = RestV10MeetingCategoriesPost201Response.from_dict(rest_v10_meeting_categories_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


