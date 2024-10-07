# procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_change_order_requests_get**](ConstructionFinancialsChangeOrdersChangeOrderRequestsApi.md#rest_v10_change_order_requests_get) | **GET** /rest/v1.0/change_order_requests | List Change Order Requests
[**rest_v10_change_order_requests_id_get**](ConstructionFinancialsChangeOrdersChangeOrderRequestsApi.md#rest_v10_change_order_requests_id_get) | **GET** /rest/v1.0/change_order_requests/{id} | Show Change Order Request
[**rest_v10_change_order_requests_id_patch**](ConstructionFinancialsChangeOrdersChangeOrderRequestsApi.md#rest_v10_change_order_requests_id_patch) | **PATCH** /rest/v1.0/change_order_requests/{id} | Update Change Order Request
[**rest_v10_change_order_requests_post**](ConstructionFinancialsChangeOrdersChangeOrderRequestsApi.md#rest_v10_change_order_requests_post) | **POST** /rest/v1.0/change_order_requests | Create Change Order Request
[**rest_v10_change_order_requests_sync_patch**](ConstructionFinancialsChangeOrdersChangeOrderRequestsApi.md#rest_v10_change_order_requests_sync_patch) | **PATCH** /rest/v1.0/change_order_requests/sync | Sync Change Order Requests


# **rest_v10_change_order_requests_get**
> List[RestV10ChangeOrderRequestsGet200ResponseInner] rest_v10_change_order_requests_get(procore_company_id, project_id, contract_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, page=page, per_page=per_page)

List Change Order Requests

Return a list of all Change Order Requests (COR) to a specific Contract in a Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_requests_get200_response_inner import RestV10ChangeOrderRequestsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_due_date = 'filters_due_date_example' # str | Returns item(s) due within the specified ISO 8601 datetime range. (optional)
    filters_invoiced_date = 'filters_invoiced_date_example' # str | Returns item(s) invoiced within the specified ISO 8601 datetime range. (optional)
    filters_paid_date = 'filters_paid_date_example' # str | Returns item(s) paid within the specified ISO 8601 datetime range. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Change Order Requests
        api_response = api_instance.rest_v10_change_order_requests_get(procore_company_id, project_id, contract_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_due_date** | **str**| Returns item(s) due within the specified ISO 8601 datetime range. | [optional] 
 **filters_invoiced_date** | **str**| Returns item(s) invoiced within the specified ISO 8601 datetime range. | [optional] 
 **filters_paid_date** | **str**| Returns item(s) paid within the specified ISO 8601 datetime range. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ChangeOrderRequestsGet200ResponseInner]**](RestV10ChangeOrderRequestsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**404** | User does not have correct permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_requests_id_get**
> ArrayOfChangeOrderRequestsEntitiesInner rest_v10_change_order_requests_id_get(procore_company_id, id, project_id, contract_id)

Show Change Order Request

Return detailed information about a specified Change Order Request (COR).

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_change_order_requests_entities_inner import ArrayOfChangeOrderRequestsEntitiesInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Show Change Order Request
        api_response = api_instance.rest_v10_change_order_requests_id_get(procore_company_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

### Return type

[**ArrayOfChangeOrderRequestsEntitiesInner**](ArrayOfChangeOrderRequestsEntitiesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_requests_id_patch**
> ArrayOfChangeOrderRequestsEntitiesInner rest_v10_change_order_requests_id_patch(procore_company_id, id, rest_v10_change_order_requests_post_request)

Update Change Order Request

Update information about a specific Change Order Request (COR).

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_change_order_requests_entities_inner import ArrayOfChangeOrderRequestsEntitiesInner
from procore_sdk.models.rest_v10_change_order_requests_post_request import RestV10ChangeOrderRequestsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    rest_v10_change_order_requests_post_request = procore_sdk.RestV10ChangeOrderRequestsPostRequest() # RestV10ChangeOrderRequestsPostRequest | 

    try:
        # Update Change Order Request
        api_response = api_instance.rest_v10_change_order_requests_id_patch(procore_company_id, id, rest_v10_change_order_requests_post_request)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **rest_v10_change_order_requests_post_request** | [**RestV10ChangeOrderRequestsPostRequest**](RestV10ChangeOrderRequestsPostRequest.md)|  | 

### Return type

[**ArrayOfChangeOrderRequestsEntitiesInner**](ArrayOfChangeOrderRequestsEntitiesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update Change Order Request due to errors. |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_requests_post**
> RestV10ChangeOrderRequestsPost201Response rest_v10_change_order_requests_post(procore_company_id, rest_v10_change_order_requests_post_request)

Create Change Order Request

Create Change Order Request (COR).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_requests_post201_response import RestV10ChangeOrderRequestsPost201Response
from procore_sdk.models.rest_v10_change_order_requests_post_request import RestV10ChangeOrderRequestsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_change_order_requests_post_request = procore_sdk.RestV10ChangeOrderRequestsPostRequest() # RestV10ChangeOrderRequestsPostRequest | 

    try:
        # Create Change Order Request
        api_response = api_instance.rest_v10_change_order_requests_post(procore_company_id, rest_v10_change_order_requests_post_request)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_change_order_requests_post_request** | [**RestV10ChangeOrderRequestsPostRequest**](RestV10ChangeOrderRequestsPostRequest.md)|  | 

### Return type

[**RestV10ChangeOrderRequestsPost201Response**](RestV10ChangeOrderRequestsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Unable to create Change Order Request due to errors. |  -  |
**403** | User does not have correct permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_requests_sync_patch**
> ArrayOfChangeOrderRequests rest_v10_change_order_requests_sync_patch(procore_company_id, project_id, contract_id, change_order_request_sync)

Sync Change Order Requests

This endpoint creates or updates a batch of Change Order Requests (COR). See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_change_order_requests import ArrayOfChangeOrderRequests
from procore_sdk.models.change_order_request_sync import ChangeOrderRequestSync
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    change_order_request_sync = procore_sdk.ChangeOrderRequestSync() # ChangeOrderRequestSync | 

    try:
        # Sync Change Order Requests
        api_response = api_instance.rest_v10_change_order_requests_sync_patch(procore_company_id, project_id, contract_id, change_order_request_sync)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderRequestsApi->rest_v10_change_order_requests_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **change_order_request_sync** | [**ChangeOrderRequestSync**](ChangeOrderRequestSync.md)|  | 

### Return type

[**ArrayOfChangeOrderRequests**](ArrayOfChangeOrderRequests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Change Order Requests |  -  |
**401** | Project is not valid |  -  |
**404** | User has insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

