# Drawing

Drawing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Drawing number | 
**title** | **str** | Drawing title | [optional] 
**drawing_discipline** | [**DrawingDrawingDiscipline**](DrawingDrawingDiscipline.md) |  | 

## Example

```python
from procore_sdk.models.drawing import Drawing

# TODO update the JSON string below
json = "{}"
# create an instance of Drawing from a JSON string
drawing_instance = Drawing.from_json(json)
# print the JSON string representation of the object
print(Drawing.to_json())

# convert the object into a dict
drawing_dict = drawing_instance.to_dict()
# create an instance of Drawing from a dict
drawing_from_dict = Drawing.from_dict(drawing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


