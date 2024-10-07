# RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner

Recycled Action Plan Section (Show)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **str** | Time the Action Plan Section was created | [optional] 
**deleted_at** | **str** | Time the Action Plan Section was deleted | [optional] 
**plan_id** | **int** | Action Plan ID of the Section | [optional] 
**position** | **int** | Postion of the Action Plan Section | [optional] 
**title** | **str** | Title of the Action Plan Section | [optional] 
**updated_at** | **str** | Time the Action Plan Section was updated | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner_instance = RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner_dict = rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner from a dict
rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner_from_dict = RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner.from_dict(rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


