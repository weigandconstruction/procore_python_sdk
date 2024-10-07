# procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_change_event_statuses_get**](ConstructionFinancialsChangeEventsChangeEventsApi.md#rest_v10_change_event_statuses_get) | **GET** /rest/v1.0/change_event/statuses | List Change Event Statuses
[**rest_v10_change_events_get**](ConstructionFinancialsChangeEventsChangeEventsApi.md#rest_v10_change_events_get) | **GET** /rest/v1.0/change_events | List Change Events
[**rest_v10_change_events_id_get**](ConstructionFinancialsChangeEventsChangeEventsApi.md#rest_v10_change_events_id_get) | **GET** /rest/v1.0/change_events/{id} | Show Change Event
[**rest_v10_change_events_id_patch**](ConstructionFinancialsChangeEventsChangeEventsApi.md#rest_v10_change_events_id_patch) | **PATCH** /rest/v1.0/change_events/{id} | Update Change Event
[**rest_v10_change_events_post**](ConstructionFinancialsChangeEventsChangeEventsApi.md#rest_v10_change_events_post) | **POST** /rest/v1.0/change_events | Create Change Event


# **rest_v10_change_event_statuses_get**
> List[RestV10ChangeEventStatusesGet200ResponseInner] rest_v10_change_event_statuses_get(procore_company_id, project_id, page=page, per_page=per_page)

List Change Event Statuses

List Change Event Statuses for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_event_statuses_get200_response_inner import RestV10ChangeEventStatusesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Change Event Statuses
        api_response = api_instance.rest_v10_change_event_statuses_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_event_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_event_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ChangeEventStatusesGet200ResponseInner]**](RestV10ChangeEventStatusesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to access Change Event Statuses. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_events_get**
> List[RestV10ChangeEventsGet200ResponseInner] rest_v10_change_events_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_include_deleted=filters_include_deleted)

List Change Events

List Change Events for a specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)

    try:
        # List Change Events
        api_response = api_instance.rest_v10_change_events_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_include_deleted=filters_include_deleted)
        print("The response of ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 

### Return type

[**List[RestV10ChangeEventsGet200ResponseInner]**](RestV10ChangeEventsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to access Change Event. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_events_id_get**
> RestV10ChangeEventsGet200ResponseInner rest_v10_change_events_id_get(procore_company_id, id, project_id)

Show Change Event

Show Change Event.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Change Event
        api_response = api_instance.rest_v10_change_events_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ChangeEventsGet200ResponseInner**](RestV10ChangeEventsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have permission access to Change Event. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_events_id_patch**
> RestV10ChangeEventsGet200ResponseInner rest_v10_change_events_id_patch(procore_company_id, id, project_id, rest_v10_change_events_id_patch_request)

Update Change Event

Update Change Event. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner
from procore_sdk.models.rest_v10_change_events_id_patch_request import RestV10ChangeEventsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_change_events_id_patch_request = procore_sdk.RestV10ChangeEventsIdPatchRequest() # RestV10ChangeEventsIdPatchRequest | 

    try:
        # Update Change Event
        api_response = api_instance.rest_v10_change_events_id_patch(procore_company_id, id, project_id, rest_v10_change_events_id_patch_request)
        print("The response of ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_change_events_id_patch_request** | [**RestV10ChangeEventsIdPatchRequest**](RestV10ChangeEventsIdPatchRequest.md)|  | 

### Return type

[**RestV10ChangeEventsGet200ResponseInner**](RestV10ChangeEventsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update Change Event due to errors. |  -  |
**403** | User does not have permission access to update Change Events. |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_events_post**
> RestV10ChangeEventsGet200ResponseInner rest_v10_change_events_post(procore_company_id, project_id, rest_v10_change_events_post_request)

Create Change Event

Create Change Event Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner
from procore_sdk.models.rest_v10_change_events_post_request import RestV10ChangeEventsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeEventsChangeEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_change_events_post_request = procore_sdk.RestV10ChangeEventsPostRequest() # RestV10ChangeEventsPostRequest | 

    try:
        # Create Change Event
        api_response = api_instance.rest_v10_change_events_post(procore_company_id, project_id, rest_v10_change_events_post_request)
        print("The response of ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeEventsChangeEventsApi->rest_v10_change_events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_change_events_post_request** | [**RestV10ChangeEventsPostRequest**](RestV10ChangeEventsPostRequest.md)|  | 

### Return type

[**RestV10ChangeEventsGet200ResponseInner**](RestV10ChangeEventsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create Change Event due to errors. |  -  |
**403** | User does not have permission access to create Change Events. |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

