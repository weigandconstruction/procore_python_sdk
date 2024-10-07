# BIMLevel

BIM Level Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevation** | **float** | Level elevation | [optional] 
**location_id** | **int** | ID of location linked to the Level | [optional] 

## Example

```python
from procore_sdk.models.bim_level import BIMLevel

# TODO update the JSON string below
json = "{}"
# create an instance of BIMLevel from a JSON string
bim_level_instance = BIMLevel.from_json(json)
# print the JSON string representation of the object
print(BIMLevel.to_json())

# convert the object into a dict
bim_level_dict = bim_level_instance.to_dict()
# create an instance of BIMLevel from a dict
bim_level_from_dict = BIMLevel.from_dict(bim_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


