# procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_file_versions_id_get**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_file_versions_id_get) | **GET** /rest/v1.0/file_versions/{id} | Show project file version
[**rest_v10_file_versions_post**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_file_versions_post) | **POST** /rest/v1.0/file_versions | Create project file version
[**rest_v10_files_id_delete**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_files_id_delete) | **DELETE** /rest/v1.0/files/{id} | Delete project File
[**rest_v10_files_id_get**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_files_id_get) | **GET** /rest/v1.0/files/{id} | Show project File
[**rest_v10_files_id_patch**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_files_id_patch) | **PATCH** /rest/v1.0/files/{id} | Update project File
[**rest_v10_files_post**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_files_post) | **POST** /rest/v1.0/files | Create project File
[**rest_v10_folders_get**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_folders_get) | **GET** /rest/v1.0/folders | List project folders and files
[**rest_v10_folders_id_delete**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_folders_id_delete) | **DELETE** /rest/v1.0/folders/{id} | Delete Project Folder
[**rest_v10_folders_id_get**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_folders_id_get) | **GET** /rest/v1.0/folders/{id} | Show Project Folder
[**rest_v10_folders_id_patch**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_folders_id_patch) | **PATCH** /rest/v1.0/folders/{id} | Update Project Folder
[**rest_v10_folders_post**](CoreProjectDocumentsProjectFoldersAndFilesApi.md#rest_v10_folders_post) | **POST** /rest/v1.0/folders | Create Project Folder


# **rest_v10_file_versions_id_get**
> RestV10FileVersionsPost201Response rest_v10_file_versions_id_get(procore_company_id, id, project_id)

Show project file version

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the file version
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show project file version
        api_response = api_instance.rest_v10_file_versions_id_get(procore_company_id, id, project_id)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_file_versions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_file_versions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the file version | 
 **project_id** | **int**| Unique identifier for the project. | 

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

# **rest_v10_file_versions_post**
> RestV10FileVersionsPost201Response rest_v10_file_versions_post(procore_company_id, project_id, file_id, file_version)

Create project file version

Upload a new version of a specific file in the Project Documents tool.  See the Procore Support website articles on [Project Documents](https://support.procore.com/products/online/user-guide/project-level/documents) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_file_versions_post201_response import RestV10FileVersionsPost201Response
from procore_sdk.models.rest_v10_file_versions_post_request_file_version import RestV10FileVersionsPostRequestFileVersion
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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    file_id = 56 # int | The id of the File
    file_version = procore_sdk.RestV10FileVersionsPostRequestFileVersion() # RestV10FileVersionsPostRequestFileVersion | 

    try:
        # Create project file version
        api_response = api_instance.rest_v10_file_versions_post(procore_company_id, project_id, file_id, file_version)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_file_versions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_file_versions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **file_id** | **int**| The id of the File | 
 **file_version** | [**RestV10FileVersionsPostRequestFileVersion**](RestV10FileVersionsPostRequestFileVersion.md)|  | 

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

# **rest_v10_files_id_delete**
> rest_v10_files_id_delete(procore_company_id, id, project_id)

Delete project File

Delete the specified File by moving it to the recycle bin.

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the File
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete project File
        api_instance.rest_v10_files_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the File | 
 **project_id** | **int**| Unique identifier for the project. | 

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

# **rest_v10_files_id_get**
> RestV10FilesPost201Response rest_v10_files_id_get(procore_company_id, id, project_id, show_latest_version_only=show_latest_version_only)

Show project File

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the File
    project_id = 56 # int | Unique identifier for the project.
    show_latest_version_only = True # bool | Show only latest File version (optional)

    try:
        # Show project File
        api_response = api_instance.rest_v10_files_id_get(procore_company_id, id, project_id, show_latest_version_only=show_latest_version_only)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the File | 
 **project_id** | **int**| Unique identifier for the project. | 
 **show_latest_version_only** | **bool**| Show only latest File version | [optional] 

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

# **rest_v10_files_id_patch**
> RestV10FilesPost201Response rest_v10_files_id_patch(procore_company_id, id, project_id, file)

Update project File

Update the specified File (creates a new file version).

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the File
    project_id = 56 # int | Unique identifier for the project.
    file = procore_sdk.RestV10FilesIdPatchRequestFile() # RestV10FilesIdPatchRequestFile | 

    try:
        # Update project File
        api_response = api_instance.rest_v10_files_id_patch(procore_company_id, id, project_id, file)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the File | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_files_post**
> RestV10FilesPost201Response rest_v10_files_post(procore_company_id, project_id, file)

Create project File

Create a new File in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_files_post201_response import RestV10FilesPost201Response
from procore_sdk.models.rest_v10_files_post_request_file import RestV10FilesPostRequestFile
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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    file = procore_sdk.RestV10FilesPostRequestFile() # RestV10FilesPostRequestFile | 

    try:
        # Create project File
        api_response = api_instance.rest_v10_files_post(procore_company_id, project_id, file)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **file** | [**RestV10FilesPostRequestFile**](RestV10FilesPostRequestFile.md)|  | 

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

# **rest_v10_folders_get**
> Folder rest_v10_folders_get(procore_company_id, project_id, exclude_folders=exclude_folders, exclude_files=exclude_files, show_latest_file_version_only=show_latest_file_version_only)

List project folders and files

Returns a list of folders and files for a specified project. Note: this operation will return all of the folders and files within the root folder of that project's document structure. For any folders that are nested more deeply an empty array [] will be returned.

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    exclude_folders = True # bool | Exclude child folders from results. Must be either true or false. (optional)
    exclude_files = True # bool | Exclude child files from results. Must be either true or false. (optional)
    show_latest_file_version_only = True # bool | Show only the latest file version. Must be either true or false. (optional)

    try:
        # List project folders and files
        api_response = api_instance.rest_v10_folders_get(procore_company_id, project_id, exclude_folders=exclude_folders, exclude_files=exclude_files, show_latest_file_version_only=show_latest_file_version_only)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **exclude_folders** | **bool**| Exclude child folders from results. Must be either true or false. | [optional] 
 **exclude_files** | **bool**| Exclude child files from results. Must be either true or false. | [optional] 
 **show_latest_file_version_only** | **bool**| Show only the latest file version. Must be either true or false. | [optional] 

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

# **rest_v10_folders_id_delete**
> rest_v10_folders_id_delete(procore_company_id, id, project_id)

Delete Project Folder

Delete the specified folder by moving it to the recycle bin.

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the folder
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Project Folder
        api_instance.rest_v10_folders_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the folder | 
 **project_id** | **int**| Unique identifier for the project. | 

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

# **rest_v10_folders_id_get**
> Folder rest_v10_folders_id_get(procore_company_id, id, project_id, exclude_folders=exclude_folders, exclude_files=exclude_files, show_latest_file_version_only=show_latest_file_version_only)

Show Project Folder

Show detail on the specified folder. Must be either true or false.

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the folder
    project_id = 56 # int | Unique identifier for the project.
    exclude_folders = True # bool | Exclude children Folders from results. Must be either true or false. (optional)
    exclude_files = True # bool | Exclude children files from results. Must be either true or false. (optional)
    show_latest_file_version_only = True # bool | Show only the latest file version. Must be either true or false. (optional)

    try:
        # Show Project Folder
        api_response = api_instance.rest_v10_folders_id_get(procore_company_id, id, project_id, exclude_folders=exclude_folders, exclude_files=exclude_files, show_latest_file_version_only=show_latest_file_version_only)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the folder | 
 **project_id** | **int**| Unique identifier for the project. | 
 **exclude_folders** | **bool**| Exclude children Folders from results. Must be either true or false. | [optional] 
 **exclude_files** | **bool**| Exclude children files from results. Must be either true or false. | [optional] 
 **show_latest_file_version_only** | **bool**| Show only the latest file version. Must be either true or false. | [optional] 

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

# **rest_v10_folders_id_patch**
> Folder1 rest_v10_folders_id_patch(procore_company_id, id, project_id, rest_v10_folders_id_patch_request)

Update Project Folder

Update the specified folder.

### Example


```python
import procore_sdk
from procore_sdk.models.folder1 import Folder1
from procore_sdk.models.rest_v10_folders_id_patch_request import RestV10FoldersIdPatchRequest
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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the folder
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_folders_id_patch_request = procore_sdk.RestV10FoldersIdPatchRequest() # RestV10FoldersIdPatchRequest | 

    try:
        # Update Project Folder
        api_response = api_instance.rest_v10_folders_id_patch(procore_company_id, id, project_id, rest_v10_folders_id_patch_request)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the folder | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_folders_id_patch_request** | [**RestV10FoldersIdPatchRequest**](RestV10FoldersIdPatchRequest.md)|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_folders_post**
> Folder1 rest_v10_folders_post(procore_company_id, project_id, rest_v10_folders_post_request)

Create Project Folder

Create a new folder in the specified project.

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
    api_instance = procore_sdk.CoreProjectDocumentsProjectFoldersAndFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_folders_post_request = procore_sdk.RestV10FoldersPostRequest() # RestV10FoldersPostRequest | 

    try:
        # Create Project Folder
        api_response = api_instance.rest_v10_folders_post(procore_company_id, project_id, rest_v10_folders_post_request)
        print("The response of CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDocumentsProjectFoldersAndFilesApi->rest_v10_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
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

