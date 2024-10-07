# procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_potential_change_orders_get**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_get) | **GET** /rest/v1.0/potential_change_orders | List Potential Change Orders
[**rest_v10_potential_change_orders_id_get**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_id_get) | **GET** /rest/v1.0/potential_change_orders/{id} | Show Potential Change Orders
[**rest_v10_potential_change_orders_id_patch**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_id_patch) | **PATCH** /rest/v1.0/potential_change_orders/{id} | Update Potential Change Order
[**rest_v10_potential_change_orders_post**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_post) | **POST** /rest/v1.0/potential_change_orders | Create Potential Change Order
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_get**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_get) | **GET** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items | List Potential Change Order Line Items
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete) | **DELETE** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items/{id} | Delete Potential Change Order Line Item
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get) | **GET** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items/{id} | Show Potential Change Order Line Item
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch) | **PATCH** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items/{id} | Update Potential Change Order Line Item
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_post**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_post) | **POST** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items | Create Potential Change Order Line Item
[**rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch) | **PATCH** /rest/v1.0/potential_change_orders/{potential_change_order_id}/line_items/sync | Sync Potential Change Order Line Items
[**rest_v10_potential_change_orders_sync_patch**](ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi.md#rest_v10_potential_change_orders_sync_patch) | **PATCH** /rest/v1.0/potential_change_orders/sync | Sync Potential Change Orders


# **rest_v10_potential_change_orders_get**
> List[RestV10PotentialChangeOrdersGet200ResponseInner] rest_v10_potential_change_orders_get(procore_company_id, project_id, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_contract_id=filters_contract_id, filters_include_deleted=filters_include_deleted, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, filters_reviewed_at=filters_reviewed_at, page=page, per_page=per_page)

List Potential Change Orders

Return a list of all Potential Change Orders (PCO).  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_potential_change_orders_get200_response_inner import RestV10PotentialChangeOrdersGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_due_date = 'filters_due_date_example' # str | Returns item(s) due within the specified ISO 8601 datetime range. (optional)
    filters_contract_id = 56 # int | Contract ID. Returns item(s) with the specified Contract ID. (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)
    filters_invoiced_date = 'filters_invoiced_date_example' # str | Returns item(s) invoiced within the specified ISO 8601 datetime range. (optional)
    filters_paid_date = 'filters_paid_date_example' # str | Returns item(s) paid within the specified ISO 8601 datetime range. (optional)
    filters_reviewed_at = 'filters_reviewed_at_example' # str | Returns item(s) reviewed within the specified ISO 8601 datetime range. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Potential Change Orders
        api_response = api_instance.rest_v10_potential_change_orders_get(procore_company_id, project_id, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_contract_id=filters_contract_id, filters_include_deleted=filters_include_deleted, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, filters_reviewed_at=filters_reviewed_at, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_due_date** | **str**| Returns item(s) due within the specified ISO 8601 datetime range. | [optional] 
 **filters_contract_id** | **int**| Contract ID. Returns item(s) with the specified Contract ID. | [optional] 
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 
 **filters_invoiced_date** | **str**| Returns item(s) invoiced within the specified ISO 8601 datetime range. | [optional] 
 **filters_paid_date** | **str**| Returns item(s) paid within the specified ISO 8601 datetime range. | [optional] 
 **filters_reviewed_at** | **str**| Returns item(s) reviewed within the specified ISO 8601 datetime range. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10PotentialChangeOrdersGet200ResponseInner]**](RestV10PotentialChangeOrdersGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**404** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_id_get**
> ArrayOfPotentialChangeOrdersEntitiesInner rest_v10_potential_change_orders_id_get(procore_company_id, id, project_id, contract_id)

Show Potential Change Orders

Return detailed information about a Potential Change Order (PCO).

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_potential_change_orders_entities_inner import ArrayOfPotentialChangeOrdersEntitiesInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID

    try:
        # Show Potential Change Orders
        api_response = api_instance.rest_v10_potential_change_orders_id_get(procore_company_id, id, project_id, contract_id)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 

### Return type

[**ArrayOfPotentialChangeOrdersEntitiesInner**](ArrayOfPotentialChangeOrdersEntitiesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_id_patch**
> ArrayOfPotentialChangeOrdersEntitiesInner rest_v10_potential_change_orders_id_patch(procore_company_id, id, rest_v10_potential_change_orders_id_patch_request)

Update Potential Change Order

Update information about a specific Potential Change Order (PCO).

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_potential_change_orders_entities_inner import ArrayOfPotentialChangeOrdersEntitiesInner
from procore_sdk.models.rest_v10_potential_change_orders_id_patch_request import RestV10PotentialChangeOrdersIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    rest_v10_potential_change_orders_id_patch_request = procore_sdk.RestV10PotentialChangeOrdersIdPatchRequest() # RestV10PotentialChangeOrdersIdPatchRequest | 

    try:
        # Update Potential Change Order
        api_response = api_instance.rest_v10_potential_change_orders_id_patch(procore_company_id, id, rest_v10_potential_change_orders_id_patch_request)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **rest_v10_potential_change_orders_id_patch_request** | [**RestV10PotentialChangeOrdersIdPatchRequest**](RestV10PotentialChangeOrdersIdPatchRequest.md)|  | 

### Return type

[**ArrayOfPotentialChangeOrdersEntitiesInner**](ArrayOfPotentialChangeOrdersEntitiesInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update change order due to errors. |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_post**
> RestV10PotentialChangeOrdersPost201Response rest_v10_potential_change_orders_post(procore_company_id, rest_v10_potential_change_orders_post_request)

Create Potential Change Order

Create a new Potential Change Order (PCO).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_potential_change_orders_post201_response import RestV10PotentialChangeOrdersPost201Response
from procore_sdk.models.rest_v10_potential_change_orders_post_request import RestV10PotentialChangeOrdersPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_potential_change_orders_post_request = procore_sdk.RestV10PotentialChangeOrdersPostRequest() # RestV10PotentialChangeOrdersPostRequest | 

    try:
        # Create Potential Change Order
        api_response = api_instance.rest_v10_potential_change_orders_post(procore_company_id, rest_v10_potential_change_orders_post_request)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_potential_change_orders_post_request** | [**RestV10PotentialChangeOrdersPostRequest**](RestV10PotentialChangeOrdersPostRequest.md)|  | 

### Return type

[**RestV10PotentialChangeOrdersPost201Response**](RestV10PotentialChangeOrdersPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create change order due to errors. |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_get**
> List[Default] rest_v10_potential_change_orders_potential_change_order_id_line_items_get(procore_company_id, potential_change_order_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)

List Potential Change Order Line Items

Return a list of all Potential Change Order Line Items.  Change Event Line Item information is only returned if a line item is associated to a change event line item and user can view change events.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.default import Default
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    potential_change_order_id = 56 # int | Potential Change Order ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_line_item_type_id = 56 # int | Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. (optional)

    try:
        # List Potential Change Order Line Items
        api_response = api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_get(procore_company_id, potential_change_order_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_cost_code_id** | **str**| Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. | [optional] 
 **filters_line_item_type_id** | **int**| Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. | [optional] 

### Return type

[**List[Default]**](Default.md)

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

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete**
> rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete(procore_company_id, potential_change_order_id, id, project_id)

Delete Potential Change Order Line Item

Delete a Potential Change Order Line Item.

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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    potential_change_order_id = 56 # int | Potential Change Order ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Potential Change Order Line Item
        api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete(procore_company_id, potential_change_order_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **id** | **int**| ID | 
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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get**
> Default rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get(procore_company_id, potential_change_order_id, id, project_id)

Show Potential Change Order Line Item

Return a Potential Change Order Line Item.  Change Event Line Item information is only returned if a line item is associated to a change event line item and user can view change events.

### Example


```python
import procore_sdk
from procore_sdk.models.default import Default
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    potential_change_order_id = 56 # int | Potential Change Order ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Potential Change Order Line Item
        api_response = api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get(procore_company_id, potential_change_order_id, id, project_id)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Default**](Default.md)

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

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch**
> Default rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch(procore_company_id, potential_change_order_id, id, body3)

Update Potential Change Order Line Item

Update a Potential Change Order Line Item. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.body3 import Body3
from procore_sdk.models.default import Default
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    potential_change_order_id = 56 # int | Potential Change Order ID
    id = 56 # int | ID
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Update Potential Change Order Line Item
        api_response = api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch(procore_company_id, potential_change_order_id, id, body3)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **id** | **int**| ID | 
 **body3** | [**Body3**](Body3.md)|  | 

### Return type

[**Default**](Default.md)

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

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_post**
> Default rest_v10_potential_change_orders_potential_change_order_id_line_items_post(procore_company_id, potential_change_order_id, body3)

Create Potential Change Order Line Item

Create a Potential Change Order Line Item. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.body3 import Body3
from procore_sdk.models.default import Default
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    potential_change_order_id = 56 # int | Potential Change Order ID
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Create Potential Change Order Line Item
        api_response = api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_post(procore_company_id, potential_change_order_id, body3)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **body3** | [**Body3**](Body3.md)|  | 

### Return type

[**Default**](Default.md)

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

# **rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch**
> ArrayOfPotentialChangeOrderLineItems rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch(procore_company_id, project_id, potential_change_order_id, line_item_sync_body)

Sync Potential Change Order Line Items

This endpoint creates or updates a batch of Potential Change Order Line Items. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_potential_change_order_line_items import ArrayOfPotentialChangeOrderLineItems
from procore_sdk.models.line_item_sync_body import LineItemSyncBody
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    potential_change_order_id = 56 # int | Potential Change Order ID
    line_item_sync_body = procore_sdk.LineItemSyncBody() # LineItemSyncBody | 

    try:
        # Sync Potential Change Order Line Items
        api_response = api_instance.rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch(procore_company_id, project_id, potential_change_order_id, line_item_sync_body)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_potential_change_order_id_line_items_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **potential_change_order_id** | **int**| Potential Change Order ID | 
 **line_item_sync_body** | [**LineItemSyncBody**](LineItemSyncBody.md)|  | 

### Return type

[**ArrayOfPotentialChangeOrderLineItems**](ArrayOfPotentialChangeOrderLineItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Potential Change Order Line Items |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_potential_change_orders_sync_patch**
> ArrayOfPotentialChangeOrders rest_v10_potential_change_orders_sync_patch(procore_company_id, project_id, contract_id, potential_change_order_body)

Sync Potential Change Orders

This endpoint creates or updates a batch of Potential Change Orders (PCO). See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_potential_change_orders import ArrayOfPotentialChangeOrders
from procore_sdk.models.potential_change_order_body import PotentialChangeOrderBody
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID
    potential_change_order_body = procore_sdk.PotentialChangeOrderBody() # PotentialChangeOrderBody | 

    try:
        # Sync Potential Change Orders
        api_response = api_instance.rest_v10_potential_change_orders_sync_patch(procore_company_id, project_id, contract_id, potential_change_order_body)
        print("The response of ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPotentialChangeOrdersApi->rest_v10_potential_change_orders_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | 
 **potential_change_order_body** | [**PotentialChangeOrderBody**](PotentialChangeOrderBody.md)|  | 

### Return type

[**ArrayOfPotentialChangeOrders**](ArrayOfPotentialChangeOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Potential Change Orders |  -  |
**401** | Company or project is not valid, user is not an active contact |  -  |
**403** | User has insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

