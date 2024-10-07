# RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision

Current drawing revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floorplan** | **bool** | Revision floorplan status | [optional] 
**has_drawing_sketches** | **bool** | Revision has drawing sketches status | [optional] 
**id** | **int** | Revision ID | [optional] 
**pdf_size** | **int** | PDF file size | [optional] 
**pdf_url** | **str** | PDF url address | [optional] 
**png_size** | **int** | PNG file size | [optional] 
**png_url** | **str** | PNG url address | [optional] 
**revision_number** | **str** | Revision number | [optional] 
**thumbnail_url** | **str** | Thumbnail url | [optional] 
**large_thumbnail_url** | **str** | Large thumbnail url | [optional] 
**updated_at** | **datetime** | Revision updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision import RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision from a JSON string
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision_instance = RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision.from_json(json)
# print the JSON string representation of the object
print(RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision.to_json())

# convert the object into a dict
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision_dict = rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision_instance.to_dict()
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision from a dict
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision_from_dict = RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision.from_dict(rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_current_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


