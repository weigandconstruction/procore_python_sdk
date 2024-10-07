# Body136BimLevel

BIM Level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevation** | **float** | Level elevation | 
**bim_file_id** | **int** | ID of the BIM File linked to the Level | 
**location_id** | **int** | ID of location linked to the Level | 

## Example

```python
from procore_sdk.models.body136_bim_level import Body136BimLevel

# TODO update the JSON string below
json = "{}"
# create an instance of Body136BimLevel from a JSON string
body136_bim_level_instance = Body136BimLevel.from_json(json)
# print the JSON string representation of the object
print(Body136BimLevel.to_json())

# convert the object into a dict
body136_bim_level_dict = body136_bim_level_instance.to_dict()
# create an instance of Body136BimLevel from a dict
body136_bim_level_from_dict = Body136BimLevel.from_dict(body136_bim_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


