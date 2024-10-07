# procore_sdk.CoreCompanyCompanyProjectsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_projects_get**](CoreCompanyCompanyProjectsApi.md#rest_v10_companies_company_id_projects_get) | **GET** /rest/v1.0/companies/{company_id}/projects | List company&#39;s projects


# **rest_v10_companies_company_id_projects_get**
> List[Project6] rest_v10_companies_company_id_projects_get(procore_company_id, company_id)

List company's projects

Returns a list of Projects associated with a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.project6 import Project6
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
    api_instance = procore_sdk.CoreCompanyCompanyProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List company's projects
        api_response = api_instance.rest_v10_companies_company_id_projects_get(procore_company_id, company_id)
        print("The response of CoreCompanyCompanyProjectsApi->rest_v10_companies_company_id_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyProjectsApi->rest_v10_companies_company_id_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[Project6]**](Project6.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

