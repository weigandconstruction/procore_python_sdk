# Hazard1


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
from procore_sdk.models.hazard1 import Hazard1

# TODO update the JSON string below
json = "{}"
# create an instance of Hazard1 from a JSON string
hazard1_instance = Hazard1.from_json(json)
# print the JSON string representation of the object
print(Hazard1.to_json())

# convert the object into a dict
hazard1_dict = hazard1_instance.to_dict()
# create an instance of Hazard1 from a dict
hazard1_from_dict = Hazard1.from_dict(hazard1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


