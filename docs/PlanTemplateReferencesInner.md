# PlanTemplateReferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_template_item_id** | **int** | Plan Template Item ID | 
**type** | **str** | Plan Template Reference Type | 
**payload** | [**PlanTemplateReferencesInnerPayload**](PlanTemplateReferencesInnerPayload.md) |  | 

## Example

```python
from procore_sdk.models.plan_template_references_inner import PlanTemplateReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanTemplateReferencesInner from a JSON string
plan_template_references_inner_instance = PlanTemplateReferencesInner.from_json(json)
# print the JSON string representation of the object
print(PlanTemplateReferencesInner.to_json())

# convert the object into a dict
plan_template_references_inner_dict = plan_template_references_inner_instance.to_dict()
# create an instance of PlanTemplateReferencesInner from a dict
plan_template_references_inner_from_dict = PlanTemplateReferencesInner.from_dict(plan_template_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


