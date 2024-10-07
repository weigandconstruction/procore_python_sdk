# ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload

To upload an attachment you must upload the entire payload as `multipart/form-data` content-type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** | Reference Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | [optional] 
**image_id** | **int** | The identifier for the project image | [optional] 
**form_id** | **int** | The identifier for the project form | [optional] 
**folder_id** | **int** | ID of the Folder File the File Version belongs to | [optional] 
**file_version_id** | **int** | ID of the Folder File the File Version belongs to | [optional] 
**drawing_revision_id** | **int** | ID of the latest Drawing Revision of the Drawing | [optional] 

## Example

```python
from procore_sdk.models.project_inspection_template_item_reference_create_body_item_template_reference_payload import ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload from a JSON string
project_inspection_template_item_reference_create_body_item_template_reference_payload_instance = ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload.from_json(json)
# print the JSON string representation of the object
print(ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload.to_json())

# convert the object into a dict
project_inspection_template_item_reference_create_body_item_template_reference_payload_dict = project_inspection_template_item_reference_create_body_item_template_reference_payload_instance.to_dict()
# create an instance of ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload from a dict
project_inspection_template_item_reference_create_body_item_template_reference_payload_from_dict = ProjectInspectionTemplateItemReferenceCreateBodyItemTemplateReferencePayload.from_dict(project_inspection_template_item_reference_create_body_item_template_reference_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


