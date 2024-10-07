# Body104CoordinationIssueViewpointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Viewpoint name | [optional] 
**view_folder_id** | **int** | ID of the BIM View Folder the viewpoint belongs to | [optional] 
**snapshot_upload_uuid** | **str** | UUID of uploaded snapshot | 
**camera_data** | **str** | JSON string representation of camera position | 
**redlines_data** | **str** | JSON string representation of markup | [optional] 
**sections_data** | **str** | JSON string representation of sections applied to a 3d model as a bounding box | [optional] 
**render_mode** | **str** | Viewer render mode when viewpoint is applied | [optional] 
**visibility** | [**Body104CoordinationIssueViewpointsInnerVisibility**](Body104CoordinationIssueViewpointsInnerVisibility.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body104_coordination_issue_viewpoints_inner import Body104CoordinationIssueViewpointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body104CoordinationIssueViewpointsInner from a JSON string
body104_coordination_issue_viewpoints_inner_instance = Body104CoordinationIssueViewpointsInner.from_json(json)
# print the JSON string representation of the object
print(Body104CoordinationIssueViewpointsInner.to_json())

# convert the object into a dict
body104_coordination_issue_viewpoints_inner_dict = body104_coordination_issue_viewpoints_inner_instance.to_dict()
# create an instance of Body104CoordinationIssueViewpointsInner from a dict
body104_coordination_issue_viewpoints_inner_from_dict = Body104CoordinationIssueViewpointsInner.from_dict(body104_coordination_issue_viewpoints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


