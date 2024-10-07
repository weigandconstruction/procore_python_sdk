# DrawingTile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Tile ID | [optional] 
**x** | **int** | Tile X | [optional] 
**y** | **int** | Tile Y | [optional] 
**z** | **int** | Zoom level | [optional] 
**url** | **str** | This has been deprecated. | [optional] 

## Example

```python
from procore_sdk.models.drawing_tile import DrawingTile

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingTile from a JSON string
drawing_tile_instance = DrawingTile.from_json(json)
# print the JSON string representation of the object
print(DrawingTile.to_json())

# convert the object into a dict
drawing_tile_dict = drawing_tile_instance.to_dict()
# create an instance of DrawingTile from a dict
drawing_tile_from_dict = DrawingTile.from_dict(drawing_tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


