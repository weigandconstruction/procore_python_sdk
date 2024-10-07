# HarmSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Harm Source ID | [optional] 
**name** | **str** | Harm Source Name | [optional] 
**active** | **bool** | Represents whether a Harm Source is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Harm Source has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.harm_source import HarmSource

# TODO update the JSON string below
json = "{}"
# create an instance of HarmSource from a JSON string
harm_source_instance = HarmSource.from_json(json)
# print the JSON string representation of the object
print(HarmSource.to_json())

# convert the object into a dict
harm_source_dict = harm_source_instance.to_dict()
# create an instance of HarmSource from a dict
harm_source_from_dict = HarmSource.from_dict(harm_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


