# RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner

Action Plan Section (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Timestamp of creation | [optional] 
**plan_id** | **int** | Action Plan ID | [optional] 
**position** | **int** | Position among other Action Plan Sections in an Action Plan | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **str** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner_instance = RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner_dict = rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner from a dict
rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner_from_dict = RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.from_dict(rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


