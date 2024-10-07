# CoordinationIssueAssignmentActivityDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Assignment ID | [optional] 
**old_assignee** | [**CoordinationIssueAssignmentActivityDetailsOldAssignee**](CoordinationIssueAssignmentActivityDetailsOldAssignee.md) |  | [optional] 
**new_assignee** | [**CoordinationIssueAssignmentActivityDetailsNewAssignee**](CoordinationIssueAssignmentActivityDetailsNewAssignee.md) |  | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**created_by** | [**CoordinationIssueAssignmentActivityDetailsCreatedBy**](CoordinationIssueAssignmentActivityDetailsCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_assignment_activity_details import CoordinationIssueAssignmentActivityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueAssignmentActivityDetails from a JSON string
coordination_issue_assignment_activity_details_instance = CoordinationIssueAssignmentActivityDetails.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueAssignmentActivityDetails.to_json())

# convert the object into a dict
coordination_issue_assignment_activity_details_dict = coordination_issue_assignment_activity_details_instance.to_dict()
# create an instance of CoordinationIssueAssignmentActivityDetails from a dict
coordination_issue_assignment_activity_details_from_dict = CoordinationIssueAssignmentActivityDetails.from_dict(coordination_issue_assignment_activity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


