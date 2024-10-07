# RFIBodyRfi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The Subject of the RFI | 
**reference** | **str** | The Reference of the RFI | [optional] 
**assignee_id** | **int** | The ID of the Assignee User. *Only admin users can set this field DEPRECATED. Please use assignee_ids instead | [optional] 
**assignee_ids** | **List[int]** | An array of IDs of the Assignees of the RFI *Only admin users can set this field **If this param is not provided, the assigned_id will be used instead | [optional] 
**required_assignee_ids** | **List[int]** | An array of IDs of the Assignees that are required to respond to the RFI * Only admin users can set this field ** IDs must also be present in assignee_ids  | [optional] 
**draft** | **bool** | The Draft status of the RFI | [optional] [default to False]
**due_date** | **date** | The Due Date of the RFI *Only admin users can set this field | [optional] 
**received_from_login_information_id** | **int** | The ID of the Received From User of the RFI | [optional] 
**responsible_contractor_id** | **int** | The ID of the Responsible Contractor Vendor of the RFI | [optional] 
**distribution_ids** | **List[int]** | An array of IDs of the Distributions of the RFI | [optional] 
**number** | **str** | The Number of the RFI *This field will be auto-populated if the RFI is not draft | [optional] 
**private** | **bool** | The Private status of the RFI | [optional] [default to False]
**project_stage_id** | **int** | The ID of the Project Stage of the RFI *If Number By Stage is enabled in RFI settings, this will add the prefix of the project stage to the full number of the RFI. | [optional] 
**schedule_impact** | [**RFIBodyRfiScheduleImpact**](RFIBodyRfiScheduleImpact.md) |  | [optional] 
**cost_impact** | [**RFIBodyRfiCostImpact**](RFIBodyRfiCostImpact.md) |  | [optional] 
**location_id** | **int** | The ID of the Location of the RFI | [optional] 
**drawing_number** | **str** | The Drawing Number of the RFI | [optional] 
**specification_section_id** | **int** | The ID of the Specification Section of the RFI | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code of the RFI | [optional] 
**rfi_manager_id** | **int** | The ID of the RFI Manager User of the RFI *Only admin users (or standard users, if the project&#39;s configuration allows for it) can set this field | 
**question** | [**RFIBodyRfiQuestion**](RFIBodyRfiQuestion.md) |  | 
**custom_textfield_1** | **str** | The Custom Textfield 1 of the RFI | [optional] 
**custom_textfield_2** | **str** | The Custom Textfield 2 of the RFI | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rfi_body_rfi import RFIBodyRfi

# TODO update the JSON string below
json = "{}"
# create an instance of RFIBodyRfi from a JSON string
rfi_body_rfi_instance = RFIBodyRfi.from_json(json)
# print the JSON string representation of the object
print(RFIBodyRfi.to_json())

# convert the object into a dict
rfi_body_rfi_dict = rfi_body_rfi_instance.to_dict()
# create an instance of RFIBodyRfi from a dict
rfi_body_rfi_from_dict = RFIBodyRfi.from_dict(rfi_body_rfi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


