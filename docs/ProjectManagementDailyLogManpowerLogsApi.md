# procore_sdk.ProjectManagementDailyLogManpowerLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_manpower_logs_contact_options_get**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_contact_options_get) | **GET** /rest/v1.0/projects/{project_id}/manpower_logs/contact_options | List Manpower Logs Contact Options
[**rest_v10_projects_project_id_manpower_logs_daily_totals_get**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_daily_totals_get) | **GET** /rest/v1.0/projects/{project_id}/manpower_logs/daily_totals | Get total workers and man hours
[**rest_v10_projects_project_id_manpower_logs_get**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_get) | **GET** /rest/v1.0/projects/{project_id}/manpower_logs | List Manpower Logs
[**rest_v10_projects_project_id_manpower_logs_id_delete**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/manpower_logs/{id} | Delete Manpower Log
[**rest_v10_projects_project_id_manpower_logs_id_get**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/manpower_logs/{id} | Show Manpower Logs
[**rest_v10_projects_project_id_manpower_logs_id_patch**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/manpower_logs/{id} | Update Manpower Log
[**rest_v10_projects_project_id_manpower_logs_post**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_post) | **POST** /rest/v1.0/projects/{project_id}/manpower_logs | Create Manpower Log
[**rest_v10_projects_project_id_manpower_logs_vendor_options_get**](ProjectManagementDailyLogManpowerLogsApi.md#rest_v10_projects_project_id_manpower_logs_vendor_options_get) | **GET** /rest/v1.0/projects/{project_id}/manpower_logs/vendor_options | List Manpower Logs Vendor Options


# **rest_v10_projects_project_id_manpower_logs_contact_options_get**
> List[RestV10ProjectsProjectIdTimesheetsPotentialTimesheetCreatorsGet200ResponseInner] rest_v10_projects_project_id_manpower_logs_contact_options_get(procore_company_id, project_id, page=page, per_page=per_page)

List Manpower Logs Contact Options

Returns all Contacts that can be assigned to a new Manpower Log given the current user permissions

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timesheets_potential_timesheet_creators_get200_response_inner import RestV10ProjectsProjectIdTimesheetsPotentialTimesheetCreatorsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Manpower Logs Contact Options
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_contact_options_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_contact_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_contact_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimesheetsPotentialTimesheetCreatorsGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsPotentialTimesheetCreatorsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_manpower_logs_daily_totals_get**
> RestV10ProjectsProjectIdManpowerLogsDailyTotalsGet200Response rest_v10_projects_project_id_manpower_logs_daily_totals_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id)

Get total workers and man hours

Returns total workers and man hours between a start date and end date. To get a single day, supply the same date for start and end.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_daily_totals_get200_response import RestV10ProjectsProjectIdManpowerLogsDailyTotalsGet200Response
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)

    try:
        # Get total workers and man hours
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_daily_totals_get(procore_company_id, project_id, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_daily_totals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_daily_totals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 

### Return type

[**RestV10ProjectsProjectIdManpowerLogsDailyTotalsGet200Response**](RestV10ProjectsProjectIdManpowerLogsDailyTotalsGet200Response.md)

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

# **rest_v10_projects_project_id_manpower_logs_get**
> List[RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner] rest_v10_projects_project_id_manpower_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, filters_vendor_id=filters_vendor_id, filters_search=filters_search, page=page, per_page=per_page)

List Manpower Logs

Returns all approved Manpower Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_status = 'filters_status_example' # str | Filter on status for \"pending\" or \"approved\" or \"all\" (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)
    filters_vendor_id = [56] # List[int] | Return item(s) with the specified Vendor IDs. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Manpower Logs
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, filters_vendor_id=filters_vendor_id, filters_search=filters_search, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_get: %s\n" % e)
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
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 
 **filters_vendor_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor IDs. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner]**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_manpower_logs_id_delete**
> rest_v10_projects_project_id_manpower_logs_id_delete(procore_company_id, project_id, id)

Delete Manpower Log

Delete single Manpower Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Manpower Log ID

    try:
        # Delete Manpower Log
        api_instance.rest_v10_projects_project_id_manpower_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Manpower Log ID | 

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

# **rest_v10_projects_project_id_manpower_logs_id_get**
> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner rest_v10_projects_project_id_manpower_logs_id_get(procore_company_id, project_id, id)

Show Manpower Logs

Returns single Manpower Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Manpower Log ID

    try:
        # Show Manpower Logs
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Manpower Log ID | 

### Return type

[**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_manpower_logs_id_patch**
> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner rest_v10_projects_project_id_manpower_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_manpower_logs_id_patch_request, run_configurable_validations=run_configurable_validations)

Update Manpower Log

Update single Manpower Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_id_patch_request import RestV10ProjectsProjectIdManpowerLogsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Manpower Log ID
    rest_v10_projects_project_id_manpower_logs_id_patch_request = procore_sdk.RestV10ProjectsProjectIdManpowerLogsIdPatchRequest() # RestV10ProjectsProjectIdManpowerLogsIdPatchRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Manpower Log
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_manpower_logs_id_patch_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Manpower Log ID | 
 **rest_v10_projects_project_id_manpower_logs_id_patch_request** | [**RestV10ProjectsProjectIdManpowerLogsIdPatchRequest**](RestV10ProjectsProjectIdManpowerLogsIdPatchRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_manpower_logs_post**
> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner rest_v10_projects_project_id_manpower_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_manpower_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Manpower Log

Creates single Manpower Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_post_request import RestV10ProjectsProjectIdManpowerLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_manpower_logs_post_request = procore_sdk.RestV10ProjectsProjectIdManpowerLogsPostRequest() # RestV10ProjectsProjectIdManpowerLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Manpower Log
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_manpower_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_manpower_logs_post_request** | [**RestV10ProjectsProjectIdManpowerLogsPostRequest**](RestV10ProjectsProjectIdManpowerLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner**](RestV10ProjectsProjectIdManpowerLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_manpower_logs_vendor_options_get**
> List[Compact] rest_v10_projects_project_id_manpower_logs_vendor_options_get(procore_company_id, project_id, page=page, per_page=per_page)

List Manpower Logs Vendor Options

Returns all Vendors that can be assigned to a new Manpower Log given the current user permissions

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
    api_instance = procore_sdk.ProjectManagementDailyLogManpowerLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Manpower Logs Vendor Options
        api_response = api_instance.rest_v10_projects_project_id_manpower_logs_vendor_options_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_vendor_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogManpowerLogsApi->rest_v10_projects_project_id_manpower_logs_vendor_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

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
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

