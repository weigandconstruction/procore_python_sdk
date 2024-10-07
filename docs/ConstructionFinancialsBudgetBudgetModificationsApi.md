# procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_budget_modifications_get**](ConstructionFinancialsBudgetBudgetModificationsApi.md#rest_v10_projects_project_id_budget_modifications_get) | **GET** /rest/v1.0/projects/{project_id}/budget_modifications | List Budget Modifications
[**rest_v10_projects_project_id_budget_modifications_id_delete**](ConstructionFinancialsBudgetBudgetModificationsApi.md#rest_v10_projects_project_id_budget_modifications_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/budget_modifications/{id} | Delete Budget Modification
[**rest_v10_projects_project_id_budget_modifications_id_get**](ConstructionFinancialsBudgetBudgetModificationsApi.md#rest_v10_projects_project_id_budget_modifications_id_get) | **GET** /rest/v1.0/projects/{project_id}/budget_modifications/{id} | Show Budget Modification
[**rest_v10_projects_project_id_budget_modifications_id_patch**](ConstructionFinancialsBudgetBudgetModificationsApi.md#rest_v10_projects_project_id_budget_modifications_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/budget_modifications/{id} | Update Budget Modification
[**rest_v10_projects_project_id_budget_modifications_post**](ConstructionFinancialsBudgetBudgetModificationsApi.md#rest_v10_projects_project_id_budget_modifications_post) | **POST** /rest/v1.0/projects/{project_id}/budget_modifications | Create Budget Modification


# **rest_v10_projects_project_id_budget_modifications_get**
> List[RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner] rest_v10_projects_project_id_budget_modifications_get(procore_company_id, project_id, page=page, per_page=per_page)

List Budget Modifications

Returns a list of all Budget Modifications for a project. For more information on the Budget Changes API, see our documentation on [upgrading from the Budget Modifications API to the Budget Changes API](https://developers.procore.com/documentation/tutorial-budget-changes-api).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budget_modifications_get200_response_inner import RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Budget Modifications
        api_response = api_instance.rest_v10_projects_project_id_budget_modifications_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner]**](RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_budget_modifications_id_delete**
> rest_v10_projects_project_id_budget_modifications_id_delete(procore_company_id, project_id, id)

Delete Budget Modification

Delete a Budget Modification only if Budget Changes are not enabled. This endpoint will be deprecated at October 16th of 2023. For more information on the Budget Changes API, see our documentation on [upgrading from the Budget Modifications API to the Budget Changes API](https://developers.procore.com/documentation/tutorial-budget-changes-api).

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Delete Budget Modification
        api_instance.rest_v10_projects_project_id_budget_modifications_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

void (empty response body)

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budget_modifications_id_get**
> RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner rest_v10_projects_project_id_budget_modifications_id_get(procore_company_id, project_id, id)

Show Budget Modification

Returns detailed information on a specified Budget Modification. For more information on the Budget Changes API, see our documentation on [upgrading from the Budget Modifications API to the Budget Changes API](https://developers.procore.com/documentation/tutorial-budget-changes-api).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budget_modifications_get200_response_inner import RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Budget Modification
        api_response = api_instance.rest_v10_projects_project_id_budget_modifications_id_get(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner**](RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.md)

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budget_modifications_id_patch**
> RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner rest_v10_projects_project_id_budget_modifications_id_patch(procore_company_id, project_id, id, body115)

Update Budget Modification

Update a Budget Modification only if Budget Changes are not enabled. This endpoint will be deprecated at October 16th of 2023. For more information on the Budget Changes API, see our documentation on [upgrading from the Budget Modifications API to the Budget Changes API](https://developers.procore.com/documentation/tutorial-budget-changes-api).

### Example


```python
import procore_sdk
from procore_sdk.models.body115 import Body115
from procore_sdk.models.rest_v10_projects_project_id_budget_modifications_get200_response_inner import RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    body115 = procore_sdk.Body115() # Body115 | 

    try:
        # Update Budget Modification
        api_response = api_instance.rest_v10_projects_project_id_budget_modifications_id_patch(procore_company_id, project_id, id, body115)
        print("The response of ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **body115** | [**Body115**](Body115.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner**](RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budget_modifications_post**
> RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner rest_v10_projects_project_id_budget_modifications_post(procore_company_id, project_id, body115)

Create Budget Modification

Creates a Budget Modification only if Budget Changes are not enabled. This endpoint will be deprecated at October 16th of 2023. For more information on the Budget Changes API, see our documentation on [upgrading from the Budget Modifications API to the Budget Changes API](https://developers.procore.com/documentation/tutorial-budget-changes-api).

### Example


```python
import procore_sdk
from procore_sdk.models.body115 import Body115
from procore_sdk.models.rest_v10_projects_project_id_budget_modifications_get200_response_inner import RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetBudgetModificationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body115 = procore_sdk.Body115() # Body115 | 

    try:
        # Create Budget Modification
        api_response = api_instance.rest_v10_projects_project_id_budget_modifications_post(procore_company_id, project_id, body115)
        print("The response of ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetBudgetModificationsApi->rest_v10_projects_project_id_budget_modifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body115** | [**Body115**](Body115.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner**](RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

