# CoordinationIssueSyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10CoordinationIssuesGet200ResponseInner]**](RestV10CoordinationIssuesGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[CoordinationIssueSyncResponseErrorsInner]**](CoordinationIssueSyncResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_sync_response import CoordinationIssueSyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueSyncResponse from a JSON string
coordination_issue_sync_response_instance = CoordinationIssueSyncResponse.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueSyncResponse.to_json())

# convert the object into a dict
coordination_issue_sync_response_dict = coordination_issue_sync_response_instance.to_dict()
# create an instance of CoordinationIssueSyncResponse from a dict
coordination_issue_sync_response_from_dict = CoordinationIssueSyncResponse.from_dict(coordination_issue_sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


