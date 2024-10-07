# procore_sdk.ConstructionFinancialsInvoicingInvoicingAsyncJobsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_invoices_async_jobs_uuid_get**](ConstructionFinancialsInvoicingInvoicingAsyncJobsApi.md#rest_v10_companies_company_id_invoices_async_jobs_uuid_get) | **GET** /rest/v1.0/companies/{company_id}/invoices/async_jobs/{uuid} | Show an Async Job for a Company


# **rest_v10_companies_company_id_invoices_async_jobs_uuid_get**
> RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response rest_v10_companies_company_id_invoices_async_jobs_uuid_get(procore_company_id, uuid, company_id)

Show an Async Job for a Company

Return detailed information about a specified Async Job.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_invoices_async_jobs_uuid_get200_response import RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsInvoicingInvoicingAsyncJobsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    uuid = '329e09cc-315b-42c8-9ffe-4a328017f747' # str | UUID of the Async Job
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show an Async Job for a Company
        api_response = api_instance.rest_v10_companies_company_id_invoices_async_jobs_uuid_get(procore_company_id, uuid, company_id)
        print("The response of ConstructionFinancialsInvoicingInvoicingAsyncJobsApi->rest_v10_companies_company_id_invoices_async_jobs_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsInvoicingInvoicingAsyncJobsApi->rest_v10_companies_company_id_invoices_async_jobs_uuid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **uuid** | **str**| UUID of the Async Job | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response**](RestV10CompaniesCompanyIdInvoicesAsyncJobsUuidGet200Response.md)

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

