# ChecklistListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**details** | **str** | Details | [optional] 
**company_template_item_details** | **str** | Details from the company template item | [optional] 
**item_response** | [**ChecklistItemResponse1**](ChecklistItemResponse1.md) |  | [optional] 
**list_id** | **int** | List ID | [optional] 
**name** | **str** | Name | [optional] 
**position** | **int** | Position | [optional] 
**responded_with** | **str** | Representation of an Item&#39;s Response | [optional] 
**response** | [**ChecklistResponse1**](ChecklistResponse1.md) |  | [optional] 
**response_set** | [**ChecklistItemResponseSet2**](ChecklistItemResponseSet2.md) |  | [optional] 
**section_id** | **int** | Checklist Section ID | [optional] 
**status** | **str** | Status | [optional] 
**template_item_id** | **int** | Template Item ID | [optional] 
**type** | [**ChecklistItemType**](ChecklistItemType.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.checklist_list_item import ChecklistListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistListItem from a JSON string
checklist_list_item_instance = ChecklistListItem.from_json(json)
# print the JSON string representation of the object
print(ChecklistListItem.to_json())

# convert the object into a dict
checklist_list_item_dict = checklist_list_item_instance.to_dict()
# create an instance of ChecklistListItem from a dict
checklist_list_item_from_dict = ChecklistListItem.from_dict(checklist_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


