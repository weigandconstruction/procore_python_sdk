# RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response

Company Action Plan Template Section (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Timestamp of creation | [optional] 
**plan_template_id** | **int** | ID of the Company Action Plan Template the Company Action Plan Template Section belongs to | [optional] 
**position** | **int** | Position among the other Company Action Plan Template Sections on the Company Action Plan Template | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **str** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response import RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response_dict = rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response from a dict
rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateSectionsCreateFromSectionPost201Response.from_dict(rest_v10_companies_company_id_action_plans_plan_template_sections_create_from_section_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


