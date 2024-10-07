# procore_sdk.ProjectManagementProjectScheduleTasksApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_tasks_get**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_get) | **GET** /rest/v1.0/tasks | List tasks
[**rest_v10_tasks_id_delete**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_id_delete) | **DELETE** /rest/v1.0/tasks/{id} | Delete task
[**rest_v10_tasks_id_get**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_id_get) | **GET** /rest/v1.0/tasks/{id} | Show task
[**rest_v10_tasks_id_patch**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_id_patch) | **PATCH** /rest/v1.0/tasks/{id} | Update task
[**rest_v10_tasks_post**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_post) | **POST** /rest/v1.0/tasks | Create task
[**rest_v10_tasks_sync_patch**](ProjectManagementProjectScheduleTasksApi.md#rest_v10_tasks_sync_patch) | **PATCH** /rest/v1.0/tasks/sync | Sync tasks


# **rest_v10_tasks_get**
> List[Task] rest_v10_tasks_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_updated_at=filters_updated_at, filters_row_number=filters_row_number, filters_query=filters_query)

List tasks

List existing tasks for the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.task import Task
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'normal' # str | The compact view contains id, name, key, formatted_name, and task_name. The normal view contains the response shown below. The default view is normal. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_row_number = 5 # int | Returns Tasks with a row_number matching the given value. This endpoint supports single values of row_number,  a range of row_numbers (filters[row_number]=4...7) as well as multiple values  (filters[row_number][]=5&filters[row_number][]=6). Exclude the filter to fetch all Tasks.  (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)

    try:
        # List tasks
        api_response = api_instance.rest_v10_tasks_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_updated_at=filters_updated_at, filters_row_number=filters_row_number, filters_query=filters_query)
        print("The response of ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The compact view contains id, name, key, formatted_name, and task_name. The normal view contains the response shown below. The default view is normal. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_row_number** | **int**| Returns Tasks with a row_number matching the given value. This endpoint supports single values of row_number,  a range of row_numbers (filters[row_number]&#x3D;4...7) as well as multiple values  (filters[row_number][]&#x3D;5&amp;filters[row_number][]&#x3D;6). Exclude the filter to fetch all Tasks.  | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 

### Return type

[**List[Task]**](Task.md)

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

# **rest_v10_tasks_id_delete**
> rest_v10_tasks_id_delete(procore_company_id, id, project_id)

Delete task

Delete the specified Task.

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the task
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete task
        api_instance.rest_v10_tasks_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the task | 
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

# **rest_v10_tasks_id_get**
> Task rest_v10_tasks_id_get(procore_company_id, id, project_id)

Show task

Show detail on the specified Task.

### Example


```python
import procore_sdk
from procore_sdk.models.task import Task
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the task
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show task
        api_response = api_instance.rest_v10_tasks_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the task | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Task**](Task.md)

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

# **rest_v10_tasks_id_patch**
> Task rest_v10_tasks_id_patch(procore_company_id, id, body14)

Update task

Update the specified Task.

### Example


```python
import procore_sdk
from procore_sdk.models.body14 import Body14
from procore_sdk.models.task import Task
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the task
    body14 = procore_sdk.Body14() # Body14 | 

    try:
        # Update task
        api_response = api_instance.rest_v10_tasks_id_patch(procore_company_id, id, body14)
        print("The response of ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the task | 
 **body14** | [**Body14**](Body14.md)|  | 

### Return type

[**Task**](Task.md)

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

# **rest_v10_tasks_post**
> Task rest_v10_tasks_post(procore_company_id, body14)

Create task

Create a new Task associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body14 import Body14
from procore_sdk.models.task import Task
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body14 = procore_sdk.Body14() # Body14 | 

    try:
        # Create task
        api_response = api_instance.rest_v10_tasks_post(procore_company_id, body14)
        print("The response of ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body14** | [**Body14**](Body14.md)|  | 

### Return type

[**Task**](Task.md)

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

# **rest_v10_tasks_sync_patch**
> ArrayOfTasks rest_v10_tasks_sync_patch(procore_company_id, project_id, rest_v10_tasks_sync_patch_request)

Sync tasks

This endpoint creates or updates a batch of tasks.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_tasks import ArrayOfTasks
from procore_sdk.models.rest_v10_tasks_sync_patch_request import RestV10TasksSyncPatchRequest
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleTasksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_tasks_sync_patch_request = procore_sdk.RestV10TasksSyncPatchRequest() # RestV10TasksSyncPatchRequest | 

    try:
        # Sync tasks
        api_response = api_instance.rest_v10_tasks_sync_patch(procore_company_id, project_id, rest_v10_tasks_sync_patch_request)
        print("The response of ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleTasksApi->rest_v10_tasks_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_tasks_sync_patch_request** | [**RestV10TasksSyncPatchRequest**](RestV10TasksSyncPatchRequest.md)|  | 

### Return type

[**ArrayOfTasks**](ArrayOfTasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of tasks |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

