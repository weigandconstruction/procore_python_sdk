# WorkOrderContract

Work Order Contract object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method. If not provided on create action, defaults to Project Configuration. | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_estimated_completion_date** | **date** | Estimated completion date | [optional] 
**contract_start_date** | **date** | Start date | [optional] 
**description** | **str** | Description | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**executed** | **bool** | Executed (or not) | [optional] [default to False]
**execution_date** | **date** | Execution date | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**invoice_contact_user_ids** | **List[int]** | IDs of users in the project directory (see the Project Users endpoint). The users with these IDs will be added as invoice contacts if they belong to the same vendor as the contract vendor. Invoice contacts are the points of contact for subcontractor invoices. | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**number** | **str** | Number | [optional] 
**private** | **bool** | If true, visible to admins and whitelisted accessors; otherwise visible to those with read only access. | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.work_order_contract import WorkOrderContract

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderContract from a JSON string
work_order_contract_instance = WorkOrderContract.from_json(json)
# print the JSON string representation of the object
print(WorkOrderContract.to_json())

# convert the object into a dict
work_order_contract_dict = work_order_contract_instance.to_dict()
# create an instance of WorkOrderContract from a dict
work_order_contract_from_dict = WorkOrderContract.from_dict(work_order_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


