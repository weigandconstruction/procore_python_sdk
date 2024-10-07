# DrawingRevisionTermSet

Drawing Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drawing_revision_id** | **int** | Revision ID | [optional] 
**updated_at** | **datetime** | Revision term coordinates updated at | [optional] 
**terms** | **Dict[str, List[DrawingRevisionTermSetTermsValueInner]]** |  | [optional] 

## Example

```python
from procore_sdk.models.drawing_revision_term_set import DrawingRevisionTermSet

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingRevisionTermSet from a JSON string
drawing_revision_term_set_instance = DrawingRevisionTermSet.from_json(json)
# print the JSON string representation of the object
print(DrawingRevisionTermSet.to_json())

# convert the object into a dict
drawing_revision_term_set_dict = drawing_revision_term_set_instance.to_dict()
# create an instance of DrawingRevisionTermSet from a dict
drawing_revision_term_set_from_dict = DrawingRevisionTermSet.from_dict(drawing_revision_term_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


