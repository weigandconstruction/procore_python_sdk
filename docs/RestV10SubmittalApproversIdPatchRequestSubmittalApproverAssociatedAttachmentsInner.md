# RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **int** | Attachment ID | 
**attachment_source_id** | **int** | ID of the resource the Attachment originally belongs to | 
**attachment_source_type** | **str** | Type of the resource the Attachment originally belongs to | 

## Example

```python
from procore_sdk.models.rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner import RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner from a JSON string
rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner_instance = RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner_dict = rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner_instance.to_dict()
# create an instance of RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner from a dict
rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner_from_dict = RestV10SubmittalApproversIdPatchRequestSubmittalApproverAssociatedAttachmentsInner.from_dict(rest_v10_submittal_approvers_id_patch_request_submittal_approver_associated_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


