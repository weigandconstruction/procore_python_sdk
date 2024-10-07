# BIMFileExtractionItemArtifact

Artifact extracted from a 3d model. Only one of grid, mobile_format, properties, web_format, ifc, object_search, and viewpoint_collection will have data associated to the artifact extracted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grid** | [**BIMFileExtractionItemArtifactGrid**](BIMFileExtractionItemArtifactGrid.md) |  | [optional] 
**mobile_format** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**properties** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**web_format** | [**BIMFileExtractionItemArtifactWebFormat**](BIMFileExtractionItemArtifactWebFormat.md) |  | [optional] 
**ifc** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**object_search** | [**BIMFileExtractionItemArtifactObjectSearch**](BIMFileExtractionItemArtifactObjectSearch.md) |  | [optional] 
**viewpoint_collection** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_file_extraction_item_artifact import BIMFileExtractionItemArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileExtractionItemArtifact from a JSON string
bim_file_extraction_item_artifact_instance = BIMFileExtractionItemArtifact.from_json(json)
# print the JSON string representation of the object
print(BIMFileExtractionItemArtifact.to_json())

# convert the object into a dict
bim_file_extraction_item_artifact_dict = bim_file_extraction_item_artifact_instance.to_dict()
# create an instance of BIMFileExtractionItemArtifact from a dict
bim_file_extraction_item_artifact_from_dict = BIMFileExtractionItemArtifact.from_dict(bim_file_extraction_item_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


