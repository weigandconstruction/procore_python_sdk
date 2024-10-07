# RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**item_id** | **int** | The ID of the parent item this document belongs to | 
**item_type** | **str** | The type of the parent item this document belongs to (eg SubmittalLog) | 
**attachment_id** | **int** |  | 

## Example

```python
from procore_sdk.models.rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request import RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest from a JSON string
rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request_instance = RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest.to_json())

# convert the object into a dict
rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request_dict = rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request_instance.to_dict()
# create an instance of RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest from a dict
rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request_from_dict = RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest.from_dict(rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


