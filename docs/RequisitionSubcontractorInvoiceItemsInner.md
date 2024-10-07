# RequisitionSubcontractorInvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **int** | The line item id of a contract line item | [optional] 
**detail_line_item_id** | **int** | Contract Detail Item ID | [optional] 
**item_type** | **str** | The type of the item your are updating. Required if you are updating a line item. | 
**work_completed_this_period** | **str** | The amount of work completed this period | [optional] 
**materials_presently_stored** | **str** | The amount of materials presently stored | [optional] 
**materials_presently_stored_from_previous_progress** | **str** | The amount of materials presently stored from the previous progress | [optional] 
**new_materials** | **str** | New materials amount | [optional] 
**stored_materials** | **str** | Currently stored materials amount | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period (admin user only, work_completed_this_period should be non-zero to hold a retainage) | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained (Admin user, amount accounting only, materials_presently_stored should be non-zero to hold a retainage. Ignored unless \&quot;Materials presently stored\&quot; is manually managed in your configuration.) | [optional] 
**work_completed_retainage_released_this_period** | **str** | The amount of work completed retainage released this period | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity (unit accounting contract only) | [optional] 
**work_completed_retainage_percent_this_period** | **str** | Work completed percentage for this period (this field is only persisted if work_completed_this_period is zero or nil) | [optional] 
**materials_stored_retainage_percent_this_period** | **str** | Materials retainage percentage for this period (This field is only persisted if materials_presently_stored is zero or nil. Ignored unless \&quot;Materials presently stored\&quot; is manually managed in your configuration.) | [optional] 
**subcontractor_claimed_amount** | **str** | The total amount the subcontractor original claimed for this line | [optional] 
**status** | **str** | Approval status of the invoice line item | [optional] 
**comment** | **str** | Comment about the invoice line item | [optional] 

## Example

```python
from procore_sdk.models.requisition_subcontractor_invoice_items_inner import RequisitionSubcontractorInvoiceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequisitionSubcontractorInvoiceItemsInner from a JSON string
requisition_subcontractor_invoice_items_inner_instance = RequisitionSubcontractorInvoiceItemsInner.from_json(json)
# print the JSON string representation of the object
print(RequisitionSubcontractorInvoiceItemsInner.to_json())

# convert the object into a dict
requisition_subcontractor_invoice_items_inner_dict = requisition_subcontractor_invoice_items_inner_instance.to_dict()
# create an instance of RequisitionSubcontractorInvoiceItemsInner from a dict
requisition_subcontractor_invoice_items_inner_from_dict = RequisitionSubcontractorInvoiceItemsInner.from_dict(requisition_subcontractor_invoice_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


