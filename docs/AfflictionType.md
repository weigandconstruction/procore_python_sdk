# AfflictionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Affliction Type ID | [optional] 
**name** | **str** | Affliction Type Name | [optional] 
**active** | **bool** | Represents whether a Affliction Type is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Affliction Type has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.affliction_type import AfflictionType

# TODO update the JSON string below
json = "{}"
# create an instance of AfflictionType from a JSON string
affliction_type_instance = AfflictionType.from_json(json)
# print the JSON string representation of the object
print(AfflictionType.to_json())

# convert the object into a dict
affliction_type_dict = affliction_type_instance.to_dict()
# create an instance of AfflictionType from a dict
affliction_type_from_dict = AfflictionType.from_dict(affliction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


