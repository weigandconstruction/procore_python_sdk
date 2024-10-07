# procore_sdk.ConstructionFinancialsCommitmentsBulkUpdateSubcontractorInvoiceRequisitionItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_requisition_id_bulk_item_update_patch**](ConstructionFinancialsCommitmentsBulkUpdateSubcontractorInvoiceRequisitionItemsApi.md#rest_v10_requisitions_requisition_id_bulk_item_update_patch) | **PATCH** /rest/v1.0/requisitions/{requisition_id}/bulk_item_update | Bulk Update Subcontractor Invoice (Requisitions) Items


# **rest_v10_requisitions_requisition_id_bulk_item_update_patch**
> rest_v10_requisitions_requisition_id_bulk_item_update_patch(procore_company_id, requisition_id, project_id, body114)

Bulk Update Subcontractor Invoice (Requisitions) Items

Updates all requisition items received in the body. Can be contract items, contract detail items, or change order items.

### Example


```python
import procore_sdk
from procore_sdk.models.body114 import Body114
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBulkUpdateSubcontractorInvoiceRequisitionItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition ID
    project_id = 56 # int | Unique identifier for the project.
    body114 = procore_sdk.Body114() # Body114 | 

    try:
        # Bulk Update Subcontractor Invoice (Requisitions) Items
        api_instance.rest_v10_requisitions_requisition_id_bulk_item_update_patch(procore_company_id, requisition_id, project_id, body114)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBulkUpdateSubcontractorInvoiceRequisitionItemsApi->rest_v10_requisitions_requisition_id_bulk_item_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body114** | [**Body114**](Body114.md)|  | 

### Return type

void (empty response body)

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

