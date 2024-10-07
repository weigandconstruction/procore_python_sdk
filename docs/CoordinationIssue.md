# CoordinationIssue

Coordination Issue Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Coordination Issue title. The title can have a maximum of 80 characters. | [optional] 
**description** | **str** | Coordination Issue description. | [optional] 
**status** | **str** | Coordination Issue status. Must be open, ready_for_review or closed. Only issue assignee can set ready_for_review. | [optional] 
**location_id** | **int** | Location where the issue is present. The location must be in the same project as the project_id | [optional] 
**assignee_id** | **int** | ID of Procore user that should be assigned the issue | [optional] 
**due_date** | **str** | Due date of the Coordination Issue | [optional] 
**issue_type** | **str** | Issue Type of the Coordination Issue | [optional] 
**priority** | **str** | Priority of the Coordination Issue | [optional] 
**trade_id** | **int** | Trade associated with the Coordination Issue | [optional] 
**origin** | **str** | Delete origin association. Only &#39;null&#39; value accepted | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue import CoordinationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssue from a JSON string
coordination_issue_instance = CoordinationIssue.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssue.to_json())

# convert the object into a dict
coordination_issue_dict = coordination_issue_instance.to_dict()
# create an instance of CoordinationIssue from a dict
coordination_issue_from_dict = CoordinationIssue.from_dict(coordination_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


