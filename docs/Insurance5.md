# Insurance5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Insurance | [optional] 
**company_id** | **int** | Company ID | 
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
**vendor_id** | **int** | Vendor ID | [optional] 
**additional_insured** | **str** | Additional Individuals and/or Companies Insured | [optional] 
**division_template** | **str** | Division Template | [optional] 
**insurance_sets** | **str** | Insurance Sets | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.insurance5 import Insurance5

# TODO update the JSON string below
json = "{}"
# create an instance of Insurance5 from a JSON string
insurance5_instance = Insurance5.from_json(json)
# print the JSON string representation of the object
print(Insurance5.to_json())

# convert the object into a dict
insurance5_dict = insurance5_instance.to_dict()
# create an instance of Insurance5 from a dict
insurance5_from_dict = Insurance5.from_dict(insurance5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


