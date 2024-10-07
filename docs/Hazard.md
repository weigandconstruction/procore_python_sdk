# Hazard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Hazard ID | [optional] 
**name** | **str** | Hazard Name | [optional] 
**active** | **bool** | Represents whether a Hazard is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Hazard has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.hazard import Hazard

# TODO update the JSON string below
json = "{}"
# create an instance of Hazard from a JSON string
hazard_instance = Hazard.from_json(json)
# print the JSON string representation of the object
print(Hazard.to_json())

# convert the object into a dict
hazard_dict = hazard_instance.to_dict()
# create an instance of Hazard from a dict
hazard_from_dict = Hazard.from_dict(hazard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


