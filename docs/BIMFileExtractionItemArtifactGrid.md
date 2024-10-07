# BIMFileExtractionItemArtifactGrid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**coordinate_system** | **str** |  | [optional] 
**gridline_file** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_artifact_grid import BIMFileExtractionItemArtifactGrid

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemArtifactGrid from a JSON string
bim_file_extraction_item_artifact_grid_instance = BIMFileExtractionItemArtifactGrid.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemArtifactGrid.to_json())

# convert the object into a dict
bim_file_extraction_item_artifact_grid_dict = bim_file_extraction_item_artifact_grid_instance.to_dict()
# create an instance of BIMFileExtractionItemArtifactGrid from a dict
bim_file_extraction_item_artifact_grid_from_dict = BIMFileExtractionItemArtifactGrid.from_dict(bim_file_extraction_item_artifact_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


