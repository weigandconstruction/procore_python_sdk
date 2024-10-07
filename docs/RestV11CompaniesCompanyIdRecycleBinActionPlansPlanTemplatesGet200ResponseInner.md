# RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner

Company Action Plan Template (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Time the Company Action Plan Template was created | [optional] 
**deleted_at** | **datetime** | Timestamp of when the Company Action Plan Template was deleted | [optional] 
**deleted_by** | [**RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInnerDeletedBy**](RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInnerDeletedBy.md) |  | [optional] 
**description** | **str** | Description of the Company Action Plan Template in rich text form | [optional] 
**description_plain_text** | **str** | Description of the Company Action Plan Template in plain text form | [optional] 
**status** | **str** | Status of the Company Action Plan Template | [optional] 
**title** | **str** | Title of the Company Action Plan Template | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**provider_type** | **str** | Template&#39;s provider type (company/project) | [optional] 
**updated_at** | **datetime** | Timestamp of when the Company Action Plan Template was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner import RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner from a JSON string
rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner_instance = RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner_dict = rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner from a dict
rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner_from_dict = RestV11CompaniesCompanyIdRecycleBinActionPlansPlanTemplatesGet200ResponseInner.from_dict(rest_v11_companies_company_id_recycle_bin_action_plans_plan_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


