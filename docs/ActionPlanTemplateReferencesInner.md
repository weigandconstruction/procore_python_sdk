# ActionPlanTemplateReferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Action Plan Template Item ID | 
**type** | **str** | Action Plan Test Record Type | 
**payload** | [**ActionPlanTemplateReferencesInnerPayload**](ActionPlanTemplateReferencesInnerPayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.action_plan_template_references_inner import ActionPlanTemplateReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanTemplateReferencesInner from a JSON string
action_plan_template_references_inner_instance = ActionPlanTemplateReferencesInner.from_json(json)
# print the JSON string representation of the object
print(ActionPlanTemplateReferencesInner.to_json())

# convert the object into a dict
action_plan_template_references_inner_dict = action_plan_template_references_inner_instance.to_dict()
# create an instance of ActionPlanTemplateReferencesInner from a dict
action_plan_template_references_inner_from_dict = ActionPlanTemplateReferencesInner.from_dict(action_plan_template_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


