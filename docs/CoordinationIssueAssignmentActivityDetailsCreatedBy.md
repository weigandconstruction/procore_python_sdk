# CoordinationIssueAssignmentActivityDetailsCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_assignment_activity_details_created_by import CoordinationIssueAssignmentActivityDetailsCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueAssignmentActivityDetailsCreatedBy from a JSON string
coordination_issue_assignment_activity_details_created_by_instance = CoordinationIssueAssignmentActivityDetailsCreatedBy.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueAssignmentActivityDetailsCreatedBy.to_json())

# convert the object into a dict
coordination_issue_assignment_activity_details_created_by_dict = coordination_issue_assignment_activity_details_created_by_instance.to_dict()
# create an instance of CoordinationIssueAssignmentActivityDetailsCreatedBy from a dict
coordination_issue_assignment_activity_details_created_by_from_dict = CoordinationIssueAssignmentActivityDetailsCreatedBy.from_dict(coordination_issue_assignment_activity_details_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


