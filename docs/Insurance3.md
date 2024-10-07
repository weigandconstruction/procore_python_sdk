# Insurance3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **date** | Effective date | [optional] 
**enable_expired_insurance_notifications** | **bool** | Enable/Disable expired insurance notifications | [optional] [default to True]
**exempt** | **bool** | Exempt status | [optional] 
**expiration_date** | **date** | Expiration date | [optional] 
**info_received** | **bool** | Information received (or not) | [optional] 
**insurance_type** | **str** | Insurance type | [optional] 
**limit** | **str** | Limit | [optional] 
**name** | **str** | Provider name | [optional] 
**notes** | **str** | Notes | [optional] 
**policy_number** | **str** | Policy number | [optional] 
**status** | **str** | Status | [optional] 
**vendor_id** | **int** | Vendor ID | 
**additional_insured** | **str** | Additional Individuals and/or Companies Insured | [optional] 
**division_template** | **str** | Division Template | [optional] 
**insurance_sets** | **str** | Insurance Sets | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.insurance3 import Insurance3

# TODO update the JSON string below
json = "{}"
# create an instance of Insurance3 from a JSON string
insurance3_instance = Insurance3.from_json(json)
# print the JSON string representation of the object
print(Insurance3.to_json())

# convert the object into a dict
insurance3_dict = insurance3_instance.to_dict()
# create an instance of Insurance3 from a dict
insurance3_from_dict = Insurance3.from_dict(insurance3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


