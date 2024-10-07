# procore_sdk.ProjectManagementModelsBIMFileExtractionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_file_extractions_get**](ProjectManagementModelsBIMFileExtractionsApi.md#rest_v10_bim_file_extractions_get) | **GET** /rest/v1.0/bim_file_extractions | List BIM File Extractions
[**rest_v10_bim_file_extractions_id_get**](ProjectManagementModelsBIMFileExtractionsApi.md#rest_v10_bim_file_extractions_id_get) | **GET** /rest/v1.0/bim_file_extractions/{id} | Show BIM File Extraction


# **rest_v10_bim_file_extractions_get**
> List[BIMFileExtraction] rest_v10_bim_file_extractions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_extraction_format=filters_extraction_format, filters_bim_file_id=filters_bim_file_id, filters_bim_file_upload_id=filters_bim_file_upload_id, filters_file_version_id=filters_file_version_id, filters_document_upload_id=filters_document_upload_id)

List BIM File Extractions

Return a list of all BIM File Extractions A BIM File Extraction can fail for several reasons. When it does, the errors attribute contains a list of errors encountered while processing the model. The following table lists the possible error codes and types.  #### Error Types  | Code | Type                   | |------|------------------------| | 1    | Undefined              | | 2    | NetworkErr             | | 3    | ServerErr              | | 4    | JsonParseErr           | | 5    | TokenExpiredErr        | | 6    | FileOpenErr            | | 7    | FileWriteErr           | | 8    | FileCompressionErr     | | 9    | FileUploadError        | | 10   | ModelReadErr           | | 11   | ModelFileSizeErr       | | 12   | ModelExportErr         | | 13   | ModelEmptyDBErr        | | 14   | ModelViewpointErr      | | 15   | ModelErr               | | 16   | InvalidStatusError     | | 17   | FileDecompressionErr   | | 18   | UnsupportedFileFormat  | | 19   | No3DGeometry           | | 20   | InvalidInputError      | | 21   | UnsupportedFileSource  | | 22   | MeshNodeLimitError     | | 23   | RateLimitExhausted     | | 24   | ODAGenericError        | | 25   | FileUploadFasError     | 

### Example


```python
import procore_sdk
from procore_sdk.models.bim_file_extraction import BIMFileExtraction
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFileExtractionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_status = 'filters_status_example' # str | Filter item(s) with matching status (optional)
    filters_extraction_format = ['filters_extraction_format_example'] # List[str] | Filter item(s) with matching extraction format (optional)
    filters_bim_file_id = [56] # List[int] | Return item(s) with the specified bim_file_id in bim_file_upload (optional)
    filters_bim_file_upload_id = [56] # List[int] | Return item(s) with the specified bim_file_upload_id (optional)
    filters_file_version_id = [56] # List[int] | Return item(s) with the specified file_version_id in bim_file_upload (optional)
    filters_document_upload_id = ['filters_document_upload_id_example'] # List[str] | Return item(s) with the specified document_upload_id in bim_file_upload (optional)

    try:
        # List BIM File Extractions
        api_response = api_instance.rest_v10_bim_file_extractions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_extraction_format=filters_extraction_format, filters_bim_file_id=filters_bim_file_id, filters_bim_file_upload_id=filters_bim_file_upload_id, filters_file_version_id=filters_file_version_id, filters_document_upload_id=filters_document_upload_id)
        print("The response of ProjectManagementModelsBIMFileExtractionsApi->rest_v10_bim_file_extractions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFileExtractionsApi->rest_v10_bim_file_extractions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_status** | **str**| Filter item(s) with matching status | [optional] 
 **filters_extraction_format** | [**List[str]**](str.md)| Filter item(s) with matching extraction format | [optional] 
 **filters_bim_file_id** | [**List[int]**](int.md)| Return item(s) with the specified bim_file_id in bim_file_upload | [optional] 
 **filters_bim_file_upload_id** | [**List[int]**](int.md)| Return item(s) with the specified bim_file_upload_id | [optional] 
 **filters_file_version_id** | [**List[int]**](int.md)| Return item(s) with the specified file_version_id in bim_file_upload | [optional] 
 **filters_document_upload_id** | [**List[str]**](str.md)| Return item(s) with the specified document_upload_id in bim_file_upload | [optional] 

### Return type

[**List[BIMFileExtraction]**](BIMFileExtraction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_file_extractions_id_get**
> BIMFileExtraction rest_v10_bim_file_extractions_id_get(procore_company_id, id, project_id)

Show BIM File Extraction

Return a single BIM File Extraction

### Example


```python
import procore_sdk
from procore_sdk.models.bim_file_extraction import BIMFileExtraction
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFileExtractionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show BIM File Extraction
        api_response = api_instance.rest_v10_bim_file_extractions_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementModelsBIMFileExtractionsApi->rest_v10_bim_file_extractions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFileExtractionsApi->rest_v10_bim_file_extractions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**BIMFileExtraction**](BIMFileExtraction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

