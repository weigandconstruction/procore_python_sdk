# ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner

Normal view of task item assignee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Email | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**date_notified** | **date** | Date when the notification was sent for each assignee | [optional] 

## Example

```python
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner import ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner from a JSON string
array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner_instance = ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner.to_json())

# convert the object into a dict
array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner_dict = array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner_instance.to_dict()
# create an instance of ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner from a dict
array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner_from_dict = ArrayOfTaskItemsThatWereSentOutInnerAllOfAssigneesInner.from_dict(array_of_task_items_that_were_sent_out_inner_all_of_assignees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


