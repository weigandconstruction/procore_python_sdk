# RequisitionBulkItemUpdateInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the item to update | [optional] 
**item_type** | **str** | The type of the item your are updating | [optional] 
**work_completed_this_period** | **str** | The amount of work completed this period | [optional] 
**materials_presently_stored** | **str** | The amount of materials presently stored | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period (admin user only, work_completed_this_period should be non-zero to hold a retainage) | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained (admin user, amount accounting only, materials_presently_stored should be non-zero to hold a retainage) | [optional] 
**work_completed_retainage_released_this_period** | **str** | The amount of work completed retainage released this period | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity (unit accounting contract only) | [optional] 
**subcontractor_claimed_amount** | **str** | The total amount the subcontractor original claimed for this line | [optional] 
**status** | **str** | Approval status of the invoice line item | [optional] 
**comment** | **str** | Comment about the invoice line item | [optional] 

## Example

```python
from procore_sdk.models.requisition_bulk_item_update_inner import RequisitionBulkItemUpdateInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequisitionBulkItemUpdateInner from a JSON string
requisition_bulk_item_update_inner_instance = RequisitionBulkItemUpdateInner.from_json(json)
# print the JSON string representation of the object
print(RequisitionBulkItemUpdateInner.to_json())

# convert the object into a dict
requisition_bulk_item_update_inner_dict = requisition_bulk_item_update_inner_instance.to_dict()
# create an instance of RequisitionBulkItemUpdateInner from a dict
requisition_bulk_item_update_inner_from_dict = RequisitionBulkItemUpdateInner.from_dict(requisition_bulk_item_update_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


