# RestV10CompaniesCompanyIdAppConfigurationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to_all_projects** | **bool** | Apply the app configuration to all projects under a company ( if set to true, project_ids field must be blank ) | [optional] 
**applies_to_company** | **bool** | Apply the app configuration to be available from company routes | [optional] 
**app_installation_id** | **int** | App Installation ID | 
**company_id** | **int** | Company ID | 
**instance_configuration** | **object** | App configuration values for a set of projects. | 
**project_ids** | **List[int]** | A list of projects which will have the app configuration | [optional] 
**title** | **str** | Single title for app configurations | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_post_request import RestV10CompaniesCompanyIdAppConfigurationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsPostRequest from a JSON string
rest_v10_companies_company_id_app_configurations_post_request_instance = RestV10CompaniesCompanyIdAppConfigurationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdAppConfigurationsPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_app_configurations_post_request_dict = rest_v10_companies_company_id_app_configurations_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsPostRequest from a dict
rest_v10_companies_company_id_app_configurations_post_request_from_dict = RestV10CompaniesCompanyIdAppConfigurationsPostRequest.from_dict(rest_v10_companies_company_id_app_configurations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


