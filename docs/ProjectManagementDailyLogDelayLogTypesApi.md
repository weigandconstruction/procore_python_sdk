# procore_sdk.ProjectManagementDailyLogDelayLogTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_logs_delay_log_types_get**](ProjectManagementDailyLogDelayLogTypesApi.md#rest_v10_projects_project_id_daily_logs_delay_log_types_get) | **GET** /rest/v1.0/projects/{project_id}/daily_logs/delay_log_types | List Delay Log Types
[**rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch**](ProjectManagementDailyLogDelayLogTypesApi.md#rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/daily_logs/delay_log_types/{id} | Update a Delay Log Type
[**rest_v10_projects_project_id_daily_logs_delay_log_types_post**](ProjectManagementDailyLogDelayLogTypesApi.md#rest_v10_projects_project_id_daily_logs_delay_log_types_post) | **POST** /rest/v1.0/projects/{project_id}/daily_logs/delay_log_types | Create new Delay Log Type


# **rest_v10_projects_project_id_daily_logs_delay_log_types_get**
> List[RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner] rest_v10_projects_project_id_daily_logs_delay_log_types_get(procore_company_id, project_id, filters_visible=filters_visible, page=page, per_page=per_page)

List Delay Log Types

Returns all Delay Log Types associated with the project and their visibility.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner import RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogDelayLogTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_visible = true # str | Filter Delay Log Types based on visible. Defaults to true, to query all types pass 'false...true' (optional) (default to true)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Delay Log Types
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_delay_log_types_get(procore_company_id, project_id, filters_visible=filters_visible, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_visible** | **str**| Filter Delay Log Types based on visible. Defaults to true, to query all types pass &#39;false...true&#39; | [optional] [default to true]
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner]**](RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have sufficient permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch**
> RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request)

Update a Delay Log Type

Update the visibility of a Delay Log Type

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner import RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request import RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDelayLogTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Delay Log Type ID
    rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request = procore_sdk.RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequest() # RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequest | 

    try:
        # Update a Delay Log Type
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request)
        print("The response of ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Delay Log Type ID | 
 **rest_v10_projects_project_id_daily_logs_delay_log_types_id_patch_request** | [**RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequest**](RestV10ProjectsProjectIdDailyLogsDelayLogTypesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner**](RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have sufficient permissions |  -  |
**422** | Delay Log Type failed validations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_daily_logs_delay_log_types_post**
> RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner rest_v10_projects_project_id_daily_logs_delay_log_types_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_delay_log_types_post_request)

Create new Delay Log Type

Create a new Delay Log Type for the project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_get200_response_inner import RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_delay_log_types_post_request import RestV10ProjectsProjectIdDailyLogsDelayLogTypesPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDelayLogTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_daily_logs_delay_log_types_post_request = procore_sdk.RestV10ProjectsProjectIdDailyLogsDelayLogTypesPostRequest() # RestV10ProjectsProjectIdDailyLogsDelayLogTypesPostRequest | 

    try:
        # Create new Delay Log Type
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_delay_log_types_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_delay_log_types_post_request)
        print("The response of ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDelayLogTypesApi->rest_v10_projects_project_id_daily_logs_delay_log_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_daily_logs_delay_log_types_post_request** | [**RestV10ProjectsProjectIdDailyLogsDelayLogTypesPostRequest**](RestV10ProjectsProjectIdDailyLogsDelayLogTypesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner**](RestV10ProjectsProjectIdDailyLogsDelayLogTypesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Delay Log Type successfully created |  -  |
**403** | User does not have sufficient permissions |  -  |
**422** | Delay Log Type failed validation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

