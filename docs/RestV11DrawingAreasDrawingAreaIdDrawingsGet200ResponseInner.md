# RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner

Drawing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing ID | [optional] 
**discipline** | **str** | Drawing discipline | [optional] 
**number** | **str** | Drawing number | [optional] 
**title** | **str** | Drawing title | [optional] 
**obsolete** | **bool** | Obsolete status | [optional] 
**current_revision** | [**RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision**](RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInnerCurrentRevision.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner import RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner from a JSON string
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_instance = RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_dict = rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_instance.to_dict()
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner from a dict
rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_from_dict = RestV11DrawingAreasDrawingAreaIdDrawingsGet200ResponseInner.from_dict(rest_v11_drawing_areas_drawing_area_id_drawings_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


