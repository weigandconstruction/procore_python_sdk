# RoundingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rounding configuration ID | [optional] 
**company_id** | **int** | Company ID | [optional] 
**time_increment** | **int** | Time increment for rounding | [optional] 
**rule** | **str** | Rounding rule | [optional] 

## Example

```python
from procore_sdk.models.rounding_configuration import RoundingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConfiguration from a JSON string
rounding_configuration_instance = RoundingConfiguration.from_json(json)
# print the JSON string representation of the object
print(RoundingConfiguration.to_json())

# convert the object into a dict
rounding_configuration_dict = rounding_configuration_instance.to_dict()
# create an instance of RoundingConfiguration from a dict
rounding_configuration_from_dict = RoundingConfiguration.from_dict(rounding_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


