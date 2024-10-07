# RFIUpdateBody1RfiQuestion

The Question of the RFI

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The Body of the Question | 
**attachments** | **List[str]** | RFI&#39;s Attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 

## Example

```python
from procore_sdk.models.rfi_update_body1_rfi_question import RFIUpdateBody1RfiQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of RFIUpdateBody1RfiQuestion from a JSON string
rfi_update_body1_rfi_question_instance = RFIUpdateBody1RfiQuestion.from_json(json)
# print the JSON string representation of the object
print(RFIUpdateBody1RfiQuestion.to_json())

# convert the object into a dict
rfi_update_body1_rfi_question_dict = rfi_update_body1_rfi_question_instance.to_dict()
# create an instance of RFIUpdateBody1RfiQuestion from a dict
rfi_update_body1_rfi_question_from_dict = RFIUpdateBody1RfiQuestion.from_dict(rfi_update_body1_rfi_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


