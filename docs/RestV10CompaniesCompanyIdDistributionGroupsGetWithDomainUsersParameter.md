# RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **int** | Domain ID | [optional] 
**provider_id** | **int** | Provider ID (provider class is inderred from domain) | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter import RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter from a JSON string
rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter_instance = RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter.to_json())

# convert the object into a dict
rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter_dict = rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter from a dict
rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter_from_dict = RestV10CompaniesCompanyIdDistributionGroupsGetWithDomainUsersParameter.from_dict(rest_v10_companies_company_id_distribution_groups_get_with_domain_users_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


