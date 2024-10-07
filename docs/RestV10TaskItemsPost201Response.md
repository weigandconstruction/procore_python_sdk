# RestV10TaskItemsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Time created | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**updated_at** | **datetime** | Time updated | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
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
from procore_sdk.models.rest_v10_task_items_post201_response import RestV10TaskItemsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaskItemsPost201Response from a JSON string
rest_v10_task_items_post201_response_instance = RestV10TaskItemsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10TaskItemsPost201Response.to_json())

# convert the object into a dict
rest_v10_task_items_post201_response_dict = rest_v10_task_items_post201_response_instance.to_dict()
# create an instance of RestV10TaskItemsPost201Response from a dict
rest_v10_task_items_post201_response_from_dict = RestV10TaskItemsPost201Response.from_dict(rest_v10_task_items_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


