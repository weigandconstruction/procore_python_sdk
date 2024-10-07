# procore_sdk.ConstructionFinancialsBudgetBudgetChangeAdjustmentLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get**](ConstructionFinancialsBudgetBudgetChangeAdjustmentLineItemsApi.md#rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/budget_changes/adjustment_line_items | Get Adjustment and Adjustment Line Items of a Project


# **rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get**
> RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200Response rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get(procore_company_id, company_id, project_id, page=page, per_page=per_page)

Get Adjustment and Adjustment Line Items of a Project

Get Adjustment and Adjustment Line Items of a Project. Each page will have a maximum of 100 items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetChangeAdjustmentLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 10 # int | Elements per page (optional) (default to 10)

    try:
        # Get Adjustment and Adjustment Line Items of a Project
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get(procore_company_id, company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsBudgetBudgetChangeAdjustmentLineItemsApi->rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetChangeAdjustmentLineItemsApi->rest_v20_companies_company_id_projects_project_id_budget_changes_adjustment_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] [default to 10]

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdBudgetChangesAdjustmentLineItemsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Link - Link headers for the first, prev, next, and last link <br>  * Page - Number of the page retrieved <br>  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

