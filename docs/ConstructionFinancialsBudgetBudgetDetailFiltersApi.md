# procore_sdk.ConstructionFinancialsBudgetBudgetDetailFiltersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_detail_filters_get**](ConstructionFinancialsBudgetBudgetDetailFiltersApi.md#rest_v10_budget_detail_filters_get) | **GET** /rest/v1.0/budget_detail_filters | List Budget Detail Filter Options


# **rest_v10_budget_detail_filters_get**
> List[RestV10BudgetDetailFiltersGet200ResponseInner] rest_v10_budget_detail_filters_get(procore_company_id, project_id, column_id)

List Budget Detail Filter Options

Returns a list of valid filter options when given a specific filter type.  Note: When using \"biller\" for column_id, the \"value\" key will contain objects, not integers.  These objects will have a \"type\" field and a \"value\" field. Type indicates whether the biller is a Sub Job or a Project and will be a string. \"value\" contains the ID of the biller and will be an array of integers.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_budget_detail_filters_get200_response_inner import RestV10BudgetDetailFiltersGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetDetailFiltersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    column_id = 'column_id_example' # str | Type of filter options to return

    try:
        # List Budget Detail Filter Options
        api_response = api_instance.rest_v10_budget_detail_filters_get(procore_company_id, project_id, column_id)
        print("The response of ConstructionFinancialsBudgetBudgetDetailFiltersApi->rest_v10_budget_detail_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetDetailFiltersApi->rest_v10_budget_detail_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **column_id** | **str**| Type of filter options to return | 

### Return type

[**List[RestV10BudgetDetailFiltersGet200ResponseInner]**](RestV10BudgetDetailFiltersGet200ResponseInner.md)

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

