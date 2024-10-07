# RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**base64_image_data** | **str** | base64 encoded image | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_settings_my_avatar_put_request import RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest from a JSON string
rest_v10_companies_company_id_settings_my_avatar_put_request_instance = RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_settings_my_avatar_put_request_dict = rest_v10_companies_company_id_settings_my_avatar_put_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest from a dict
rest_v10_companies_company_id_settings_my_avatar_put_request_from_dict = RestV10CompaniesCompanyIdSettingsMyAvatarPutRequest.from_dict(rest_v10_companies_company_id_settings_my_avatar_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


