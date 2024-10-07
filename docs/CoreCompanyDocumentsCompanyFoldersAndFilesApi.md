# procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_file_versions_id_get**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_file_versions_id_get) | **GET** /rest/v1.0/companies/{company_id}/file_versions/{id} | Show company file version
[**rest_v10_companies_company_id_file_versions_post**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_file_versions_post) | **POST** /rest/v1.0/companies/{company_id}/file_versions | Create company file version
[**rest_v10_companies_company_id_files_id_delete**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_files_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/files/{id} | Delete company File
[**rest_v10_companies_company_id_files_id_get**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_files_id_get) | **GET** /rest/v1.0/companies/{company_id}/files/{id} | Show company File
[**rest_v10_companies_company_id_files_id_patch**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_files_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/files/{id} | Update company File
[**rest_v10_companies_company_id_files_id_send_email_post**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_files_id_send_email_post) | **POST** /rest/v1.0/companies/{company_id}/files/{id}/send_email | Send email for file sharing
[**rest_v10_companies_company_id_files_post**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_files_post) | **POST** /rest/v1.0/companies/{company_id}/files | Create company File
[**rest_v10_companies_company_id_folders_get**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_folders_get) | **GET** /rest/v1.0/companies/{company_id}/folders | List company Folders and Files
[**rest_v10_companies_company_id_folders_id_delete**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_folders_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/folders/{id} | Delete company Folder
[**rest_v10_companies_company_id_folders_id_get**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_folders_id_get) | **GET** /rest/v1.0/companies/{company_id}/folders/{id} | Show company Folder
[**rest_v10_companies_company_id_folders_id_patch**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_folders_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/folders/{id} | Update company Folder
[**rest_v10_companies_company_id_folders_post**](CoreCompanyDocumentsCompanyFoldersAndFilesApi.md#rest_v10_companies_company_id_folders_post) | **POST** /rest/v1.0/companies/{company_id}/folders | Create company Folder


# **rest_v10_companies_company_id_file_versions_id_get**
> RestV10FileVersionsPost201Response rest_v10_companies_company_id_file_versions_id_get(procore_company_id, company_id, id)

Show company file version

Show detailed information about a File Version.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_file_versions_post201_response import RestV10FileVersionsPost201Response
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the file version

    try:
        # Show company file version
        api_response = api_instance.rest_v10_companies_company_id_file_versions_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_file_versions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_file_versions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the file version | 

### Return type

[**RestV10FileVersionsPost201Response**](RestV10FileVersionsPost201Response.md)

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

# **rest_v10_companies_company_id_file_versions_post**
> RestV10FileVersionsPost201Response rest_v10_companies_company_id_file_versions_post(procore_company_id, company_id, file_id, file_version)

Create company file version

Uploads a new version of a specific file in the Company Documents tool.  See the Procore Support website articles on [Company Documents](https://support.procore.com/products/online/user-guide/company-level/documents).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_file_versions_post_request_file_version import RestV10CompaniesCompanyIdFileVersionsPostRequestFileVersion
from procore_sdk.models.rest_v10_file_versions_post201_response import RestV10FileVersionsPost201Response
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    file_id = 56 # int | The id of the File
    file_version = procore_sdk.RestV10CompaniesCompanyIdFileVersionsPostRequestFileVersion() # RestV10CompaniesCompanyIdFileVersionsPostRequestFileVersion | 

    try:
        # Create company file version
        api_response = api_instance.rest_v10_companies_company_id_file_versions_post(procore_company_id, company_id, file_id, file_version)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_file_versions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_file_versions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **file_id** | **int**| The id of the File | 
 **file_version** | [**RestV10CompaniesCompanyIdFileVersionsPostRequestFileVersion**](RestV10CompaniesCompanyIdFileVersionsPostRequestFileVersion.md)|  | 

### Return type

[**RestV10FileVersionsPost201Response**](RestV10FileVersionsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **rest_v10_companies_company_id_files_id_delete**
> rest_v10_companies_company_id_files_id_delete(procore_company_id, company_id, id)

Delete company File

Delete a specific File.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the File

    try:
        # Delete company File
        api_instance.rest_v10_companies_company_id_files_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the File | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **rest_v10_companies_company_id_files_id_get**
> RestV10FilesPost201Response rest_v10_companies_company_id_files_id_get(procore_company_id, company_id, id, show_latest_version_only=show_latest_version_only)

Show company File

Show detailed information about a File.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_files_post201_response import RestV10FilesPost201Response
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the File
    show_latest_version_only = True # bool | Show only latest File Version (optional)

    try:
        # Show company File
        api_response = api_instance.rest_v10_companies_company_id_files_id_get(procore_company_id, company_id, id, show_latest_version_only=show_latest_version_only)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the File | 
 **show_latest_version_only** | **bool**| Show only latest File Version | [optional] 

### Return type

[**RestV10FilesPost201Response**](RestV10FilesPost201Response.md)

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

# **rest_v10_companies_company_id_files_id_patch**
> RestV10FilesPost201Response rest_v10_companies_company_id_files_id_patch(procore_company_id, company_id, id, file)

Update company File

Update a specific File (creates a new file version).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_files_id_patch_request_file import RestV10FilesIdPatchRequestFile
from procore_sdk.models.rest_v10_files_post201_response import RestV10FilesPost201Response
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the File
    file = procore_sdk.RestV10FilesIdPatchRequestFile() # RestV10FilesIdPatchRequestFile | 

    try:
        # Update company File
        api_response = api_instance.rest_v10_companies_company_id_files_id_patch(procore_company_id, company_id, id, file)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the File | 
 **file** | [**RestV10FilesIdPatchRequestFile**](RestV10FilesIdPatchRequestFile.md)|  | 

### Return type

[**RestV10FilesPost201Response**](RestV10FilesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_files_id_send_email_post**
> rest_v10_companies_company_id_files_id_send_email_post(procore_company_id, company_id, id, body29)

Send email for file sharing

Send email for file sharing.

### Example


```python
import procore_sdk
from procore_sdk.models.body29 import Body29
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the File
    body29 = procore_sdk.Body29() # Body29 | 

    try:
        # Send email for file sharing
        api_instance.rest_v10_companies_company_id_files_id_send_email_post(procore_company_id, company_id, id, body29)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the File | 
 **body29** | [**Body29**](Body29.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_files_post**
> RestV10FilesPost201Response rest_v10_companies_company_id_files_post(procore_company_id, company_id, file)

Create company File

Create a new File associated with specific Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_files_post_request_file import RestV10CompaniesCompanyIdFilesPostRequestFile
from procore_sdk.models.rest_v10_files_post201_response import RestV10FilesPost201Response
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    file = procore_sdk.RestV10CompaniesCompanyIdFilesPostRequestFile() # RestV10CompaniesCompanyIdFilesPostRequestFile | 

    try:
        # Create company File
        api_response = api_instance.rest_v10_companies_company_id_files_post(procore_company_id, company_id, file)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **file** | [**RestV10CompaniesCompanyIdFilesPostRequestFile**](RestV10CompaniesCompanyIdFilesPostRequestFile.md)|  | 

### Return type

[**RestV10FilesPost201Response**](RestV10FilesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **rest_v10_companies_company_id_folders_get**
> Folder rest_v10_companies_company_id_folders_get(procore_company_id, company_id, exclude_folders=exclude_folders, exclude_files=exclude_files)

List company Folders and Files

Return a list of Folders and Files associated with a specific Company.

### Example


```python
import procore_sdk
from procore_sdk.models.folder import Folder
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    exclude_folders = True # bool | Exclude children Folders from results (optional)
    exclude_files = True # bool | Exclude children Files from results (optional)

    try:
        # List company Folders and Files
        api_response = api_instance.rest_v10_companies_company_id_folders_get(procore_company_id, company_id, exclude_folders=exclude_folders, exclude_files=exclude_files)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **exclude_folders** | **bool**| Exclude children Folders from results | [optional] 
 **exclude_files** | **bool**| Exclude children Files from results | [optional] 

### Return type

[**Folder**](Folder.md)

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

# **rest_v10_companies_company_id_folders_id_delete**
> rest_v10_companies_company_id_folders_id_delete(procore_company_id, company_id, id)

Delete company Folder

Delete the specified Folder by moving it to the recycle bin.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Folder

    try:
        # Delete company Folder
        api_instance.rest_v10_companies_company_id_folders_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Folder | 

### Return type

void (empty response body)

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

# **rest_v10_companies_company_id_folders_id_get**
> Folder rest_v10_companies_company_id_folders_id_get(procore_company_id, company_id, id, exclude_folders=exclude_folders, exclude_files=exclude_files)

Show company Folder

Show detail on a specific Folder.

### Example


```python
import procore_sdk
from procore_sdk.models.folder import Folder
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Folder
    exclude_folders = True # bool | Exclude children Folders from results (optional)
    exclude_files = True # bool | Exclude children Files from results (optional)

    try:
        # Show company Folder
        api_response = api_instance.rest_v10_companies_company_id_folders_id_get(procore_company_id, company_id, id, exclude_folders=exclude_folders, exclude_files=exclude_files)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Folder | 
 **exclude_folders** | **bool**| Exclude children Folders from results | [optional] 
 **exclude_files** | **bool**| Exclude children Files from results | [optional] 

### Return type

[**Folder**](Folder.md)

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

# **rest_v10_companies_company_id_folders_id_patch**
> Folder rest_v10_companies_company_id_folders_id_patch(procore_company_id, company_id, id, rest_v10_folders_post_request)

Update company Folder

Update a specific Folder.

### Example


```python
import procore_sdk
from procore_sdk.models.folder import Folder
from procore_sdk.models.rest_v10_folders_post_request import RestV10FoldersPostRequest
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Folder
    rest_v10_folders_post_request = procore_sdk.RestV10FoldersPostRequest() # RestV10FoldersPostRequest | 

    try:
        # Update company Folder
        api_response = api_instance.rest_v10_companies_company_id_folders_id_patch(procore_company_id, company_id, id, rest_v10_folders_post_request)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Folder | 
 **rest_v10_folders_post_request** | [**RestV10FoldersPostRequest**](RestV10FoldersPostRequest.md)|  | 

### Return type

[**Folder**](Folder.md)

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

# **rest_v10_companies_company_id_folders_post**
> Folder1 rest_v10_companies_company_id_folders_post(procore_company_id, company_id, rest_v10_folders_post_request)

Create company Folder

Create a new Folder associated with a specific Company.

### Example


```python
import procore_sdk
from procore_sdk.models.folder1 import Folder1
from procore_sdk.models.rest_v10_folders_post_request import RestV10FoldersPostRequest
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
    api_instance = procore_sdk.CoreCompanyDocumentsCompanyFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_folders_post_request = procore_sdk.RestV10FoldersPostRequest() # RestV10FoldersPostRequest | 

    try:
        # Create company Folder
        api_response = api_instance.rest_v10_companies_company_id_folders_post(procore_company_id, company_id, rest_v10_folders_post_request)
        print("The response of CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDocumentsCompanyFoldersAndFilesApi->rest_v10_companies_company_id_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_folders_post_request** | [**RestV10FoldersPostRequest**](RestV10FoldersPostRequest.md)|  | 

### Return type

[**Folder1**](Folder1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

