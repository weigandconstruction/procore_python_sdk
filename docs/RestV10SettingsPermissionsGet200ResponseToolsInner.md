# RestV10SettingsPermissionsGet200ResponseToolsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**domain_id** | **int** |  | [optional] 
**tab_group** | **str** |  | [optional] 
**available_for_user** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**user_access_level** | [**RestV10SettingsPermissionsGet200ResponseToolsInnerUserAccessLevel**](RestV10SettingsPermissionsGet200ResponseToolsInnerUserAccessLevel.md) |  | [optional] 
**permitted_actions** | [**List[RestV10SettingsPermissionsGet200ResponseToolsInnerPermittedActionsInner]**](RestV10SettingsPermissionsGet200ResponseToolsInnerPermittedActionsInner.md) |  | [optional] 
**create_url** | **str** |  | [optional] 
**can_create** | **bool** |  | [optional] 
**trial** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_settings_permissions_get200_response_tools_inner import RestV10SettingsPermissionsGet200ResponseToolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SettingsPermissionsGet200ResponseToolsInner from a JSON string
rest_v10_settings_permissions_get200_response_tools_inner_instance = RestV10SettingsPermissionsGet200ResponseToolsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SettingsPermissionsGet200ResponseToolsInner.to_json())

# convert the object into a dict
rest_v10_settings_permissions_get200_response_tools_inner_dict = rest_v10_settings_permissions_get200_response_tools_inner_instance.to_dict()
# create an instance of RestV10SettingsPermissionsGet200ResponseToolsInner from a dict
rest_v10_settings_permissions_get200_response_tools_inner_from_dict = RestV10SettingsPermissionsGet200ResponseToolsInner.from_dict(rest_v10_settings_permissions_get200_response_tools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


