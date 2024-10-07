# RestV10TaskItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_item** | [**RestV10TaskItemsPostRequestTaskItem**](RestV10TaskItemsPostRequestTaskItem.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_task_items_post_request import RestV10TaskItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaskItemsPostRequest from a JSON string
rest_v10_task_items_post_request_instance = RestV10TaskItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TaskItemsPostRequest.to_json())

# convert the object into a dict
rest_v10_task_items_post_request_dict = rest_v10_task_items_post_request_instance.to_dict()
# create an instance of RestV10TaskItemsPostRequest from a dict
rest_v10_task_items_post_request_from_dict = RestV10TaskItemsPostRequest.from_dict(rest_v10_task_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


