# Commitment1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Commitment ID | [optional] 
**title** | **str** | Title | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | Status | [optional] 
**description** | **str** | Description of the Prime Contract | [optional] 
**executed** | **bool** | Executed status | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**vendor** | [**RestV10PrimeContractsGet200ResponseInnerContractor**](RestV10PrimeContractsGet200ResponseInnerContractor.md) |  | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**allow_comments** | **bool** | Allow comments status | [optional] 
**allow_markups** | **bool** | Allow markups status | [optional] 
**allow_payment_applications** | **bool** | Enable/Disable Payment Applications (Owner Invoices) | [optional] 
**allow_payments** | **bool** | Enable/Disable payments | [optional] 
**allow_redistributions** | **bool** | Deprecated - always false | [optional] 
**approved_change_orders** | **str** | Approved change orders amount | [optional] 
**bill_to** | **str** | Bill to address | [optional] 
**budget_line_item_id** | **int** | Budget line item ID | [optional] 
**contract_estimated_completion_date** | **date** | Contract estimated completion date | [optional] 
**contract_start_date** | **date** | Contract start date | [optional] 
**contract_termination_date** | **date** | Contract termination date | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**display_materials_retainage** | **bool** | Display materials retainage status | [optional] 
**display_stored_materials** | **bool** | Enable/Disable stored materials | [optional] 
**display_work_retainage** | **bool** | Display work retainage | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**grand_total** | **str** | Total of Line items including markup, plus project level (vertical) markup, if any | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**line_items_extended_total** | **str** | Total of Line items including markup | [optional] 
**line_items_total** | **str** | Total of Line items without markup | [optional] 
**payment_terms** | **str** | Payment terms | [optional] 
**pending_change_orders** | **str** | Total of all pending and revised change orders | [optional] 
**pending_revised_contract** | **str** | Revised contract amount, plus pending and revised change orders | [optional] 
**percentage_paid** | **str** | Percentage paid | [optional] 
**position** | **int** | Position | [optional] 
**remaining_balance_outstanding** | **str** | Revised contract amount minus total payments | [optional] 
**requisition_number** | **str** | Requisition (Subcontractor Invoice) number | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**revised_contract** | **str** | Grand total, plus approved change orders | [optional] 
**ship_to** | **str** | Ship to address | [optional] 
**ship_via** | **str** | Ship via | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**total_payments** | **str** | Total payments | [optional] 
**total_draw_requests_amount** | **str** | Total draw requests amount | [optional] 
**type** | **str** | Type | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**architect** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**assigned_to** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**change_order_packages** | [**List[RFQChangeOrderPackages]**](RFQChangeOrderPackages.md) | Change order packages | [optional] 
**change_order_requests** | **List[List[Commitment1ChangeOrderRequestsInnerInner]]** | Change order requests (tiers &gt; 2) | [optional] 
**contractor** | [**RestV10PrimeContractsGet200ResponseInnerContractor**](RestV10PrimeContractsGet200ResponseInnerContractor.md) |  | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**line_items** | [**List[Commitment1LineItemsInner]**](Commitment1LineItemsInner.md) | Line items | [optional] 
**potential_change_orders** | [**List[Commitment1PotentialChangeOrdersInner]**](Commitment1PotentialChangeOrdersInner.md) | Potential change orders (tiers &gt; 1) | [optional] 
**payments_issued** | [**List[Commitment1PaymentsIssuedInner]**](Commitment1PaymentsIssuedInner.md) | Payments issued | [optional] 
**received_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.commitment1 import Commitment1

# TODO update the JSON string below
json = "{}"
# create an instance of Commitment1 from a JSON string
commitment1_instance = Commitment1.from_json(json)
# print the JSON string representation of the object
print(Commitment1.to_json())

# convert the object into a dict
commitment1_dict = commitment1_instance.to_dict()
# create an instance of Commitment1 from a dict
commitment1_from_dict = Commitment1.from_dict(commitment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


