# ManagedEquipmentDependentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependent_import_params** | [**DependentImportParams**](DependentImportParams.md) |  | 

## Example

```python
from procore_sdk.models.managed_equipment_dependent_body import ManagedEquipmentDependentBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentDependentBody from a JSON string
managed_equipment_dependent_body_instance = ManagedEquipmentDependentBody.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentDependentBody.to_json())

# convert the object into a dict
managed_equipment_dependent_body_dict = managed_equipment_dependent_body_instance.to_dict()
# create an instance of ManagedEquipmentDependentBody from a dict
managed_equipment_dependent_body_from_dict = ManagedEquipmentDependentBody.from_dict(managed_equipment_dependent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


