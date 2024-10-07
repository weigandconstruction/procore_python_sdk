# RestV10AppInstallationsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest** | **object** | Manifest Content | [optional] 
**post_installation_instruction** | **object** | Post Installation Instructions For App | [optional] 
**id** | **int** | ID | [optional] 
**app_uid** | **str** | App UID | [optional] 
**app_version_id** | **str** | App Version Id | [optional] 
**status** | **str** | Installation status | [optional] 
**installed_by** | **str** | Email Address of the user who installed the app | [optional] 
**installed_at** | **datetime** | Date the app was installed or reinstalled | [optional] 
**uninstalled_at** | **datetime** | Date the app was uninstalled | [optional] 
**uninstalled_by** | **str** | Email Address of the user who uninstalled the app | [optional] 
**manifest_url** | **str** | Presigned Temporary Url For Manifest Instance | [optional] 
**developer_app** | **object** | Information on associated developer app from dev-portal | [optional] 
**components** | **List[str]** | Component types associated with the installation | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_post201_response import RestV10AppInstallationsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsPost201Response from a JSON string
rest_v10_app_installations_post201_response_instance = RestV10AppInstallationsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsPost201Response.to_json())

# convert the object into a dict
rest_v10_app_installations_post201_response_dict = rest_v10_app_installations_post201_response_instance.to_dict()
# create an instance of RestV10AppInstallationsPost201Response from a dict
rest_v10_app_installations_post201_response_from_dict = RestV10AppInstallationsPost201Response.from_dict(rest_v10_app_installations_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


