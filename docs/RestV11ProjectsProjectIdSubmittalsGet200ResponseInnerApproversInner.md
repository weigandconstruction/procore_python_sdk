# RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**approver_type** | **str** |  | [optional] 
**associated_attachments** | [**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerAssociatedAttachmentsInner]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerAssociatedAttachmentsInner.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**due_date** | **date** |  | [optional] 
**response_required** | **bool** |  | [optional] 
**response** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerResponse.md) |  | [optional] 
**returned_date** | **date** |  | [optional] 
**sent_date** | **date** |  | [optional] 
**user** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**workflow_group_number** | **int** | The step in the workflow that the approver is on | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner from a JSON string
rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_instance = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_dict = rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner from a dict
rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_from_dict = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInner.from_dict(rest_v11_projects_project_id_submittals_get200_response_inner_approvers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


