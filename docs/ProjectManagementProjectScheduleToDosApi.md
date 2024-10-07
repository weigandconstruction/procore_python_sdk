# procore_sdk.ProjectManagementProjectScheduleToDosApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_todos_id_delete**](ProjectManagementProjectScheduleToDosApi.md#rest_v10_todos_id_delete) | **DELETE** /rest/v1.0/todos/{id} | Delete todo
[**rest_v10_todos_id_get**](ProjectManagementProjectScheduleToDosApi.md#rest_v10_todos_id_get) | **GET** /rest/v1.0/todos/{id} | Show todo
[**rest_v10_todos_id_patch**](ProjectManagementProjectScheduleToDosApi.md#rest_v10_todos_id_patch) | **PATCH** /rest/v1.0/todos/{id} | Update todo
[**rest_v10_todos_post**](ProjectManagementProjectScheduleToDosApi.md#rest_v10_todos_post) | **POST** /rest/v1.0/todos | Create todo
[**rest_v10_todos_sync_patch**](ProjectManagementProjectScheduleToDosApi.md#rest_v10_todos_sync_patch) | **PATCH** /rest/v1.0/todos/sync | Sync ToDos


# **rest_v10_todos_id_delete**
> rest_v10_todos_id_delete(procore_company_id, id, project_id)

Delete todo

Delete a specific ToDo Item in a specified Project.  This endpoint has been deprecated. Instead, use [/rest/v1/calendar-items)

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleToDosApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the todo
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete todo
        api_instance.rest_v10_todos_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleToDosApi->rest_v10_todos_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the todo | 
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

# **rest_v10_todos_id_get**
> ToDo1 rest_v10_todos_id_get(procore_company_id, id, project_id)

Show todo

Return detailed information about a ToDo Item in a specified Project.  This endpoint has been deprecated. Instead, use [/rest/v1/calendar-items)

### Example


```python
import procore_sdk
from procore_sdk.models.to_do1 import ToDo1
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleToDosApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the todo
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show todo
        api_response = api_instance.rest_v10_todos_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementProjectScheduleToDosApi->rest_v10_todos_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleToDosApi->rest_v10_todos_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the todo | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ToDo1**](ToDo1.md)

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

# **rest_v10_todos_id_patch**
> ToDo1 rest_v10_todos_id_patch(procore_company_id, id, body11)

Update todo

Update a ToDo item for a specified Project.  This endpoint has been deprecated. Instead, use [/rest/v1/calendar-items)

### Example


```python
import procore_sdk
from procore_sdk.models.body11 import Body11
from procore_sdk.models.to_do1 import ToDo1
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleToDosApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the todo
    body11 = procore_sdk.Body11() # Body11 | 

    try:
        # Update todo
        api_response = api_instance.rest_v10_todos_id_patch(procore_company_id, id, body11)
        print("The response of ProjectManagementProjectScheduleToDosApi->rest_v10_todos_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleToDosApi->rest_v10_todos_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the todo | 
 **body11** | [**Body11**](Body11.md)|  | 

### Return type

[**ToDo1**](ToDo1.md)

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

# **rest_v10_todos_post**
> ToDo1 rest_v10_todos_post(procore_company_id, body10)

Create todo

Create a ToDo Item for a specified Project.  This endpoint has been deprecated. Instead, use [/rest/v1/calendar-items)

### Example


```python
import procore_sdk
from procore_sdk.models.body10 import Body10
from procore_sdk.models.to_do1 import ToDo1
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleToDosApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body10 = procore_sdk.Body10() # Body10 | 

    try:
        # Create todo
        api_response = api_instance.rest_v10_todos_post(procore_company_id, body10)
        print("The response of ProjectManagementProjectScheduleToDosApi->rest_v10_todos_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleToDosApi->rest_v10_todos_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body10** | [**Body10**](Body10.md)|  | 

### Return type

[**ToDo1**](ToDo1.md)

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

# **rest_v10_todos_sync_patch**
> ArrayOfTodos rest_v10_todos_sync_patch(procore_company_id, project_id, rest_v10_todos_sync_patch_request)

Sync ToDos

This endpoint creates or updates a batch of ToDos.  This endpoint has been deprecated. Instead, use [/rest/v1/calendar-items)

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_todos import ArrayOfTodos
from procore_sdk.models.rest_v10_todos_sync_patch_request import RestV10TodosSyncPatchRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleToDosApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_todos_sync_patch_request = procore_sdk.RestV10TodosSyncPatchRequest() # RestV10TodosSyncPatchRequest | 

    try:
        # Sync ToDos
        api_response = api_instance.rest_v10_todos_sync_patch(procore_company_id, project_id, rest_v10_todos_sync_patch_request)
        print("The response of ProjectManagementProjectScheduleToDosApi->rest_v10_todos_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleToDosApi->rest_v10_todos_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_todos_sync_patch_request** | [**RestV10TodosSyncPatchRequest**](RestV10TodosSyncPatchRequest.md)|  | 

### Return type

[**ArrayOfTodos**](ArrayOfTodos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of todos |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

