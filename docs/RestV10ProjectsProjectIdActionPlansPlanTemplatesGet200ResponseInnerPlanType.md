# RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**active** | **bool** | Flag indicating if Action Plan Type is intended for use | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**name** | **str** | Name | [optional] 
**updated_at** | **datetime** | Timestamp of the last update | [optional] 
**source_key** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type import RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType from a JSON string
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type_instance = RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type_dict = rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType from a dict
rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type_from_dict = RestV10ProjectsProjectIdActionPlansPlanTemplatesGet200ResponseInnerPlanType.from_dict(rest_v10_projects_project_id_action_plans_plan_templates_get200_response_inner_plan_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


