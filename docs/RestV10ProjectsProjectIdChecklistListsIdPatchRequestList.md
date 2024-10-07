# RestV10ProjectsProjectIdChecklistListsIdPatchRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Inspection | [optional] 
**description** | **str** | Description of the Inspection | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due. | [optional] 
**inspection_date** | **date** | Date of the Inspection | [optional] 
**inspection_type_id** | **int** | The ID of the Inspection&#39;s Type | [optional] 
**number** | **int** | The Number of the Checklist. If no number is passed in, the next available number will be used. | [optional] 
**point_of_contact_id** | **int** | The ID of the Inspection&#39;s Point of Contact | [optional] 
**inspector_ids** | **List[int]** | The IDs of the Inspectors performing the Inspection | [optional] 
**private** | **bool** | Indicates whether this Inspection is private | [optional] [default to True]
**responsible_contractor_id** | **int** | The ID of the Inspection&#39;s Responsible Contractor | [optional] 
**spec_section_id** | **int** | The ID of the Inspection&#39;s Specification Section | [optional] 
**status** | **str** | The Inspection&#39;s status | [optional] 
**trade_id** | **int** | The ID of the Trade involved in the Inspection | [optional] 
**distribution_member_ids** | **List[int]** | The IDs of the Distribution Members for the Inspection | [optional] 
**location_id** | **int** | The ID of the Location of the Inspection | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_checklist_lists_id_patch_request_list import RestV10ProjectsProjectIdChecklistListsIdPatchRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdChecklistListsIdPatchRequestList from a JSON string
rest_v10_projects_project_id_checklist_lists_id_patch_request_list_instance = RestV10ProjectsProjectIdChecklistListsIdPatchRequestList.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdChecklistListsIdPatchRequestList.to_json())

# convert the object into a dict
rest_v10_projects_project_id_checklist_lists_id_patch_request_list_dict = rest_v10_projects_project_id_checklist_lists_id_patch_request_list_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdChecklistListsIdPatchRequestList from a dict
rest_v10_projects_project_id_checklist_lists_id_patch_request_list_from_dict = RestV10ProjectsProjectIdChecklistListsIdPatchRequestList.from_dict(rest_v10_projects_project_id_checklist_lists_id_patch_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


