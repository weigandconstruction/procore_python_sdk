# procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get) | **GET** /rest/v1.0/projects/{project_id}/direct_costs/{direct_cost_id}/line_items | List Direct Cost Line Items
[**rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/direct_costs/{direct_cost_id}/line_items/{id} | Delete a Direct Cost Line Item
[**rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get) | **GET** /rest/v1.0/projects/{project_id}/direct_costs/{direct_cost_id}/line_items/{id} | Show Direct Cost Line Item
[**rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/direct_costs/{direct_cost_id}/line_items/{id} | Update Direct Cost Line Item
[**rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post) | **POST** /rest/v1.0/projects/{project_id}/direct_costs/{direct_cost_id}/line_items | Create Direct Cost Line Item
[**rest_v10_projects_project_id_direct_costs_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_get) | **GET** /rest/v1.0/projects/{project_id}/direct_costs | List Direct Cost Items
[**rest_v10_projects_project_id_direct_costs_id_delete**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/direct_costs/{id} | Delete Direct Cost Item
[**rest_v10_projects_project_id_direct_costs_id_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_id_get) | **GET** /rest/v1.0/projects/{project_id}/direct_costs/{id} | Show Direct Cost Item
[**rest_v10_projects_project_id_direct_costs_id_patch**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/direct_costs/{id} | Update Direct Cost Item
[**rest_v10_projects_project_id_direct_costs_line_items_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_line_items_get) | **GET** /rest/v1.0/projects/{project_id}/direct_costs/line_items | List All Direct Cost Line Items
[**rest_v10_projects_project_id_direct_costs_line_items_sync_patch**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_line_items_sync_patch) | **PATCH** /rest/v1.0/projects/{project_id}/direct_costs/line_items/sync | Sync Direct Cost Line Items
[**rest_v10_projects_project_id_direct_costs_post**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_post) | **POST** /rest/v1.0/projects/{project_id}/direct_costs | Create Direct Cost Item
[**rest_v10_projects_project_id_direct_costs_sync_patch**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v10_projects_project_id_direct_costs_sync_patch) | **PATCH** /rest/v1.0/projects/{project_id}/direct_costs/sync | Sync Direct Cost Items
[**rest_v11_projects_project_id_direct_costs_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v11_projects_project_id_direct_costs_get) | **GET** /rest/v1.1/projects/{project_id}/direct_costs | List Direct Cost Items
[**rest_v11_projects_project_id_direct_costs_id_delete**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v11_projects_project_id_direct_costs_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/direct_costs/{id} | Delete Direct Cost Item
[**rest_v11_projects_project_id_direct_costs_id_get**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v11_projects_project_id_direct_costs_id_get) | **GET** /rest/v1.1/projects/{project_id}/direct_costs/{id} | Show Direct Cost Item
[**rest_v11_projects_project_id_direct_costs_id_patch**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v11_projects_project_id_direct_costs_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/direct_costs/{id} | Update Direct Cost Item
[**rest_v11_projects_project_id_direct_costs_post**](ConstructionFinancialsDirectCostDirectCostsApi.md#rest_v11_projects_project_id_direct_costs_post) | **POST** /rest/v1.1/projects/{project_id}/direct_costs | Create Direct Cost Item


# **rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get**
> List[RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner] rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get(procore_company_id, project_id, direct_cost_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)

List Direct Cost Line Items

Return a list of all Direct Cost Line Items.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_id = 56 # int | ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_line_item_type_id = 56 # int | Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. (optional)

    try:
        # List Direct Cost Line Items
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get(procore_company_id, project_id, direct_cost_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_id** | **int**| ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_cost_code_id** | **str**| Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. | [optional] 
 **filters_line_item_type_id** | **int**| Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner]**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete**
> rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete(procore_company_id, project_id, direct_cost_id, id)

Delete a Direct Cost Line Item

Delete a specified Direct Cost Line Item.

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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_id = 56 # int | ID
    id = 56 # int | Direct Cost Line Item ID

    try:
        # Delete a Direct Cost Line Item
        api_instance.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete(procore_company_id, project_id, direct_cost_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_id** | **int**| ID | 
 **id** | **int**| Direct Cost Line Item ID | 

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

# **rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get**
> RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get(procore_company_id, project_id, direct_cost_id, id)

Show Direct Cost Line Item

Returns detailed information on a Direct Cost Line Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_id = 56 # int | ID
    id = 56 # int | Direct Cost Line Item ID

    try:
        # Show Direct Cost Line Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get(procore_company_id, project_id, direct_cost_id, id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_id** | **int**| ID | 
 **id** | **int**| Direct Cost Line Item ID | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch**
> RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch(procore_company_id, project_id, direct_cost_id, id, body94)

Update Direct Cost Line Item

Update a Direct Cost Line Item. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.body94 import Body94
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_id = 56 # int | ID
    id = 56 # int | Direct Cost Line Item ID
    body94 = procore_sdk.Body94() # Body94 | 

    try:
        # Update Direct Cost Line Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch(procore_company_id, project_id, direct_cost_id, id, body94)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_id** | **int**| ID | 
 **id** | **int**| Direct Cost Line Item ID | 
 **body94** | [**Body94**](Body94.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.md)

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post**
> RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post(procore_company_id, project_id, direct_cost_id, body94)

Create Direct Cost Line Item

Create a new Direct Cost Line Item. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.body94 import Body94
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_id = 56 # int | ID
    body94 = procore_sdk.Body94() # Body94 | 

    try:
        # Create Direct Cost Line Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post(procore_company_id, project_id, direct_cost_id, body94)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_id** | **int**| ID | 
 **body94** | [**Body94**](Body94.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.md)

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_direct_costs_get**
> List[RestV11ProjectsProjectIdDirectCostsGet200ResponseInner] rest_v10_projects_project_id_direct_costs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_invoice_number=filters_invoice_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_payment_date=filters_payment_date, filters_received_date=filters_received_date)

List Direct Cost Items

Returns a list of all Direct Cost Items for a Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.  Note: In addition to the values documented below for the **direct_cost_type** attribute, an enum value of `subcontractor_invoice` is also allowed. To enable this feature in the Procore web application, contact [apisupport@procore.com](mailto:apisupport@procore.com).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_get200_response_inner import RestV11ProjectsProjectIdDirectCostsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_invoice_number = 'filters_invoice_number_example' # str | Returns item(s) with the specified Invoice Number. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_payment_date = 'filters_payment_date_example' # str | Returns item(s) with a payment date within the specified ISO 8601 datetime range. (optional)
    filters_received_date = 'filters_received_date_example' # str | Returns item(s) with a received date within the specified ISO 8601 datetime range. (optional)

    try:
        # List Direct Cost Items
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_invoice_number=filters_invoice_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_payment_date=filters_payment_date, filters_received_date=filters_received_date)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_invoice_number** | **str**| Returns item(s) with the specified Invoice Number. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_payment_date** | **str**| Returns item(s) with a payment date within the specified ISO 8601 datetime range. | [optional] 
 **filters_received_date** | **str**| Returns item(s) with a received date within the specified ISO 8601 datetime range. | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdDirectCostsGet200ResponseInner]**](RestV11ProjectsProjectIdDirectCostsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_direct_costs_id_delete**
> RestV11ProjectsProjectIdDirectCostsIdDelete200Response rest_v10_projects_project_id_direct_costs_id_delete(procore_company_id, project_id, id)

Delete Direct Cost Item

Delete a specific Direct Cost Item and its Line Items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_id_delete200_response import RestV11ProjectsProjectIdDirectCostsIdDelete200Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Delete Direct Cost Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_id_delete(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV11ProjectsProjectIdDirectCostsIdDelete200Response**](RestV11ProjectsProjectIdDirectCostsIdDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Direct Cost Item ID |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_direct_costs_id_get**
> RestV10ProjectsProjectIdDirectCostsPost201Response rest_v10_projects_project_id_direct_costs_id_get(procore_company_id, project_id, id)

Show Direct Cost Item

Show detail on specified Direct Cost Item.  Note: In addition to the values documented below for the **direct_cost_type** attribute, an enum value of `subcontractor_invoice` is also allowed. To enable this feature in the Procore web application, contact [apisupport@procore.com](mailto:apisupport@procore.com).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_post201_response import RestV10ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Direct Cost Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_id_get(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsPost201Response**](RestV10ProjectsProjectIdDirectCostsPost201Response.md)

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

# **rest_v10_projects_project_id_direct_costs_id_patch**
> RestV10ProjectsProjectIdDirectCostsPost201Response rest_v10_projects_project_id_direct_costs_id_patch(procore_company_id, project_id, id, body97)

Update Direct Cost Item

Update a specific Direct Cost Item.

### Example


```python
import procore_sdk
from procore_sdk.models.body97 import Body97
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_post201_response import RestV10ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    body97 = procore_sdk.Body97() # Body97 | 

    try:
        # Update Direct Cost Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_id_patch(procore_company_id, project_id, id, body97)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **body97** | [**Body97**](Body97.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsPost201Response**](RestV10ProjectsProjectIdDirectCostsPost201Response.md)

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

# **rest_v10_projects_project_id_direct_costs_line_items_get**
> List[RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner] rest_v10_projects_project_id_direct_costs_line_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_direct_cost_id=filters_direct_cost_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)

List All Direct Cost Line Items

Return a list of all Direct Cost Line Items.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_direct_cost_id = 56 # int | Return item(s) with the specified Direct Cost ID or range of Direct Cost IDs. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_line_item_type_id = 56 # int | Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. (optional)

    try:
        # List All Direct Cost Line Items
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_line_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_direct_cost_id=filters_direct_cost_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_direct_cost_id** | **int**| Return item(s) with the specified Direct Cost ID or range of Direct Cost IDs. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_cost_code_id** | **str**| Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. | [optional] 
 **filters_line_item_type_id** | **int**| Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner]**](RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_direct_costs_line_items_sync_patch**
> ArrayOfDirectCostLineItems rest_v10_projects_project_id_direct_costs_line_items_sync_patch(procore_company_id, project_id, direct_cost_line_item_sync_body)

Sync Direct Cost Line Items

This endpoint creates or updates a batch of Direct Cost Line Items. For this endpoint either wbs_code_id or cost_code_id and line_item_type_id are required when creating a line item. If both wbs_code_id and cost_code_id are provided, the endpoint will use wbs_code_id. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_direct_cost_line_items import ArrayOfDirectCostLineItems
from procore_sdk.models.direct_cost_line_item_sync_body import DirectCostLineItemSyncBody
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    direct_cost_line_item_sync_body = procore_sdk.DirectCostLineItemSyncBody() # DirectCostLineItemSyncBody | 

    try:
        # Sync Direct Cost Line Items
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_line_items_sync_patch(procore_company_id, project_id, direct_cost_line_item_sync_body)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_line_items_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_line_items_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **direct_cost_line_item_sync_body** | [**DirectCostLineItemSyncBody**](DirectCostLineItemSyncBody.md)|  | 

### Return type

[**ArrayOfDirectCostLineItems**](ArrayOfDirectCostLineItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Direct Cost Line Items |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_direct_costs_post**
> RestV10ProjectsProjectIdDirectCostsPost201Response rest_v10_projects_project_id_direct_costs_post(procore_company_id, project_id, body95)

Create Direct Cost Item

Create a new Direct Cost Item in the specified Project.  Note: In addition to the values documented below for the **direct_cost_type** attribute, an enum value of `subcontractor_invoice` is also allowed. To enable this feature in the Procore web application, contact [apisupport@procore.com](mailto:apisupport@procore.com).

### Example


```python
import procore_sdk
from procore_sdk.models.body95 import Body95
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_post201_response import RestV10ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body95 = procore_sdk.Body95() # Body95 | 

    try:
        # Create Direct Cost Item
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_post(procore_company_id, project_id, body95)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body95** | [**Body95**](Body95.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDirectCostsPost201Response**](RestV10ProjectsProjectIdDirectCostsPost201Response.md)

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

# **rest_v10_projects_project_id_direct_costs_sync_patch**
> ArrayOfDirectCostItems rest_v10_projects_project_id_direct_costs_sync_patch(procore_company_id, project_id, body96)

Sync Direct Cost Items

This endpoint creates or updates a batch of Direct Cost Items. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.  Note: In addition to the values documented below for the **direct_cost_type** attribute, an enum value of `subcontractor_invoice` is also allowed. To enable this feature in the Procore web application, contact [apisupport@procore.com](mailto:apisupport@procore.com).

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_direct_cost_items import ArrayOfDirectCostItems
from procore_sdk.models.body96 import Body96
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body96 = procore_sdk.Body96() # Body96 | 

    try:
        # Sync Direct Cost Items
        api_response = api_instance.rest_v10_projects_project_id_direct_costs_sync_patch(procore_company_id, project_id, body96)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v10_projects_project_id_direct_costs_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body96** | [**Body96**](Body96.md)|  | 

### Return type

[**ArrayOfDirectCostItems**](ArrayOfDirectCostItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Direct Cost Items |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_direct_costs_get**
> List[RestV11ProjectsProjectIdDirectCostsGet200ResponseInner] rest_v11_projects_project_id_direct_costs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_invoice_number=filters_invoice_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_payment_date=filters_payment_date, filters_received_date=filters_received_date)

List Direct Cost Items

Returns a list of all Direct Cost Items for a Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_get200_response_inner import RestV11ProjectsProjectIdDirectCostsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_invoice_number = 'filters_invoice_number_example' # str | Returns item(s) with the specified Invoice Number. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_payment_date = 'filters_payment_date_example' # str | Returns item(s) with a payment date within the specified ISO 8601 datetime range. (optional)
    filters_received_date = 'filters_received_date_example' # str | Returns item(s) with a received date within the specified ISO 8601 datetime range. (optional)

    try:
        # List Direct Cost Items
        api_response = api_instance.rest_v11_projects_project_id_direct_costs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_origin_id=filters_origin_id, filters_invoice_number=filters_invoice_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_payment_date=filters_payment_date, filters_received_date=filters_received_date)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_invoice_number** | **str**| Returns item(s) with the specified Invoice Number. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_payment_date** | **str**| Returns item(s) with a payment date within the specified ISO 8601 datetime range. | [optional] 
 **filters_received_date** | **str**| Returns item(s) with a received date within the specified ISO 8601 datetime range. | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdDirectCostsGet200ResponseInner]**](RestV11ProjectsProjectIdDirectCostsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_direct_costs_id_delete**
> RestV11ProjectsProjectIdDirectCostsIdDelete200Response rest_v11_projects_project_id_direct_costs_id_delete(procore_company_id, project_id, id)

Delete Direct Cost Item

Delete a specific Direct Cost Item and its Line Items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_id_delete200_response import RestV11ProjectsProjectIdDirectCostsIdDelete200Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Delete Direct Cost Item
        api_response = api_instance.rest_v11_projects_project_id_direct_costs_id_delete(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV11ProjectsProjectIdDirectCostsIdDelete200Response**](RestV11ProjectsProjectIdDirectCostsIdDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Direct Cost Item ID |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_direct_costs_id_get**
> RestV11ProjectsProjectIdDirectCostsPost201Response rest_v11_projects_project_id_direct_costs_id_get(procore_company_id, project_id, id)

Show Direct Cost Item

Show detail on specified Direct Cost Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_post201_response import RestV11ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Direct Cost Item
        api_response = api_instance.rest_v11_projects_project_id_direct_costs_id_get(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV11ProjectsProjectIdDirectCostsPost201Response**](RestV11ProjectsProjectIdDirectCostsPost201Response.md)

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

# **rest_v11_projects_project_id_direct_costs_id_patch**
> RestV11ProjectsProjectIdDirectCostsPost201Response rest_v11_projects_project_id_direct_costs_id_patch(procore_company_id, project_id, id, body93)

Update Direct Cost Item

Update a specific Direct Cost Item. The number of Line Items that can be sent in a single update request is limited to 100.

### Example


```python
import procore_sdk
from procore_sdk.models.body93 import Body93
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_post201_response import RestV11ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    body93 = procore_sdk.Body93() # Body93 | 

    try:
        # Update Direct Cost Item
        api_response = api_instance.rest_v11_projects_project_id_direct_costs_id_patch(procore_company_id, project_id, id, body93)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **body93** | [**Body93**](Body93.md)|  | 

### Return type

[**RestV11ProjectsProjectIdDirectCostsPost201Response**](RestV11ProjectsProjectIdDirectCostsPost201Response.md)

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

# **rest_v11_projects_project_id_direct_costs_post**
> RestV11ProjectsProjectIdDirectCostsPost201Response rest_v11_projects_project_id_direct_costs_post(procore_company_id, project_id, body92)

Create Direct Cost Item

Create a new Direct Cost Item in the specified Project. The number of Line Items that can be sent in a single create request is limited to 100.

### Example


```python
import procore_sdk
from procore_sdk.models.body92 import Body92
from procore_sdk.models.rest_v11_projects_project_id_direct_costs_post201_response import RestV11ProjectsProjectIdDirectCostsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsDirectCostDirectCostsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body92 = procore_sdk.Body92() # Body92 | 

    try:
        # Create Direct Cost Item
        api_response = api_instance.rest_v11_projects_project_id_direct_costs_post(procore_company_id, project_id, body92)
        print("The response of ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsDirectCostDirectCostsApi->rest_v11_projects_project_id_direct_costs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body92** | [**Body92**](Body92.md)|  | 

### Return type

[**RestV11ProjectsProjectIdDirectCostsPost201Response**](RestV11ProjectsProjectIdDirectCostsPost201Response.md)

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

