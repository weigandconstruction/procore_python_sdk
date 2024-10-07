# DrawingSet1

Drawing Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Set ID | [optional] 
**project_id** | **int** | Drawing Set project ID | [optional] 
**name** | **str** | Drawing Set name | [optional] 
**created_at** | **datetime** | Drawing Set created at | [optional] 
**updated_at** | **datetime** | Drawing Set updated at | [optional] 
**var_date** | **date** | Drawing Set date | [optional] 
**position** | **int** | Drawing Set position | [optional] 
**drawing_revisions_count** | **int** | Amount of Drawing Revisions | [optional] 

## Example

```python
from procore_sdk.models.drawing_set1 import DrawingSet1

# TODO update the JSON string below
json = "{}"
# create an instance of DrawingSet1 from a JSON string
drawing_set1_instance = DrawingSet1.from_json(json)
# print the JSON string representation of the object
print(DrawingSet1.to_json())

# convert the object into a dict
drawing_set1_dict = drawing_set1_instance.to_dict()
# create an instance of DrawingSet1 from a dict
drawing_set1_from_dict = DrawingSet1.from_dict(drawing_set1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


