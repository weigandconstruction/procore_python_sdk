# ChecklistComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**body** | **str** | Comment body | [optional] 
**item_id** | **int** | Checklist Item ID | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**created_by** | [**ChecklistCommentCreatedBy**](ChecklistCommentCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_comment import ChecklistComment

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistComment from a JSON string
checklist_comment_instance = ChecklistComment.from_json(json)
# print the JSON string representation of the object
print(ChecklistComment.to_json())

# convert the object into a dict
checklist_comment_dict = checklist_comment_instance.to_dict()
# create an instance of ChecklistComment from a dict
checklist_comment_from_dict = ChecklistComment.from_dict(checklist_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


