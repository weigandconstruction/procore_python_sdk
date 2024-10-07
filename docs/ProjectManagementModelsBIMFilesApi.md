# procore_sdk.ProjectManagementModelsBIMFilesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_files_get**](ProjectManagementModelsBIMFilesApi.md#rest_v10_bim_files_get) | **GET** /rest/v1.0/bim_files | List BIM Files
[**rest_v10_bim_files_id_delete**](ProjectManagementModelsBIMFilesApi.md#rest_v10_bim_files_id_delete) | **DELETE** /rest/v1.0/bim_files/{id} | Delete BIM File
[**rest_v10_bim_files_id_get**](ProjectManagementModelsBIMFilesApi.md#rest_v10_bim_files_id_get) | **GET** /rest/v1.0/bim_files/{id} | Show BIM File
[**rest_v10_bim_files_id_patch**](ProjectManagementModelsBIMFilesApi.md#rest_v10_bim_files_id_patch) | **PATCH** /rest/v1.0/bim_files/{id} | Update BIM File
[**rest_v10_bim_files_post**](ProjectManagementModelsBIMFilesApi.md#rest_v10_bim_files_post) | **POST** /rest/v1.0/bim_files | Create BIM File


# **rest_v10_bim_files_get**
> List[RestV10BimFilesGet200ResponseInner] rest_v10_bim_files_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_id=filters_id)

List BIM Files

Lists BIM Files associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_files_get200_response_inner import RestV10BimFilesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The normal and extended view contains the response shown below. The default view is normal. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)

    try:
        # List BIM Files
        api_response = api_instance.rest_v10_bim_files_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_id=filters_id)
        print("The response of ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The normal and extended view contains the response shown below. The default view is normal. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 

### Return type

[**List[RestV10BimFilesGet200ResponseInner]**](RestV10BimFilesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Files listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_files_id_delete**
> rest_v10_bim_files_id_delete(procore_company_id, id, project_id)

Delete BIM File

Delete a BIM File from the system. A BIM File can only be deleted if it is not associated with BIM Levels, Revisions, or Viewpoints or Coordination Issues.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM File ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete BIM File
        api_instance.rest_v10_bim_files_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM File ID | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_files_id_get**
> RestV10BimFilesGet200ResponseInner rest_v10_bim_files_id_get(procore_company_id, id, project_id, view=view)

Show BIM File

Return a single BIM File item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_files_get200_response_inner import RestV10BimFilesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 'id_example' # str | BIM File ID.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The normal and extended view contains the response shown below. The default view is normal. (optional)

    try:
        # Show BIM File
        api_response = api_instance.rest_v10_bim_files_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **str**| BIM File ID. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The normal and extended view contains the response shown below. The default view is normal. | [optional] 

### Return type

[**RestV10BimFilesGet200ResponseInner**](RestV10BimFilesGet200ResponseInner.md)

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

# **rest_v10_bim_files_id_patch**
> RestV10BimFilesGet200ResponseInner rest_v10_bim_files_id_patch(procore_company_id, id, body141)

Update BIM File

Updates a BIM File

### Example


```python
import procore_sdk
from procore_sdk.models.body141 import Body141
from procore_sdk.models.rest_v10_bim_files_get200_response_inner import RestV10BimFilesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM File ID
    body141 = procore_sdk.Body141() # Body141 | 

    try:
        # Update BIM File
        api_response = api_instance.rest_v10_bim_files_id_patch(procore_company_id, id, body141)
        print("The response of ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM File ID | 
 **body141** | [**Body141**](Body141.md)|  | 

### Return type

[**RestV10BimFilesGet200ResponseInner**](RestV10BimFilesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_files_post**
> RestV10BimFilesGet200ResponseInner rest_v10_bim_files_post(procore_company_id, body140)

Create BIM File

Create a BIM File in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.body140 import Body140
from procore_sdk.models.rest_v10_bim_files_get200_response_inner import RestV10BimFilesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMFilesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body140 = procore_sdk.Body140() # Body140 | 

    try:
        # Create BIM File
        api_response = api_instance.rest_v10_bim_files_post(procore_company_id, body140)
        print("The response of ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMFilesApi->rest_v10_bim_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body140** | [**Body140**](Body140.md)|  | 

### Return type

[**RestV10BimFilesGet200ResponseInner**](RestV10BimFilesGet200ResponseInner.md)

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

