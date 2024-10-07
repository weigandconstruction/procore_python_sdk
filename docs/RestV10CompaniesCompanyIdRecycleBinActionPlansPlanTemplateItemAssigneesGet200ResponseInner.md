# RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner

Recycled Company Action Plan Template Item Assignee (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_id** | **int** | Recycled Company Plan Template Item ID the Company Action Plan Template Item Assignee belongs to | [optional] 
**created_at** | **str** | Time the Recycled Company Action Plan Template Item Assignee was created | [optional] 
**deleted_at** | **str** | Time the Recycled Company Action Plan Template Item Assignee was deleted | [optional] 
**is_holding** | **bool** | Boolean flag indicating whether the Action Plan Template Item Assignee is necessary to sign for a hold point | [optional] 
**plan_template_id** | **int** | Action Plan Template ID the Company Action Plan Template Item Assignee belongs to | [optional] 
**role** | **str** | Role of the Recycled Company Action Plan Template Item Assignee | [optional] 
**updated_at** | **str** | Time the Recycled Company Action Plan Template Item Assignee was updated | [optional] 
**verification_method** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod**](RestV10CompaniesCompanyIdActionPlansPlanTemplateItemsCreateFromItemPost201ResponsePlanTemplateItemAssigneesInnerVerificationMethod.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner_instance = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner_dict = rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner from a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner_from_dict = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateItemAssigneesGet200ResponseInner.from_dict(rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_item_assignees_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


