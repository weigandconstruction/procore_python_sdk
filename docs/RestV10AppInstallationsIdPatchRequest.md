# RestV10AppInstallationsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uid** | **str** | Third party application UID | 
**project_id** | **int** | Project ID. Note: Only one of project_id or company_id is required. | 
**company_id** | **int** | Company ID. Note: Only one of project_id or company_id is required. | 
**app_installation** | [**RestV10AppInstallationsIdPatchRequestAppInstallation**](RestV10AppInstallationsIdPatchRequestAppInstallation.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_app_installations_id_patch_request import RestV10AppInstallationsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10AppInstallationsIdPatchRequest from a JSON string
rest_v10_app_installations_id_patch_request_instance = RestV10AppInstallationsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10AppInstallationsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_app_installations_id_patch_request_dict = rest_v10_app_installations_id_patch_request_instance.to_dict()
# create an instance of RestV10AppInstallationsIdPatchRequest from a dict
rest_v10_app_installations_id_patch_request_from_dict = RestV10AppInstallationsIdPatchRequest.from_dict(rest_v10_app_installations_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


