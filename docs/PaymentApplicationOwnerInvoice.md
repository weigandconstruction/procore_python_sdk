# PaymentApplicationOwnerInvoice

Payment Application (Owner Invoice)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_billing_period_id** | **int** | Billing Period ID | [optional] 
**period_start** | **date** | Period start date | [optional] 
**period_end** | **date** | Period end date | [optional] 
**billing_date** | **date** | Billing date | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**origin_data** | **str** | Payment Application (Owner Invoice) third party data | [optional] 
**origin_id** | **str** | Payment Application (Owner Invoice) third party ID | [optional] 
**status** | **str** | Status | [optional] 
**include_attachments** | **bool** | If true, all attachments from requisitions in the billing period will be attached to the payment application | [optional] 

## Example

```python
from procore_sdk.models.payment_application_owner_invoice import PaymentApplicationOwnerInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentApplicationOwnerInvoice from a JSON string
payment_application_owner_invoice_instance = PaymentApplicationOwnerInvoice.from_json(json)
# print the JSON string representation of the object
print(PaymentApplicationOwnerInvoice.to_json())

# convert the object into a dict
payment_application_owner_invoice_dict = payment_application_owner_invoice_instance.to_dict()
# create an instance of PaymentApplicationOwnerInvoice from a dict
payment_application_owner_invoice_from_dict = PaymentApplicationOwnerInvoice.from_dict(payment_application_owner_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


