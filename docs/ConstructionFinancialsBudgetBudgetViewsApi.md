# procore_sdk.ConstructionFinancialsBudgetBudgetViewsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_views_get**](ConstructionFinancialsBudgetBudgetViewsApi.md#rest_v10_budget_views_get) | **GET** /rest/v1.0/budget_views | List Budget Views


# **rest_v10_budget_views_get**
> List[RestV10BudgetViewsGet200ResponseInner] rest_v10_budget_views_get(procore_company_id, project_id, page=page, per_page=per_page)

List Budget Views

Return a list of all Budget Views for a project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_views_get200_response_inner import RestV10BudgetViewsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetViewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Budget Views
        api_response = api_instance.rest_v10_budget_views_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsBudgetBudgetViewsApi->rest_v10_budget_views_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetViewsApi->rest_v10_budget_views_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10BudgetViewsGet200ResponseInner]**](RestV10BudgetViewsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

