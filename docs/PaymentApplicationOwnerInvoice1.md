# PaymentApplicationOwnerInvoice1

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

## Example

```python
from procore_sdk.models.payment_application_owner_invoice1 import PaymentApplicationOwnerInvoice1

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentApplicationOwnerInvoice1 from a JSON string
payment_application_owner_invoice1_instance = PaymentApplicationOwnerInvoice1.from_json(json)
# print the JSON string representation of the object
print(PaymentApplicationOwnerInvoice1.to_json())

# convert the object into a dict
payment_application_owner_invoice1_dict = payment_application_owner_invoice1_instance.to_dict()
# create an instance of PaymentApplicationOwnerInvoice1 from a dict
payment_application_owner_invoice1_from_dict = PaymentApplicationOwnerInvoice1.from_dict(payment_application_owner_invoice1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


