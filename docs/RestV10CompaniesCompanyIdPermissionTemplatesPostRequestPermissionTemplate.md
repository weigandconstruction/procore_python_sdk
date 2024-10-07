# RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Permission Template | [optional] 
**company_id** | **int** | The ID of the Company the Permission Template belongs to | [optional] 
**name** | **str** | The name of the Permission Template | [optional] 
**provider_type** | **str** | &#39;Project&#39; or &#39;Company&#39; | [optional] 
**type** | **str** | &#39;company_tools&#39;, &#39;global&#39; or &#39;project_specific&#39; | [optional] 
**provider_id** | **int** | Either the company_id or project_id based on provider_type | [optional] 
**user_access_levels** | **object** | user access levels for active tools | [optional] 
**permissions** | **object** | permitted actions for active tools | [optional] 
**project_id** | **int** | id of corresponding project if provider_type &#x3D;&#x3D; Project | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_permission_templates_post_request_permission_template import RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate from a JSON string
rest_v10_companies_company_id_permission_templates_post_request_permission_template_instance = RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.to_json())

# convert the object into a dict
rest_v10_companies_company_id_permission_templates_post_request_permission_template_dict = rest_v10_companies_company_id_permission_templates_post_request_permission_template_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate from a dict
rest_v10_companies_company_id_permission_templates_post_request_permission_template_from_dict = RestV10CompaniesCompanyIdPermissionTemplatesPostRequestPermissionTemplate.from_dict(rest_v10_companies_company_id_permission_templates_post_request_permission_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


