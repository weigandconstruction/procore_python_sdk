# EnvironmentalType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Environmental Type ID | [optional] 
**name** | **str** | Environmental Type Name | [optional] 
**active** | **bool** | Represents whether a Environmental Type is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Environmental Type has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.environmental_type import EnvironmentalType

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentalType from a JSON string
environmental_type_instance = EnvironmentalType.from_json(json)
# print the JSON string representation of the object
print(EnvironmentalType.to_json())

# convert the object into a dict
environmental_type_dict = environmental_type_instance.to_dict()
# create an instance of EnvironmentalType from a dict
environmental_type_from_dict = EnvironmentalType.from_dict(environmental_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


