# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature

Action Plan Approver Signature (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**attachment** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureAttachment**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureAttachment.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of when signature was added. | [optional] 
**captured_by** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignatureCapturedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInnerSignature.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_approvers_inner_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


