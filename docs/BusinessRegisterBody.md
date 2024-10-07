# BusinessRegisterBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_register** | [**BusinessRegisterBodyBusinessRegister**](BusinessRegisterBodyBusinessRegister.md) |  | [optional] 

## Example

```python
from procore_sdk.models.business_register_body import BusinessRegisterBody

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessRegisterBody from a JSON string
business_register_body_instance = BusinessRegisterBody.from_json(json)
# print the JSON string representation of the object
print(BusinessRegisterBody.to_json())

# convert the object into a dict
business_register_body_dict = business_register_body_instance.to_dict()
# create an instance of BusinessRegisterBody from a dict
business_register_body_from_dict = BusinessRegisterBody.from_dict(business_register_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


