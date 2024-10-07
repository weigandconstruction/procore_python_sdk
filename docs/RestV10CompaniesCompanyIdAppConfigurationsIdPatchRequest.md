# RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_configuration** | **object** | Configuration values for an configuration of an app installation. | [optional] 
**title** | **str** | Title for app configuration | [optional] 
**project_ids** | **List[int]** | A list of projects which will have the app configuration | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_id_patch_request import RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest from a JSON string
rest_v10_companies_company_id_app_configurations_id_patch_request_instance = RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_app_configurations_id_patch_request_dict = rest_v10_companies_company_id_app_configurations_id_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest from a dict
rest_v10_companies_company_id_app_configurations_id_patch_request_from_dict = RestV10CompaniesCompanyIdAppConfigurationsIdPatchRequest.from_dict(rest_v10_companies_company_id_app_configurations_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


