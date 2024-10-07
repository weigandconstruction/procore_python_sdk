# ArrayOfTaskItemsThatWereSentOutInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number | [optional] 
**date_notified** | **date** | Date when the notification was sent | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Date and time due | [optional] 
**status** | **str** | Status | [optional] 
**private** | **bool** |  | [optional] 
**task_item_category** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfTaskItemCategory**](ArrayOfTaskItemsThatWereSentOutInnerAllOfTaskItemCategory.md) |  | [optional] 
**assignee** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**assignees** | [**List[ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner]**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner.md) |  | [optional] 
**id** | **int** | ID | [optional] 
**title** | **str** | Title | [optional] 

## Example

```python
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner import ArrayOfTaskItemsThatWereSentOutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskItemsThatWereSentOutInner from a JSON string
array_of_task_items_that_were_sent_out_inner_instance = ArrayOfTaskItemsThatWereSentOutInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfTaskItemsThatWereSentOutInner.to_json())

# convert the object into a dict
array_of_task_items_that_were_sent_out_inner_dict = array_of_task_items_that_were_sent_out_inner_instance.to_dict()
# create an instance of ArrayOfTaskItemsThatWereSentOutInner from a dict
array_of_task_items_that_were_sent_out_inner_from_dict = ArrayOfTaskItemsThatWereSentOutInner.from_dict(array_of_task_items_that_were_sent_out_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


