# RoundingConfigurationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rounding_configuration** | [**RoundingConfigurationBodyRoundingConfiguration**](RoundingConfigurationBodyRoundingConfiguration.md) |  | 

## Example

```python
from procore_sdk.models.rounding_configuration_body import RoundingConfigurationBody

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConfigurationBody from a JSON string
rounding_configuration_body_instance = RoundingConfigurationBody.from_json(json)
# print the JSON string representation of the object
print(RoundingConfigurationBody.to_json())

# convert the object into a dict
rounding_configuration_body_dict = rounding_configuration_body_instance.to_dict()
# create an instance of RoundingConfigurationBody from a dict
rounding_configuration_body_from_dict = RoundingConfigurationBody.from_dict(rounding_configuration_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


