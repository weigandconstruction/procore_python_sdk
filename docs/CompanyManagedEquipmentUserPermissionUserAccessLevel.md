# CompanyManagedEquipmentUserPermissionUserAccessLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | access level | [optional] 
**name** | **str** | friendly name for level | [optional] 

## Example

```python
from procore_sdk.models.company_managed_equipment_user_permission_user_access_level import CompanyManagedEquipmentUserPermissionUserAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyManagedEquipmentUserPermissionUserAccessLevel from a JSON string
company_managed_equipment_user_permission_user_access_level_instance = CompanyManagedEquipmentUserPermissionUserAccessLevel.from_json(json)
# print the JSON string representation of the object
print(CompanyManagedEquipmentUserPermissionUserAccessLevel.to_json())

# convert the object into a dict
company_managed_equipment_user_permission_user_access_level_dict = company_managed_equipment_user_permission_user_access_level_instance.to_dict()
# create an instance of CompanyManagedEquipmentUserPermissionUserAccessLevel from a dict
company_managed_equipment_user_permission_user_access_level_from_dict = CompanyManagedEquipmentUserPermissionUserAccessLevel.from_dict(company_managed_equipment_user_permission_user_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


