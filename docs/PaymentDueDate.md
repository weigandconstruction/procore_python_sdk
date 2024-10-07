# PaymentDueDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **str** | Payment Due Date for the Requisition (Subcontractor Invoice) | [optional] 

## Example

```python
from procore_sdk.models.payment_due_date import PaymentDueDate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDueDate from a JSON string
payment_due_date_instance = PaymentDueDate.from_json(json)
# print the JSON string representation of the object
print(PaymentDueDate.to_json())

# convert the object into a dict
payment_due_date_dict = payment_due_date_instance.to_dict()
# create an instance of PaymentDueDate from a dict
payment_due_date_from_dict = PaymentDueDate.from_dict(payment_due_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


