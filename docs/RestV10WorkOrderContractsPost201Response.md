# RestV10WorkOrderContractsPost201Response

Work Order Contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**approved_change_orders** | **str** | Approved change orders amount | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**change_order_packages** | [**List[RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner]**](RestV10WorkOrderContractsPost201ResponseChangeOrderPackagesInner.md) | Change order packages | [optional] 
**change_order_requests** | **List[List[RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner]]** | Change order requests | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_start_date** | **date** | Start date | [optional] 
**contract_estimated_completion_date** | **date** | Estimated completion date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by_id** | **int** | ID of the user who created the Contract | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**draft_change_orders_amount** | **str** | Total of all draft change orders | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**executed** | **bool** | Executed (or not) | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**id** | **int** | ID | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**invoice_contacts** | [**List[RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner]**](RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.md) | Invoice Contacts | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**line_items** | [**List[RestV10WorkOrderContractsPost201ResponseLineItemsInner]**](RestV10WorkOrderContractsPost201ResponseLineItemsInner.md) | Line items | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payments_issued** | [**List[RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner]**](RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner.md) | Payment issued | [optional] 
**pending_change_orders** | **str** | Pending change orders amount | [optional] 
**pending_revised_contract** | **str** | Pending revised contracts amount | [optional] 
**percentage_paid** | **str** | Percentage paid | [optional] 
**potential_change_orders** | [**List[RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner]**](RestV10WorkOrderContractsPost201ResponsePotentialChangeOrdersInner.md) | Work Order Contract potential change orders | [optional] 
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
**vendor** | [**RestV10WorkOrderContractsPost201ResponseVendor**](RestV10WorkOrderContractsPost201ResponseVendor.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response import RestV10WorkOrderContractsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201Response from a JSON string
rest_v10_work_order_contracts_post201_response_instance = RestV10WorkOrderContractsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201Response.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_dict = rest_v10_work_order_contracts_post201_response_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201Response from a dict
rest_v10_work_order_contracts_post201_response_from_dict = RestV10WorkOrderContractsPost201Response.from_dict(rest_v10_work_order_contracts_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


