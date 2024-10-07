# RestV10AppInstallationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**app_uid** | **str** | App UID | [optional] 
**components** | **List[str]** | Component types associated with the installation | [optional] 
**developer_app** | [**RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp.md) |  | [optional] 
**installed_at** | **datetime** | Date the app was installed or reinstalled | [optional] 
**installer** | [**RestV10AppInstallationsGet200ResponseInnerAllOfInstaller**](RestV10AppInstallationsGet200ResponseInnerAllOfInstaller.md) |  | [optional] 
**semantic_version** | **str** | Semantic version of the app | [optional] 
**status** | **str** | Installation status | [optional] 
**uninstalled_at** | **datetime** | Date the app was uninstalled | [optional] 
**uninstaller** | [**RestV10AppInstallationsGet200ResponseInnerAllOfInstaller**](RestV10AppInstallationsGet200ResponseInnerAllOfInstaller.md) |  | [optional] 
**updatable_app_version_id** | **str** | ID of the app version that can be updated to | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_get200_response_inner import RestV10AppInstallationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsGet200ResponseInner from a JSON string
rest_v10_app_installations_get200_response_inner_instance = RestV10AppInstallationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_app_installations_get200_response_inner_dict = rest_v10_app_installations_get200_response_inner_instance.to_dict()
# create an instance of RestV10AppInstallationsGet200ResponseInner from a dict
rest_v10_app_installations_get200_response_inner_from_dict = RestV10AppInstallationsGet200ResponseInner.from_dict(rest_v10_app_installations_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


