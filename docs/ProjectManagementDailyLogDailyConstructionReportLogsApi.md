# procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_construction_report_logs_get**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_get) | **GET** /rest/v1.0/projects/{project_id}/daily_construction_report_logs | List Daily Construction Report Logs
[**rest_v10_projects_project_id_daily_construction_report_logs_id_delete**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/daily_construction_report_logs/{id} | Delete Daily Construction Report Log
[**rest_v10_projects_project_id_daily_construction_report_logs_id_get**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/daily_construction_report_logs/{id} | Show Daily Construction Report Logs
[**rest_v10_projects_project_id_daily_construction_report_logs_id_patch**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/daily_construction_report_logs/{id} | Update Daily Construction Report Log
[**rest_v10_projects_project_id_daily_construction_report_logs_post**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_post) | **POST** /rest/v1.0/projects/{project_id}/daily_construction_report_logs | Create Daily Construction Report Log
[**rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get**](ProjectManagementDailyLogDailyConstructionReportLogsApi.md#rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get) | **GET** /rest/v1.0/projects/{project_id}/daily_construction_report_logs/vendor_options | List Daily Construction Report Logs Vendor Options


# **rest_v10_projects_project_id_daily_construction_report_logs_get**
> List[RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner] rest_v10_projects_project_id_daily_construction_report_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)

List Daily Construction Report Logs

Returns all approved Daily Construction Report Logs for the current date. See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner import RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_status = 'filters_status_example' # str | Filter on status for \"pending\" or \"approved\" or \"all\" (optional)
    filters_created_by_id = 56 # int | Return item(s) created by the specified User ID (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Daily Construction Report Logs
        api_response = api_instance.rest_v10_projects_project_id_daily_construction_report_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_get: %s\n" % e)
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
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner]**](RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_daily_construction_report_logs_id_delete**
> rest_v10_projects_project_id_daily_construction_report_logs_id_delete(procore_company_id, project_id, id)

Delete Daily Construction Report Log

Delete single Daily Construction Report Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Daily Construction Report Log ID

    try:
        # Delete Daily Construction Report Log
        api_instance.rest_v10_projects_project_id_daily_construction_report_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Daily Construction Report Log ID | 

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

# **rest_v10_projects_project_id_daily_construction_report_logs_id_get**
> RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner rest_v10_projects_project_id_daily_construction_report_logs_id_get(procore_company_id, project_id, id)

Show Daily Construction Report Logs

Returns single Daily Construction Report Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner import RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Daily Construction Report Log ID

    try:
        # Show Daily Construction Report Logs
        api_response = api_instance.rest_v10_projects_project_id_daily_construction_report_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Daily Construction Report Log ID | 

### Return type

[**RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner**](RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_daily_construction_report_logs_id_patch**
> RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner rest_v10_projects_project_id_daily_construction_report_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Daily Construction Report Log

Update single Daily Construction Report Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner import RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request import RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Daily Construction Report Log ID
    rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequest() # RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Daily Construction Report Log
        api_response = api_instance.rest_v10_projects_project_id_daily_construction_report_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Daily Construction Report Log ID | 
 **rest_v10_projects_project_id_daily_construction_report_logs_id_patch_request** | [**RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequest**](RestV10ProjectsProjectIdDailyConstructionReportLogsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner**](RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_daily_construction_report_logs_post**
> RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner rest_v10_projects_project_id_daily_construction_report_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_construction_report_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Daily Construction Report Log

Creates single Daily Construction Report Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_get200_response_inner import RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_daily_construction_report_logs_post_request import RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_daily_construction_report_logs_post_request = procore_sdk.RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest() # RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Daily Construction Report Log
        api_response = api_instance.rest_v10_projects_project_id_daily_construction_report_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_construction_report_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_daily_construction_report_logs_post_request** | [**RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest**](RestV10ProjectsProjectIdDailyConstructionReportLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner**](RestV10ProjectsProjectIdDailyConstructionReportLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get**
> List[Compact] rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get(procore_company_id, project_id)

List Daily Construction Report Logs Vendor Options

Returns all Vendors that can be assigned to a new Daily Construction Report Log given the current user permissions

### Example


```python
import procore_sdk
from procore_sdk.models.compact import Compact
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyConstructionReportLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Daily Construction Report Logs Vendor Options
        api_response = api_instance.rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get(procore_company_id, project_id)
        print("The response of ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyConstructionReportLogsApi->rest_v10_projects_project_id_daily_construction_report_logs_vendor_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[Compact]**](Compact.md)

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

