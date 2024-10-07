# CoordinationIssueSyncResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[CoordinationIssueSyncResponse1EntitiesInner]**](CoordinationIssueSyncResponse1EntitiesInner.md) |  | [optional] 
**errors** | [**List[RestV10TaxTypesPost400Response]**](RestV10TaxTypesPost400Response.md) |  | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_sync_response1 import CoordinationIssueSyncResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueSyncResponse1 from a JSON string
coordination_issue_sync_response1_instance = CoordinationIssueSyncResponse1.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueSyncResponse1.to_json())

# convert the object into a dict
coordination_issue_sync_response1_dict = coordination_issue_sync_response1_instance.to_dict()
# create an instance of CoordinationIssueSyncResponse1 from a dict
coordination_issue_sync_response1_from_dict = CoordinationIssueSyncResponse1.from_dict(coordination_issue_sync_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


