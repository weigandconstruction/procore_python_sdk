# PlanTemplateReferencesInnerPayload

Payload for the attachment type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** |  | [optional] 

## Example

```python
from procore_sdk.models.plan_template_references_inner_payload import PlanTemplateReferencesInnerPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlanTemplateReferencesInnerPayload from a JSON string
plan_template_references_inner_payload_instance = PlanTemplateReferencesInnerPayload.from_json(json)
# print the JSON string representation of the object
print(PlanTemplateReferencesInnerPayload.to_json())

# convert the object into a dict
plan_template_references_inner_payload_dict = plan_template_references_inner_payload_instance.to_dict()
# create an instance of PlanTemplateReferencesInnerPayload from a dict
plan_template_references_inner_payload_from_dict = PlanTemplateReferencesInnerPayload.from_dict(plan_template_references_inner_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


