# procore_sdk.ProjectManagementMeetingsMeetingAttendeesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_meeting_attendee_records_id_delete**](ProjectManagementMeetingsMeetingAttendeesApi.md#rest_v10_meeting_attendee_records_id_delete) | **DELETE** /rest/v1.0/meeting_attendee_records/{id} | Delete meeting attendee record
[**rest_v10_meeting_attendee_records_id_patch**](ProjectManagementMeetingsMeetingAttendeesApi.md#rest_v10_meeting_attendee_records_id_patch) | **PATCH** /rest/v1.0/meeting_attendee_records/{id} | Update meeting attendee record
[**rest_v10_meeting_attendee_records_post**](ProjectManagementMeetingsMeetingAttendeesApi.md#rest_v10_meeting_attendee_records_post) | **POST** /rest/v1.0/meeting_attendee_records | Create meeting attendee record


# **rest_v10_meeting_attendee_records_id_delete**
> rest_v10_meeting_attendee_records_id_delete(procore_company_id, meeting_id, project_id, id)

Delete meeting attendee record

Delete a specified meeting attendee record, disassociating a given user from a meeting

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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingAttendeesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    meeting_id = 56 # int | ID of the Meeting
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Meeting Attendee record

    try:
        # Delete meeting attendee record
        api_instance.rest_v10_meeting_attendee_records_id_delete(procore_company_id, meeting_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingAttendeesApi->rest_v10_meeting_attendee_records_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **meeting_id** | **int**| ID of the Meeting | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Meeting Attendee record | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_meeting_attendee_records_id_patch**
> RestV10MeetingAttendeeRecordsPost201Response rest_v10_meeting_attendee_records_id_patch(procore_company_id, meeting_id, project_id, id, body68)

Update meeting attendee record

Update a Meeting Attendee record.

### Example


```python
import procore_sdk
from procore_sdk.models.body68 import Body68
from procore_sdk.models.rest_v10_meeting_attendee_records_post201_response import RestV10MeetingAttendeeRecordsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingAttendeesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    meeting_id = 56 # int | ID of the Meeting
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Meeting Attendee record
    body68 = procore_sdk.Body68() # Body68 | 

    try:
        # Update meeting attendee record
        api_response = api_instance.rest_v10_meeting_attendee_records_id_patch(procore_company_id, meeting_id, project_id, id, body68)
        print("The response of ProjectManagementMeetingsMeetingAttendeesApi->rest_v10_meeting_attendee_records_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingAttendeesApi->rest_v10_meeting_attendee_records_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **meeting_id** | **int**| ID of the Meeting | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Meeting Attendee record | 
 **body68** | [**Body68**](Body68.md)|  | 

### Return type

[**RestV10MeetingAttendeeRecordsPost201Response**](RestV10MeetingAttendeeRecordsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_meeting_attendee_records_post**
> RestV10MeetingAttendeeRecordsPost201Response rest_v10_meeting_attendee_records_post(procore_company_id, project_id, meeting_id, body68)

Create meeting attendee record

Create a new Meeting Attendee record. This associates a user with a meeting.

### Example


```python
import procore_sdk
from procore_sdk.models.body68 import Body68
from procore_sdk.models.rest_v10_meeting_attendee_records_post201_response import RestV10MeetingAttendeeRecordsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingAttendeesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    meeting_id = 56 # int | ID of the Meeting
    body68 = procore_sdk.Body68() # Body68 | 

    try:
        # Create meeting attendee record
        api_response = api_instance.rest_v10_meeting_attendee_records_post(procore_company_id, project_id, meeting_id, body68)
        print("The response of ProjectManagementMeetingsMeetingAttendeesApi->rest_v10_meeting_attendee_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingAttendeesApi->rest_v10_meeting_attendee_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **meeting_id** | **int**| ID of the Meeting | 
 **body68** | [**Body68**](Body68.md)|  | 

### Return type

[**RestV10MeetingAttendeeRecordsPost201Response**](RestV10MeetingAttendeeRecordsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

