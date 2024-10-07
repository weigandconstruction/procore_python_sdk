# RoundingConfigurationBodyRoundingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_increment** | **int** | Time increment available for Timecard Entries. Options are 5, 6, 10, and 15 | [optional] 
**rule** | **str** | Rule to apply to rounding. Options are &#39;up&#39;, &#39;down&#39;, &#39;nearest&#39;, and &#39;favor_employee&#39; | [optional] 

## Example

```python
from procore_sdk.models.rounding_configuration_body_rounding_configuration import RoundingConfigurationBodyRoundingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConfigurationBodyRoundingConfiguration from a JSON string
rounding_configuration_body_rounding_configuration_instance = RoundingConfigurationBodyRoundingConfiguration.from_json(json)
# print the JSON string representation of the object
print(RoundingConfigurationBodyRoundingConfiguration.to_json())

# convert the object into a dict
rounding_configuration_body_rounding_configuration_dict = rounding_configuration_body_rounding_configuration_instance.to_dict()
# create an instance of RoundingConfigurationBodyRoundingConfiguration from a dict
rounding_configuration_body_rounding_configuration_from_dict = RoundingConfigurationBodyRoundingConfiguration.from_dict(rounding_configuration_body_rounding_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


