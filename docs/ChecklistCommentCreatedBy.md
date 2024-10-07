# ChecklistCommentCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company_name** | **str** | User Company name | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.checklist_comment_created_by import ChecklistCommentCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistCommentCreatedBy from a JSON string
checklist_comment_created_by_instance = ChecklistCommentCreatedBy.from_json(json)
# print the JSON string representation of the object
print(ChecklistCommentCreatedBy.to_json())

# convert the object into a dict
checklist_comment_created_by_dict = checklist_comment_created_by_instance.to_dict()
# create an instance of ChecklistCommentCreatedBy from a dict
checklist_comment_created_by_from_dict = ChecklistCommentCreatedBy.from_dict(checklist_comment_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


