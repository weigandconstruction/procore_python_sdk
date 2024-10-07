# procore_sdk.ProjectManagementDailyLogProductivityLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_productivity_logs_get**](ProjectManagementDailyLogProductivityLogsApi.md#rest_v10_projects_project_id_productivity_logs_get) | **GET** /rest/v1.0/projects/{project_id}/productivity_logs | List Productivity Logs
[**rest_v10_projects_project_id_productivity_logs_id_delete**](ProjectManagementDailyLogProductivityLogsApi.md#rest_v10_projects_project_id_productivity_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/productivity_logs/{id} | Delete Productivity Log
[**rest_v10_projects_project_id_productivity_logs_id_get**](ProjectManagementDailyLogProductivityLogsApi.md#rest_v10_projects_project_id_productivity_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/productivity_logs/{id} | Show Productivity Logs
[**rest_v10_projects_project_id_productivity_logs_id_patch**](ProjectManagementDailyLogProductivityLogsApi.md#rest_v10_projects_project_id_productivity_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/productivity_logs/{id} | Update Productivity Log
[**rest_v10_projects_project_id_productivity_logs_post**](ProjectManagementDailyLogProductivityLogsApi.md#rest_v10_projects_project_id_productivity_logs_post) | **POST** /rest/v1.0/projects/{project_id}/productivity_logs | Create Productivity Log


# **rest_v10_projects_project_id_productivity_logs_get**
> List[RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner] rest_v10_projects_project_id_productivity_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)

List Productivity Logs

Returns all Productivity Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogProductivityLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = 'log_date_example' # str | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Productivity Logs
        api_response = api_instance.rest_v10_projects_project_id_productivity_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **str**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner]**](RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_productivity_logs_id_delete**
> rest_v10_projects_project_id_productivity_logs_id_delete(procore_company_id, project_id, id)

Delete Productivity Log

Delete single Productivity Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogProductivityLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Productivity Log ID

    try:
        # Delete Productivity Log
        api_instance.rest_v10_projects_project_id_productivity_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Productivity Log ID | 

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

# **rest_v10_projects_project_id_productivity_logs_id_get**
> RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner rest_v10_projects_project_id_productivity_logs_id_get(procore_company_id, project_id, id)

Show Productivity Logs

Returns single Productivity Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogProductivityLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Productivity Log ID

    try:
        # Show Productivity Logs
        api_response = api_instance.rest_v10_projects_project_id_productivity_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Productivity Log ID | 

### Return type

[**RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner**](RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_productivity_logs_id_patch**
> RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner rest_v10_projects_project_id_productivity_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_productivity_logs_id_patch_request)

Update Productivity Log

Update single Productivity Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_id_patch_request import RestV10ProjectsProjectIdProductivityLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogProductivityLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Productivity Log ID
    rest_v10_projects_project_id_productivity_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdProductivityLogsIdPatchRequest() # RestV10ProjectsProjectIdProductivityLogsIdPatchRequest | 

    try:
        # Update Productivity Log
        api_response = api_instance.rest_v10_projects_project_id_productivity_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_productivity_logs_id_patch_request)
        print("The response of ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Productivity Log ID | 
 **rest_v10_projects_project_id_productivity_logs_id_patch_request** | [**RestV10ProjectsProjectIdProductivityLogsIdPatchRequest**](RestV10ProjectsProjectIdProductivityLogsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner**](RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_productivity_logs_post**
> RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner rest_v10_projects_project_id_productivity_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_productivity_logs_post_request)

Create Productivity Log

Creates single Productivity Log  #### Click - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments  #### Note: The required Line Item ID to create a Productivity Log must be from an approved Contract  #### How to find a Line Item ID * If the Line Item comes from a Work Order Contract use the `Work Order Contracts List` endpoint * If the Line Item comes from a Purchase Order Contract use the `Purchase Order Contracts List` endpoint * Use filter - `filters[status] 'Approved'` - to get list of approved Contracts * Use the Contract ID to the Show endpoint to get the Line Item ID associated with the Contract

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_post_request import RestV10ProjectsProjectIdProductivityLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogProductivityLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_productivity_logs_post_request = procore_sdk.RestV10ProjectsProjectIdProductivityLogsPostRequest() # RestV10ProjectsProjectIdProductivityLogsPostRequest | 

    try:
        # Create Productivity Log
        api_response = api_instance.rest_v10_projects_project_id_productivity_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_productivity_logs_post_request)
        print("The response of ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogProductivityLogsApi->rest_v10_projects_project_id_productivity_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_productivity_logs_post_request** | [**RestV10ProjectsProjectIdProductivityLogsPostRequest**](RestV10ProjectsProjectIdProductivityLogsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner**](RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.md)

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

