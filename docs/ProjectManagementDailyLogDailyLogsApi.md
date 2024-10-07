# procore_sdk.ProjectManagementDailyLogDailyLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_logs_count_get**](ProjectManagementDailyLogDailyLogsApi.md#rest_v10_projects_project_id_daily_logs_count_get) | **GET** /rest/v1.0/projects/{project_id}/daily_logs/count | List Counts of Daily Logs


# **rest_v10_projects_project_id_daily_logs_count_get**
> List[RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner] rest_v10_projects_project_id_daily_logs_count_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id)

List Counts of Daily Logs

Returns counts of all daily logs arranged by type, given the current user permissions. Read Only/Standard users will see only counts of approved logs, Collaborator users will see only counts of logs created by themselves, Admins can use filter options to see all logs, or only a specific approval status (defaulting to approved).  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.  This is a deprecated endpoint, please use [/rest/v1.1/projects/{project_id}/daily_logs/counts](daily_logs#counts)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_count_get200_response_inner import RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_status = 'filters_status_example' # str | Filter on status for \"pending\" or \"approved\" or \"all\" (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)

    try:
        # List Counts of Daily Logs
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_count_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id)
        print("The response of ProjectManagementDailyLogDailyLogsApi->rest_v10_projects_project_id_daily_logs_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogsApi->rest_v10_projects_project_id_daily_logs_count_get: %s\n" % e)
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

### Return type

[**List[RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner]**](RestV10ProjectsProjectIdDailyLogsCountGet200ResponseInner.md)

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

