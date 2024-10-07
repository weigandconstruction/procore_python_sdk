# ManagedEquipmentChangeHistory

Equipment Change History

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | Column Name | [optional] 
**created_at** | **str** | Created At | [optional] 
**created_by** | **str** | Created By | [optional] 
**new_value** | **str** | Created By | [optional] 
**old_value** | **str** | Created By | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_change_history import ManagedEquipmentChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentChangeHistory from a JSON string
managed_equipment_change_history_instance = ManagedEquipmentChangeHistory.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentChangeHistory.to_json())

# convert the object into a dict
managed_equipment_change_history_dict = managed_equipment_change_history_instance.to_dict()
# create an instance of ManagedEquipmentChangeHistory from a dict
managed_equipment_change_history_from_dict = ManagedEquipmentChangeHistory.from_dict(managed_equipment_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


