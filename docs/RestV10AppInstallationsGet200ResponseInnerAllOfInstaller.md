# RestV10AppInstallationsGet200ResponseInnerAllOfInstaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the user. | [optional] 
**login** | **str** | The email address of the user that is used to log in. | [optional] 
**name** | **str** | The name of the user. | [optional] 
**is_active** | **bool** | User&#39;s contact is active in company | [optional] 
**contact_id** | **int** | User&#39;s contact id in company | [optional] 
**company_name** | **str** | Vendor name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_get200_response_inner_all_of_installer import RestV10AppInstallationsGet200ResponseInnerAllOfInstaller

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfInstaller from a JSON string
rest_v10_app_installations_get200_response_inner_all_of_installer_instance = RestV10AppInstallationsGet200ResponseInnerAllOfInstaller.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsGet200ResponseInnerAllOfInstaller.to_json())

# convert the object into a dict
rest_v10_app_installations_get200_response_inner_all_of_installer_dict = rest_v10_app_installations_get200_response_inner_all_of_installer_instance.to_dict()
# create an instance of RestV10AppInstallationsGet200ResponseInnerAllOfInstaller from a dict
rest_v10_app_installations_get200_response_inner_all_of_installer_from_dict = RestV10AppInstallationsGet200ResponseInnerAllOfInstaller.from_dict(rest_v10_app_installations_get200_response_inner_all_of_installer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


