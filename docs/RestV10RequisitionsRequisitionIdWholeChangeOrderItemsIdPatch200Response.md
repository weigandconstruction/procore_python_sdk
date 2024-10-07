# RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response

Requisition (Subcontractor Invoice) Whole Change Order Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Whole Change Order Item | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**item_type** | **str** | Item type | [optional] 
**line_item_id** | **int** | Line Item ID | [optional] 
**description_of_work** | **str** | Description of work | [optional] 
**scheduled_value** | **str** | Scheduled value amount | [optional] 
**work_completed_from_previous_application** | **str** | Work completed from previous application amount | [optional] 
**work_completed_this_period** | **str** | Work completed this period amount | [optional] 
**materials_presently_stored** | **str** | Materials presently stored amount | [optional] 
**total_completed_and_stored_to_date** | **str** | Total completed and stored to date amount | [optional] 
**total_completed_and_stored_to_date_percent** | **str** | Total completed and stored to date percent | [optional] 
**work_completed_retainage_from_previous_application** | **str** | Work completed retainage amount from previous application | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period | [optional] 
**work_completed_retainage_percent_this_period** | **str** | Work completed retainage percent this period | [optional] 
**ssr_manual_override** | **bool** | SSR manual override | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained | [optional] 
**materials_stored_retainage_percent_this_period** | **str** | Materials stored retainage percent this period | [optional] 
**work_completed_retainage_released_this_period** | **str** | Work completed retainage amount released this period | [optional] 
**materials_stored_retainage_released_this_period** | **str** | Materials stored retainage amount released this period | [optional] 
**scheduled_quantity** | **str** | Scheduled quantity | [optional] 
**scheduled_unit_price** | **str** | Scheduled unit price | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity | [optional] 
**work_completed_from_previous_application_quantity** | **str** | Work completed from previous application quantity | [optional] 
**change_order_package_id** | **int** | ID for Change Order Package | [optional] 
**subcontractor_claimed_amount** | **str** | Amount claimed by the subcontractor | [optional] 
**comment** | **str** | Comment for the Whole Change Order Item | [optional] 
**status** | **str** | Status of the Whole Change Order Item | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**position** | **int** | Position | [optional] 
**currency_configuration** | [**RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInnerCurrencyConfiguration**](RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**materials_moved** | **str** | Materials automatically moved from previous line item into previous work completed. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application. | [optional] 
**materials_retainage_retained_moved** | **str** | Retainage on materials automatically moved from previous line item into work completed retainage amount accrued previously. This will be non-zero only if move_materials_to_previous_work_completed is true on the payment application. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response import RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response from a JSON string
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response_instance = RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response.to_json())

# convert the object into a dict
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response_dict = rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response_instance.to_dict()
# create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response from a dict
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response_from_dict = RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response.from_dict(rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


