# RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo

Params used only when forwarding for review. Designates who the new reviewer is and what their due date is

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID of the new reviewer | 
**due_date** | **date** | Due Date of the new reviewer | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to import RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo from a JSON string
rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to_instance = RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo.to_json())

# convert the object into a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to_dict = rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to_instance.to_dict()
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo from a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to_from_dict = RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo.from_dict(rest_v10_submittal_approvers_id_patch_request_submittal_approver_forward_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


