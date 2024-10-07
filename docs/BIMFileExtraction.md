# BIMFileExtraction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**parent_bim_file_extraction_id** | **int** | ID of the parent BIM File Extraction | [optional] 
**bim_file_upload_id** | **int** | ID of the uploaded BIM File | [optional] 
**bim_file_upload** | [**BIMFileUpload**](BIMFileUpload.md) |  | [optional] 
**bim_model_revision_id** | **int** | ID of the BIM Model Revision | [optional] 
**status** | **str** | Extraction Status | [optional] 
**progress** | **float** | Progress of overall extraction taking into account the individual extraction items | [optional] 
**retry_count** | **int** | No. of retries performed on the extraction | [optional] 
**viewpoint_id** | **int** | ID of the BIM Viewpoint | [optional] 
**extraction_format_requests** | [**List[BIMFileExtractionItemType]**](BIMFileExtractionItemType.md) | Array of items indicating formats of items requested to be extracted | [optional] 
**extraction_items** | [**List[BIMFileExtractionItem]**](BIMFileExtractionItem.md) | An array of items extracted from a 3d model | [optional] 
**errors** | [**List[BIMFileExtractionItemError]**](BIMFileExtractionItemError.md) | An array of errors encountered during extraction | [optional] 
**created_by** | [**BIMFileExtractionCreatedBy**](BIMFileExtractionCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction import BIMFileExtraction

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtraction from a JSON string
bim_file_extraction_instance = BIMFileExtraction.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtraction.to_json())

# convert the object into a dict
bim_file_extraction_dict = bim_file_extraction_instance.to_dict()
# create an instance of BIMFileExtraction from a dict
bim_file_extraction_from_dict = BIMFileExtraction.from_dict(bim_file_extraction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


