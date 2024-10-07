# RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response

Drawing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing ID | [optional] 
**number** | **str** | Drawing number | [optional] 
**title** | **str** | Drawing title | [optional] 
**obsolete** | **bool** | Obsolete status | [optional] 
**discipline** | **str** | Drawing discipline | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_drawing_areas_drawing_area_id_drawings_post201_response import RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response from a JSON string
rest_v11_drawing_areas_drawing_area_id_drawings_post201_response_instance = RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.to_json())

# convert the object into a dict
rest_v11_drawing_areas_drawing_area_id_drawings_post201_response_dict = rest_v11_drawing_areas_drawing_area_id_drawings_post201_response_instance.to_dict()
# create an instance of RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response from a dict
rest_v11_drawing_areas_drawing_area_id_drawings_post201_response_from_dict = RestV11DrawingAreasDrawingAreaIdDrawingsPost201Response.from_dict(rest_v11_drawing_areas_drawing_area_id_drawings_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


