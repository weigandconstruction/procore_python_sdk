# RestV10SubmittalApproversIdPatchRequestSubmittalApprover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments_to_upload** | **List[str]** | Submittal Approver&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments_to_upload[]&#x60; as files. | [optional] 
**attachment_ids** | **List[int]** | Submittal Approver&#39;s Attachment IDs. The Attachments specified here will be saved as attachments through the request. | [optional] 
**comment** | **str** |  | [optional] 
**submittal_response_id** | **int** |  | 
**sent_date** | **str** | Parameter is only available to admins. | [optional] 
**returned_date** | **str** | Parameter is only available to admins. | [optional] 
**forward_to** | [**RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo**](RestV10SubmittalApproversIdPatchRequestSubmittalApproverForwardTo.md) |  | [optional] 
**associated_attachments** | [**List[RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner]**](RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner.md) | Submital Approver&#39;s Attachments to be carried forward. The Attachments specified here will be carried forward to the next person in the workflow. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request_submittal_approver import RestV10SubmittalApproversIdPatchRequestSubmittalApprover

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApprover from a JSON string
rest_v10_submittal_approvers_id_patch_request_submittal_approver_instance = RestV10SubmittalApproversIdPatchRequestSubmittalApprover.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalApproversIdPatchRequestSubmittalApprover.to_json())

# convert the object into a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_dict = rest_v10_submittal_approvers_id_patch_request_submittal_approver_instance.to_dict()
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApprover from a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_from_dict = RestV10SubmittalApproversIdPatchRequestSubmittalApprover.from_dict(rest_v10_submittal_approvers_id_patch_request_submittal_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


