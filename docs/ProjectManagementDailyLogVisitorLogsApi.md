# procore_sdk.ProjectManagementDailyLogVisitorLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_visitor_logs_get**](ProjectManagementDailyLogVisitorLogsApi.md#rest_v10_projects_project_id_visitor_logs_get) | **GET** /rest/v1.0/projects/{project_id}/visitor_logs | List Visitor Logs
[**rest_v10_projects_project_id_visitor_logs_id_delete**](ProjectManagementDailyLogVisitorLogsApi.md#rest_v10_projects_project_id_visitor_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/visitor_logs/{id} | Delete Visitor Log
[**rest_v10_projects_project_id_visitor_logs_id_get**](ProjectManagementDailyLogVisitorLogsApi.md#rest_v10_projects_project_id_visitor_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/visitor_logs/{id} | Show Visitor Logs
[**rest_v10_projects_project_id_visitor_logs_id_patch**](ProjectManagementDailyLogVisitorLogsApi.md#rest_v10_projects_project_id_visitor_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/visitor_logs/{id} | Update Visitor Log
[**rest_v10_projects_project_id_visitor_logs_post**](ProjectManagementDailyLogVisitorLogsApi.md#rest_v10_projects_project_id_visitor_logs_post) | **POST** /rest/v1.0/projects/{project_id}/visitor_logs | Create Visitor Log


# **rest_v10_projects_project_id_visitor_logs_get**
> List[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner] rest_v10_projects_project_id_visitor_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)

List Visitor Logs

Returns all Visitor Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogVisitorLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Visitor Logs
        api_response = api_instance.rest_v10_projects_project_id_visitor_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner]**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_visitor_logs_id_delete**
> rest_v10_projects_project_id_visitor_logs_id_delete(procore_company_id, project_id, id)

Delete Visitor Log

Delete single Visitor Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogVisitorLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Visitor Log ID

    try:
        # Delete Visitor Log
        api_instance.rest_v10_projects_project_id_visitor_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Visitor Log ID | 

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
**400** | Can not delete due to errors |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_visitor_logs_id_get**
> RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner rest_v10_projects_project_id_visitor_logs_id_get(procore_company_id, project_id, id)

Show Visitor Logs

Returns single Visitor Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogVisitorLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Visitor Log ID

    try:
        # Show Visitor Logs
        api_response = api_instance.rest_v10_projects_project_id_visitor_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Visitor Log ID | 

### Return type

[**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_visitor_logs_id_patch**
> RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner rest_v10_projects_project_id_visitor_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_visitor_logs_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Visitor Log

Updates a single Visitor Log in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_id_patch_request import RestV10ProjectsProjectIdVisitorLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogVisitorLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Visitor Log ID
    rest_v10_projects_project_id_visitor_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdVisitorLogsIdPatchRequest() # RestV10ProjectsProjectIdVisitorLogsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Visitor Log
        api_response = api_instance.rest_v10_projects_project_id_visitor_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_visitor_logs_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Visitor Log ID | 
 **rest_v10_projects_project_id_visitor_logs_id_patch_request** | [**RestV10ProjectsProjectIdVisitorLogsIdPatchRequest**](RestV10ProjectsProjectIdVisitorLogsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_visitor_logs_post**
> RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner rest_v10_projects_project_id_visitor_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_visitor_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Visitor Log

Creates a single Visitor Log in the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_get200_response_inner import RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_visitor_logs_post_request import RestV10ProjectsProjectIdVisitorLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogVisitorLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_visitor_logs_post_request = procore_sdk.RestV10ProjectsProjectIdVisitorLogsPostRequest() # RestV10ProjectsProjectIdVisitorLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Visitor Log
        api_response = api_instance.rest_v10_projects_project_id_visitor_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_visitor_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogVisitorLogsApi->rest_v10_projects_project_id_visitor_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_visitor_logs_post_request** | [**RestV10ProjectsProjectIdVisitorLogsPostRequest**](RestV10ProjectsProjectIdVisitorLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

