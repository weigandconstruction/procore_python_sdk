# RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner

Recycled Action Plan Template Section (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Time the Action Plan Template Section was created | [optional] 
**deleted_at** | **str** | Time the Action Plan Template Section was deleted | [optional] 
**plan_template_id** | **int** | Action Plan Template ID of the Action Plan Template Section | [optional] 
**position** | **int** | Postion of the Action Plan Template Section | [optional] 
**title** | **str** | Title of the Action Plan Template Section | [optional] 
**updated_at** | **str** | Time the Action Plan Template Section was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner import RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner_instance = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner_dict = rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner from a dict
rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner_from_dict = RestV10CompaniesCompanyIdRecycleBinActionPlansPlanTemplateSectionsGet200ResponseInner.from_dict(rest_v10_companies_company_id_recycle_bin_action_plans_plan_template_sections_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


