# procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_get**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_get) | **GET** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items | List Work Order Contract Line Items
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete) | **DELETE** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items/{id} | Delete Work Order Contract line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get) | **GET** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items/{id} | Show Work Order Contract line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch) | **PATCH** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items/{id} | Update Work Order Contract line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_post**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_post) | **POST** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items | Create Work Order Contract line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch**](ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch) | **PATCH** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_items/sync | Sync Work Order Contract Line Items


# **rest_v10_work_order_contracts_work_order_contract_id_line_items_get**
> List[RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner] rest_v10_work_order_contracts_work_order_contract_id_line_items_get(procore_company_id, work_order_contract_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id, view=view)

List Work Order Contract Line Items

Return a list of all Line Items of a specified Work Order Contract in a specified Project.  Change Event Line Item information is only returned if a line item is associated to a change event line item and user can view change events.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner import RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_line_item_type_id = 56 # int | Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. (optional)
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. 'default' view will be rendered by default if the parameter is not provided. For the 'ssov_source_lines' view lower permissions are acceptable. It's enough to be added to invoice contacts and contract accessors even if SOV line items are hidden from non-admins.  (optional)

    try:
        # List Work Order Contract Line Items
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_get(procore_company_id, work_order_contract_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_cost_code_id=filters_cost_code_id, filters_line_item_type_id=filters_line_item_type_id, view=view)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_cost_code_id** | **str**| Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. | [optional] 
 **filters_line_item_type_id** | **int**| Line Item Type ID. Returns item(s) with the specified Line Item Type ID or range of Line Item Type IDs. | [optional] 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. &#39;default&#39; view will be rendered by default if the parameter is not provided. For the &#39;ssov_source_lines&#39; view lower permissions are acceptable. It&#39;s enough to be added to invoice contacts and contract accessors even if SOV line items are hidden from non-admins.  | [optional] 

### Return type

[**List[RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner]**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner.md)

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

# **rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete**
> rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete(procore_company_id, work_order_contract_id, id, project_id)

Delete Work Order Contract line item

Delete a Line Item in a specific Work Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Work Order Contract line item
        api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete(procore_company_id, work_order_contract_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get(procore_company_id, work_order_contract_id, id, project_id, view=view)

Show Work Order Contract line item

Return a specific Line Item in a specified Work Order Contract.  Change Event Line Item information is only returned if a line item is associated to a change event line item and user can view change events.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_get200_response_inner import RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. 'default' view will be rendered by default if the parameter is not provided. For the 'ssov_source_lines' view lower permissions are acceptable. It's enough to be added to invoice contacts and contract accessors even if SOV line items are hidden from non-admins.  (optional)

    try:
        # Show Work Order Contract line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get(procore_company_id, work_order_contract_id, id, project_id, view=view)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. &#39;default&#39; view will be rendered by default if the parameter is not provided. For the &#39;ssov_source_lines&#39; view lower permissions are acceptable. It&#39;s enough to be added to invoice contacts and contract accessors even if SOV line items are hidden from non-admins.  | [optional] 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsGet200ResponseInner.md)

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

# **rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch**
> Default rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch(procore_company_id, work_order_contract_id, id, body3)

Update Work Order Contract line item

Update a Line Item in a specific Work Order Contract. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Update Work Order Contract line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch(procore_company_id, work_order_contract_id, id, body3)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
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

# **rest_v10_work_order_contracts_work_order_contract_id_line_items_post**
> Default rest_v10_work_order_contracts_work_order_contract_id_line_items_post(procore_company_id, work_order_contract_id, body3)

Create Work Order Contract line item

Create a new Line Item in a specified Work Order Contract. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    body3 = procore_sdk.Body3() # Body3 | 

    try:
        # Create Work Order Contract line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_post(procore_company_id, work_order_contract_id, body3)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
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

# **rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200Response rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch(procore_company_id, work_order_contract_id, project_id, line_item_sync_body)

Sync Work Order Contract Line Items

Sync Work Order Contract Line Items. Note: A budget line item will automatically be created for Non-budgeted line items for all new projects and for projects enabled with Non-Budgeted line item beta functionality

### Example


```python
import procore_sdk
from procore_sdk.models.line_item_sync_body import LineItemSyncBody
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    project_id = 56 # int | Unique identifier for the project.
    line_item_sync_body = procore_sdk.LineItemSyncBody() # LineItemSyncBody | 

    try:
        # Sync Work Order Contract Line Items
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch(procore_company_id, work_order_contract_id, project_id, line_item_sync_body)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **line_item_sync_body** | [**LineItemSyncBody**](LineItemSyncBody.md)|  | 

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
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**413** | Payload Too Large |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

