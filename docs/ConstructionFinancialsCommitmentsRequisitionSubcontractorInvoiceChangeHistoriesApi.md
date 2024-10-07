# procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceChangeHistoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_requisition_id_change_histories_get**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceChangeHistoriesApi.md#rest_v10_requisitions_requisition_id_change_histories_get) | **GET** /rest/v1.0/requisitions/{requisition_id}/change_histories | List Requisition (Subcontractor Invoice) Change Histories


# **rest_v10_requisitions_requisition_id_change_histories_get**
> List[RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner] rest_v10_requisitions_requisition_id_change_histories_get(procore_company_id, requisition_id, project_id)

List Requisition (Subcontractor Invoice) Change Histories

Return a list of Requisition (Subcontractor Invoice) Change Histories

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_change_histories_get200_response_inner import RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceChangeHistoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Requisition (Subcontractor Invoice) Change Histories
        api_response = api_instance.rest_v10_requisitions_requisition_id_change_histories_get(procore_company_id, requisition_id, project_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceChangeHistoriesApi->rest_v10_requisitions_requisition_id_change_histories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceChangeHistoriesApi->rest_v10_requisitions_requisition_id_change_histories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner]**](RestV10RequisitionsRequisitionIdChangeHistoriesGet200ResponseInner.md)

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

