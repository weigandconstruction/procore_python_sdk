# procore_sdk.ProjectManagementDailyLogNotesLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_notes_logs_get**](ProjectManagementDailyLogNotesLogsApi.md#rest_v10_projects_project_id_notes_logs_get) | **GET** /rest/v1.0/projects/{project_id}/notes_logs | List Notes Logs
[**rest_v10_projects_project_id_notes_logs_id_delete**](ProjectManagementDailyLogNotesLogsApi.md#rest_v10_projects_project_id_notes_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/notes_logs/{id} | Delete Notes Log
[**rest_v10_projects_project_id_notes_logs_id_get**](ProjectManagementDailyLogNotesLogsApi.md#rest_v10_projects_project_id_notes_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/notes_logs/{id} | Show Notes Logs
[**rest_v10_projects_project_id_notes_logs_id_patch**](ProjectManagementDailyLogNotesLogsApi.md#rest_v10_projects_project_id_notes_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/notes_logs/{id} | Update Notes Log
[**rest_v10_projects_project_id_notes_logs_post**](ProjectManagementDailyLogNotesLogsApi.md#rest_v10_projects_project_id_notes_logs_post) | **POST** /rest/v1.0/projects/{project_id}/notes_logs | Create Notes Log


# **rest_v10_projects_project_id_notes_logs_get**
> List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInner] rest_v10_projects_project_id_notes_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, page=page, per_page=per_page)

List Notes Logs

Returns all approved Notes Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogNotesLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_status = 'approved' # str | Filter on status for \"pending\" or \"approved\" or \"all\" (optional)
    filters_created_by_id = 56 # int | Return item(s) created by the specified User ID (optional)
    filters_location_id = 56 # int | Filters by specific location (Note: Use *either* this or location_id_with_sublocations, but not both) (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Notes Logs
        api_response = api_instance.rest_v10_projects_project_id_notes_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_status** | **str**| Filter on status for \&quot;pending\&quot; or \&quot;approved\&quot; or \&quot;all\&quot; | [optional] 
 **filters_created_by_id** | **int**| Return item(s) created by the specified User ID | [optional] 
 **filters_location_id** | **int**| Filters by specific location (Note: Use *either* this or location_id_with_sublocations, but not both) | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdNotesLogsGet200ResponseInner]**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_notes_logs_id_delete**
> rest_v10_projects_project_id_notes_logs_id_delete(procore_company_id, project_id, id)

Delete Notes Log

Delete single Notes Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogNotesLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Notes Log ID

    try:
        # Delete Notes Log
        api_instance.rest_v10_projects_project_id_notes_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Notes Log ID | 

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

# **rest_v10_projects_project_id_notes_logs_id_get**
> RestV10ProjectsProjectIdNotesLogsGet200ResponseInner rest_v10_projects_project_id_notes_logs_id_get(procore_company_id, project_id, id)

Show Notes Logs

Returns single Notes Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogNotesLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Notes Log ID

    try:
        # Show Notes Logs
        api_response = api_instance.rest_v10_projects_project_id_notes_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Notes Log ID | 

### Return type

[**RestV10ProjectsProjectIdNotesLogsGet200ResponseInner**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_notes_logs_id_patch**
> RestV10ProjectsProjectIdNotesLogsGet200ResponseInner rest_v10_projects_project_id_notes_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_notes_logs_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Notes Log

Update single Notes Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_id_patch_request import RestV10ProjectsProjectIdNotesLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogNotesLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Notes Log ID
    rest_v10_projects_project_id_notes_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdNotesLogsIdPatchRequest() # RestV10ProjectsProjectIdNotesLogsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Notes Log
        api_response = api_instance.rest_v10_projects_project_id_notes_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_notes_logs_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Notes Log ID | 
 **rest_v10_projects_project_id_notes_logs_id_patch_request** | [**RestV10ProjectsProjectIdNotesLogsIdPatchRequest**](RestV10ProjectsProjectIdNotesLogsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdNotesLogsGet200ResponseInner**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_notes_logs_post**
> RestV10ProjectsProjectIdNotesLogsGet200ResponseInner rest_v10_projects_project_id_notes_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_notes_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Notes Log

Creates single Notes Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_get200_response_inner import RestV10ProjectsProjectIdNotesLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_notes_logs_post_request import RestV10ProjectsProjectIdNotesLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogNotesLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_notes_logs_post_request = procore_sdk.RestV10ProjectsProjectIdNotesLogsPostRequest() # RestV10ProjectsProjectIdNotesLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Notes Log
        api_response = api_instance.rest_v10_projects_project_id_notes_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_notes_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogNotesLogsApi->rest_v10_projects_project_id_notes_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_notes_logs_post_request** | [**RestV10ProjectsProjectIdNotesLogsPostRequest**](RestV10ProjectsProjectIdNotesLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdNotesLogsGet200ResponseInner**](RestV10ProjectsProjectIdNotesLogsGet200ResponseInner.md)

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

