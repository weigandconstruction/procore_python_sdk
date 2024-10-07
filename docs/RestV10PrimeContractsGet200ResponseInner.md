# RestV10PrimeContractsGet200ResponseInner

Prime Contracts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Prime Contract ID | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**approval_letter_date** | **date** | Approval letter date | [optional] 
**approved_change_orders** | **str** | Approved change orders amount | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_estimated_completion_date** | **date** | Contract estimated completion date | [optional] 
**contract_start_date** | **date** | Contract start date | [optional] 
**contract_termination_date** | **date** | Contract termination date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description of the Prime Contract | [optional] 
**executed** | **bool** | Executed status | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**grand_total** | **str** | Total of Line items including markup, plus project level (vertical) markup, if any | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**number** | **str** | Number | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Prime Contract third party data | [optional] 
**origin_id** | **str** | Prime Contract third party ID | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**show_line_items_to_non_admins** | **bool** | If true and the contract is private, non admins with access to the contract will be able to view the SOV items | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**architect** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**contractor** | [**RestV10PrimeContractsGet200ResponseInnerContractor**](RestV10PrimeContractsGet200ResponseInnerContractor.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**vendor** | [**RestV10PrimeContractsGet200ResponseInnerContractor**](RestV10PrimeContractsGet200ResponseInnerContractor.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_prime_contracts_get200_response_inner import RestV10PrimeContractsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PrimeContractsGet200ResponseInner from a JSON string
rest_v10_prime_contracts_get200_response_inner_instance = RestV10PrimeContractsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10PrimeContractsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_prime_contracts_get200_response_inner_dict = rest_v10_prime_contracts_get200_response_inner_instance.to_dict()
# create an instance of RestV10PrimeContractsGet200ResponseInner from a dict
rest_v10_prime_contracts_get200_response_inner_from_dict = RestV10PrimeContractsGet200ResponseInner.from_dict(rest_v10_prime_contracts_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


