# RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner

Action Plan (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**closed_item_count** | **int** | Plan Items that have a status of \&quot;closed\&quot; | [optional] 
**created_at** | **datetime** | Time the Action Plan was created | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**description** | **str** | Description of the Action Plan in rich text form | [optional] 
**description_plain_text** | **str** | Description of the Action Plan in plain text form | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**manager** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**number** | **int** | Number of the Action Plan | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**plan_status** | [**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanStatus.md) |  | [optional] 
**plan_approvers** | [**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanApproversInner.md) |  | [optional] 
**plan_receivers** | [**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.md) |  | [optional] 
**private** | **bool** | Flag for if the Action Plan is private | [optional] 
**status** | **str** | Name of the Status of the Action Plan | [optional] 
**status_type** | **str** | Type of the Status of the Action Plan | [optional] 
**title** | **str** | Title of the Action Plan | [optional] 
**total_item_count** | **int** | Total number of Plan Items | [optional] 
**updated_at** | **datetime** | Timestamp of when the Action Plan was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plans_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plans_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plans_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


