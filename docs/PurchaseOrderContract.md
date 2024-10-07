# PurchaseOrderContract

Purchase Order Contract object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method. If not provided on create action, defaults to Project Configuration. | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**assignee_id** | **int** | Assignee ID | [optional] 
**bill_to_address** | **str** | Bill to address | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**description** | **str** | Description | [optional] 
**executed** | **bool** | Executed status | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**invoice_contact_user_ids** | **List[int]** | IDs of users in the project directory (see the Project Users endpoint). The users with these IDs will be added as invoice contacts if they belong to the same vendor as the contract vendor. Invoice contacts are the points of contact for subcontractor invoices. | [optional] 
**issued_on_date** | **date** | Issued on | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**number** | **str** | Number | [optional] 
**payment_terms** | **str** | Payment terms | [optional] 
**private** | **bool** | Enable/Disable private status | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**ship_to_address** | **str** | Ship to address | [optional] 
**ship_via** | **str** | Ship via | [optional] 
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
from procore_sdk.models.purchase_order_contract import PurchaseOrderContract

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderContract from a JSON string
purchase_order_contract_instance = PurchaseOrderContract.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderContract.to_json())

# convert the object into a dict
purchase_order_contract_dict = purchase_order_contract_instance.to_dict()
# create an instance of PurchaseOrderContract from a dict
purchase_order_contract_from_dict = PurchaseOrderContract.from_dict(purchase_order_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


