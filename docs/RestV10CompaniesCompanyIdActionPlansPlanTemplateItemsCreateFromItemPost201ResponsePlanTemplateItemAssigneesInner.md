# RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner

Company Action Plan Template Item Assignee (Compact)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Time the Company Action Plan Template Item Assignee was created | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the assignee is necessary to sign for a hold point | [optional] 
**role** | **str** | Role of the Company Action Plan Template Item Assignee | [optional] 
**updated_at** | **datetime** | Time the Company Action Plan Template Item Assignee was updated | [optional] 
**verification_method** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod**](RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_dict = rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner from a dict
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner.from_dict(rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_plan_template_item_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


