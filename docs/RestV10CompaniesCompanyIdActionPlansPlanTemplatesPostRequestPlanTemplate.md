# RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | 
**description** | **str** | Description | [optional] 
**plan_type_id** | **int** | ID of an Action Plan Type | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template import RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate from a JSON string
rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template_dict = rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate from a dict
rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplatesPostRequestPlanTemplate.from_dict(rest_v10_companies_company_id_action_plans_plan_templates_post_request_plan_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


