# CoordinationIssueCreationActivityDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Creation ID | [optional] 
**assignee** | [**CoordinationIssueAssignmentActivityDetailsOldAssignee**](CoordinationIssueAssignmentActivityDetailsOldAssignee.md) |  | [optional] 
**created_by** | [**CoordinationIssueAssignmentActivityDetailsOldAssignee**](CoordinationIssueAssignmentActivityDetailsOldAssignee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_creation_activity_details import CoordinationIssueCreationActivityDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueCreationActivityDetails from a JSON string
coordination_issue_creation_activity_details_instance = CoordinationIssueCreationActivityDetails.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueCreationActivityDetails.to_json())

# convert the object into a dict
coordination_issue_creation_activity_details_dict = coordination_issue_creation_activity_details_instance.to_dict()
# create an instance of CoordinationIssueCreationActivityDetails from a dict
coordination_issue_creation_activity_details_from_dict = CoordinationIssueCreationActivityDetails.from_dict(coordination_issue_creation_activity_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


