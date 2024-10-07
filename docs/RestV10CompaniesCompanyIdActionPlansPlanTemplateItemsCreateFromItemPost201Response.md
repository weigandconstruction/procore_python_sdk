# RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response

Company Action Plan Template Item (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_assignees** | [**List[RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner]**](RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**description** | **str** | Description | [optional] 
**holding_type** | **str** | Company Plan Template Item holding type specifies whether the current item holds all the succeeding items in the section or the plan | [optional] 
**plan_template_id** | **int** | ID the Company Action Plan Template Item belongs to | [optional] 
**position** | **int** | Position among other Company Action Plan Template Items within a Company Action Plan Template Section | [optional] 
**plan_template_section_id** | **int** | ID of the Company Action Plan Template Section the Company Action Plan Template Item belongs to | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_dict = rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response from a dict
rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201Response.from_dict(rest_v10_companies_company_id_action_plans_plan_template_items_create_from_item_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


