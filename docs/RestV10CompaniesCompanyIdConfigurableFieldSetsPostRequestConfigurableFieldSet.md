# RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**class_name** | **str** | Class Name of the object the Configurable Field Set is applied to | 
**fields** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSetFields**](RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSetFields.md) |  | 
**project_ids** | **List[int]** |  | [optional] 
**category** | **str** | Required and only needed when associating projects for an Observations Configurable Field Set.(0 &#x3D; quality, 1 &#x3D; safety, 2 &#x3D; commissioning, 3 &#x3D; warranty, 4 &#x3D; work to complete) | [optional] 
**action_plan_type_id** | **int** | Action Plan Type unique identifier | [optional] 
**inspection_type_id** | **int** | Inspection type unique identifier | [optional] 
**generic_tool_id** | **int** | Generic tool unique identifier | [optional] 
**company_default** | **bool** | If the Configurable Field Set is the company default for new projects | [optional] 
**company_configurable_field_set_default_column_name** | **str** | the column name on CompanyConfigurableFieldSetDefault to set the Configurable Field Set as default to. Only needed if company_default is true. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set import RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet from a JSON string
rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_dict = rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet from a dict
rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsPostRequestConfigurableFieldSet.from_dict(rest_v10_companies_company_id_configurable_field_sets_post_request_configurable_field_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


