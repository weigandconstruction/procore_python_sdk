# procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationOwnerInvoiceLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch**](ConstructionFinancialsPrimeContractPaymentApplicationOwnerInvoiceLineItemsApi.md#rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch) | **PATCH** /rest/v1.0/prime_contracts/{prime_contract_id}/payment_application_line_items/{id} | Update Payment Application (Owner Invoice) Line Item for Prime Contract


# **rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch**
> RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch(procore_company_id, prime_contract_id, id, body53)

Update Payment Application (Owner Invoice) Line Item for Prime Contract

Update a Payment Application (Owner Invoice) Line Item on a specified Prime Contract Payment Application (Owner Invoice)

### Example


```python
import procore_sdk
from procore_sdk.models.body53 import Body53
from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsPrimeContractPaymentApplicationOwnerInvoiceLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    prime_contract_id = 56 # int | Prime Contract ID
    id = 56 # int | Payment Application (Owner Invoice) Line item ID
    body53 = procore_sdk.Body53() # Body53 | 

    try:
        # Update Payment Application (Owner Invoice) Line Item for Prime Contract
        api_response = api_instance.rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch(procore_company_id, prime_contract_id, id, body53)
        print("The response of ConstructionFinancialsPrimeContractPaymentApplicationOwnerInvoiceLineItemsApi->rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsPrimeContractPaymentApplicationOwnerInvoiceLineItemsApi->rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **prime_contract_id** | **int**| Prime Contract ID | 
 **id** | **int**| Payment Application (Owner Invoice) Line item ID | 
 **body53** | [**Body53**](Body53.md)|  | 

### Return type

[**RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response**](RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response.md)

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

