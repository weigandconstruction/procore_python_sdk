# RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner

Recycled Company Action Plan Template Reference (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_id** | **int** | ID of the associated Company Action Plan Template Item | [optional] 
**created_at** | **str** | Time the Company Action Plan Template Reference was created | [optional] 
**deleted_at** | **str** | Time the Company Action Plan Template Reference was deleted | [optional] 
**payload** | [**RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayload**](RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayload.md) |  | [optional] 
**plan_template_id** | **int** | Company Action Plan Template ID | [optional] 
**type** | **str** | Company Action Plan Template Reference Type | [optional] 
**updated_at** | **str** | Time the Recycled Company Action Plan Template Reference was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner from a JSON string
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_instance = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_dict = rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner from a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_from_dict = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateReferencesGet200ResponseInner.from_dict(rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_references_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


