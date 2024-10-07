# DrawingRevision

Drawing Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drawing_date** | **date** | Drawing date | [optional] 
**received_date** | **date** | Received date | [optional] 
**revision_number** | **str** | Revision number | [optional] 
**floorplan** | **bool** | Revision floorplan status | [optional] 
**drawing_set_id** | **int** | Drawing Set ID | [optional] 
**drawing_id** | **int** | Drawing ID | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_revision import DrawingRevision

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingRevision from a JSON string
drawing_revision_instance = DrawingRevision.from_json(json)
# print the JSON string representation of the object
print(DrawingRevision.to_json())

# convert the object into a dict
drawing_revision_dict = drawing_revision_instance.to_dict()
# create an instance of DrawingRevision from a dict
drawing_revision_from_dict = DrawingRevision.from_dict(drawing_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


