# BIMFileExtractionItemArtifactWebFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_file** | [**BIMFileExtractionItemArtifactWebFormatCellFile**](BIMFileExtractionItemArtifactWebFormatCellFile.md) |  | [optional] 
**node_file** | [**BIMFileExtractionItemArtifactWebFormatCellFile**](BIMFileExtractionItemArtifactWebFormatCellFile.md) |  | [optional] 
**mesh_node_file** | [**BIMFileExtractionItemArtifactWebFormatCellFile**](BIMFileExtractionItemArtifactWebFormatCellFile.md) |  | [optional] 
**mesh_file** | [**BIMFileExtractionItemArtifactWebFormatCellFile**](BIMFileExtractionItemArtifactWebFormatCellFile.md) |  | [optional] 
**manifest_file** | [**BIMFileExtractionItemArtifactWebFormatCellFile**](BIMFileExtractionItemArtifactWebFormatCellFile.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_artifact_web_format import BIMFileExtractionItemArtifactWebFormat

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemArtifactWebFormat from a JSON string
bim_file_extraction_item_artifact_web_format_instance = BIMFileExtractionItemArtifactWebFormat.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemArtifactWebFormat.to_json())

# convert the object into a dict
bim_file_extraction_item_artifact_web_format_dict = bim_file_extraction_item_artifact_web_format_instance.to_dict()
# create an instance of BIMFileExtractionItemArtifactWebFormat from a dict
bim_file_extraction_item_artifact_web_format_from_dict = BIMFileExtractionItemArtifactWebFormat.from_dict(bim_file_extraction_item_artifact_web_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


