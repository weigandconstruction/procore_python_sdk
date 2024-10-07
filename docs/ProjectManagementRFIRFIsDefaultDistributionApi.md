# procore_sdk.ProjectManagementRFIRFIsDefaultDistributionApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_rfis_default_distribution_get**](ProjectManagementRFIRFIsDefaultDistributionApi.md#rest_v10_projects_project_id_rfis_default_distribution_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/default_distribution | List RFI Default Distribution


# **rest_v10_projects_project_id_rfis_default_distribution_get**
> List[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner] rest_v10_projects_project_id_rfis_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)

List RFI Default Distribution

Returns a list of contacts that comprise the RFI default distribution

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_default_distribution_get200_response_inner import RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsDefaultDistributionApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List RFI Default Distribution
        api_response = api_instance.rest_v10_projects_project_id_rfis_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementRFIRFIsDefaultDistributionApi->rest_v10_projects_project_id_rfis_default_distribution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsDefaultDistributionApi->rest_v10_projects_project_id_rfis_default_distribution_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner]**](RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

