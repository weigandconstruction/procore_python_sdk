# procore_sdk.ProjectManagementDocumentMarkupDocumentMarkupApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_document_markup_downloadable_pdfs_find_or_create_post**](ProjectManagementDocumentMarkupDocumentMarkupApi.md#rest_v10_document_markup_downloadable_pdfs_find_or_create_post) | **POST** /rest/v1.0/document_markup_downloadable_pdfs/find_or_create | Show or Create Document Markup Downloadable PDF


# **rest_v10_document_markup_downloadable_pdfs_find_or_create_post**
> RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost200Response rest_v10_document_markup_downloadable_pdfs_find_or_create_post(procore_company_id, rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request, version_datetime=version_datetime)

Show or Create Document Markup Downloadable PDF

Find or Create Document Markup Downloadable PDF. Starts processing to create a downloadable PDF with markup. When completed, the same request will include a download URL for the PDF. item_id, item_type, and attachment_id paramters are the same parameters included in the URL when viewing the attachment in procore. Example: app.procore.com/161072/project/submittal_logs/document_viewer?attachment_id=43&item_id=42&item_type=SubmittalLog&project_id=161072

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_document_markup_downloadable_pdfs_find_or_create_post200_response import RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost200Response
from procore_sdk.models.rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request import RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ProjectManagementDocumentMarkupDocumentMarkupApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request = procore_sdk.RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest() # RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest | 
    version_datetime = 'version_datetime_example' # str | Version Datetime of the Document (optional)

    try:
        # Show or Create Document Markup Downloadable PDF
        api_response = api_instance.rest_v10_document_markup_downloadable_pdfs_find_or_create_post(procore_company_id, rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request, version_datetime=version_datetime)
        print("The response of ProjectManagementDocumentMarkupDocumentMarkupApi->rest_v10_document_markup_downloadable_pdfs_find_or_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDocumentMarkupDocumentMarkupApi->rest_v10_document_markup_downloadable_pdfs_find_or_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_document_markup_downloadable_pdfs_find_or_create_post_request** | [**RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest**](RestV10DocumentMarkupDownloadablePdfsFindOrCreatePostRequest.md)|  | 
 **version_datetime** | **str**| Version Datetime of the Document | [optional] 

### Return type

[**RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost200Response**](RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Markup Downloadable PDF completed and download URL is included in the response. |  -  |
**202** | Document Markup Downloadable PDF job has been created and is processing. |  -  |
**400** | Invalid params submitted |  -  |
**403** | User does not have permission to view Document Markup Downloadable PDF |  -  |
**404** | Document Markup Downloadable PDF not found |  -  |
**409** | Document Markup Downloadable PDF errored |  -  |
**422** | Error updating Document Markup Downloadable PDF |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

