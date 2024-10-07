# RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1

Existing Custom Fields to be edited for this Configurable Field Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Metadatum ID | [optional] 
**name** | **str** | The name of the Custom Field | [optional] 
**label** | **str** | The label of the Custom Field Definition | [optional] 
**description** | **str** | The description of the Custom Field Definition | [optional] 
**custom_field_definition_id** | **int** | Custom Field Definition ID | [optional] 
**data_type** | **str** | Data type of the Custom Field | [optional] 
**position** | **int** | The display position of the Custom Field, which is sorted ascending, lowest position is visually the top left of the page on a grid basis (used in conjunction with column_width property to calculate row and column properties). | [optional] 
**required** | **bool** | Whether or not the Field is required | [optional] 
**visible** | **bool** | Whether or not the Custom Field is visible | [optional] 
**row** | **float** | Row the Field is position on the Form | [optional] 
**column** | **float** | Column the Field is position on the Form | [optional] 
**column_width** | **float** | How many columns the field spans on the Form | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1 import RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1 from a JSON string
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1_instance = RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1.to_json())

# convert the object into a dict
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1_dict = rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1 from a dict
rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1_from_dict = RestV10CompaniesCompanyIdConfigurableFieldSetsIdPatchRequestConfigurableFieldSetFieldsCustomField1.from_dict(rest_v10_companies_company_id_configurable_field_sets_id_patch_request_configurable_field_set_fields_custom_field1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


