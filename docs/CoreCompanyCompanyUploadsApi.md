# procore_sdk.CoreCompanyCompanyUploadsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_uploads_post**](CoreCompanyCompanyUploadsApi.md#rest_v10_companies_company_id_uploads_post) | **POST** /rest/v1.0/companies/{company_id}/uploads | Create Upload
[**rest_v10_companies_company_id_uploads_uuid_get**](CoreCompanyCompanyUploadsApi.md#rest_v10_companies_company_id_uploads_uuid_get) | **GET** /rest/v1.0/companies/{company_id}/uploads/{uuid} | Show Upload
[**rest_v10_companies_company_id_uploads_uuid_patch**](CoreCompanyCompanyUploadsApi.md#rest_v10_companies_company_id_uploads_uuid_patch) | **PATCH** /rest/v1.0/companies/{company_id}/uploads/{uuid} | Update Upload
[**rest_v11_companies_company_id_uploads_post**](CoreCompanyCompanyUploadsApi.md#rest_v11_companies_company_id_uploads_post) | **POST** /rest/v1.1/companies/{company_id}/uploads | Create Upload
[**rest_v11_companies_company_id_uploads_uuid_get**](CoreCompanyCompanyUploadsApi.md#rest_v11_companies_company_id_uploads_uuid_get) | **GET** /rest/v1.1/companies/{company_id}/uploads/{uuid} | Show Upload
[**rest_v11_companies_company_id_uploads_uuid_patch**](CoreCompanyCompanyUploadsApi.md#rest_v11_companies_company_id_uploads_uuid_patch) | **PATCH** /rest/v1.1/companies/{company_id}/uploads/{uuid} | Update Upload


# **rest_v10_companies_company_id_uploads_post**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v10_companies_company_id_uploads_post(procore_company_id, company_id, response_filename=response_filename, response_content_type=response_content_type, attachment_content_disposition=attachment_content_disposition, segments=segments)

Create Upload

Creating an Upload is the first step in associating a file to a resource in Procore. Creating an Upload can be seen as fetching instruction on how to post your file directly to Procore's storage service.  The instructions contain three properties: a UUID to reference the Upload, a URL which has to be used to post the file, and fields which need to be posted together with the file.  To upload the file you must POST to the URL in the _url_ property with a multipart/form-data body (see RFC 2388). Make sure to include **all** the names and values from _fields_ without altering them. The URL and fields necessary to complete the upload may vary between companies and may also change over time so none of these may be hard-coded. Finally add a field named _file_ with the actual file data.  Uploads are associated to a Company so they can use company specific upload settings. The currently authenticated user will become the owner of the Upload and only that user can use the Upload in subsequent requests.  You will have to initiate the upload within one hour or you can expect a 403 Forbidden response. Other errors are usually clearly explained in the response body.  For an example of how to associate a finalized upload to another resource in Procore see the Photos resource. An Upload will have to be associated to another resource within a week or it will be automatically deleted from Procore servers.  Note that there is also a variant of this API endpoint that works using a Project ID.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
from procore_sdk.models.upload_segments_inner import UploadSegmentsInner
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_filename = 'response_filename_example' # str | By setting a filename you ensure that the storage service knows the filename of the upload. Files are often downloaded directly from the storage service and without the filename they will save on the end users' device without a readable name or extension.  Setting this parameter is optional but highly recommended. (optional)
    response_content_type = 'response_content_type_example' # str | The content-type set through this parameter will be used by the storage service during download just like the response_filename. Setting this value is less important because HTTP clients and operating systems are generally well equipped to determine file types.  Setting this parameter is optional and should only be included when you are certain it's correct or when you want to force a content-type other than what the filename extension suggests. (optional)
    attachment_content_disposition = True # bool | The content type set through this parameter will be used by the storage system during download, similar to the response_filename. When set to true, the file will be downloaded as an attachment. Otherwise, the file content will be rendered inline in the browser. (optional)
    segments = [procore_sdk.UploadSegmentsInner()] # List[UploadSegmentsInner] | Upload segments (optional)

    try:
        # Create Upload
        api_response = api_instance.rest_v10_companies_company_id_uploads_post(procore_company_id, company_id, response_filename=response_filename, response_content_type=response_content_type, attachment_content_disposition=attachment_content_disposition, segments=segments)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_filename** | **str**| By setting a filename you ensure that the storage service knows the filename of the upload. Files are often downloaded directly from the storage service and without the filename they will save on the end users&#39; device without a readable name or extension.  Setting this parameter is optional but highly recommended. | [optional] 
 **response_content_type** | **str**| The content-type set through this parameter will be used by the storage service during download just like the response_filename. Setting this value is less important because HTTP clients and operating systems are generally well equipped to determine file types.  Setting this parameter is optional and should only be included when you are certain it&#39;s correct or when you want to force a content-type other than what the filename extension suggests. | [optional] 
 **attachment_content_disposition** | **bool**| The content type set through this parameter will be used by the storage system during download, similar to the response_filename. When set to true, the file will be downloaded as an attachment. Otherwise, the file content will be rendered inline in the browser. | [optional] 
 **segments** | [**List[UploadSegmentsInner]**](UploadSegmentsInner.md)| Upload segments | [optional] 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_uploads_uuid_get**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v10_companies_company_id_uploads_uuid_get(procore_company_id, company_id, uuid)

Show Upload

Show detailed information on an upload

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    uuid = 'uuid_example' # str | Upload UUID

    try:
        # Show Upload
        api_response = api_instance.rest_v10_companies_company_id_uploads_uuid_get(procore_company_id, company_id, uuid)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **uuid** | **str**| Upload UUID | 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_uploads_uuid_patch**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v10_companies_company_id_uploads_uuid_patch(procore_company_id, company_id, uuid, upload1=upload1)

Update Upload

Update the upload.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
from procore_sdk.models.upload1 import Upload1
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    uuid = 'uuid_example' # str | Upload UUID
    upload1 = procore_sdk.Upload1() # Upload1 |  (optional)

    try:
        # Update Upload
        api_response = api_instance.rest_v10_companies_company_id_uploads_uuid_patch(procore_company_id, company_id, uuid, upload1=upload1)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_uuid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v10_companies_company_id_uploads_uuid_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **uuid** | **str**| Upload UUID | 
 **upload1** | [**Upload1**](Upload1.md)|  | [optional] 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_companies_company_id_uploads_post**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v11_companies_company_id_uploads_post(procore_company_id, company_id, response_filename, response_content_type=response_content_type, attachment_content_disposition=attachment_content_disposition, segments=segments)

Create Upload

Creating an Upload is the first step in associating a file to a resource in Procore. Creating an Upload can be seen as fetching instruction on how to post your file directly to Procore's storage service.  The instructions contain three properties: a UUID to reference the Upload, a URL which has to be used to post the file, and fields which need to be posted together with the file.  To upload the file you must POST to the URL in the _url_ property with a multipart/form-data body (see RFC 2388). Make sure to include **all** the names and values from _fields_ without altering them. The URL and fields necessary to complete the upload may vary between companies and may also change over time so none of these may be hard-coded. Finally add a field named _file_ with the actual file data.  Uploads are associated to a Company so they can use company specific upload settings. The currently authenticated user will become the owner of the Upload and only that user can use the Upload in subsequent requests.  You will have to initiate the upload within one hour or you can expect a 403 Forbidden response. Other errors are usually clearly explained in the response body.  For an example of how to associate a finalized upload to another resource in Procore see the Photos resource. An Upload will have to be associated to another resource within a week or it will be automatically deleted from Procore servers.  Note that there is also a variant of this API endpoint that works using a Project ID.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
from procore_sdk.models.upload_segments_inner import UploadSegmentsInner
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    response_filename = 'response_filename_example' # str | By setting a filename you ensure that the storage service knows the filename of the upload. Files are often downloaded directly from the storage service and without the filename they will save on the end users' device without a readable name or extension.
    response_content_type = 'response_content_type_example' # str | The content-type set through this parameter will be used by the storage service during download just like the response_filename. Setting this value is less important because HTTP clients and operating systems are generally well equipped to determine file types.  Setting this parameter is optional and should only be included when you are certain it's correct or when you want to force a content-type other than what the filename extension suggests. (optional)
    attachment_content_disposition = True # bool | The content type set through this parameter will be used by the storage system during download, similar to the response_filename. When set to true, the file will be downloaded as an attachment. Otherwise, the file content will be rendered inline in the browser. (optional)
    segments = [procore_sdk.UploadSegmentsInner()] # List[UploadSegmentsInner] | Upload segments (optional)

    try:
        # Create Upload
        api_response = api_instance.rest_v11_companies_company_id_uploads_post(procore_company_id, company_id, response_filename, response_content_type=response_content_type, attachment_content_disposition=attachment_content_disposition, segments=segments)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **response_filename** | **str**| By setting a filename you ensure that the storage service knows the filename of the upload. Files are often downloaded directly from the storage service and without the filename they will save on the end users&#39; device without a readable name or extension. | 
 **response_content_type** | **str**| The content-type set through this parameter will be used by the storage service during download just like the response_filename. Setting this value is less important because HTTP clients and operating systems are generally well equipped to determine file types.  Setting this parameter is optional and should only be included when you are certain it&#39;s correct or when you want to force a content-type other than what the filename extension suggests. | [optional] 
 **attachment_content_disposition** | **bool**| The content type set through this parameter will be used by the storage system during download, similar to the response_filename. When set to true, the file will be downloaded as an attachment. Otherwise, the file content will be rendered inline in the browser. | [optional] 
 **segments** | [**List[UploadSegmentsInner]**](UploadSegmentsInner.md)| Upload segments | [optional] 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_companies_company_id_uploads_uuid_get**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v11_companies_company_id_uploads_uuid_get(procore_company_id, company_id, uuid)

Show Upload

Show detailed information on an upload

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    uuid = 'uuid_example' # str | Upload UUID

    try:
        # Show Upload
        api_response = api_instance.rest_v11_companies_company_id_uploads_uuid_get(procore_company_id, company_id, uuid)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **uuid** | **str**| Upload UUID | 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_companies_company_id_uploads_uuid_patch**
> RestV11ProjectsProjectIdUploadsPost201Response rest_v11_companies_company_id_uploads_uuid_patch(procore_company_id, company_id, uuid, upload1=upload1)

Update Upload

Update the upload.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response
from procore_sdk.models.upload1 import Upload1
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
    api_instance = procore_sdk.CoreCompanyCompanyUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    uuid = 'uuid_example' # str | Upload UUID
    upload1 = procore_sdk.Upload1() # Upload1 |  (optional)

    try:
        # Update Upload
        api_response = api_instance.rest_v11_companies_company_id_uploads_uuid_patch(procore_company_id, company_id, uuid, upload1=upload1)
        print("The response of CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_uuid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyUploadsApi->rest_v11_companies_company_id_uploads_uuid_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **uuid** | **str**| Upload UUID | 
 **upload1** | [**Upload1**](Upload1.md)|  | [optional] 

### Return type

[**RestV11ProjectsProjectIdUploadsPost201Response**](RestV11ProjectsProjectIdUploadsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

