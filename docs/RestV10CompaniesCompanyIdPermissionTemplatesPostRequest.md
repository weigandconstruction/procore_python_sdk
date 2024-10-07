# RestV10CompaniesCompanyIdPermissionTemplatesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_template** | [**RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate**](RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_permission_templates_post_request import RestV10CompaniesCompanyIdPermissionTemplatesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdPermissionTemplatesPostRequest from a JSON string
rest_v10_companies_company_id_permission_templates_post_request_instance = RestV10CompaniesCompanyIdPermissionTemplatesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdPermissionTemplatesPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_permission_templates_post_request_dict = rest_v10_companies_company_id_permission_templates_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdPermissionTemplatesPostRequest from a dict
rest_v10_companies_company_id_permission_templates_post_request_from_dict = RestV10CompaniesCompanyIdPermissionTemplatesPostRequest.from_dict(rest_v10_companies_company_id_permission_templates_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


