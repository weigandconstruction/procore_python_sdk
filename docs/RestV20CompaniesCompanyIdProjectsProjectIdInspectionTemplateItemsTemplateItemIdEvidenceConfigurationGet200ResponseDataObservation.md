# RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_ids** | **List[str]** | Array of Inspection Item Status IDs that would trigger the requirement of a Observation | [optional] 
**response_option_ids** | **List[str]** | Array of Inspection Response Option IDs that would trigger the requirement of a Observation | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation from a JSON string
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation_instance = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation_dict = rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation from a dict
rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseDataObservation.from_dict(rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


