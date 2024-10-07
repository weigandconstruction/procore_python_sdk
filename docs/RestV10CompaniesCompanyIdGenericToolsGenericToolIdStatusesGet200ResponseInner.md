# RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**status_name** | **str** | Status Name | [optional] 
**status** | **str** | Status | [optional] 
**is_used** | **bool** | Is Used in generic tool item or workflow | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner import RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner_instance = RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner_dict = rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner from a dict
rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner_from_dict = RestV10CompaniesCompanyIdGenericToolsGenericToolIdStatusesGet200ResponseInner.from_dict(rest_v10_companies_company_id_generic_tools_generic_tool_id_statuses_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


