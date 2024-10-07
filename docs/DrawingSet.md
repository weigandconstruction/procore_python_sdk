# DrawingSet

Drawing Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Set ID | [optional] 
**project_id** | **int** | Drawing Set project ID | [optional] 
**company_id** | **int** | Drawing Set company ID | [optional] 
**name** | **str** | Drawing Set name | [optional] 
**created_at** | **datetime** | Drawing Set created at | [optional] 
**updated_at** | **datetime** | Drawing Set updated at | [optional] 
**var_date** | **date** | Drawing Set date | [optional] 
**position** | **int** | Drawing Set position | [optional] 

## Example

```python
from procore_sdk.models.drawing_set import DrawingSet

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingSet from a JSON string
drawing_set_instance = DrawingSet.from_json(json)
# print the JSON string representation of the object
print(DrawingSet.to_json())

# convert the object into a dict
drawing_set_dict = drawing_set_instance.to_dict()
# create an instance of DrawingSet from a dict
drawing_set_from_dict = DrawingSet.from_dict(drawing_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


