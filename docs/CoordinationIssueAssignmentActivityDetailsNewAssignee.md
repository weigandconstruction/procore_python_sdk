# CoordinationIssueAssignmentActivityDetailsNewAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_assignment_activity_details_new_assignee import CoordinationIssueAssignmentActivityDetailsNewAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueAssignmentActivityDetailsNewAssignee from a JSON string
coordination_issue_assignment_activity_details_new_assignee_instance = CoordinationIssueAssignmentActivityDetailsNewAssignee.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueAssignmentActivityDetailsNewAssignee.to_json())

# convert the object into a dict
coordination_issue_assignment_activity_details_new_assignee_dict = coordination_issue_assignment_activity_details_new_assignee_instance.to_dict()
# create an instance of CoordinationIssueAssignmentActivityDetailsNewAssignee from a dict
coordination_issue_assignment_activity_details_new_assignee_from_dict = CoordinationIssueAssignmentActivityDetailsNewAssignee.from_dict(coordination_issue_assignment_activity_details_new_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


