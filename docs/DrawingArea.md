# DrawingArea

Drawing Area

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Area ID | [optional] 
**name** | **str** | Drawing Area name | [optional] 
**drawings_count** | **int** | Amount of Drawings | [optional] 
**description** | **str** | Drawing Area Description | [optional] 

## Example

```python
from procore_sdk.models.drawing_area import DrawingArea

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingArea from a JSON string
drawing_area_instance = DrawingArea.from_json(json)
# print the JSON string representation of the object
print(DrawingArea.to_json())

# convert the object into a dict
drawing_area_dict = drawing_area_instance.to_dict()
# create an instance of DrawingArea from a dict
drawing_area_from_dict = DrawingArea.from_dict(drawing_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


