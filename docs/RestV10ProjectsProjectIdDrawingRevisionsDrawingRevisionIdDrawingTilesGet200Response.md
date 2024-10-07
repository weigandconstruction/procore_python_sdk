# RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_zoom_level** | **int** | Max zoom level | [optional] 
**tile_size** | **List[int]** | Array of tile width and height | [optional] 
**zip_url** | **str** | ZIP url | [optional] 
**tiles** | [**List[DrawingTile]**](DrawingTile.md) | Array of drawing tiles | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response import RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response from a JSON string
rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response_instance = RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response_dict = rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response from a dict
rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response_from_dict = RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response.from_dict(rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


