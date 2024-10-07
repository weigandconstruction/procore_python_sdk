# procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractSubcontractorSOVStatusApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch**](ConstructionFinancialsCommitmentsPurchaseOrderContractSubcontractorSOVStatusApi.md#rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch) | **PATCH** /rest/v1.0/purchase_order_contracts/{purchase_order_contract_id}/subcontractor_schedule_of_values_status | Update Purchase Order Contract Subcontractor SOV status


# **rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch**
> RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch200Response rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch(procore_company_id, purchase_order_contract_id, body2)

Update Purchase Order Contract Subcontractor SOV status

Update the Subcontractor SOV status of a specific Purchase Order Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body2 import Body2
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_subcontractor_schedule_of_values_status_patch200_response import RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsPurchaseOrderContractSubcontractorSOVStatusApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    purchase_order_contract_id = 56 # int | Purchase Order Contract ID
    body2 = procore_sdk.Body2() # Body2 | 

    try:
        # Update Purchase Order Contract Subcontractor SOV status
        api_response = api_instance.rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch(procore_company_id, purchase_order_contract_id, body2)
        print("The response of ConstructionFinancialsCommitmentsPurchaseOrderContractSubcontractorSOVStatusApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsPurchaseOrderContractSubcontractorSOVStatusApi->rest_v10_purchase_order_contracts_purchase_order_contract_id_subcontractor_schedule_of_values_status_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **purchase_order_contract_id** | **int**| Purchase Order Contract ID | 
 **body2** | [**Body2**](Body2.md)|  | 

### Return type

[**RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch200Response**](RestV10WorkOrderContractsWorkOrderContractIdSubcontractorScheduleOfValuesStatusPatch200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

