# RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**created_by** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerApproversInnerUser.md) |  | [optional] 
**description** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**specification_section_id** | **int** |  | [optional] 
**submittal_ids** | **List[int]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage from a JSON string
rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package_instance = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package_dict = rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage from a dict
rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package_from_dict = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSubmittalPackage.from_dict(rest_v11_projects_project_id_submittals_get200_response_inner_submittal_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


