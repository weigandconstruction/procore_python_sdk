# DrawingRevisionDiscipline

Drawing discipline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Discipline ID | [optional] 
**name** | **str** | Discipline name | [optional] 
**position** | **int** | Discipline position | [optional] 

## Example

```python
from procore_sdk.models.drawing_revision_discipline import DrawingRevisionDiscipline

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingRevisionDiscipline from a JSON string
drawing_revision_discipline_instance = DrawingRevisionDiscipline.from_json(json)
# print the JSON string representation of the object
print(DrawingRevisionDiscipline.to_json())

# convert the object into a dict
drawing_revision_discipline_dict = drawing_revision_discipline_instance.to_dict()
# create an instance of DrawingRevisionDiscipline from a dict
drawing_revision_discipline_from_dict = DrawingRevisionDiscipline.from_dict(drawing_revision_discipline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


