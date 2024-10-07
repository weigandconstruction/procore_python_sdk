# NormalViewBusinessRegister

business register

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** | business register type (ABN, EIN) | [optional] 
**identifier** | **str** | Identification code | [optional] 
**verified_at** | **datetime** | Verified at | [optional] 
**verification_status** | **str** | Verification status (active, cancelled, does_not_exist) | [optional] 

## Example

```python
from procore_sdk.models.normal_view_business_register import NormalViewBusinessRegister

# TODO update the JSON string below
json = "{}"
# create an instance of NormalViewBusinessRegister from a JSON string
normal_view_business_register_instance = NormalViewBusinessRegister.from_json(json)
# print the JSON string representation of the object
print(NormalViewBusinessRegister.to_json())

# convert the object into a dict
normal_view_business_register_dict = normal_view_business_register_instance.to_dict()
# create an instance of NormalViewBusinessRegister from a dict
normal_view_business_register_from_dict = NormalViewBusinessRegister.from_dict(normal_view_business_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


