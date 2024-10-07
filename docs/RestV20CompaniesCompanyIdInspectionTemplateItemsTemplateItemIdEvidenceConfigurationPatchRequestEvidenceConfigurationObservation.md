# RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_ids** | **List[str]** | Array of Company Inspection Template Item Status IDs that would trigger the requirement of an Observation | [optional] 
**response_option_ids** | **List[str]** | Array of Inspection Response Option IDs that would trigger the requirement of an Observation | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation import RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation from a JSON string
rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation_instance = RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation.to_json())

# convert the object into a dict
rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation_dict = rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation from a dict
rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation_from_dict = RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfigurationObservation.from_dict(rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


