# DrawingLogImport

Drawing Log Import

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Log Import ID | [optional] 
**filename** | **str** | Filename | [optional] 
**drawing_set_id** | **int** | Drawing Set ID | [optional] 
**drawing_date** | **date** | Drawing date | [optional] 
**received_date** | **date** | Received date | [optional] 
**default_revision** | **str** | Default Revision for any Drawing Revisions in the Import | [optional] 
**drawing_id** | **int** | Drawing ID | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_log_import import DrawingLogImport

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingLogImport from a JSON string
drawing_log_import_instance = DrawingLogImport.from_json(json)
# print the JSON string representation of the object
print(DrawingLogImport.to_json())

# convert the object into a dict
drawing_log_import_dict = drawing_log_import_instance.to_dict()
# create an instance of DrawingLogImport from a dict
drawing_log_import_from_dict = DrawingLogImport.from_dict(drawing_log_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


