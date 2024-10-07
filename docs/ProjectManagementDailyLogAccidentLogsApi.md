# procore_sdk.ProjectManagementDailyLogAccidentLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_accident_logs_get**](ProjectManagementDailyLogAccidentLogsApi.md#rest_v10_projects_project_id_accident_logs_get) | **GET** /rest/v1.0/projects/{project_id}/accident_logs | List Accident Logs
[**rest_v10_projects_project_id_accident_logs_id_delete**](ProjectManagementDailyLogAccidentLogsApi.md#rest_v10_projects_project_id_accident_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/accident_logs/{id} | Delete Accident Log
[**rest_v10_projects_project_id_accident_logs_id_get**](ProjectManagementDailyLogAccidentLogsApi.md#rest_v10_projects_project_id_accident_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/accident_logs/{id} | Show Accident Logs
[**rest_v10_projects_project_id_accident_logs_id_patch**](ProjectManagementDailyLogAccidentLogsApi.md#rest_v10_projects_project_id_accident_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/accident_logs/{id} | Update Accident Log
[**rest_v10_projects_project_id_accident_logs_post**](ProjectManagementDailyLogAccidentLogsApi.md#rest_v10_projects_project_id_accident_logs_post) | **POST** /rest/v1.0/projects/{project_id}/accident_logs | Create Accident Log


# **rest_v10_projects_project_id_accident_logs_get**
> List[RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner] rest_v10_projects_project_id_accident_logs_get(procore_company_id, project_id, per_page=per_page, page=page, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id)

List Accident Logs

Returns all Accident Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_get200_response_inner import RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogAccidentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    per_page = 56 # int | Elements per page (optional)
    page = 56 # int | Page (optional)
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_created_by_id = 56 # int | Return item(s) created by the specified User ID (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)

    try:
        # List Accident Logs
        api_response = api_instance.rest_v10_projects_project_id_accident_logs_get(procore_company_id, project_id, per_page=per_page, page=page, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id)
        print("The response of ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **per_page** | **int**| Elements per page | [optional] 
 **page** | **int**| Page | [optional] 
 **log_date** | **date**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_created_by_id** | **int**| Return item(s) created by the specified User ID | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_accident_logs_id_delete**
> rest_v10_projects_project_id_accident_logs_id_delete(procore_company_id, project_id, id)

Delete Accident Log

Delete single Accident Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogAccidentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Accident log ID

    try:
        # Delete Accident Log
        api_instance.rest_v10_projects_project_id_accident_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Accident log ID | 

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

# **rest_v10_projects_project_id_accident_logs_id_get**
> RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner rest_v10_projects_project_id_accident_logs_id_get(procore_company_id, project_id, id)

Show Accident Logs

Returns single Accident Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_get200_response_inner import RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogAccidentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Accident log ID

    try:
        # Show Accident Logs
        api_response = api_instance.rest_v10_projects_project_id_accident_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Accident log ID | 

### Return type

[**RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner**](RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_accident_logs_id_patch**
> RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner rest_v10_projects_project_id_accident_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_accident_logs_id_patch_request)

Update Accident Log

Update single Accident Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_get200_response_inner import RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_id_patch_request import RestV10ProjectsProjectIdAccidentLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogAccidentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Accident log ID
    rest_v10_projects_project_id_accident_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdAccidentLogsIdPatchRequest() # RestV10ProjectsProjectIdAccidentLogsIdPatchRequest | 

    try:
        # Update Accident Log
        api_response = api_instance.rest_v10_projects_project_id_accident_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_accident_logs_id_patch_request)
        print("The response of ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Accident log ID | 
 **rest_v10_projects_project_id_accident_logs_id_patch_request** | [**RestV10ProjectsProjectIdAccidentLogsIdPatchRequest**](RestV10ProjectsProjectIdAccidentLogsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner**](RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_accident_logs_post**
> RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner rest_v10_projects_project_id_accident_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_accident_logs_post_request)

Create Accident Log

Creates single Accident Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_get200_response_inner import RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_accident_logs_post_request import RestV10ProjectsProjectIdAccidentLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogAccidentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_accident_logs_post_request = procore_sdk.RestV10ProjectsProjectIdAccidentLogsPostRequest() # RestV10ProjectsProjectIdAccidentLogsPostRequest | 

    try:
        # Create Accident Log
        api_response = api_instance.rest_v10_projects_project_id_accident_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_accident_logs_post_request)
        print("The response of ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAccidentLogsApi->rest_v10_projects_project_id_accident_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_accident_logs_post_request** | [**RestV10ProjectsProjectIdAccidentLogsPostRequest**](RestV10ProjectsProjectIdAccidentLogsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner**](RestV10ProjectsProjectIdAccidentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

