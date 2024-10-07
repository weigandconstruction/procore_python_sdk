# RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem

Requisition (Subcontractor Invoice) Whole Change Order Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_completed_this_period** | **str** | The amount of work completed this period | [optional] 
**materials_presently_stored** | **str** | The amount of materials presently stored | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained | [optional] 
**work_completed_retainage_released_this_period** | **str** | The amount of work completed retainage released this period | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity | [optional] 
**ssr_manual_override** | **bool** | SSR manual override | [optional] 
**comment** | **str** | Comment for the Whole Change Order Item | [optional] 
**status** | **str** | Status of the Whole Change Order Item | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item import RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem from a JSON string
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item_instance = RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem.from_json(json)
# print the JSON string representation of the object
print(RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem.to_json())

# convert the object into a dict
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item_dict = rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item_instance.to_dict()
# create an instance of RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem from a dict
rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item_from_dict = RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequestRequisitionWholeChangeOrderItem.from_dict(rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request_requisition_whole_change_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


