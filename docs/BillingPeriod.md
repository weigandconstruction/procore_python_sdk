# BillingPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Billing Period ID | [optional] 
**created_at** | **datetime** | Date/time the Billing Period was created | [optional] 
**due_date** | **date** | Due date for the Billing Period | [optional] 
**end_date** | **date** | End date for the Billing Period | [optional] 
**position** | **int** | Position of the Billing Period | [optional] 
**project_id** | **int** | Project ID for the Billing Period | [optional] 
**start_date** | **date** | Start date for the Billing Period | [optional] 
**status** | **str** | Billing Period status | [optional] 
**updated_at** | **datetime** | Date/time the Billing Period was last updated | [optional] 

## Example

```python
from procore_sdk.models.billing_period import BillingPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPeriod from a JSON string
billing_period_instance = BillingPeriod.from_json(json)
# print the JSON string representation of the object
print(BillingPeriod.to_json())

# convert the object into a dict
billing_period_dict = billing_period_instance.to_dict()
# create an instance of BillingPeriod from a dict
billing_period_from_dict = BillingPeriod.from_dict(billing_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


