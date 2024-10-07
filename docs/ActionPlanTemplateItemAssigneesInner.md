# ActionPlanTemplateItemAssigneesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | The ID of the Action Plan Template Item Assignee | 
**is_holding** | **bool** | Indicates whether or not the Assignee&#39;s signature is holding | [optional] 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Project Action Plan Template Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.action_plan_template_item_assignees_inner import ActionPlanTemplateItemAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanTemplateItemAssigneesInner from a JSON string
action_plan_template_item_assignees_inner_instance = ActionPlanTemplateItemAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(ActionPlanTemplateItemAssigneesInner.to_json())

# convert the object into a dict
action_plan_template_item_assignees_inner_dict = action_plan_template_item_assignees_inner_instance.to_dict()
# create an instance of ActionPlanTemplateItemAssigneesInner from a dict
action_plan_template_item_assignees_inner_from_dict = ActionPlanTemplateItemAssigneesInner.from_dict(action_plan_template_item_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


