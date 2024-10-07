# RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response

Coordination Issue Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**coordination_issue_id** | **int** | Coordination Issue ID | [optional] 
**old_assignee_id** | **int** | Coordination Issue Assignee ID before the change | [optional] 
**new_assignee_id** | **int** | Coordination Issue Assignee ID after the change | [optional] 
**created_by_id** | **int** | ID of the user responsible for the reassignment | [optional] 
**created_at** | **datetime** | Created date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response import RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response from a JSON string
rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response_instance = RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response.to_json())

# convert the object into a dict
rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response_dict = rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response_instance.to_dict()
# create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response from a dict
rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response_from_dict = RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response.from_dict(rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


