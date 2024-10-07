# RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner import RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner from a JSON string
rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner_instance = RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner.to_json())

# convert the object into a dict
rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner_dict = rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner_instance.to_dict()
# create an instance of RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner from a dict
rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner_from_dict = RestV10SubmittalApproversIdPatch200ResponseInnerAttachmentsInner.from_dict(rest_v10_submittal_approvers_id_patch200_response_inner_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


