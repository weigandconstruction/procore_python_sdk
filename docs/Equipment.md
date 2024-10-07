# Equipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Equipment ID | [optional] 
**name** | **str** | Equipment name | [optional] 

## Example

```python
from procore_sdk.models.equipment import Equipment

# TODO update the JSON string below
json = "{}"
# create an instance of Equipment from a JSON string
equipment_instance = Equipment.from_json(json)
# print the JSON string representation of the object
print(Equipment.to_json())

# convert the object into a dict
equipment_dict = equipment_instance.to_dict()
# create an instance of Equipment from a dict
equipment_from_dict = Equipment.from_dict(equipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


