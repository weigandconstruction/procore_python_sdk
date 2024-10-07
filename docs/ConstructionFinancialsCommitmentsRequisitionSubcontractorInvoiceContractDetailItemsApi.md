# procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_requisition_id_contract_detail_items_get**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi.md#rest_v10_requisitions_requisition_id_contract_detail_items_get) | **GET** /rest/v1.0/requisitions/{requisition_id}/contract_detail_items | List Requisition (Subcontractor Invoice) Contract Detail Items
[**rest_v10_requisitions_requisition_id_contract_detail_items_id_get**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi.md#rest_v10_requisitions_requisition_id_contract_detail_items_id_get) | **GET** /rest/v1.0/requisitions/{requisition_id}/contract_detail_items/{id} | Show Requisition (Subcontractor Invoice) Contract Detail Item
[**rest_v10_requisitions_requisition_id_contract_detail_items_id_patch**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi.md#rest_v10_requisitions_requisition_id_contract_detail_items_id_patch) | **PATCH** /rest/v1.0/requisitions/{requisition_id}/contract_detail_items/{id} | Update Requisition (Subcontractor Invoice) Contract Detail Item


# **rest_v10_requisitions_requisition_id_contract_detail_items_get**
> List[RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner] rest_v10_requisitions_requisition_id_contract_detail_items_get(procore_company_id, requisition_id, project_id, page=page, per_page=per_page)

List Requisition (Subcontractor Invoice) Contract Detail Items

Return a list of Requisition (Subcontractor Invoice) Contract Detail Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_contract_detail_items_get200_response_inner import RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Requisition (Subcontractor Invoice) Contract Detail Items
        api_response = api_instance.rest_v10_requisitions_requisition_id_contract_detail_items_get(procore_company_id, requisition_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner]**](RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requisitions_requisition_id_contract_detail_items_id_get**
> RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner rest_v10_requisitions_requisition_id_contract_detail_items_id_get(procore_company_id, requisition_id, id, project_id)

Show Requisition (Subcontractor Invoice) Contract Detail Item

Return a Requisition (Subcontractor Invoice) Contract Detail Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_contract_detail_items_get200_response_inner import RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    id = 56 # int | Contract Detail Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Requisition (Subcontractor Invoice) Contract Detail Item
        api_response = api_instance.rest_v10_requisitions_requisition_id_contract_detail_items_id_get(procore_company_id, requisition_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **id** | **int**| Contract Detail Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner**](RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner.md)

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

# **rest_v10_requisitions_requisition_id_contract_detail_items_id_patch**
> RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner rest_v10_requisitions_requisition_id_contract_detail_items_id_patch(procore_company_id, requisition_id, id, project_id, body24)

Update Requisition (Subcontractor Invoice) Contract Detail Item

This is a deprecated endpoint, please use [/rest/v1.0/requisitions/{requisition_id}/bulk_item_update](bulk-update-subcontractor-invoice-requisition-items#bulk-update-subcontractor-invoice-requisitions-items)

### Example


```python
import procore_sdk
from procore_sdk.models.body24 import Body24
from procore_sdk.models.rest_v10_requisitions_requisition_id_contract_detail_items_get200_response_inner import RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    id = 56 # int | Contract Detail Item ID
    project_id = 56 # int | Unique identifier for the project.
    body24 = procore_sdk.Body24() # Body24 | 

    try:
        # Update Requisition (Subcontractor Invoice) Contract Detail Item
        api_response = api_instance.rest_v10_requisitions_requisition_id_contract_detail_items_id_patch(procore_company_id, requisition_id, id, project_id, body24)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceContractDetailItemsApi->rest_v10_requisitions_requisition_id_contract_detail_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **id** | **int**| Contract Detail Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body24** | [**Body24**](Body24.md)|  | 

### Return type

[**RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner**](RestV10RequisitionsRequisitionIdContractDetailItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

