# RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_file_id** | **int** | ID of associated BIM File | [optional] 
**view_folder_id** | **int** | ID of associated BIM View Folder | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**snapshot** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot.md) |  | [optional] 
**name** | **str** | Viewpoint name | [optional] 
**render_mode** | **str** | Viewer render mode when viewpoint is applied | [optional] 
**visibility** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibility**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfVisibility.md) |  | [optional] 
**camera_data** | **str** | JSON string representation of camera position | [optional] 
**redlines_data** | **str** | JSON string representation of markup | [optional] 
**sections_data** | **str** | JSON string representation of sections applied to a 3d model as a set of clipping planes | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_dict = rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


