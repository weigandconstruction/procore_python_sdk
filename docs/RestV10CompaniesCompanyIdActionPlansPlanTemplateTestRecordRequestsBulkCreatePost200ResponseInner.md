# RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Action Plan Template Item ID | [optional] 
**type** | **str** | Action Plan Test Record Type | [optional] 
**payload** | [**ActionPlanTemplateReferencesInnerPayload**](ActionPlanTemplateReferencesInnerPayload.md) |  | [optional] 
**status** | **str** | Status of the update on that Item | [optional] 
**errors** | **object** | errors of the record | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner import RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner from a JSON string
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_instance = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_dict = rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner from a dict
rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_from_dict = RestV10CompaniesCompanyIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInner.from_dict(rest_v10_companies_company_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


