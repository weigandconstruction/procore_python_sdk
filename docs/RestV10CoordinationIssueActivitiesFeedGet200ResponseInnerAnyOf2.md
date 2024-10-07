# RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2

Coordination Issue Creation Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**coordination_issue_id** | **float** | Coordination Issue ID | [optional] 
**type** | **str** | Activity Type. | [optional] 
**details** | [**CoordinationIssueCreationActivityDetails**](CoordinationIssueCreationActivityDetails.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2 import RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2 from a JSON string
rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2_instance = RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2.to_json())

# convert the object into a dict
rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2_dict = rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2_instance.to_dict()
# create an instance of RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2 from a dict
rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2_from_dict = RestV10CoordinationIssueActivitiesFeedGet200ResponseInnerAnyOf2.from_dict(rest_v10_coordination_issue_activities_feed_get200_response_inner_any_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


