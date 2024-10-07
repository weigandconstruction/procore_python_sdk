# procore_sdk.CoreTasksTaskItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_task_items_get**](CoreTasksTaskItemsApi.md#rest_v10_task_items_get) | **GET** /rest/v1.0/task_items | List task items
[**rest_v10_task_items_id_delete**](CoreTasksTaskItemsApi.md#rest_v10_task_items_id_delete) | **DELETE** /rest/v1.0/task_items/{id} | Destroy task item
[**rest_v10_task_items_id_get**](CoreTasksTaskItemsApi.md#rest_v10_task_items_id_get) | **GET** /rest/v1.0/task_items/{id} | Show task item
[**rest_v10_task_items_id_patch**](CoreTasksTaskItemsApi.md#rest_v10_task_items_id_patch) | **PATCH** /rest/v1.0/task_items/{id} | Update task item
[**rest_v10_task_items_post**](CoreTasksTaskItemsApi.md#rest_v10_task_items_post) | **POST** /rest/v1.0/task_items | Create task item
[**rest_v10_task_items_send_unsent_post**](CoreTasksTaskItemsApi.md#rest_v10_task_items_send_unsent_post) | **POST** /rest/v1.0/task_items/send_unsent | Send unsent Task Items


# **rest_v10_task_items_get**
> List[ArrayOfTaskItemsThatWereSentOutInner] rest_v10_task_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_query=filters_query, filters_assigned_id=filters_assigned_id, filters_created_at=filters_created_at, filters_created_by_id=filters_created_by_id, filters_due_date=filters_due_date, filters_status=filters_status, filters_task_item_category_id=filters_task_item_category_id, filters_id=filters_id, sort=sort)

List task items

Returns a list of task items on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner import ArrayOfTaskItemsThatWereSentOutInner
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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_assigned_id = 'filters_assigned_id_example' # str | Assigned ID (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_due_date = 'filters_due_date_example' # str | Returns item(s) due within the specified ISO 8601 datetime range. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_task_item_category_id = 'filters_task_item_category_id_example' # str | Returns item(s) matching the specified Task Item Category ID. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    sort = 'sort_example' # str | Return item(s) with the specified sort. (optional)

    try:
        # List task items
        api_response = api_instance.rest_v10_task_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_query=filters_query, filters_assigned_id=filters_assigned_id, filters_created_at=filters_created_at, filters_created_by_id=filters_created_by_id, filters_due_date=filters_due_date, filters_status=filters_status, filters_task_item_category_id=filters_task_item_category_id, filters_id=filters_id, sort=sort)
        print("The response of CoreTasksTaskItemsApi->rest_v10_task_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_assigned_id** | **str**| Assigned ID | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_due_date** | **str**| Returns item(s) due within the specified ISO 8601 datetime range. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_task_item_category_id** | **str**| Returns item(s) matching the specified Task Item Category ID. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **sort** | **str**| Return item(s) with the specified sort. | [optional] 

### Return type

[**List[ArrayOfTaskItemsThatWereSentOutInner]**](ArrayOfTaskItemsThatWereSentOutInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_task_items_id_delete**
> rest_v10_task_items_id_delete(procore_company_id, project_id, id)

Destroy task item

Send a task item to the recycle bin.

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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Task Item ID

    try:
        # Destroy task item
        api_instance.rest_v10_task_items_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Task Item ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_task_items_id_get**
> RestV10TaskItemsPost201Response rest_v10_task_items_id_get(procore_company_id, project_id, id)

Show task item

Show detailed information for a specific task item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_task_items_post201_response import RestV10TaskItemsPost201Response
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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Task Item ID

    try:
        # Show task item
        api_response = api_instance.rest_v10_task_items_id_get(procore_company_id, project_id, id)
        print("The response of CoreTasksTaskItemsApi->rest_v10_task_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Task Item ID | 

### Return type

[**RestV10TaskItemsPost201Response**](RestV10TaskItemsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_task_items_id_patch**
> RestV10TaskItemsPost201Response rest_v10_task_items_id_patch(procore_company_id, project_id, id, task_item)

Update task item

Update a task item's attributes

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_task_items_post201_response import RestV10TaskItemsPost201Response
from procore_sdk.models.rest_v10_task_items_post_request_task_item import RestV10TaskItemsPostRequestTaskItem
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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Task Item ID
    task_item = procore_sdk.RestV10TaskItemsPostRequestTaskItem() # RestV10TaskItemsPostRequestTaskItem | 

    try:
        # Update task item
        api_response = api_instance.rest_v10_task_items_id_patch(procore_company_id, project_id, id, task_item)
        print("The response of CoreTasksTaskItemsApi->rest_v10_task_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Task Item ID | 
 **task_item** | [**RestV10TaskItemsPostRequestTaskItem**](RestV10TaskItemsPostRequestTaskItem.md)|  | 

### Return type

[**RestV10TaskItemsPost201Response**](RestV10TaskItemsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_task_items_post**
> RestV10TaskItemsPost201Response rest_v10_task_items_post(procore_company_id, project_id, rest_v10_task_items_post_request)

Create task item

Creates a task item on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_task_items_post201_response import RestV10TaskItemsPost201Response
from procore_sdk.models.rest_v10_task_items_post_request import RestV10TaskItemsPostRequest
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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_task_items_post_request = procore_sdk.RestV10TaskItemsPostRequest() # RestV10TaskItemsPostRequest | 

    try:
        # Create task item
        api_response = api_instance.rest_v10_task_items_post(procore_company_id, project_id, rest_v10_task_items_post_request)
        print("The response of CoreTasksTaskItemsApi->rest_v10_task_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_task_items_post_request** | [**RestV10TaskItemsPostRequest**](RestV10TaskItemsPostRequest.md)|  | 

### Return type

[**RestV10TaskItemsPost201Response**](RestV10TaskItemsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_task_items_send_unsent_post**
> List[ArrayOfTaskItemsThatWereSentOutInner] rest_v10_task_items_send_unsent_post(procore_company_id)

Send unsent Task Items

Sends email notifications for unsent Task Items.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_task_items_that_were_sent_out_inner import ArrayOfTaskItemsThatWereSentOutInner
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
    api_instance = procore_sdk.CoreTasksTaskItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.

    try:
        # Send unsent Task Items
        api_response = api_instance.rest_v10_task_items_send_unsent_post(procore_company_id)
        print("The response of CoreTasksTaskItemsApi->rest_v10_task_items_send_unsent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemsApi->rest_v10_task_items_send_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 

### Return type

[**List[ArrayOfTaskItemsThatWereSentOutInner]**](ArrayOfTaskItemsThatWereSentOutInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

