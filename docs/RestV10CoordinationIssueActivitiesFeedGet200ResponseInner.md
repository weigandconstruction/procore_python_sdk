# RestV10CoordinationIssueActivitiesFeedGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**coordination_issue_id** | **float** | Coordination Issue ID | [optional] 
**type** | **str** | Activity Type | [optional] 
**details** | [**RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner**](RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issue_activities_feed_get200_response_inner import RestV10CoordinationIssueActivitiesFeedGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssueActivitiesFeedGet200ResponseInner from a JSON string
rest_v10_coordination_issue_activities_feed_get200_response_inner_instance = RestV10CoordinationIssueActivitiesFeedGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssueActivitiesFeedGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_coordination_issue_activities_feed_get200_response_inner_dict = rest_v10_coordination_issue_activities_feed_get200_response_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssueActivitiesFeedGet200ResponseInner from a dict
rest_v10_coordination_issue_activities_feed_get200_response_inner_from_dict = RestV10CoordinationIssueActivitiesFeedGet200ResponseInner.from_dict(rest_v10_coordination_issue_activities_feed_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


