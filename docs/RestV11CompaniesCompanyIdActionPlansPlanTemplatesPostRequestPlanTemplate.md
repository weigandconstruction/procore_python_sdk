# RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | 
**description** | **str** | Description | [optional] 
**private** | **bool** | Privacy flag of the Company Action Plan Template | [optional] 
**plan_type_id** | **int** | ID of an Action Plan Type | 

## Example

```python
from procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template import RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate from a JSON string
rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template_instance = RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.from_json(json)
# print the JSON string representation of the object
print(RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.to_json())

# convert the object into a dict
rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template_dict = rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template_instance.to_dict()
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate from a dict
rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template_from_dict = RestV11CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.from_dict(rest_v11_companies_company_id_action_plans_plan_templates_post_request_plan_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


