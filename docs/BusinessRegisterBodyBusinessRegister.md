# BusinessRegisterBodyBusinessRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entity Type | 
**identifier** | **str** | Entity ID. This field ignores spaces and dashes. | 

## Example

```python
from procore_sdk.models.business_register_body_business_register import BusinessRegisterBodyBusinessRegister

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessRegisterBodyBusinessRegister from a JSON string
business_register_body_business_register_instance = BusinessRegisterBodyBusinessRegister.from_json(json)
# print the JSON string representation of the object
print(BusinessRegisterBodyBusinessRegister.to_json())

# convert the object into a dict
business_register_body_business_register_dict = business_register_body_business_register_instance.to_dict()
# create an instance of BusinessRegisterBodyBusinessRegister from a dict
business_register_body_business_register_from_dict = BusinessRegisterBodyBusinessRegister.from_dict(business_register_body_business_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


