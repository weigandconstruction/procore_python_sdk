# procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get**](ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get) | **GET** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/line_item_contract_details | List Purchase Order Contract detail line items
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete**](ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete) | **DELETE** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/line_item_contract_details/{id} | Delete Purchase Order Contract detail line item
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get**](ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get) | **GET** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/line_item_contract_details/{id} | Show Purchase Order Contract detail line item
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch**](ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch) | **PATCH** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/line_item_contract_details/{id} | Update Purchase Order Contract detail line item
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post**](ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post) | **POST** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/line_item_contract_details | Create Purchase Order Contract detail line item


# **rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get**
> List[RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsGet200ResponseInner] rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get(procore_company_id, purchase_order_contract_id, project_id, filters_id=filters_id, filters_line_item_id=filters_line_item_id)

List Purchase Order Contract detail line items

List Detail Line Items on a given Purchase Order Contract

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_line_item_id = 56 # int | Line Item ID. Returns item(s) with the specified Line Item ID or within a range of Line Item IDs. (optional)

    try:
        # List Purchase Order Contract detail line items
        api_response = api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get(procore_company_id, purchase_order_contract_id, project_id, filters_id=filters_id, filters_line_item_id=filters_line_item_id)
        print("The response of ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
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

# **rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete**
> rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete(procore_company_id, purchase_order_contract_id, id, project_id)

Delete Purchase Order Contract detail line item

Delete a Detail Line Item in a specific Purchase Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Purchase Order Contract detail line item
        api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete(procore_company_id, purchase_order_contract_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
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

# **rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get(procore_company_id, purchase_order_contract_id, id, project_id)

Show Purchase Order Contract detail line item

Return a Detail Line Item in a specific Purchase Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Purchase Order Contract detail line item
        api_response = api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get(procore_company_id, purchase_order_contract_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
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

# **rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch(procore_company_id, purchase_order_contract_id, id, body4)

Update Purchase Order Contract detail line item

Update a Detail Line Item in a specific Purchase Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    id = 56 # int | ID
    body4 = procore_sdk.Body4() # Body4 | 

    try:
        # Update Purchase Order Contract detail line item
        api_response = api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch(procore_company_id, purchase_order_contract_id, id, body4)
        print("The response of ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
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

# **rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post**
> RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post(procore_company_id, purchase_order_contract_id, body4)

Create Purchase Order Contract detail line item

Creates a Detail Line Item on a given Purchase Order Contract Line Item

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    body4 = procore_sdk.Body4() # Body4 | 

    try:
        # Create Purchase Order Contract detail line item
        api_response = api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post(procore_company_id, purchase_order_contract_id, body4)
        print("The response of ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractDetailLineItemsApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_line_item_contract_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
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

