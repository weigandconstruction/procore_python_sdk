# ObservationCategoryConfigurableFieldSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Observation Cateogry Configurable Field Set | 
**category** | **str** | Observation Cateogry Configurable Field Set category | 
**category_key** | **str** | Observation Type category (snake_case) | [optional] 
**configurable_field_set** | [**ConfigurableFieldSet1**](ConfigurableFieldSet1.md) |  | 

## Example

```python
from procore_sdk.models.observation_category_configurable_field_sets import ObservationCategoryConfigurableFieldSets

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCategoryConfigurableFieldSets from a JSON string
observation_category_configurable_field_sets_instance = ObservationCategoryConfigurableFieldSets.from_json(json)
# print the JSON string representation of the object
print(ObservationCategoryConfigurableFieldSets.to_json())

# convert the object into a dict
observation_category_configurable_field_sets_dict = observation_category_configurable_field_sets_instance.to_dict()
# create an instance of ObservationCategoryConfigurableFieldSets from a dict
observation_category_configurable_field_sets_from_dict = ObservationCategoryConfigurableFieldSets.from_dict(observation_category_configurable_field_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


