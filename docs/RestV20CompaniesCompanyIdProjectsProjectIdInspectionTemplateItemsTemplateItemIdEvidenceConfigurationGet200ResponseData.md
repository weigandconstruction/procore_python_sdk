# RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Item ID for the Evidence Configuration | [optional] 
**photo** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataPhoto**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataPhoto.md) |  | [optional] 
**observation** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation.md) |  | [optional] 
**is_editable** | **bool** | Indicates if the Item Evidence Configuration can be edited. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Date updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData from a JSON string
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_instance = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_dict = rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData from a dict
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData.from_dict(rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


