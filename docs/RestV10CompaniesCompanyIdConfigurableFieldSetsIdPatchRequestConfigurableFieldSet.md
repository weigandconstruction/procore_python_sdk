# RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**fields** | [**RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFields**](RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFields.md) |  | 
**project_ids** | **List[int]** |  | [optional] 
**category** | **str** | Required and only needed when associating projects for an Observations Configurable Field Set.(0 &#x3D; quality, 1 &#x3D; safety, 2 &#x3D; commissioning, 3 &#x3D; warranty, 4 &#x3D; work to complete) | [optional] 
**include_all_projects** | **bool** | Whether or not all projects selected | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set import RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_dict = rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet from a dict
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSet.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


