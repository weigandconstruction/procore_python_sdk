# InspectionItemSignatureAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**url** | **str** | URL | [optional] 
**filename** | **str** | Filename | [optional] 
**name** | **str** | Attachment name | [optional] 

## Example

```python
from procore_sdk.models.inspection_item_signature_attachment import InspectionItemSignatureAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionItemSignatureAttachment from a JSON string
inspection_item_signature_attachment_instance = InspectionItemSignatureAttachment.from_json(json)
# print the JSON string representation of the object
print(InspectionItemSignatureAttachment.to_json())

# convert the object into a dict
inspection_item_signature_attachment_dict = inspection_item_signature_attachment_instance.to_dict()
# create an instance of InspectionItemSignatureAttachment from a dict
inspection_item_signature_attachment_from_dict = InspectionItemSignatureAttachment.from_dict(inspection_item_signature_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


