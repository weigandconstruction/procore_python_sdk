# procore_sdk.ProjectManagementDailyLogDailyLogHeadersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_log_headers_get**](ProjectManagementDailyLogDailyLogHeadersApi.md#rest_v10_projects_project_id_daily_log_headers_get) | **GET** /rest/v1.0/projects/{project_id}/daily_log_headers | Get the Daily Log Header via date or id
[**rest_v10_projects_project_id_daily_log_headers_index_get**](ProjectManagementDailyLogDailyLogHeadersApi.md#rest_v10_projects_project_id_daily_log_headers_index_get) | **GET** /rest/v1.0/projects/{project_id}/daily_log_headers/index | Get Daily Log Headers for the Project
[**rest_v10_projects_project_id_daily_log_headers_patch**](ProjectManagementDailyLogDailyLogHeadersApi.md#rest_v10_projects_project_id_daily_log_headers_patch) | **PATCH** /rest/v1.0/projects/{project_id}/daily_log_headers | Update the state of a Daily Log Header


# **rest_v10_projects_project_id_daily_log_headers_get**
> RestV10ProjectsProjectIdDailyLogHeadersGet200Response rest_v10_projects_project_id_daily_log_headers_get(procore_company_id, project_id, id=id, log_date=log_date)

Get the Daily Log Header via date or id

Returns the Daily Log Header for a given date or id

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_get200_response import RestV10ProjectsProjectIdDailyLogHeadersGet200Response
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogHeadersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | The id of the requested Daily Log Header (optional)
    log_date = '2013-10-20' # date | The log date for the requested Daily Log Header (optional)

    try:
        # Get the Daily Log Header via date or id
        api_response = api_instance.rest_v10_projects_project_id_daily_log_headers_get(procore_company_id, project_id, id=id, log_date=log_date)
        print("The response of ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| The id of the requested Daily Log Header | [optional] 
 **log_date** | **date**| The log date for the requested Daily Log Header | [optional] 

### Return type

[**RestV10ProjectsProjectIdDailyLogHeadersGet200Response**](RestV10ProjectsProjectIdDailyLogHeadersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have permissions to view the requested Daily Log Header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_daily_log_headers_index_get**
> List[RestV10ProjectsProjectIdDailyLogHeadersGet200Response] rest_v10_projects_project_id_daily_log_headers_index_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)

Get Daily Log Headers for the Project

Returns Daily Log Headers for the Project for specified date range or all if not specified

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_get200_response import RestV10ProjectsProjectIdDailyLogHeadersGet200Response
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogHeadersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    start_date = '2013-10-20' # date | The left boundary of requested date range (optional)
    end_date = '2013-10-20' # date | The right boundary of requested date range (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # Get Daily Log Headers for the Project
        api_response = api_instance.rest_v10_projects_project_id_daily_log_headers_index_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **start_date** | **date**| The left boundary of requested date range | [optional] 
 **end_date** | **date**| The right boundary of requested date range | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDailyLogHeadersGet200Response]**](RestV10ProjectsProjectIdDailyLogHeadersGet200Response.md)

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
**403** | User does not have permissions to view the requested Daily Log Header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_daily_log_headers_patch**
> RestV10ProjectsProjectIdDailyLogHeadersGet200Response rest_v10_projects_project_id_daily_log_headers_patch(procore_company_id, project_id, rest_v10_projects_project_id_daily_log_headers_patch_request, id=id, log_date=log_date, app_name=app_name)

Update the state of a Daily Log Header

Sets the completed boolean value and/or distributes the Daily Log to its distribution list

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_get200_response import RestV10ProjectsProjectIdDailyLogHeadersGet200Response
from procore_sdk.models.rest_v10_projects_project_id_daily_log_headers_patch_request import RestV10ProjectsProjectIdDailyLogHeadersPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogHeadersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_daily_log_headers_patch_request = procore_sdk.RestV10ProjectsProjectIdDailyLogHeadersPatchRequest() # RestV10ProjectsProjectIdDailyLogHeadersPatchRequest | 
    id = 56 # int | The id of the requested Daily Log Header (optional)
    log_date = '2013-10-20' # date | The log date for the requested Daily Log Header (optional)
    app_name = 'web' # str | The name of app which issues this request. If app name is 'web' and request completes day then web filters of user which completes day are applied to pdf which is sent to distribution users. (optional)

    try:
        # Update the state of a Daily Log Header
        api_response = api_instance.rest_v10_projects_project_id_daily_log_headers_patch(procore_company_id, project_id, rest_v10_projects_project_id_daily_log_headers_patch_request, id=id, log_date=log_date, app_name=app_name)
        print("The response of ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogHeadersApi->rest_v10_projects_project_id_daily_log_headers_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_daily_log_headers_patch_request** | [**RestV10ProjectsProjectIdDailyLogHeadersPatchRequest**](RestV10ProjectsProjectIdDailyLogHeadersPatchRequest.md)|  | 
 **id** | **int**| The id of the requested Daily Log Header | [optional] 
 **log_date** | **date**| The log date for the requested Daily Log Header | [optional] 
 **app_name** | **str**| The name of app which issues this request. If app name is &#39;web&#39; and request completes day then web filters of user which completes day are applied to pdf which is sent to distribution users. | [optional] 

### Return type

[**RestV10ProjectsProjectIdDailyLogHeadersGet200Response**](RestV10ProjectsProjectIdDailyLogHeadersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Daily Log Header updated |  -  |
**400** | Daily Log Header parameter was missing or invalid |  -  |
**403** | User does not have permission to update Daily Log Headers |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

