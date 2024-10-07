# RestV10RequestedChangesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_changes** | [**List[RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner]**](RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requested_changes_get200_response import RestV10RequestedChangesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequestedChangesGet200Response from a JSON string
rest_v10_requested_changes_get200_response_instance = RestV10RequestedChangesGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10RequestedChangesGet200Response.to_json())

# convert the object into a dict
rest_v10_requested_changes_get200_response_dict = rest_v10_requested_changes_get200_response_instance.to_dict()
# create an instance of RestV10RequestedChangesGet200Response from a dict
rest_v10_requested_changes_get200_response_from_dict = RestV10RequestedChangesGet200Response.from_dict(rest_v10_requested_changes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


