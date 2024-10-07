# ObservationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Observation Type ID | 
**category** | **str** | Observation Type category | 
**category_key** | **str** | Observation Type category (snake_case) | [optional] 
**name** | **str** | Type name | 
**active** | **bool** | Flag denoting if the Observation Type is available for use | [optional] 
**company_active** | **bool** | Flag denoting if the Company is available for use | [optional] 
**parent_inactive** | **bool** | Flag denoting if the Parent is available for use | [optional] 
**in_use** | **bool** | Flag denoting if the in use is available for use | [optional] 
**kind** | **str** | kind | [optional] 
**name_translations** | [**ObservationTypeNameTranslations**](ObservationTypeNameTranslations.md) |  | [optional] 
**localized_name** | **str** | returns the localized observation_type name. It&#39;ll return custom traslations depending on the param sent in. | [optional] 

## Example

```python
from procore_sdk.models.observation_type import ObservationType

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationType from a JSON string
observation_type_instance = ObservationType.from_json(json)
# print the JSON string representation of the object
print(ObservationType.to_json())

# convert the object into a dict
observation_type_dict = observation_type_instance.to_dict()
# create an instance of ObservationType from a dict
observation_type_from_dict = ObservationType.from_dict(observation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


