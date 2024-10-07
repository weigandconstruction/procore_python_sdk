# RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner

Coordination Issue Status Change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**coordination_issue_id** | **int** | ID of the parent Coordination Issue | [optional] 
**old_status** | **str** | Value of the status prior to change | [optional] 
**new_status** | **str** | Value of the status following the change | [optional] 
**created_by_id** | **int** | Creator ID | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**linked_rfi** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner**](RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner.md) |  | [optional] 
**linked_observation_item** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner**](RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_id_status_changes_get200_response_inner import RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner from a JSON string
rest_v10_coordination_issues_id_status_changes_get200_response_inner_instance = RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_id_status_changes_get200_response_inner_dict = rest_v10_coordination_issues_id_status_changes_get200_response_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner from a dict
rest_v10_coordination_issues_id_status_changes_get200_response_inner_from_dict = RestV10CoordinationIssuesIdStatusChangesGet200ResponseInner.from_dict(rest_v10_coordination_issues_id_status_changes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


