# RestV10ProjectsProjectIdSpecificationUploadsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_set_id** | **int** | The ID of the specification set to upload to | 
**specification_section_id** | **int** | The ID of a Specification Section to apply to all pages in the attached file. If present, the upload will not require review unless the Specification Section is deleted during processing. | [optional] 
**default_revision** | **str** | A default revision designation to be applied to Specification Section Revisions generated from this upload | [optional] 
**files** | **List[str]** | One or more files in PDF format to include in the upload (limited to one if specification_section_id is set). *To upload drawings you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;files[]&#x60; as files. *Required only if upload_uuids is empty | [optional] 
**upload_uuids** | **List[str]** | Array of uploaded files UUIDs. *Required only if files is empty | [optional] 
**issued_date** | **str** | The date when the specifications were issued by the design team | [optional] 
**received_date** | **str** | The date when the specifications were received by the GC | [optional] 
**ignore_number** | **str** | Numbers that resemble a spec section number can make it difficult to accurately split up and auto-label the spec sections. This field contains a number flagged to be ignored by the OCR technology and therefore not read as a spec section number, which should improve upload results | [optional] 
**spec_format** | **str** | Specification format to apply to the upload. | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_post_request import RestV10ProjectsProjectIdSpecificationUploadsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdSpecificationUploadsPostRequest from a JSON string
rest_v10_projects_project_id_specification_uploads_post_request_instance = RestV10ProjectsProjectIdSpecificationUploadsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdSpecificationUploadsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_specification_uploads_post_request_dict = rest_v10_projects_project_id_specification_uploads_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdSpecificationUploadsPostRequest from a dict
rest_v10_projects_project_id_specification_uploads_post_request_from_dict = RestV10ProjectsProjectIdSpecificationUploadsPostRequest.from_dict(rest_v10_projects_project_id_specification_uploads_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


