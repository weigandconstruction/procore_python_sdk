# RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**app_type** | **str** | App Type | [optional] 
**connectable** | **bool** | Connectable | [optional] 
**description** | **str** | User provided description of developer app | [optional] 
**internal** | **bool** | Is the developer app internal | [optional] 
**internal_name** | **str** | Internal name of developer app | [optional] 
**marketplace_app** | [**RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp**](RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp.md) |  | [optional] 
**marketplace_app_url** | **str** | URL to the marketplace app | [optional] 
**name** | **str** | User name of developer app | [optional] 
**published_app_version_id** | **str** | ID of the published app version | [optional] 
**thumbnail_url** | **str** | URL to the thumbnail image | [optional] 
**uid** | **str** | UID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_get200_response_inner_all_of_developer_app import RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp from a JSON string
rest_v10_app_installations_get200_response_inner_all_of_developer_app_instance = RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp.to_json())

# convert the object into a dict
rest_v10_app_installations_get200_response_inner_all_of_developer_app_dict = rest_v10_app_installations_get200_response_inner_all_of_developer_app_instance.to_dict()
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp from a dict
rest_v10_app_installations_get200_response_inner_all_of_developer_app_from_dict = RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperApp.from_dict(rest_v10_app_installations_get200_response_inner_all_of_developer_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


