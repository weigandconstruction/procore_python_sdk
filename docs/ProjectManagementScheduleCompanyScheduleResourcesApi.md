# procore_sdk.ProjectManagementScheduleCompanyScheduleResourcesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_schedule_resources_get**](ProjectManagementScheduleCompanyScheduleResourcesApi.md#rest_v10_companies_company_id_schedule_resources_get) | **GET** /rest/v1.0/companies/{company_id}/schedule/resources | List Schedule Resources


# **rest_v10_companies_company_id_schedule_resources_get**
> RestV10CompaniesCompanyIdScheduleResourcesGet200Response rest_v10_companies_company_id_schedule_resources_get(procore_company_id, company_id, page=page, per_page=per_page, filters_name=filters_name)

List Schedule Resources

Returns all resources for a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_schedule_resources_get200_response import RestV10CompaniesCompanyIdScheduleResourcesGet200Response
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
    api_instance = procore_sdk.ProjectManagementScheduleCompanyScheduleResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_name = ['filters_name_example'] # List[str] | Filter item(s) with matching name. (optional)

    try:
        # List Schedule Resources
        api_response = api_instance.rest_v10_companies_company_id_schedule_resources_get(procore_company_id, company_id, page=page, per_page=per_page, filters_name=filters_name)
        print("The response of ProjectManagementScheduleCompanyScheduleResourcesApi->rest_v10_companies_company_id_schedule_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementScheduleCompanyScheduleResourcesApi->rest_v10_companies_company_id_schedule_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_name** | [**List[str]**](str.md)| Filter item(s) with matching name. | [optional] 

### Return type

[**RestV10CompaniesCompanyIdScheduleResourcesGet200Response**](RestV10CompaniesCompanyIdScheduleResourcesGet200Response.md)

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
**403** | User does not have right permissions |  -  |
**404** | Endpoint not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

