# CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_upload_uuid** | **str** | UUID of uploaded snapshot | 
**snapshot** | **str** | File to use as image data. Note that it&#39;s only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use snapshot_upload_uuid. You should not use both file and upload_uuid fields in the same request. | [optional] 
**name** | **str** | Viewpoint name | [optional] 
**camera_data** | **str** | Camera data for the building model associated with the issue | 
**redlines_data** | **str** | Lines data for the building model associated with the issue | [optional] 
**sections_data** | **str** | Clipping plane data for the building model associated with the issue | [optional] 

## Example

```python
from procore_sdk.models.coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner import CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner from a JSON string
coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner_instance = CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner.from_json(json)
# print the JSON string representation of the object
print(CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner.to_json())

# convert the object into a dict
coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner_dict = coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner_instance.to_dict()
# create an instance of CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner from a dict
coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner_from_dict = CoordinationIssueSyncResponseErrorsInnerAllOfViewpointsInner.from_dict(coordination_issue_sync_response_errors_inner_all_of_viewpoints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


