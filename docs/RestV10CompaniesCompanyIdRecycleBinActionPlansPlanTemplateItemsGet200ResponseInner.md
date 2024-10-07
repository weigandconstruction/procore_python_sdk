# RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner

Recycled Action Plan Template Item (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_assignees** | [**List[RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner]**](RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInner.md) |  | [optional] 
**created_at** | **str** | Time the Recycled Action Plan Template Item was created | [optional] 
**deleted_at** | **str** | Time the Recycled Action Plan Template Item was deleted | [optional] 
**description** | **str** | Description of the Recycled Action Plan Template Item | [optional] 
**holding_type** | **str** | Recycled Action Plan Template Item holding type specifies whether the current item holds all the succeeding items in the section or the plan | [optional] 
**plan_template_id** | **int** | Action Plan Template ID the Recycled Action Plan Template Item belongs to | [optional] 
**position** | **int** | Postion of the Recycled Action Plan Template Item | [optional] 
**plan_template_section_id** | **int** | Action Plan Template Section ID the Recycled Action Plan Template Item belongs to | [optional] 
**title** | **str** | Title of the Recycled Action Plan Template Item | [optional] 
**updated_at** | **str** | Time the Recycled Action Plan Template Item was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner_instance = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner_dict = rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner from a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner_from_dict = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemsGet200ResponseInner.from_dict(rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


