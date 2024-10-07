# RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**description** | **str** | Description | [optional] 
**private** | **bool** | Privacy flag of the Company Action Plan Template | [optional] 
**plan_type_id** | **int** | ID of an Action Plan Type | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template import RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate from a JSON string
rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template_instance = RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate.from_json(json)
# print the JSON string representation of the object
print(RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate.to_json())

# convert the object into a dict
rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template_dict = rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template_instance.to_dict()
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate from a dict
rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template_from_dict = RestV11CompaniesCompanyIdActionPlansPlanTemplatesIdPatchRequestPlanTemplate.from_dict(rest_v11_companies_company_id_action_plans_plan_templates_id_patch_request_plan_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


