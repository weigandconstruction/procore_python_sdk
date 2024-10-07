# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Party Person ID | [optional] 
**first_name** | **str** | First name of the Party Person | [optional] 
**last_name** | **str** | Last name of the Party Person | [optional] 
**name** | **str** | Full name of the Party Person | [optional] 
**user_id** | **int** | User ID associated with the Party Person | [optional] 
**is_employee** | **bool** | Indicates whether Party is an Employee of the current Company | [optional] 
**employee_id** | **int** | Employee ID of the Party | [optional] 
**login** | **str** | User Login associated with the Party Person | [optional] 
**vendor** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedByVendor.md) |  | [optional] 
**updated_at** | **datetime** | Time capture by was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_captured_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


