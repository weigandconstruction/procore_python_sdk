# RestV10WorkOrderContractsGet200ResponseInner

Work Order Contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**approved_change_orders** | **str** | Approved change orders amount | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_start_date** | **date** | Start date | [optional] 
**contract_estimated_completion_date** | **date** | Estimated completion date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**draft_change_orders_amount** | **str** | Total of all draft change orders | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**executed** | **bool** | Executed (or not) | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**id** | **int** | ID | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**pending_change_orders** | **str** | Pending change orders amount | [optional] 
**pending_revised_contract** | **str** | Pending revised contracts amount | [optional] 
**percentage_paid** | **str** | Percentage paid | [optional] 
**private** | **bool** | If true, visible to admins and whitelisted accessors; otherwise visible to those with read only access. | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**remaining_balance_outstanding** | **str** | Remaining outstanding balance | [optional] 
**requisitions_are_enabled** | **bool** | If true, Requisitions (Subcontractor Invoice) are enabled on the Commitment Contract | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**revised_contract** | **str** | Revised contract amount | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**show_line_items_to_non_admins** | **bool** | If true and the contract is private, non admins with access to the contract will be able to view the SOV items | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**total_draw_requests_amount** | **str** | Total draw requests amount | [optional] 
**total_payments** | **str** | Total payments amount | [optional] 
**total_requisitions_amount** | **str** | Total requisitions (sub invoices) amount | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV10WorkOrderContractsGet200ResponseInnerVendor**](RestV10WorkOrderContractsGet200ResponseInnerVendor.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner import RestV10WorkOrderContractsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsGet200ResponseInner from a JSON string
rest_v10_work_order_contracts_get200_response_inner_instance = RestV10WorkOrderContractsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_get200_response_inner_dict = rest_v10_work_order_contracts_get200_response_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsGet200ResponseInner from a dict
rest_v10_work_order_contracts_get200_response_inner_from_dict = RestV10WorkOrderContractsGet200ResponseInner.from_dict(rest_v10_work_order_contracts_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


