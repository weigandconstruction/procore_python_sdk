# RestV10PurchaseOrderContractsPost201Response

Purchase Order Contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**approved_change_orders** | **str** | Approved Change Orders Amount | [optional] 
**assignee** | [**RestV10PurchaseOrderContractsGet200ResponseInnerAssignee**](RestV10PurchaseOrderContractsGet200ResponseInnerAssignee.md) |  | [optional] 
**attachments** | [**RestV10WorkOrderContractsPost201ResponseAttachmentsInner**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**bill_to_address** | **str** | Bill to Address | [optional] 
**change_order_packages** | [**List[RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner]**](RestV10PurchaseOrderContractsPost201ResponseChangeOrderPackagesInner.md) |  | [optional] 
**change_order_requests** | [**List[RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner]**](RestV10WorkOrderContractsPost201ResponseChangeOrderRequestsInnerInner.md) |  | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**created_by_id** | **int** | ID of the user who created the Contract | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**description** | **str** | Description | [optional] 
**draft_change_orders_amount** | **str** | Total of all draft change orders | [optional] 
**executed** | **bool** | Executed status | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**grand_total** | **str** | Grand total | [optional] 
**invoice_contacts** | [**List[RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner]**](RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.md) | Invoice Contacts | [optional] 
**issued_on_date** | **date** | Issued on | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**line_items** | [**List[RestV10WorkOrderContractsPost201ResponseLineItemsInner]**](RestV10WorkOrderContractsPost201ResponseLineItemsInner.md) | Line items | [optional] 
**number** | **str** | Number | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**payment_terms** | **str** | Payment terms | [optional] 
**payments_issued** | [**List[RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner]**](RestV10WorkOrderContractsPost201ResponsePaymentsIssuedInner.md) | Payments issued | [optional] 
**pending_change_orders** | **str** | Pending Change Orders amount | [optional] 
**pending_revised_contract** | **str** | Pending Revised Contract amount | [optional] 
**percentage_paid** | **str** | Percentage paid amount | [optional] 
**potential_change_orders** | **List[List[RestV10PurchaseOrderContractsPost201ResponsePotentialChangeOrdersInnerInner]]** | Potential Change Orders | [optional] 
**private** | **bool** | Enable/Disable Pivate status | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**remaining_balance_outstanding** | **str** | Remaining Balance Outstanding amount | [optional] 
**requisitions_are_enabled** | **bool** | If true, Requisitions (Subcontractor Invoices) are enabled on the Commitment Contract | [optional] 
**retainage_percent** | **str** | Retainage Percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**revised_contract** | **str** | Revised contracts amount | [optional] 
**ship_to_address** | **str** | Ship to address | [optional] 
**ship_via** | **str** | Ship via | [optional] 
**show_line_items_to_non_admins** | **bool** | If true and the contract is private, non admins with access to the contract will be able to view the SOV items | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**total_draw_requests_amount** | **str** | Total Draw Requests amount | [optional] 
**total_payments** | **str** | Total Payments amount | [optional] 
**total_requisitions_amount** | **str** | Total Requisitions (Subcontractor Invoices) amount | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV10WorkOrderContractsPost201ResponseVendor**](RestV10WorkOrderContractsPost201ResponseVendor.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_purchase_order_contracts_post201_response import RestV10PurchaseOrderContractsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10PurchaseOrderContractsPost201Response from a JSON string
rest_v10_purchase_order_contracts_post201_response_instance = RestV10PurchaseOrderContractsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10PurchaseOrderContractsPost201Response.to_json())

# convert the object into a dict
rest_v10_purchase_order_contracts_post201_response_dict = rest_v10_purchase_order_contracts_post201_response_instance.to_dict()
# create an instance of RestV10PurchaseOrderContractsPost201Response from a dict
rest_v10_purchase_order_contracts_post201_response_from_dict = RestV10PurchaseOrderContractsPost201Response.from_dict(rest_v10_purchase_order_contracts_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


