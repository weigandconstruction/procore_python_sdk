# RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**coordination_issue_assignment** | [**RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequestCoordinationIssueAssignment**](RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequestCoordinationIssueAssignment.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_coordination_issue_id_assignments_post_request import RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest from a JSON string
rest_v10_coordination_issues_coordination_issue_id_assignments_post_request_instance = RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest.to_json())

# convert the object into a dict
rest_v10_coordination_issues_coordination_issue_id_assignments_post_request_dict = rest_v10_coordination_issues_coordination_issue_id_assignments_post_request_instance.to_dict()
# create an instance of RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest from a dict
rest_v10_coordination_issues_coordination_issue_id_assignments_post_request_from_dict = RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPostRequest.from_dict(rest_v10_coordination_issues_coordination_issue_id_assignments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


