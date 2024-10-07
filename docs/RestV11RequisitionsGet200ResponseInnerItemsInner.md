# RestV11RequisitionsGet200ResponseInnerItemsInner

Requisition (Subcontractor Invoice) item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Contract Item or Contract Detail Item or Change Order Item or Whole Change Order Item | [optional] 
**item_type** | **str** | Item Type - (contract_item, contract_detail_item, change_order_item, whole_change_order_item) | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**currency_configuration** | [**RestV11RequisitionsGet200ResponseInnerCurrencyConfiguration**](RestV11RequisitionsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**line_item_id** | **int** | Line Item ID | [optional] 
**description_of_work** | **str** |  | [optional] 
**net_amount** | **str** | Net amount of line item | [optional] 
**gross_amount** | **str** | Gross amount of line item | [optional] 
**wbs_code** | [**RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode**](RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode.md) |  | [optional] 
**scheduled_value** | **str** | Scheduled value amount | [optional] 
**work_completed_from_previous_application** | **str** | Work completed from previous application amount | [optional] 
**work_completed_this_period** | **str** | Work completed this period amount | [optional] 
**materials_presently_stored** | **str** | Amount of materials presently stored | [optional] 
**materials_presently_stored_quantity** | **str** | Quantity of the Materials presently stored, only for unit based line items | [optional] 
**materials_presently_stored_from_previous_progress** | **str** | Materials presently stored from previous progress | [optional] 
**materials_previously_stored_quantity** | **str** | Quantity of the Materials stored from the previous invoice, only for unit based line items | [optional] 
**materials_moved** | **str** | Materials automatically moved from previous line item into previous work completed. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application. | [optional] 
**materials_retainage_retained_moved** | **str** | Retainage on materials automatically moved from previous line item into work completed retainage amount accrued previously. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application. | [optional] 
**total_completed_and_stored_to_date** | **str** | Total completed and stored to date amount | [optional] 
**total_completed_and_stored_to_date_percent** | **str** | Total completed and stored to date percent | [optional] 
**total_completed_and_stored_to_date_from_previous** | **str** | Total completed and stored to date from previous | [optional] 
**work_completed_retainage_from_previous_application** | **str** | Work completed retainage amount from previous application | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period | [optional] 
**work_completed_retainage_percent_this_period** | **str** | Work completed retainage percent this period | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained | [optional] 
**materials_stored_retainage_percent_this_period** | **str** | Materials stored retainage percent this period, present | [optional] 
**materials_stored_retainage_new_materials** | **str** | Materials stored retainage from new materials, present | [optional] 
**work_completed_retainage_released_this_period** | **str** | Work completed retainage amount released this period | [optional] 
**materials_stored_retainage_released_this_period** | **str** | Materials stored retainage amount released this period | [optional] 
**scheduled_quantity** | **str** | Scheduled quantity | [optional] 
**scheduled_unit_price** | **str** | Scheduled unit price | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity | [optional] 
**work_completed_from_previous_application_quantity** | **str** | Work completed from previous application quantity | [optional] 
**comment** | **str** | Comment | [optional] 
**status** | **str** | Status | [optional] 
**position** | **int** | Position of this item | [optional] 
**line_number** | **str** | Line Number for the item | [optional] 
**ssr_manual_override** | **bool** | SSR Manual Override | [optional] 
**subcontractor_claimed_amount** | **str** | Amount claimed by the subcontractor | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_items_inner import RestV11RequisitionsGet200ResponseInnerItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInner from a JSON string
rest_v11_requisitions_get200_response_inner_items_inner_instance = RestV11RequisitionsGet200ResponseInnerItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemsInner.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_items_inner_dict = rest_v11_requisitions_get200_response_inner_items_inner_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInner from a dict
rest_v11_requisitions_get200_response_inner_items_inner_from_dict = RestV11RequisitionsGet200ResponseInnerItemsInner.from_dict(rest_v11_requisitions_get200_response_inner_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


