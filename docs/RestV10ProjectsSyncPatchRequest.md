# RestV10ProjectsSyncPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The company identifier the project is associated with. Required only if &#x60;company_id&#x60; is not included in the request&#39;s query parameters. | 
**updates** | [**List[RestV10ProjectsSyncPatchRequestUpdatesInner]**](RestV10ProjectsSyncPatchRequestUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_sync_patch_request import RestV10ProjectsSyncPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsSyncPatchRequest from a JSON string
rest_v10_projects_sync_patch_request_instance = RestV10ProjectsSyncPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsSyncPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_sync_patch_request_dict = rest_v10_projects_sync_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsSyncPatchRequest from a dict
rest_v10_projects_sync_patch_request_from_dict = RestV10ProjectsSyncPatchRequest.from_dict(rest_v10_projects_sync_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


