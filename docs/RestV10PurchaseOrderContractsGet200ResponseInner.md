# RestV10PurchaseOrderContractsGet200ResponseInner

Purchase Order Contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**approved_change_orders** | **str** | Approved Change Orders amount | [optional] 
**assignee** | [**RestV10PurchaseOrderContractsGet200ResponseInnerAssignee**](RestV10PurchaseOrderContractsGet200ResponseInnerAssignee.md) |  | [optional] 
**bill_to_address** | **str** | Bill to address | [optional] 
**billing_schedule_of_values_status** | **str** | Subcontractor SOV status | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**description** | **str** | Description | [optional] 
**draft_change_orders_amount** | **str** | Total of all draft change orders | [optional] 
**executed** | **bool** | Executed status | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**id** | **int** | ID | [optional] 
**issued_on_date** | **date** | Issued on | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**number** | **str** | Number | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_terms** | **str** | Payment terms | [optional] 
**pending_change_orders** | **str** | Pending Change Orders amount | [optional] 
**pending_revised_contract** | **str** | Pending Revised Contract amount | [optional] 
**percentage_paid** | **str** | Purchase Order Contract percentage paid | [optional] 
**private** | **bool** | Enable/Disable Private status | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**remaining_balance_outstanding** | **str** | Remaining Balance Outstanding amount | [optional] 
**requisitions_are_enabled** | **bool** | If true, Requisitions (Subcontractor Invoices) are enabled on the Commitment Contract | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**revised_contract** | **str** | Revised Contract amount | [optional] 
**ship_to_address** | **str** | Ship to address | [optional] 
**ship_via** | **str** | Ship via | [optional] 
**show_line_items_to_non_admins** | **bool** | If true and the contract is private, non admins with access to the contract will be able to view the SOV items | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**total_draw_requests_amount** | **str** | Total Draw Requests Amount | [optional] 
**total_payments** | **str** | Total Payments Amount | [optional] 
**total_requisitions_amount** | **str** | Total Requisitions (Subcontractor Invoices) Amount | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV10WorkOrderContractsGet200ResponseInnerVendor**](RestV10WorkOrderContractsGet200ResponseInnerVendor.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_purchase_order_contracts_get200_response_inner import RestV10PurchaseOrderContractsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PurchaseOrderContractsGet200ResponseInner from a JSON string
rest_v10_purchase_order_contracts_get200_response_inner_instance = RestV10PurchaseOrderContractsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10PurchaseOrderContractsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_purchase_order_contracts_get200_response_inner_dict = rest_v10_purchase_order_contracts_get200_response_inner_instance.to_dict()
# create an instance of RestV10PurchaseOrderContractsGet200ResponseInner from a dict
rest_v10_purchase_order_contracts_get200_response_inner_from_dict = RestV10PurchaseOrderContractsGet200ResponseInner.from_dict(rest_v10_purchase_order_contracts_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


