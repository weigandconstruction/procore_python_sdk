# Body121BimViewpointOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_file_id** | **int** | ID of a BIM File to be associated to the viewpoint | 
**name** | **str** | Viewpoint name | [optional] 
**view_folder_id** | **int** | ID of the BIM View Folder the viewpoint belongs to | [optional] 
**upload_uuid** | **str** | UUID of uploaded snapshot | 
**camera_data** | **str** | JSON string representation of camera position | 
**redlines_data** | **str** | JSON string representation of markup | [optional] 
**sections_data** | **str** | JSON string representation of sections applied to a 3d model | [optional] 
**render_mode** | **str** | Viewer render mode when viewpoint is applied | [optional] 
**visibility** | [**Body104CoordinationIssueViewpointsInnerVisibility**](Body104CoordinationIssueViewpointsInnerVisibility.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body121_bim_viewpoint_one_of import Body121BimViewpointOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Body121BimViewpointOneOf from a JSON string
body121_bim_viewpoint_one_of_instance = Body121BimViewpointOneOf.from_json(json)
# print the JSON string representation of the object
print(Body121BimViewpointOneOf.to_json())

# convert the object into a dict
body121_bim_viewpoint_one_of_dict = body121_bim_viewpoint_one_of_instance.to_dict()
# create an instance of Body121BimViewpointOneOf from a dict
body121_bim_viewpoint_one_of_from_dict = Body121BimViewpointOneOf.from_dict(body121_bim_viewpoint_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


