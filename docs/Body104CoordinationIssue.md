# Body104CoordinationIssue

Coordination Issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Coordination Issue UUID. This is an optional parameter, and is set automatically on server if not present in the payload | [optional] 
**title** | **str** | Coordination Issue title. The title can have a maximum of 80 characters | 
**description** | **str** | Coordination Issue description. | [optional] 
**status** | **str** | Status of the issue. Should be either open or closed | [optional] 
**creation_source** | **str** | Source of issue creation. This attribute is ignored when issue is create by third party developers. | [optional] 
**location_id** | **int** | Location where the issue is present. The location must be in the same project as the project_id | [optional] 
**assignee_id** | **int** | ID of Procore user that should be assigned the issue | [optional] 
**coordination_issue_file_id** | **int** | ID of the BIM File to be set as origin source (required if viewpoints is included in payload) | [optional] 
**drawing_revision_id** | **int** | ID of the drawing revision to be set as origin source. Only one of drawing_revision_id or coordination_issue_file_id can be present | [optional] 
**bim_model_id** | **int** | ID of the model to be associated | [optional] 
**due_date** | **str** | Due date of the Coordination Issue | [optional] 
**issue_type** | **str** | Issue Type of the Coordination Issue | [optional] 
**priority** | **str** | Priority of the Coordination Issue | [optional] 
**trade_id** | **int** | Trade associated with the Coordination Issue | [optional] 
**origin** | [**Body104CoordinationIssueOrigin**](Body104CoordinationIssueOrigin.md) |  | [optional] 
**attachment_upload_uuids** | **List[str]** |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**viewpoints** | [**List[Body104CoordinationIssueViewpointsInner]**](Body104CoordinationIssueViewpointsInner.md) | An array of issue viewpoints. Only one viewpoint is allowed at this time. If specified, must also include coordination_issue_file_id. | [optional] 

## Example

```python
from procore_sdk.models.body104_coordination_issue import Body104CoordinationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of Body104CoordinationIssue from a JSON string
body104_coordination_issue_instance = Body104CoordinationIssue.from_json(json)
# print the JSON string representation of the object
print(Body104CoordinationIssue.to_json())

# convert the object into a dict
body104_coordination_issue_dict = body104_coordination_issue_instance.to_dict()
# create an instance of Body104CoordinationIssue from a dict
body104_coordination_issue_from_dict = Body104CoordinationIssue.from_dict(body104_coordination_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


