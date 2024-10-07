# DrawingUploadDrawingLogImportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_uuid** | **str** | An Uploads objects uuid. Must be a pdf. | 
**drawing_date** | **datetime** | Drawing date *Required only if a drawing_id is provided | 
**received_date** | **datetime** | Received date | [optional] 
**default_revision** | **str** | Default Revision for any Drawing Revisions in the Import *Required only if a drawing_id is provided | 
**drawing_id** | **int** | Drawing ID to associate any created Drawing Revisions to | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_upload_drawing_log_imports_inner import DrawingUploadDrawingLogImportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingUploadDrawingLogImportsInner from a JSON string
drawing_upload_drawing_log_imports_inner_instance = DrawingUploadDrawingLogImportsInner.from_json(json)
# print the JSON string representation of the object
print(DrawingUploadDrawingLogImportsInner.to_json())

# convert the object into a dict
drawing_upload_drawing_log_imports_inner_dict = drawing_upload_drawing_log_imports_inner_instance.to_dict()
# create an instance of DrawingUploadDrawingLogImportsInner from a dict
drawing_upload_drawing_log_imports_inner_from_dict = DrawingUploadDrawingLogImportsInner.from_dict(drawing_upload_drawing_log_imports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


