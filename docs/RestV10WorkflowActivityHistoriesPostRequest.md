# RestV10WorkflowActivityHistoriesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_activity_history** | [**WorkflowActivityHistory**](WorkflowActivityHistory.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_workflow_activity_histories_post_request import RestV10WorkflowActivityHistoriesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkflowActivityHistoriesPostRequest from a JSON string
rest_v10_workflow_activity_histories_post_request_instance = RestV10WorkflowActivityHistoriesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkflowActivityHistoriesPostRequest.to_json())

# convert the object into a dict
rest_v10_workflow_activity_histories_post_request_dict = rest_v10_workflow_activity_histories_post_request_instance.to_dict()
# create an instance of RestV10WorkflowActivityHistoriesPostRequest from a dict
rest_v10_workflow_activity_histories_post_request_from_dict = RestV10WorkflowActivityHistoriesPostRequest.from_dict(rest_v10_workflow_activity_histories_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


