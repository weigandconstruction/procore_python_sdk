# CompanyManagedEquipmentUserPermission

Company Managed Equipment User Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company_directory_admin** | **bool** | User is a Company directory admin | [optional] 
**name** | **str** | Full name of user | [optional] 
**user_access_level** | [**CompanyManagedEquipmentUserPermissionUserAccessLevel**](CompanyManagedEquipmentUserPermissionUserAccessLevel.md) |  | [optional] 
**permission_template** | [**CompanyManagedEquipmentUserPermissionPermissionTemplate**](CompanyManagedEquipmentUserPermissionPermissionTemplate.md) |  | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.company_managed_equipment_user_permission import CompanyManagedEquipmentUserPermission

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyManagedEquipmentUserPermission from a JSON string
company_managed_equipment_user_permission_instance = CompanyManagedEquipmentUserPermission.from_json(json)
# print the JSON string representation of the object
print(CompanyManagedEquipmentUserPermission.to_json())

# convert the object into a dict
company_managed_equipment_user_permission_dict = company_managed_equipment_user_permission_instance.to_dict()
# create an instance of CompanyManagedEquipmentUserPermission from a dict
company_managed_equipment_user_permission_from_dict = CompanyManagedEquipmentUserPermission.from_dict(company_managed_equipment_user_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


