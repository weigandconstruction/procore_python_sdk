# procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get**](ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get) | **GET** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_item_contract_details | List Work Order Contract detail line items
[**rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete**](ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete) | **DELETE** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_item_contract_details/{id} | Delete Work Order Contract detail line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get**](ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get) | **GET** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_item_contract_details/{id} | Show Work Order Contract detail line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch**](ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch) | **PATCH** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_item_contract_details/{id} | Update Work Order Contract detail line item
[**rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post**](ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi.md#rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post) | **POST** /rest/v1.0/work_order_contracts/{work_order_contract_id}/line_item_contract_details | Create Work Order Contract detail line item


# **rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get**
> List[RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsGet200ResponseInner] rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get(procore_company_id, work_order_contract_id, project_id, filters_id=filters_id, filters_line_item_id=filters_line_item_id)

List Work Order Contract detail line items

List Detail Line Items on a given Work Order Contract

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get200_response_inner import RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_line_item_id = 56 # int | Line Item ID. Returns item(s) with the specified Line Item ID or within a range of Line Item IDs. (optional)

    try:
        # List Work Order Contract detail line items
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get(procore_company_id, work_order_contract_id, project_id, filters_id=filters_id, filters_line_item_id=filters_line_item_id)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_line_item_id** | **int**| Line Item ID. Returns item(s) with the specified Line Item ID or within a range of Line Item IDs. | [optional] 

### Return type

[**List[RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsGet200ResponseInner]**](RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete**
> rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete(procore_company_id, work_order_contract_id, id, project_id)

Delete Work Order Contract detail line item

Delete a Detail Line Item in a specific Work Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Work Order Contract detail line item
        api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete(procore_company_id, work_order_contract_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_delete: %s\n" % e)
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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get(procore_company_id, work_order_contract_id, id, project_id)

Show Work Order Contract detail line item

Return a Detail Line Item in a specific Work Order Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Work Order Contract detail line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get(procore_company_id, work_order_contract_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response**](RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch(procore_company_id, work_order_contract_id, id, body4)

Update Work Order Contract detail line item

Update a Detail Line Item in a specific Work Order Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body4 import Body4
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    id = 56 # int | ID
    body4 = procore_sdk.Body4() # Body4 | 

    try:
        # Update Work Order Contract detail line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch(procore_company_id, work_order_contract_id, id, body4)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **id** | **int**| ID | 
 **body4** | [**Body4**](Body4.md)|  | 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response**](RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.md)

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

# **rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post(procore_company_id, work_order_contract_id, body4)

Create Work Order Contract detail line item

Creates a Detail Line Item on a given Work Order Contract Line Item

### Example


```python
import procore_sdk
from procore_sdk.models.body4 import Body4
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    work_order_contract_id = 56 # int | Work Order Contract ID
    body4 = procore_sdk.Body4() # Body4 | 

    try:
        # Create Work Order Contract detail line item
        api_response = api_instance.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post(procore_company_id, work_order_contract_id, body4)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractDetailLineItemsApi->rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **work_order_contract_id** | **int**| Work Order Contract ID | 
 **body4** | [**Body4**](Body4.md)|  | 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response**](RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

