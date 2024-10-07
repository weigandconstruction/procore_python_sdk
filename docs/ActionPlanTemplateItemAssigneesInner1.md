# ActionPlanTemplateItemAssigneesInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Action Plan Template Item Assignee | 
**is_holding** | **bool** | Indicates whether or not the Assignee&#39;s signature is holding | [optional] 
**party_id** | **int** | Party Person ID of the Action Plan Item Assignee to be set | [optional] 
**role** | **str** | Role of the Project Action Plan Template Item Assignee to be set | [optional] 
**verification_method_id** | **int** | Verification Method ID of the Project Action Plan Template Item Assignee to be set | [optional] 

## Example

```python
from procore_sdk.models.action_plan_template_item_assignees_inner1 import ActionPlanTemplateItemAssigneesInner1

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanTemplateItemAssigneesInner1 from a JSON string
action_plan_template_item_assignees_inner1_instance = ActionPlanTemplateItemAssigneesInner1.from_json(json)
# print the JSON string representation of the object
print(ActionPlanTemplateItemAssigneesInner1.to_json())

# convert the object into a dict
action_plan_template_item_assignees_inner1_dict = action_plan_template_item_assignees_inner1_instance.to_dict()
# create an instance of ActionPlanTemplateItemAssigneesInner1 from a dict
action_plan_template_item_assignees_inner1_from_dict = ActionPlanTemplateItemAssigneesInner1.from_dict(action_plan_template_item_assignees_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


