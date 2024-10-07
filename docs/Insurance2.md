# Insurance2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Insurance | [optional] 
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
**additional_insured** | **str** | Additional Individuals and/or Companies Insured | [optional] 
**division_template** | **str** | Division Template | [optional] 
**insurance_sets** | **str** | Insurance Sets | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.insurance2 import Insurance2

# TODO update the JSON string below
json = "{}"
# create an instance of Insurance2 from a JSON string
insurance2_instance = Insurance2.from_json(json)
# print the JSON string representation of the object
print(Insurance2.to_json())

# convert the object into a dict
insurance2_dict = insurance2_instance.to_dict()
# create an instance of Insurance2 from a dict
insurance2_from_dict = Insurance2.from_dict(insurance2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


