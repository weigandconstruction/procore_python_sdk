# procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceWholeChangeOrderItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch**](ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceWholeChangeOrderItemsApi.md#rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch) | **PATCH** /rest/v1.0/requisitions/{requisition_id}/whole_change_order_items/{id} | Update Requisition (Subcontractor Invoice) Whole Change Order Item


# **rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch**
> RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch(procore_company_id, requisition_id, id, rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request)

Update Requisition (Subcontractor Invoice) Whole Change Order Item

Update a specific Requisition (Subcontractor Invoice) Whole Change Order Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch200_response import RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response
from procore_sdk.models.rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request import RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceWholeChangeOrderItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    id = 56 # int | Whole Change Order Item ID
    rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request = procore_sdk.RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequest() # RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequest | 

    try:
        # Update Requisition (Subcontractor Invoice) Whole Change Order Item
        api_response = api_instance.rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch(procore_company_id, requisition_id, id, rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request)
        print("The response of ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceWholeChangeOrderItemsApi->rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionSubcontractorInvoiceWholeChangeOrderItemsApi->rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **id** | **int**| Whole Change Order Item ID | 
 **rest_v10_requisitions_requisition_id_whole_change_order_items_id_patch_request** | [**RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequest**](RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatchRequest.md)|  | 

### Return type

[**RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response**](RestV10RequisitionsRequisitionIdWholeChangeOrderItemsIdPatch200Response.md)

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

