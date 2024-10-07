# RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner

Company Action Plan Template Test Record Request (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**plan_template_item_id** | **int** | ID of the associated Company Action Plan Template Item | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**payload** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInnerPayload**](RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInnerPayload.md) |  | [optional] 
**plan_template_id** | **int** | Company Action Plan Template ID | [optional] 
**type** | **str** | Action Plan Test Record Type | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner_dict = rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner from a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner.from_dict(rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


