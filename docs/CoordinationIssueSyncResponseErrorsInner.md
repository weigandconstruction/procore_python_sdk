# CoordinationIssueSyncResponseErrorsInner


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
**coordination_issue_file_id** | **int** | ID of the BIM File to be set as origin source | [optional] 
**drawing_revision_id** | **int** | ID of the drawing revision to be set as origin source. Only one of drawing_revision_id or coordination_issue_file_id can be present | [optional] 
**bim_model_id** | **int** | ID of the model to be associated | [optional] 
**due_date** | **str** | Due date of the Coordination Issue | [optional] 
**origin** | [**Body104CoordinationIssueOrigin**](Body104CoordinationIssueOrigin.md) |  | [optional] 
**attachment_upload_uuids** | **List[str]** |  | [optional] 
**attachments** | **List[str]** |  | [optional] 
**viewpoints** | [**List[CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner]**](CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner.md) | An array of issue viewpoints. Only one viewpoint is allowed at this time. | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_sync_response_errors_inner import CoordinationIssueSyncResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueSyncResponseErrorsInner from a JSON string
coordination_issue_sync_response_errors_inner_instance = CoordinationIssueSyncResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueSyncResponseErrorsInner.to_json())

# convert the object into a dict
coordination_issue_sync_response_errors_inner_dict = coordination_issue_sync_response_errors_inner_instance.to_dict()
# create an instance of CoordinationIssueSyncResponseErrorsInner from a dict
coordination_issue_sync_response_errors_inner_from_dict = CoordinationIssueSyncResponseErrorsInner.from_dict(coordination_issue_sync_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


