# PrimeContract

Prime Contract object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_completion_date** | **str** | Actual Completion Date | [optional] 
**approval_letter_date** | **date** | Approval letter date | [optional] 
**architect_id** | **int** | Architect ID | [optional] 
**contractor_id** | **int** | Contractor ID | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_estimated_completion_date** | **str** | Contract Estimated Completion Date | [optional] 
**contract_start_date** | **str** | Contract Start Date | [optional] 
**description** | **str** | Description | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**executed** | **bool** | Executed | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**number** | **str** | Number of the Prime Contract | [optional] 
**origin_data** | **str** | Prime Contract third party data | [optional] 
**origin_id** | **str** | Prime Contract third party ID | [optional] 
**retainage_percent** | **str** | Retainage Percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**signed_contract_received_date** | **str** | Signed Contract Received Date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title of the Prime Contract | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.prime_contract import PrimeContract

# TODO update the JSON string below
json = "{}"
# create an instance of PrimeContract from a JSON string
prime_contract_instance = PrimeContract.from_json(json)
# print the JSON string representation of the object
print(PrimeContract.to_json())

# convert the object into a dict
prime_contract_dict = prime_contract_instance.to_dict()
# create an instance of PrimeContract from a dict
prime_contract_from_dict = PrimeContract.from_dict(prime_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


