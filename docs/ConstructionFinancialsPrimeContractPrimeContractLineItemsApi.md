# procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_prime_contracts_prime_contract_id_line_items_get**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_get) | **GET** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items | List Prime Contract line items
[**rest_v10_prime_contracts_prime_contract_id_line_items_id_delete**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_id_delete) | **DELETE** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items/{id} | Delete a Prime Contract line item
[**rest_v10_prime_contracts_prime_contract_id_line_items_id_get**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_id_get) | **GET** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items/{id} | Show Prime Contract line item
[**rest_v10_prime_contracts_prime_contract_id_line_items_id_patch**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_id_patch) | **PATCH** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items/{id} | Update Prime Contract line item
[**rest_v10_prime_contracts_prime_contract_id_line_items_post**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_post) | **POST** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items | Create Prime Contract line item
[**rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch**](ConstructionFinancialsPrimeContractPrimeContractLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch) | **PATCH** /rest/v1.0/prime_contracts/{prime_contract_id}/line_items/sync | Sync Prime Contract Line Items


# **rest_v10_prime_contracts_prime_contract_id_line_items_get**
> List[Default] rest_v10_prime_contracts_prime_contract_id_line_items_get(procore_company_id, prime_contract_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)

List Prime Contract line items

Return a list of all Line Items for the Prime Contract.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_line_item_type_id = 56 # int | Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. (optional)

    try:
        # List Prime Contract line items
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_get(procore_company_id, prime_contract_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_prime_contracts_prime_contract_id_line_items_id_delete**
> rest_v10_prime_contracts_prime_contract_id_line_items_id_delete(procore_company_id, prime_contract_id, id, project_id)

Delete a Prime Contract line item

Delete a Line Item from the Prime Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    id = 56 # int | Line Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete a Prime Contract line item
        api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_id_delete(procore_company_id, prime_contract_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **id** | **int**| Line Item ID | 
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

# **rest_v10_prime_contracts_prime_contract_id_line_items_id_get**
> Default rest_v10_prime_contracts_prime_contract_id_line_items_id_get(procore_company_id, prime_contract_id, id, project_id)

Show Prime Contract line item

Return a specific Line Item from the Prime Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    id = 56 # int | Line Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Prime Contract line item
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_id_get(procore_company_id, prime_contract_id, id, project_id)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **id** | **int**| Line Item ID | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_prime_contracts_prime_contract_id_line_items_id_patch**
> Default rest_v10_prime_contracts_prime_contract_id_line_items_id_patch(procore_company_id, prime_contract_id, id, project_id, body3)

Update Prime Contract line item

Update a Line Item from the Prime Contract. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    id = 56 # int | Line Item ID
    project_id = 56 # int | Unique identifier for the project.
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Update Prime Contract line item
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_id_patch(procore_company_id, prime_contract_id, id, project_id, body3)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **id** | **int**| Line Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_prime_contracts_prime_contract_id_line_items_post**
> Default rest_v10_prime_contracts_prime_contract_id_line_items_post(procore_company_id, prime_contract_id, project_id, body3)

Create Prime Contract line item

Create a new Line Item for the Prime Contract. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    project_id = 56 # int | Unique identifier for the project.
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Create Prime Contract line item
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_post(procore_company_id, prime_contract_id, project_id, body3)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch(procore_company_id, prime_contract_id, project_id, line_item_sync_body1)

Sync Prime Contract Line Items

Sync Prime Contract Line Items.

### Example


```python
import procore_sdk
from procore_sdk.models.line_item_sync_body1 import LineItemSyncBody1
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch200_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPrimeContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    project_id = 56 # int | Unique identifier for the project.
    line_item_sync_body1 = procore_sdk.LineItemSyncBody1() # LineItemSyncBody1 | 

    try:
        # Sync Prime Contract Line Items
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch(procore_company_id, prime_contract_id, project_id, line_item_sync_body1)
        print("The response of ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPrimeContractLineItemsApi->rest_v10_prime_contracts_prime_contract_id_line_items_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **line_item_sync_body1** | [**LineItemSyncBody1**](LineItemSyncBody1.md)|  | 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response.md)

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
**413** | Payload Too Large |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

