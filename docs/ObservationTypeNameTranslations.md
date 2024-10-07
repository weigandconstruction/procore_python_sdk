# ObservationTypeNameTranslations

Company's custom translations for observation type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**en** | **str** | Company default value for commissioning observation type assuming company locale to be en | [optional] 
**es** | **str** | Company custom translation for commissioning observation type | [optional] 
**fr_ca** | **str** | Company custom translation for commissioning observation type | [optional] 
**en_au** | **str** | Company custom translation for commissioning observation type | [optional] 

## Example

```python
from procore_sdk.models.observation_type_name_translations import ObservationTypeNameTranslations

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationTypeNameTranslations from a JSON string
observation_type_name_translations_instance = ObservationTypeNameTranslations.from_json(json)
# print the JSON string representation of the object
print(ObservationTypeNameTranslations.to_json())

# convert the object into a dict
observation_type_name_translations_dict = observation_type_name_translations_instance.to_dict()
# create an instance of ObservationTypeNameTranslations from a dict
observation_type_name_translations_from_dict = ObservationTypeNameTranslations.from_dict(observation_type_name_translations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


