# ActionPlanItemAssigneesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Action Plan Item Assignee | 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Action Plan Item Assignee to be set | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.action_plan_item_assignees_inner import ActionPlanItemAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanItemAssigneesInner from a JSON string
action_plan_item_assignees_inner_instance = ActionPlanItemAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(ActionPlanItemAssigneesInner.to_json())

# convert the object into a dict
action_plan_item_assignees_inner_dict = action_plan_item_assignees_inner_instance.to_dict()
# create an instance of ActionPlanItemAssigneesInner from a dict
action_plan_item_assignees_inner_from_dict = ActionPlanItemAssigneesInner.from_dict(action_plan_item_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


