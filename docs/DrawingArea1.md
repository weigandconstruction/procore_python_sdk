# DrawingArea1

Drawing Area

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Area ID | [optional] 
**name** | **str** | Drawing Area name | [optional] 
**drawings_count** | **int** | Amount of Drawings | [optional] 
**description** | **str** | Drawing Area Description | [optional] 
**drawing_sets** | [**List[DrawingSet1]**](DrawingSet1.md) | Array of Drawing Sets | [optional] 
**drawing_disciplines** | [**List[DrawingArea1DrawingDisciplinesInner]**](DrawingArea1DrawingDisciplinesInner.md) | Array of Drawing Disciplines | [optional] 

## Example

```python
from procore_sdk.models.drawing_area1 import DrawingArea1

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingArea1 from a JSON string
drawing_area1_instance = DrawingArea1.from_json(json)
# print the JSON string representation of the object
print(DrawingArea1.to_json())

# convert the object into a dict
drawing_area1_dict = drawing_area1_instance.to_dict()
# create an instance of DrawingArea1 from a dict
drawing_area1_from_dict = DrawingArea1.from_dict(drawing_area1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


