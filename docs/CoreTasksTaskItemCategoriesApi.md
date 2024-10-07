# procore_sdk.CoreTasksTaskItemCategoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_projects_project_id_task_item_categories_get**](CoreTasksTaskItemCategoriesApi.md#rest_v10_companies_company_id_projects_project_id_task_item_categories_get) | **GET** /rest/v1.0/companies/{company_id}/projects/{project_id}/task_item_categories | List task item categories


# **rest_v10_companies_company_id_projects_project_id_task_item_categories_get**
> List[RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCategoriesGet200ResponseInner] rest_v10_companies_company_id_projects_project_id_task_item_categories_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, view=view)

List task item categories

Returns a list of task item categories associated with the company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_categories_get200_response_inner import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCategoriesGet200ResponseInner
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
    api_instance = procore_sdk.CoreTasksTaskItemCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | View to use when generating json. Defaults to normal (optional)

    try:
        # List task item categories
        api_response = api_instance.rest_v10_companies_company_id_projects_project_id_task_item_categories_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, view=view)
        print("The response of CoreTasksTaskItemCategoriesApi->rest_v10_companies_company_id_projects_project_id_task_item_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreTasksTaskItemCategoriesApi->rest_v10_companies_company_id_projects_project_id_task_item_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| View to use when generating json. Defaults to normal | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCategoriesGet200ResponseInner]**](RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCategoriesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have required permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

