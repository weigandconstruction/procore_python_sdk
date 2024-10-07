# ChecklistListItem1ResponseSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the response set | [optional] 
**name** | **str** | Name of the response set | [optional] 
**responses** | [**List[ChecklistResponse2]**](ChecklistResponse2.md) |  | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_item1_response_set import ChecklistListItem1ResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListItem1ResponseSet from a JSON string
checklist_list_item1_response_set_instance = ChecklistListItem1ResponseSet.from_json(json)
# print the JSON string representation of the object
print(ChecklistListItem1ResponseSet.to_json())

# convert the object into a dict
checklist_list_item1_response_set_dict = checklist_list_item1_response_set_instance.to_dict()
# create an instance of ChecklistListItem1ResponseSet from a dict
checklist_list_item1_response_set_from_dict = ChecklistListItem1ResponseSet.from_dict(checklist_list_item1_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


