# RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_installation_id** | **int** | App Installation ID | [optional] 
**company_id** | **int** | Company ID | [optional] 
**manifest_url** | **str** | Presigned Temporary Url For Manifest Configuration | [optional] 
**projects** | [**List[RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInnerProjectsInner]**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInnerProjectsInner.md) | List of project ids the app configuration applies to | [optional] 
**id** | **int** | ID | [optional] 
**title** | **str** | Title of app configuration | [optional] 
**created_by** | [**RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInnerAllOfCreatedBy**](RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInnerAllOfCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | The UTC datetime for the creation of the resource in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | The UTC datetime for the last update of the resource in ISO 8601 format. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_app_configurations_get200_response_inner import RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_app_configurations_get200_response_inner_instance = RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_app_configurations_get200_response_inner_dict = rest_v10_companies_company_id_app_configurations_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner from a dict
rest_v10_companies_company_id_app_configurations_get200_response_inner_from_dict = RestV10CompaniesCompanyIdAppConfigurationsGet200ResponseInner.from_dict(rest_v10_companies_company_id_app_configurations_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


