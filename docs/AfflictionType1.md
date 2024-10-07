# AfflictionType1


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
from procore_sdk.models.affliction_type1 import AfflictionType1

# TODO update the JSON string below
json = "{}"
# create an instance of AfflictionType1 from a JSON string
affliction_type1_instance = AfflictionType1.from_json(json)
# print the JSON string representation of the object
print(AfflictionType1.to_json())

# convert the object into a dict
affliction_type1_dict = affliction_type1_instance.to_dict()
# create an instance of AfflictionType1 from a dict
affliction_type1_from_dict = AfflictionType1.from_dict(affliction_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


