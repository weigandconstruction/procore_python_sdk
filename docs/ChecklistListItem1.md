# ChecklistListItem1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**details** | **str** | Details | [optional] 
**item_response** | [**ChecklistItemResponse1**](ChecklistItemResponse1.md) |  | [optional] 
**list_id** | **int** | List ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**responded_with** | **str** | Representation of an Item&#39;s Response | [optional] 
**response** | [**ChecklistResponse1**](ChecklistResponse1.md) |  | [optional] 
**response_set** | [**ChecklistListItem1ResponseSet**](ChecklistListItem1ResponseSet.md) |  | [optional] 
**response_type_id** | **int** | Response Type ID | [optional] 
**section_id** | **int** | Checklist Section ID | [optional] 
**status** | **str** | Status | [optional] 
**template_item_id** | **int** | Template Item ID | [optional] 
**type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_item1 import ChecklistListItem1

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListItem1 from a JSON string
checklist_list_item1_instance = ChecklistListItem1.from_json(json)
# print the JSON string representation of the object
print(ChecklistListItem1.to_json())

# convert the object into a dict
checklist_list_item1_dict = checklist_list_item1_instance.to_dict()
# create an instance of ChecklistListItem1 from a dict
checklist_list_item1_from_dict = ChecklistListItem1.from_dict(checklist_list_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


