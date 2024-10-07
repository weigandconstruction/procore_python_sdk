# RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions

Group of model objects represented as an array of object ids, or object ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[int]** | Array of object ids | [optional] 
**object_ranges** | **List[List[int]]** | Array of object ranges. A range is an array containing two numbers, the first represents object id, the second represents the number of objects in the range. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions import RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions_dict = rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibilityExceptions.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


