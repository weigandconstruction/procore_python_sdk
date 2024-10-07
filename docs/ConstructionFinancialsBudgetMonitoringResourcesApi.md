# procore_sdk.ConstructionFinancialsBudgetMonitoringResourcesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_monitoring_resources_get**](ConstructionFinancialsBudgetMonitoringResourcesApi.md#rest_v10_projects_project_id_monitoring_resources_get) | **GET** /rest/v1.0/projects/{project_id}/monitoring_resources | List Monitoring Resources
[**rest_v10_projects_project_id_monitoring_resources_id_delete**](ConstructionFinancialsBudgetMonitoringResourcesApi.md#rest_v10_projects_project_id_monitoring_resources_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/monitoring_resources/{id} | Delete Monitoring Resource
[**rest_v10_projects_project_id_monitoring_resources_id_patch**](ConstructionFinancialsBudgetMonitoringResourcesApi.md#rest_v10_projects_project_id_monitoring_resources_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/monitoring_resources/{id} | Update Monitoring Resource
[**rest_v10_projects_project_id_monitoring_resources_post**](ConstructionFinancialsBudgetMonitoringResourcesApi.md#rest_v10_projects_project_id_monitoring_resources_post) | **POST** /rest/v1.0/projects/{project_id}/monitoring_resources | Create Monitoring Resource


# **rest_v10_projects_project_id_monitoring_resources_get**
> List[RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner] rest_v10_projects_project_id_monitoring_resources_get(procore_company_id, project_id, forecast_start_date=forecast_start_date)

List Monitoring Resources

Returns a list of Monitoring Resources on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_get200_response_inner import RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetMonitoringResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    forecast_start_date = 'forecast_start_date_example' # str | Forecast start date, expressed in ISO 8601 date format (YYYY-MM-DD) (optional)

    try:
        # List Monitoring Resources
        api_response = api_instance.rest_v10_projects_project_id_monitoring_resources_get(procore_company_id, project_id, forecast_start_date=forecast_start_date)
        print("The response of ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **forecast_start_date** | **str**| Forecast start date, expressed in ISO 8601 date format (YYYY-MM-DD) | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner]**](RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_monitoring_resources_id_delete**
> rest_v10_projects_project_id_monitoring_resources_id_delete(procore_company_id, project_id, id)

Delete Monitoring Resource

Deletes a Monitoring Resource

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
    api_instance = procore_sdk.ConstructionFinancialsBudgetMonitoringResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Monitoring Resource ID

    try:
        # Delete Monitoring Resource
        api_instance.rest_v10_projects_project_id_monitoring_resources_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Monitoring Resource ID | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_monitoring_resources_id_patch**
> RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner rest_v10_projects_project_id_monitoring_resources_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_monitoring_resources_id_patch_request)

Update Monitoring Resource

Updates a Monitoring Resource's attributes

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_get200_response_inner import RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_id_patch_request import RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetMonitoringResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Monitoring Resource ID
    rest_v10_projects_project_id_monitoring_resources_id_patch_request = procore_sdk.RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequest() # RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequest | 

    try:
        # Update Monitoring Resource
        api_response = api_instance.rest_v10_projects_project_id_monitoring_resources_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_monitoring_resources_id_patch_request)
        print("The response of ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Monitoring Resource ID | 
 **rest_v10_projects_project_id_monitoring_resources_id_patch_request** | [**RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequest**](RestV10ProjectsProjectIdMonitoringResourcesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner**](RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_monitoring_resources_post**
> RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner rest_v10_projects_project_id_monitoring_resources_post(procore_company_id, project_id, rest_v10_projects_project_id_monitoring_resources_post_request)

Create Monitoring Resource

Creates a Monitoring Resource on a given Project's Budget Line Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_get200_response_inner import RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_monitoring_resources_post_request import RestV10ProjectsProjectIdMonitoringResourcesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetMonitoringResourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_monitoring_resources_post_request = procore_sdk.RestV10ProjectsProjectIdMonitoringResourcesPostRequest() # RestV10ProjectsProjectIdMonitoringResourcesPostRequest | 

    try:
        # Create Monitoring Resource
        api_response = api_instance.rest_v10_projects_project_id_monitoring_resources_post(procore_company_id, project_id, rest_v10_projects_project_id_monitoring_resources_post_request)
        print("The response of ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetMonitoringResourcesApi->rest_v10_projects_project_id_monitoring_resources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_monitoring_resources_post_request** | [**RestV10ProjectsProjectIdMonitoringResourcesPostRequest**](RestV10ProjectsProjectIdMonitoringResourcesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner**](RestV10ProjectsProjectIdMonitoringResourcesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

