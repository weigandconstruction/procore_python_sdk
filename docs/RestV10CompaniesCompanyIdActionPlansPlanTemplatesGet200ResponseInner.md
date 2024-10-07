# RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner

Company Action Plan Template (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**description** | **str** | Description in rich text form | [optional] 
**description_plain_text** | **str** | Description in plain text form | [optional] 
**status** | **str** | Current state of the Company Action Plan Template | [optional] 
**title** | **str** | Title | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**template_type** | **str** | Type of template (company/project) | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner_dict = rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner from a dict
rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.from_dict(rest_v10_companies_company_id_action_plans_plan_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


