# procore_sdk.ProjectManagementProjectScheduleCalendarEventsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_calendar_events_get**](ProjectManagementProjectScheduleCalendarEventsApi.md#rest_v10_calendar_events_get) | **GET** /rest/v1.0/calendar_events | List calendar events


# **rest_v10_calendar_events_get**
> RestV10CalendarEventsGet200Response rest_v10_calendar_events_get(procore_company_id, project_id, calendar_start_datetime=calendar_start_datetime, calendar_finish_datetime=calendar_finish_datetime, page=page, per_page=per_page)

List calendar events

DEPRECATED: This endpoint is not accurate across time zones and has been deprecated. It will be removed in a future version of the API. Use the Schedule Tasks, Calendar Items, and Schedule endpoints instead.  List all Calendar Events for a specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_calendar_events_get200_response import RestV10CalendarEventsGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleCalendarEventsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    calendar_start_datetime = '2013-10-20T19:20:30+01:00' # datetime | Start date or date-time (optional)
    calendar_finish_datetime = '2013-10-20T19:20:30+01:00' # datetime | Finish date or date-time (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List calendar events
        api_response = api_instance.rest_v10_calendar_events_get(procore_company_id, project_id, calendar_start_datetime=calendar_start_datetime, calendar_finish_datetime=calendar_finish_datetime, page=page, per_page=per_page)
        print("The response of ProjectManagementProjectScheduleCalendarEventsApi->rest_v10_calendar_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleCalendarEventsApi->rest_v10_calendar_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **calendar_start_datetime** | **datetime**| Start date or date-time | [optional] 
 **calendar_finish_datetime** | **datetime**| Finish date or date-time | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV10CalendarEventsGet200Response**](RestV10CalendarEventsGet200Response.md)

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
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

