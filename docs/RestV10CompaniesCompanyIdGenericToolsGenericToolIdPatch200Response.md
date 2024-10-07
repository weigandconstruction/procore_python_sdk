# RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the generic tool. | [optional] 
**abbreviation** | **str** | Abbreviation for the Title. Will be used as a prefix for the Generic Tool Item number. | [optional] 
**domain_id** | **int** | Unique identifier for the generic tool domain. | [optional] 
**title** | **str** | Primary name/title for the generic tool. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response import RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response from a JSON string
rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response_instance = RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response_dict = rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response from a dict
rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response_from_dict = RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response.from_dict(rest_v10_companies_company_id_generic_tools_generic_tool_id_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


