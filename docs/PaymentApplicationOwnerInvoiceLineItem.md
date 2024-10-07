# PaymentApplicationOwnerInvoiceLineItem

Payment Application (Owner Invoice) Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_completed_this_period** | **str** | The amount of work completed this period (only for lines that use amount accounting or are calculated manually) | [optional] 
**materials_presently_stored** | **str** | The amount of materials presently stored (only for lines that use amount accounting) | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period (work_completed_this_period should be non-zero to hold a retainage) | [optional] 
**materials_stored_retainage_retained_this_period** | **str** | Materials stored retainage amount retained this period (materials_presently_stored should be non-zero to hold a retainage) | [optional] 
**work_completed_retainage_released_this_period** | **str** | The amount of work completed retainage released this period | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity (only for lines that use unit accounting and are not calculated manually) | [optional] 

## Example

```python
from procore_sdk.models.payment_application_owner_invoice_line_item import PaymentApplicationOwnerInvoiceLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentApplicationOwnerInvoiceLineItem from a JSON string
payment_application_owner_invoice_line_item_instance = PaymentApplicationOwnerInvoiceLineItem.from_json(json)
# print the JSON string representation of the object
print(PaymentApplicationOwnerInvoiceLineItem.to_json())

# convert the object into a dict
payment_application_owner_invoice_line_item_dict = payment_application_owner_invoice_line_item_instance.to_dict()
# create an instance of PaymentApplicationOwnerInvoiceLineItem from a dict
payment_application_owner_invoice_line_item_from_dict = PaymentApplicationOwnerInvoiceLineItem.from_dict(payment_application_owner_invoice_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


