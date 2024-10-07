# BIMFileExtractionItemArtifactWebFormatCellFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**size** | **int** | File size in bytes | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_artifact_web_format_cell_file import BIMFileExtractionItemArtifactWebFormatCellFile

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemArtifactWebFormatCellFile from a JSON string
bim_file_extraction_item_artifact_web_format_cell_file_instance = BIMFileExtractionItemArtifactWebFormatCellFile.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemArtifactWebFormatCellFile.to_json())

# convert the object into a dict
bim_file_extraction_item_artifact_web_format_cell_file_dict = bim_file_extraction_item_artifact_web_format_cell_file_instance.to_dict()
# create an instance of BIMFileExtractionItemArtifactWebFormatCellFile from a dict
bim_file_extraction_item_artifact_web_format_cell_file_from_dict = BIMFileExtractionItemArtifactWebFormatCellFile.from_dict(bim_file_extraction_item_artifact_web_format_cell_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


