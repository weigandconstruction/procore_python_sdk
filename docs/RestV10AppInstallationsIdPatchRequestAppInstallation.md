# RestV10AppInstallationsIdPatchRequestAppInstallation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current installation status | 
**installation_configuration** | **object** | Configuration values for installation. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_id_patch_request_app_installation import RestV10AppInstallationsIdPatchRequestAppInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsIdPatchRequestAppInstallation from a JSON string
rest_v10_app_installations_id_patch_request_app_installation_instance = RestV10AppInstallationsIdPatchRequestAppInstallation.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsIdPatchRequestAppInstallation.to_json())

# convert the object into a dict
rest_v10_app_installations_id_patch_request_app_installation_dict = rest_v10_app_installations_id_patch_request_app_installation_instance.to_dict()
# create an instance of RestV10AppInstallationsIdPatchRequestAppInstallation from a dict
rest_v10_app_installations_id_patch_request_app_installation_from_dict = RestV10AppInstallationsIdPatchRequestAppInstallation.from_dict(rest_v10_app_installations_id_patch_request_app_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


