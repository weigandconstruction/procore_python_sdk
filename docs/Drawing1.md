# Drawing1

Drawing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Drawing number | [optional] 
**title** | **str** | Drawing title | [optional] 
**obsolete** | **bool** | Obsolete status | [optional] 
**drawing_discipline** | [**Drawing1DrawingDiscipline**](Drawing1DrawingDiscipline.md) |  | [optional] 
**ordered_revision_ids** | **List[int]** | Ordered array of the complete list of reviewed and published Drawing Revision IDs that belong to the drawing | [optional] 

## Example

```python
from procore_sdk.models.drawing1 import Drawing1

# TODO update the JSON string below
json = "{}"
# create an instance of Drawing1 from a JSON string
drawing1_instance = Drawing1.from_json(json)
# print the JSON string representation of the object
print(Drawing1.to_json())

# convert the object into a dict
drawing1_dict = drawing1_instance.to_dict()
# create an instance of Drawing1 from a dict
drawing1_from_dict = Drawing1.from_dict(drawing1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


