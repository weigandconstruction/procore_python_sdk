# RestV10SubmittalApproversIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submittal_approver** | [**RestV10SubmittalApproversIdPatchRequestSubmittalApprover**](RestV10SubmittalApproversIdPatchRequestSubmittalApprover.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request import RestV10SubmittalApproversIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalApproversIdPatchRequest from a JSON string
rest_v10_submittal_approvers_id_patch_request_instance = RestV10SubmittalApproversIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalApproversIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_submittal_approvers_id_patch_request_dict = rest_v10_submittal_approvers_id_patch_request_instance.to_dict()
# create an instance of RestV10SubmittalApproversIdPatchRequest from a dict
rest_v10_submittal_approvers_id_patch_request_from_dict = RestV10SubmittalApproversIdPatchRequest.from_dict(rest_v10_submittal_approvers_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


