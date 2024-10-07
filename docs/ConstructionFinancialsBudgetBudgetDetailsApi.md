# procore_sdk.ConstructionFinancialsBudgetBudgetDetailsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_budget_views_budget_view_id_budget_details_post**](ConstructionFinancialsBudgetBudgetDetailsApi.md#rest_v10_budget_views_budget_view_id_budget_details_post) | **POST** /rest/v1.0/budget_views/{budget_view_id}/budget_details | List Budget Details


# **rest_v10_budget_views_budget_view_id_budget_details_post**
> List[RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner] rest_v10_budget_views_budget_view_id_budget_details_post(procore_company_id, budget_view_id, project_id, budget_details_body)

List Budget Details

Return a list of all rows from the Budget Detail Report for a Project and Budget View.  Note: In addition to all the fields outlined in the response example, there will be an additional key for each visible, non-formula, non-qualitative column (Ex: Original Budget Amount, Budget Modifications, Forecast to Complete, and Source Columns).  The integer keys returned represent the IDs of the budget columns which are returned by the Budget Detail Columns API.  As well, valid filter values can be found through the Budget Detail Filter Options API.

### Example


```python
import procore_sdk
from procore_sdk.models.budget_details_body import BudgetDetailsBody
from procore_sdk.models.rest_v10_budget_views_budget_view_id_budget_details_post200_response_inner import RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetDetailsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    budget_view_id = 56 # int | Budget View ID
    project_id = 56 # int | Unique identifier for the project.
    budget_details_body = procore_sdk.BudgetDetailsBody() # BudgetDetailsBody | 

    try:
        # List Budget Details
        api_response = api_instance.rest_v10_budget_views_budget_view_id_budget_details_post(procore_company_id, budget_view_id, project_id, budget_details_body)
        print("The response of ConstructionFinancialsBudgetBudgetDetailsApi->rest_v10_budget_views_budget_view_id_budget_details_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetDetailsApi->rest_v10_budget_views_budget_view_id_budget_details_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **budget_view_id** | **int**| Budget View ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **budget_details_body** | [**BudgetDetailsBody**](BudgetDetailsBody.md)|  | 

### Return type

[**List[RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner]**](RestV10BudgetViewsBudgetViewIdBudgetDetailsPost200ResponseInner.md)

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
**408** | Request Timeout |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

