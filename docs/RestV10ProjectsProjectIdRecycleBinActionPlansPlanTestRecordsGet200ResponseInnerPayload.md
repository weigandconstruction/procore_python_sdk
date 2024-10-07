# RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload

Contains specific attributes depending on the type of Action Plan Test Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_id** | **int** | Checklist ID | [optional] 
**checklist_template_id** | **int** | Checklist Template ID | [optional] 
**attachment** | [**RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment**](RestV10ProjectsProjectIdInspectionTemplatesInspectionTemplateIdItemReferencesGet200ResponseInnerPayloadAttachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInnerPayload.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


