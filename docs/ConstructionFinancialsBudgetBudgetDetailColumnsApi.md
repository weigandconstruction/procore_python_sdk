# procore_sdk.ConstructionFinancialsBudgetBudgetDetailColumnsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_views_budget_view_id_budget_detail_columns_get**](ConstructionFinancialsBudgetBudgetDetailColumnsApi.md#rest_v10_budget_views_budget_view_id_budget_detail_columns_get) | **GET** /rest/v1.0/budget_views/{budget_view_id}/budget_detail_columns | List Budget Detail Columns


# **rest_v10_budget_views_budget_view_id_budget_detail_columns_get**
> List[RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner] rest_v10_budget_views_budget_view_id_budget_detail_columns_get(procore_company_id, budget_view_id, project_id)

List Budget Detail Columns

Return a list of columns relevant to a Budget View for a Budget Detail Report.  Note: The ID field of each Budget Column will appear as keys in rows returned by the List Budget Details API.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_views_budget_view_id_budget_detail_columns_get200_response_inner import RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetDetailColumnsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    budget_view_id = 56 # int | Budget View ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Budget Detail Columns
        api_response = api_instance.rest_v10_budget_views_budget_view_id_budget_detail_columns_get(procore_company_id, budget_view_id, project_id)
        print("The response of ConstructionFinancialsBudgetBudgetDetailColumnsApi->rest_v10_budget_views_budget_view_id_budget_detail_columns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetDetailColumnsApi->rest_v10_budget_views_budget_view_id_budget_detail_columns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **budget_view_id** | **int**| Budget View ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner]**](RestV10BudgetViewsBudgetViewIdBudgetDetailColumnsGet200ResponseInner.md)

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

