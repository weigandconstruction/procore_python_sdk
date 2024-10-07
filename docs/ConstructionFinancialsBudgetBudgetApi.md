# procore_sdk.ConstructionFinancialsBudgetBudgetApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_budget_get**](ConstructionFinancialsBudgetBudgetApi.md#rest_v10_projects_project_id_budget_get) | **GET** /rest/v1.0/projects/{project_id}/budget | Show Budget meta data
[**rest_v10_projects_project_id_budget_lock_delete**](ConstructionFinancialsBudgetBudgetApi.md#rest_v10_projects_project_id_budget_lock_delete) | **DELETE** /rest/v1.0/projects/{project_id}/budget/lock | Delete budget lock
[**rest_v10_projects_project_id_budget_lock_post**](ConstructionFinancialsBudgetBudgetApi.md#rest_v10_projects_project_id_budget_lock_post) | **POST** /rest/v1.0/projects/{project_id}/budget/lock | Create a budget lock


# **rest_v10_projects_project_id_budget_get**
> RestV10ProjectsProjectIdBudgetGet200Response rest_v10_projects_project_id_budget_get(procore_company_id, project_id)

Show Budget meta data

Show meta data for a project's budget

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budget_get200_response import RestV10ProjectsProjectIdBudgetGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Budget meta data
        api_response = api_instance.rest_v10_projects_project_id_budget_get(procore_company_id, project_id)
        print("The response of ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdBudgetGet200Response**](RestV10ProjectsProjectIdBudgetGet200Response.md)

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

# **rest_v10_projects_project_id_budget_lock_delete**
> RestV10ProjectsProjectIdBudgetLockDelete200Response rest_v10_projects_project_id_budget_lock_delete(procore_company_id, project_id, destroy_all_budget_line_item_transfers=destroy_all_budget_line_item_transfers)

Delete budget lock

Unlock the budget

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budget_lock_delete200_response import RestV10ProjectsProjectIdBudgetLockDelete200Response
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    destroy_all_budget_line_item_transfers = True # bool | Allows users to unlock the budget while either preserving or destroying the existing budget modifications. Defaults to 'true' when not included in request. (optional)

    try:
        # Delete budget lock
        api_response = api_instance.rest_v10_projects_project_id_budget_lock_delete(procore_company_id, project_id, destroy_all_budget_line_item_transfers=destroy_all_budget_line_item_transfers)
        print("The response of ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_lock_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_lock_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **destroy_all_budget_line_item_transfers** | **bool**| Allows users to unlock the budget while either preserving or destroying the existing budget modifications. Defaults to &#39;true&#39; when not included in request. | [optional] 

### Return type

[**RestV10ProjectsProjectIdBudgetLockDelete200Response**](RestV10ProjectsProjectIdBudgetLockDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**422** | Unprocesssable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budget_lock_post**
> RestV10ProjectsProjectIdBudgetGet200Response rest_v10_projects_project_id_budget_lock_post(procore_company_id, project_id)

Create a budget lock

Lock the budget

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budget_get200_response import RestV10ProjectsProjectIdBudgetGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Create a budget lock
        api_response = api_instance.rest_v10_projects_project_id_budget_lock_post(procore_company_id, project_id)
        print("The response of ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_lock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetApi->rest_v10_projects_project_id_budget_lock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdBudgetGet200Response**](RestV10ProjectsProjectIdBudgetGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

