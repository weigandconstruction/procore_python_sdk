# ActionPlanTemplateReferencesInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Action Plan Template Item ID | 
**type** | **str** | Action Plan Reference Type | 
**payload** | [**ActionPlanTemplateReferencesInner1Payload**](ActionPlanTemplateReferencesInner1Payload.md) |  | 

## Example

```python
from procore_sdk.models.action_plan_template_references_inner1 import ActionPlanTemplateReferencesInner1

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanTemplateReferencesInner1 from a JSON string
action_plan_template_references_inner1_instance = ActionPlanTemplateReferencesInner1.from_json(json)
# print the JSON string representation of the object
print(ActionPlanTemplateReferencesInner1.to_json())

# convert the object into a dict
action_plan_template_references_inner1_dict = action_plan_template_references_inner1_instance.to_dict()
# create an instance of ActionPlanTemplateReferencesInner1 from a dict
action_plan_template_references_inner1_from_dict = ActionPlanTemplateReferencesInner1.from_dict(action_plan_template_references_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


