# RestV10BimViewpointsPost201ResponseOneOf


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
**sections_data** | **str** | JSON string representation of sections applied to a 3d model | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_viewpoints_post201_response_one_of import RestV10BimViewpointsPost201ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimViewpointsPost201ResponseOneOf from a JSON string
rest_v10_bim_viewpoints_post201_response_one_of_instance = RestV10BimViewpointsPost201ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimViewpointsPost201ResponseOneOf.to_json())

# convert the object into a dict
rest_v10_bim_viewpoints_post201_response_one_of_dict = rest_v10_bim_viewpoints_post201_response_one_of_instance.to_dict()
# create an instance of RestV10BimViewpointsPost201ResponseOneOf from a dict
rest_v10_bim_viewpoints_post201_response_one_of_from_dict = RestV10BimViewpointsPost201ResponseOneOf.from_dict(rest_v10_bim_viewpoints_post201_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


