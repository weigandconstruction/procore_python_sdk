# DrawingArea1DrawingDisciplinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Discipline ID | [optional] 
**name** | **str** | Drawing Discipline name | [optional] 
**position** | **int** | Drawing Discipline position | [optional] 

## Example

```python
from procore_sdk.models.drawing_area1_drawing_disciplines_inner import DrawingArea1DrawingDisciplinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingArea1DrawingDisciplinesInner from a JSON string
drawing_area1_drawing_disciplines_inner_instance = DrawingArea1DrawingDisciplinesInner.from_json(json)
# print the JSON string representation of the object
print(DrawingArea1DrawingDisciplinesInner.to_json())

# convert the object into a dict
drawing_area1_drawing_disciplines_inner_dict = drawing_area1_drawing_disciplines_inner_instance.to_dict()
# create an instance of DrawingArea1DrawingDisciplinesInner from a dict
drawing_area1_drawing_disciplines_inner_from_dict = DrawingArea1DrawingDisciplinesInner.from_dict(drawing_area1_drawing_disciplines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


