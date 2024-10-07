# BillingPeriod1

The Billing Period object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **date** | Due date | 
**start_date** | **date** | Start date | 
**end_date** | **date** | End date | 
**status** | **str** | Status | 

## Example

```python
from procore_sdk.models.billing_period1 import BillingPeriod1

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPeriod1 from a JSON string
billing_period1_instance = BillingPeriod1.from_json(json)
# print the JSON string representation of the object
print(BillingPeriod1.to_json())

# convert the object into a dict
billing_period1_dict = billing_period1_instance.to_dict()
# create an instance of BillingPeriod1 from a dict
billing_period1_from_dict = BillingPeriod1.from_dict(billing_period1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


