# RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner

Project Action Plan Templates (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Time the Project Action Plan Template was created | [optional] 
**description** | **str** | Description of the Project Action Plan Template in rich text form | [optional] 
**description_plain_text** | **str** | Description of the Project Action Plan Template in plain text form | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**manager** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerManager.md) |  | [optional] 
**status** | **str** | Status of the Project Action Plan Template | [optional] 
**private** | **bool** | Flag for if the Action Plan Template is private | [optional] 
**title** | **str** | Title of the Project Action Plan Template | [optional] 
**plan_type** | [**RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType**](RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.md) |  | [optional] 
**provider_type** | **str** | Template&#39;s provider type (company/project) | [optional] 
**updated_at** | **datetime** | Timestamp of when the Project Action Plan Template was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


