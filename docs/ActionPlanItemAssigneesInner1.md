# ActionPlanItemAssigneesInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Action Plan Item Assignee | 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Action Plan Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.action_plan_item_assignees_inner1 import ActionPlanItemAssigneesInner1

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanItemAssigneesInner1 from a JSON string
action_plan_item_assignees_inner1_instance = ActionPlanItemAssigneesInner1.from_json(json)
# print the JSON string representation of the object
print(ActionPlanItemAssigneesInner1.to_json())

# convert the object into a dict
action_plan_item_assignees_inner1_dict = action_plan_item_assignees_inner1_instance.to_dict()
# create an instance of ActionPlanItemAssigneesInner1 from a dict
action_plan_item_assignees_inner1_from_dict = ActionPlanItemAssigneesInner1.from_dict(action_plan_item_assignees_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


