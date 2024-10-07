# RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | ID of the associated Template Item | 
**type** | **str** | Company Action Plan Template Reference Type | 
**payload** | [**CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload**](CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference import RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference_dict = rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference from a dict
rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateReferencesPostRequestPlanTemplateReference.from_dict(rest_v10_companies_company_id_action_plans_plan_template_references_post_request_plan_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


