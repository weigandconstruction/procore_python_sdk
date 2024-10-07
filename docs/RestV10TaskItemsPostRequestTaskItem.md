# RestV10TaskItemsPostRequestTaskItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**number** | **str** | Number | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **datetime** | Date and time due | [optional] 
**status** | **str** | Status | [optional] 
**task_item_category_id** | **int** | The task item category to associate with the task item. | [optional] 
**private** | **bool** | Privacy flag | [optional] 
**assigned_id** | **int** | Assignee ID | [optional] 
**assignee_ids** | **List[int]** | Assignee IDs | [optional] 
**attachments** | **List[str]** | Task Item attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_task_items_post_request_task_item import RestV10TaskItemsPostRequestTaskItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaskItemsPostRequestTaskItem from a JSON string
rest_v10_task_items_post_request_task_item_instance = RestV10TaskItemsPostRequestTaskItem.from_json(json)
# print the JSON string representation of the object
print(RestV10TaskItemsPostRequestTaskItem.to_json())

# convert the object into a dict
rest_v10_task_items_post_request_task_item_dict = rest_v10_task_items_post_request_task_item_instance.to_dict()
# create an instance of RestV10TaskItemsPostRequestTaskItem from a dict
rest_v10_task_items_post_request_task_item_from_dict = RestV10TaskItemsPostRequestTaskItem.from_dict(rest_v10_task_items_post_request_task_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


