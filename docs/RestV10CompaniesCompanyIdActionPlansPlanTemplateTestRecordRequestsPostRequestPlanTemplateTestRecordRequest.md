# RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | ID of the associated Company Action Plan Template Item | 
**type** | **str** | Action Plan Template Test Record Type | 
**payload** | [**RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequestPayload**](RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequestPayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request import RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request_dict = rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest from a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsPostRequestPlanTemplateTestRecordRequest.from_dict(rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_post_request_plan_template_test_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


