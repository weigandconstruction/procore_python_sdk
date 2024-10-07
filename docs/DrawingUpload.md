# DrawingUpload

Drawing Upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Upload ID | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**company_id** | **int** | Unique identifier for the company. | [optional] 
**created_by_id** | **int** | ID of creator | [optional] 
**created_at** | **datetime** | Drawing Upload created at | [optional] 
**updated_at** | **datetime** | Drawing Upload updated at | [optional] 
**error_email_sent** | **bool** | Error email sent status | [optional] 
**notify_on_success** | **bool** | Notify on success status | [optional] 
**deletion_in_progress** | **bool** | Deletion in progress status | [optional] 
**success_email_sent** | **bool** | Success email sent status | [optional] 
**drawing_area_id** | **int** | Drawing Area ID | [optional] 
**status** | **str** |  | [optional] 
**pre_adaptive_complete** | **bool** | Pre adaptive complete status | [optional] 
**drawing_number_contains_revision** | **bool** | Drawing number contains revision | [optional] 
**get_info_from_filename** | **bool** | Get info from filename | [optional] 
**language** | **str** | Language for OCR | [optional] 
**drawing_log_imports** | [**List[DrawingLogImport]**](DrawingLogImport.md) | Drawing Log Imports (Only included in &#39;with_drawing_log_imports&#39; view) | [optional] 

## Example

```python
from procore_sdk.models.drawing_upload import DrawingUpload

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingUpload from a JSON string
drawing_upload_instance = DrawingUpload.from_json(json)
# print the JSON string representation of the object
print(DrawingUpload.to_json())

# convert the object into a dict
drawing_upload_dict = drawing_upload_instance.to_dict()
# create an instance of DrawingUpload from a dict
drawing_upload_from_dict = DrawingUpload.from_dict(drawing_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


