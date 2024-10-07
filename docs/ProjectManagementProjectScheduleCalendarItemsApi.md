# procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_schedule_calendar_items_get**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_get) | **GET** /rest/v1.0/projects/{project_id}/schedule/calendar_items | List Calendar Items
[**rest_v10_projects_project_id_schedule_calendar_items_id_delete**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/schedule/calendar_items/{id} | Delete Calendar Item
[**rest_v10_projects_project_id_schedule_calendar_items_id_get**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_id_get) | **GET** /rest/v1.0/projects/{project_id}/schedule/calendar_items/{id} | Show Calendar Item
[**rest_v10_projects_project_id_schedule_calendar_items_id_patch**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/schedule/calendar_items/{id} | Update Calendar Item
[**rest_v10_projects_project_id_schedule_calendar_items_post**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_post) | **POST** /rest/v1.0/projects/{project_id}/schedule/calendar_items | Create Calendar Item
[**rest_v10_projects_project_id_schedule_calendar_items_sync_patch**](ProjectManagementProjectScheduleCalendarItemsApi.md#rest_v10_projects_project_id_schedule_calendar_items_sync_patch) | **PATCH** /rest/v1.0/projects/{project_id}/schedule/calendar_items/sync | Sync Calendar Items


# **rest_v10_projects_project_id_schedule_calendar_items_get**
> List[RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner] rest_v10_projects_project_id_schedule_calendar_items_get(procore_company_id, project_id, view=view, start_date=start_date, finish_date=finish_date, page=page, per_page=per_page, filters_query=filters_query, filters_updated_at=filters_updated_at, filters_assigned_id=filters_assigned_id, filters_date=filters_date, sort=sort)

List Calendar Items

Returns all Calendar Items for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner import RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The view to use when serializing Calendar Item data. The ids_only view returns an array of Calendar Item IDs. The total_count_only view returns total count of Calendar Items. (optional)
    start_date = '2013-10-20' # date | Calendar Items that occur after this date (optional)
    finish_date = '2013-10-20' # date | Calendar Items that occur before this date (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_assigned_id = [56] # List[int] | Returns task(s) with specified assignee(s) (optional)
    filters_date = 'filters_date_example' # str | Returns task(s) existing on the specified ISO 8601 datetime (optional)
    sort = 'sort_example' # str | Return item(s) with the specified sort.  Prepend \"-\" to specify descending order. (optional)

    try:
        # List Calendar Items
        api_response = api_instance.rest_v10_projects_project_id_schedule_calendar_items_get(procore_company_id, project_id, view=view, start_date=start_date, finish_date=finish_date, page=page, per_page=per_page, filters_query=filters_query, filters_updated_at=filters_updated_at, filters_assigned_id=filters_assigned_id, filters_date=filters_date, sort=sort)
        print("The response of ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The view to use when serializing Calendar Item data. The ids_only view returns an array of Calendar Item IDs. The total_count_only view returns total count of Calendar Items. | [optional] 
 **start_date** | **date**| Calendar Items that occur after this date | [optional] 
 **finish_date** | **date**| Calendar Items that occur before this date | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_assigned_id** | [**List[int]**](int.md)| Returns task(s) with specified assignee(s) | [optional] 
 **filters_date** | **str**| Returns task(s) existing on the specified ISO 8601 datetime | [optional] 
 **sort** | **str**| Return item(s) with the specified sort.  Prepend \&quot;-\&quot; to specify descending order. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner]**](RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_calendar_items_id_delete**
> rest_v10_projects_project_id_schedule_calendar_items_id_delete(procore_company_id, project_id, id)

Delete Calendar Item

Delete a single Calendar Item

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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Calendar Item ID

    try:
        # Delete Calendar Item
        api_instance.rest_v10_projects_project_id_schedule_calendar_items_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Calendar Item ID | 

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
**403** | User does not have right permissions |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_calendar_items_id_get**
> RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner rest_v10_projects_project_id_schedule_calendar_items_id_get(procore_company_id, project_id, id)

Show Calendar Item

Get the details of a single Calendar Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner import RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Calendar Item ID

    try:
        # Show Calendar Item
        api_response = api_instance.rest_v10_projects_project_id_schedule_calendar_items_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Calendar Item ID | 

### Return type

[**RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner**](RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_calendar_items_id_patch**
> RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner rest_v10_projects_project_id_schedule_calendar_items_id_patch(procore_company_id, project_id, id, body112)

Update Calendar Item

Update attributes on a single Calendar Item

### Example


```python
import procore_sdk
from procore_sdk.models.body112 import Body112
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner import RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Calendar Item ID
    body112 = procore_sdk.Body112() # Body112 | 

    try:
        # Update Calendar Item
        api_response = api_instance.rest_v10_projects_project_id_schedule_calendar_items_id_patch(procore_company_id, project_id, id, body112)
        print("The response of ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Calendar Item ID | 
 **body112** | [**Body112**](Body112.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner**](RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.md)

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
**403** | User does not have right permissions |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_calendar_items_post**
> RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner rest_v10_projects_project_id_schedule_calendar_items_post(procore_company_id, project_id, body112)

Create Calendar Item

Create a new Calendar Item

### Example


```python
import procore_sdk
from procore_sdk.models.body112 import Body112
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_get200_response_inner import RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body112 = procore_sdk.Body112() # Body112 | 

    try:
        # Create Calendar Item
        api_response = api_instance.rest_v10_projects_project_id_schedule_calendar_items_post(procore_company_id, project_id, body112)
        print("The response of ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body112** | [**Body112**](Body112.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner**](RestV10ProjectsProjectIdScheduleCalendarItemsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_calendar_items_sync_patch**
> RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response rest_v10_projects_project_id_schedule_calendar_items_sync_patch(procore_company_id, project_id, body113)

Sync Calendar Items

Create or update a batch of Calendar Items

### Example


```python
import procore_sdk
from procore_sdk.models.body113 import Body113
from procore_sdk.models.rest_v10_projects_project_id_schedule_calendar_items_sync_patch200_response import RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body113 = procore_sdk.Body113() # Body113 | 

    try:
        # Sync Calendar Items
        api_response = api_instance.rest_v10_projects_project_id_schedule_calendar_items_sync_patch(procore_company_id, project_id, body113)
        print("The response of ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarItemsApi->rest_v10_projects_project_id_schedule_calendar_items_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body113** | [**Body113**](Body113.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response**](RestV10ProjectsProjectIdScheduleCalendarItemsSyncPatch200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

