# InspectionItemSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**captured_by** | [**InspectionItemSignatureCapturedBy**](InspectionItemSignatureCapturedBy.md) |  | [optional] 
**captured_at** | **datetime** | Timestamp of creation | [optional] 
**attachment** | [**InspectionItemSignatureAttachment**](InspectionItemSignatureAttachment.md) |  | [optional] 

## Example

```python
from procore_sdk.models.inspection_item_signature import InspectionItemSignature

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionItemSignature from a JSON string
inspection_item_signature_instance = InspectionItemSignature.from_json(json)
# print the JSON string representation of the object
print(InspectionItemSignature.to_json())

# convert the object into a dict
inspection_item_signature_dict = inspection_item_signature_instance.to_dict()
# create an instance of InspectionItemSignature from a dict
inspection_item_signature_from_dict = InspectionItemSignature.from_dict(inspection_item_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


