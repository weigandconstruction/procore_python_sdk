# procore_sdk.ConstructionFinancialsBudgetAdvancedForecastingApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get**](ConstructionFinancialsBudgetAdvancedForecastingApi.md#rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/advanced_forecastings/rows | Get Advanced Forecasting Rows of a Project
[**rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post**](ConstructionFinancialsBudgetAdvancedForecastingApi.md#rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post) | **POST** /rest/v2.0/companies/{company_id}/projects/{project_id}/advanced_forecastings/rows | Update Advanced Forecasting Rows


# **rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get**
> RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, filters=filters)

Get Advanced Forecasting Rows of a Project

Get Advanced forecasting rows. Each page will have a maximum of 100 items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get_filters_parameter_inner import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetFiltersParameterInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetAdvancedForecastingApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 10 # int | Elements per page (optional) (default to 10)
    filters = [procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetFiltersParameterInner()] # List[RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetFiltersParameterInner] | Structure to filter the result of the advanced forecasting endpoint (optional)

    try:
        # Get Advanced Forecasting Rows of a Project
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, filters=filters)
        print("The response of ConstructionFinancialsBudgetAdvancedForecastingApi->rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetAdvancedForecastingApi->rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] [default to 10]
 **filters** | [**List[RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetFiltersParameterInner]**](RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGetFiltersParameterInner.md)| Structure to filter the result of the advanced forecasting endpoint | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response.md)

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

# **rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post**
> RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post(procore_company_id, company_id, project_id, rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request)

Update Advanced Forecasting Rows

Update Advanced Forecasting Rows

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request import RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetAdvancedForecastingApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request = procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest() # RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest | 

    try:
        # Update Advanced Forecasting Rows
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post(procore_company_id, company_id, project_id, rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request)
        print("The response of ConstructionFinancialsBudgetAdvancedForecastingApi->rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetAdvancedForecastingApi->rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **rest_v20_companies_company_id_projects_project_id_advanced_forecastings_rows_post_request** | [**RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest**](RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsPostRequest.md)|  | 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdAdvancedForecastingsRowsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

