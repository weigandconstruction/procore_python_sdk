# RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_section_id** | **int** | Section ID of the Action Plan Item | 
**title** | **str** | Title of the Action Plan Item | 
**description** | **str** | Description of the Action Plan Item | [optional] 
**notes** | **str** | Notes for the Action Plan Item | [optional] 
**due_at** | **datetime** | Due Date of the Action Plan Item | [optional] 
**holding_type** | **str** | Action Plan Item holding type specifies whether the current item holds all the succeeding items in the section or the plan | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item import RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem from a JSON string
rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item_instance = RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem.to_json())

# convert the object into a dict
rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item_dict = rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem from a dict
rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item_from_dict = RestV10ProjectsProjectIdActionPlansPlanItemsPostRequestPlanItem.from_dict(rest_v10_projects_project_id_action_plans_plan_items_post_request_plan_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


