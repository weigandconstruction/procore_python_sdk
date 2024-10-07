# procore_sdk.CoreCompanySubmittalStatusesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_submittal_statuses_get**](CoreCompanySubmittalStatusesApi.md#rest_v10_companies_company_id_submittal_statuses_get) | **GET** /rest/v1.0/companies/{company_id}/submittal_statuses | List Submittal Statuses


# **rest_v10_companies_company_id_submittal_statuses_get**
> List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus] rest_v10_companies_company_id_submittal_statuses_get(procore_company_id, company_id, page=page, per_page=per_page)

List Submittal Statuses

Return a list of all Submittal  Statuses from a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_status import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus
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
    api_instance = procore_sdk.CoreCompanySubmittalStatusesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Submittal Statuses
        api_response = api_instance.rest_v10_companies_company_id_submittal_statuses_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanySubmittalStatusesApi->rest_v10_companies_company_id_submittal_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanySubmittalStatusesApi->rest_v10_companies_company_id_submittal_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus]**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Submittal Statuses listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

