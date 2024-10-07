# ManagedEquipmentPermissionUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**user_access_level_id** | **int** | User Access Level ID - &#39;1&#39; for None, &#39;2&#39; for Read-Only, &#39;3&#39; for Standard, &#39;4&#39; for Admin | [optional] 

## Example

```python
from procore_sdk.models.managed_equipment_permission_update_body import ManagedEquipmentPermissionUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedEquipmentPermissionUpdateBody from a JSON string
managed_equipment_permission_update_body_instance = ManagedEquipmentPermissionUpdateBody.from_json(json)
# print the JSON string representation of the object
print(ManagedEquipmentPermissionUpdateBody.to_json())

# convert the object into a dict
managed_equipment_permission_update_body_dict = managed_equipment_permission_update_body_instance.to_dict()
# create an instance of ManagedEquipmentPermissionUpdateBody from a dict
managed_equipment_permission_update_body_from_dict = ManagedEquipmentPermissionUpdateBody.from_dict(managed_equipment_permission_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


