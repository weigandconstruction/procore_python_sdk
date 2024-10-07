# RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Company Action Plan Template Item ID of the Company Action Plan Template Item Assignee to be set | 
**is_holding** | **bool** | Indicates whether or not the Assignee&#39;s signature is holding | [optional] 
**role** | **str** | Role of the Company Action Plan Template Item Assignee to be set | 
**verification_method_id** | **int** | Verification Method ID of the Company Action Plan Template Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee import RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee_dict = rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee from a dict
rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateItemAssigneesPostRequestPlanTemplateItemAssignee.from_dict(rest_v10_companies_company_id_action_plans_plan_template_item_assignees_post_request_plan_template_item_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


