# ActionPlanTemplateReferencesInnerPayload

Used to specify extra required details for some types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_template_id** | **int** | Checklist Template ID for the checklist type test record request | [optional] 
**form_template_id** | **int** | Form Template ID for the form type test record request | [optional] 
**generic_tool_id** | **int** | Generic Tool ID for the generic_tool type test record request | [optional] 

## Example

```python
from procore_sdk.models.action_plan_template_references_inner_payload import ActionPlanTemplateReferencesInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ActionPlanTemplateReferencesInnerPayload from a JSON string
action_plan_template_references_inner_payload_instance = ActionPlanTemplateReferencesInnerPayload.from_json(json)
# print the JSON string representation of the object
print(ActionPlanTemplateReferencesInnerPayload.to_json())

# convert the object into a dict
action_plan_template_references_inner_payload_dict = action_plan_template_references_inner_payload_instance.to_dict()
# create an instance of ActionPlanTemplateReferencesInnerPayload from a dict
action_plan_template_references_inner_payload_from_dict = ActionPlanTemplateReferencesInnerPayload.from_dict(action_plan_template_references_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


