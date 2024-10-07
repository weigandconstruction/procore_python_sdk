# DrawingRevision1

Drawing Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Revision ID | [optional] 
**drawing_date** | **date** | Drawing date | [optional] 
**received_date** | **date** | Received date | [optional] 
**revision_number** | **str** | Revision number | [optional] 
**floorplan** | **bool** | Revision floorplan status | [optional] 
**current** | **bool** | Current Drawing Revision | [optional] 
**drawing_id** | **int** | Drawing ID | [optional] 
**drawing_set** | [**DrawingRevisionDrawingSet**](DrawingRevisionDrawingSet.md) |  | [optional] 
**ordered_revision_ids** | **List[int]** | Ordered array of the complete list of reviewed and published Drawing Revision IDs that belong to the drawing | [optional] 
**custom_fields** | [**DrawingRevisionCustomFields**](DrawingRevisionCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_revision1 import DrawingRevision1

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingRevision1 from a JSON string
drawing_revision1_instance = DrawingRevision1.from_json(json)
# print the JSON string representation of the object
print(DrawingRevision1.to_json())

# convert the object into a dict
drawing_revision1_dict = drawing_revision1_instance.to_dict()
# create an instance of DrawingRevision1 from a dict
drawing_revision1_from_dict = DrawingRevision1.from_dict(drawing_revision1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


