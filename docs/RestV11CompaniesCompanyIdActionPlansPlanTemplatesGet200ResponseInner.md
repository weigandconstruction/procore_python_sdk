# RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner

Company Action Plan Template (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**description** | **str** | Description in rich text form | [optional] 
**description_plain_text** | **str** | Description in plain text form | [optional] 
**status** | **str** | Current state of the Company Action Plan Template | [optional] 
**private** | **bool** | Flag for if the Action Plan Template is private | [optional] 
**title** | **str** | Title | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**provider_type** | **str** | Template&#39;s provider type (company/project) | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner import RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner from a JSON string
rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner_instance = RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner_dict = rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner from a dict
rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner_from_dict = RestV11CompaniesCompanyIdActionPlansPlanTemplatesGet200ResponseInner.from_dict(rest_v11_companies_company_id_action_plans_plan_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


