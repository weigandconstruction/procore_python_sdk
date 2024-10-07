# RestV11ProjectsProjectIdChecklistListsPostRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Inspection | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due. | [optional] 
**identifier** | **str** | Identifier of the Inspection | [optional] 
**inspection_date** | **date** | Date of the Inspection | [optional] 
**inspection_type_id** | **int** | The ID of the Inspection&#39;s Type | [optional] 
**number** | **int** | The Number of the Checklist. If no number is passed in, the next available number will be used. | [optional] 
**managed_equipment_id** | **int** | The ID of the Inspection&#39;s Managed Equipment | [optional] 
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
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_checklist_lists_post_request_list import RestV11ProjectsProjectIdChecklistListsPostRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdChecklistListsPostRequestList from a JSON string
rest_v11_projects_project_id_checklist_lists_post_request_list_instance = RestV11ProjectsProjectIdChecklistListsPostRequestList.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdChecklistListsPostRequestList.to_json())

# convert the object into a dict
rest_v11_projects_project_id_checklist_lists_post_request_list_dict = rest_v11_projects_project_id_checklist_lists_post_request_list_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdChecklistListsPostRequestList from a dict
rest_v11_projects_project_id_checklist_lists_post_request_list_from_dict = RestV11ProjectsProjectIdChecklistListsPostRequestList.from_dict(rest_v11_projects_project_id_checklist_lists_post_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


