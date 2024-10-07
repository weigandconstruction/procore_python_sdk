# CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload

To upload an attachment you must upload the entire payload as `multipart/form-data` content-type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** | Reference Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | [optional] 

## Example

```python
from procore_sdk.models.company_inspection_template_item_reference_create_body_template_reference_payload import CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload from a JSON string
company_inspection_template_item_reference_create_body_template_reference_payload_instance = CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload.from_json(json)
# print the JSON string representation of the object
print(CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload.to_json())

# convert the object into a dict
company_inspection_template_item_reference_create_body_template_reference_payload_dict = company_inspection_template_item_reference_create_body_template_reference_payload_instance.to_dict()
# create an instance of CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload from a dict
company_inspection_template_item_reference_create_body_template_reference_payload_from_dict = CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload.from_dict(company_inspection_template_item_reference_create_body_template_reference_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


