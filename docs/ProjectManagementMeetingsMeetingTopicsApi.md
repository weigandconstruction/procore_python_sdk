# procore_sdk.ProjectManagementMeetingsMeetingTopicsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_meeting_topics_id_patch**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v10_meeting_topics_id_patch) | **PATCH** /rest/v1.0/meeting_topics/{id} | Update meeting topic
[**rest_v10_meeting_topics_parent_minutes_get**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v10_meeting_topics_parent_minutes_get) | **GET** /rest/v1.0/meeting_topics/parent_minutes | Get the minutes and date created for all parent topics
[**rest_v10_meeting_topics_post**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v10_meeting_topics_post) | **POST** /rest/v1.0/meeting_topics | Create meeting topic
[**rest_v11_projects_project_id_meeting_topics_id_patch**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v11_projects_project_id_meeting_topics_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/meeting_topics/{id} | Update meeting topic
[**rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get) | **GET** /rest/v1.1/projects/{project_id}/meeting_topics/{meeting_topic_id}/parent_minutes | Get the minutes and date created for all parent topics
[**rest_v11_projects_project_id_meeting_topics_post**](ProjectManagementMeetingsMeetingTopicsApi.md#rest_v11_projects_project_id_meeting_topics_post) | **POST** /rest/v1.1/projects/{project_id}/meeting_topics | Create meeting topic


# **rest_v10_meeting_topics_id_patch**
> RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner rest_v10_meeting_topics_id_patch(procore_company_id, id, body66)

Update meeting topic

Update an existing Meeting Topic.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body66 import Body66
from procore_sdk.models.rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner import RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the meeting topic
    body66 = procore_sdk.Body66() # Body66 | 

    try:
        # Update meeting topic
        api_response = api_instance.rest_v10_meeting_topics_id_patch(procore_company_id, id, body66)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the meeting topic | 
 **body66** | [**Body66**](Body66.md)|  | 

### Return type

[**RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner**](RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.md)

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

# **rest_v10_meeting_topics_parent_minutes_get**
> List[RestV10MeetingTopicsParentMinutesGet200ResponseInner] rest_v10_meeting_topics_parent_minutes_get(procore_company_id, meeting_id, meeting_topic_id)

Get the minutes and date created for all parent topics

Returns an array of objects of minutes and created_on values for all parent meeting topics

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_meeting_topics_parent_minutes_get200_response_inner import RestV10MeetingTopicsParentMinutesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    meeting_id = 56 # int | ID of the meeting
    meeting_topic_id = 56 # int | ID of the meeting topic

    try:
        # Get the minutes and date created for all parent topics
        api_response = api_instance.rest_v10_meeting_topics_parent_minutes_get(procore_company_id, meeting_id, meeting_topic_id)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_parent_minutes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_parent_minutes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **meeting_id** | **int**| ID of the meeting | 
 **meeting_topic_id** | **int**| ID of the meeting topic | 

### Return type

[**List[RestV10MeetingTopicsParentMinutesGet200ResponseInner]**](RestV10MeetingTopicsParentMinutesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have the right permissions to view the meeting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_meeting_topics_post**
> RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner rest_v10_meeting_topics_post(procore_company_id, body66)

Create meeting topic

Creates Meeting Topic.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body66 import Body66
from procore_sdk.models.rest_v10_meetings_post201_response_meeting_categories_inner_meeting_topic_inner import RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body66 = procore_sdk.Body66() # Body66 | 

    try:
        # Create meeting topic
        api_response = api_instance.rest_v10_meeting_topics_post(procore_company_id, body66)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v10_meeting_topics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body66** | [**Body66**](Body66.md)|  | 

### Return type

[**RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner**](RestV10MeetingsPost201ResponseMeetingCategoriesInnerMeetingTopicInner.md)

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

# **rest_v11_projects_project_id_meeting_topics_id_patch**
> RestV11ProjectsProjectIdMeetingTopicsPost201Response rest_v11_projects_project_id_meeting_topics_id_patch(procore_company_id, project_id, id, body65)

Update meeting topic

Update an existing Meeting Topic.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body65 import Body65
from procore_sdk.models.rest_v11_projects_project_id_meeting_topics_post201_response import RestV11ProjectsProjectIdMeetingTopicsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Meeting Topic
    body65 = procore_sdk.Body65() # Body65 | 

    try:
        # Update meeting topic
        api_response = api_instance.rest_v11_projects_project_id_meeting_topics_id_patch(procore_company_id, project_id, id, body65)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Meeting Topic | 
 **body65** | [**Body65**](Body65.md)|  | 

### Return type

[**RestV11ProjectsProjectIdMeetingTopicsPost201Response**](RestV11ProjectsProjectIdMeetingTopicsPost201Response.md)

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

# **rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get**
> List[RestV11ProjectsProjectIdMeetingTopicsMeetingTopicIdParentMinutesGet200ResponseInner] rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get(procore_company_id, project_id, meeting_id, meeting_topic_id)

Get the minutes and date created for all parent topics

Returns an array of objects of minutes and created_on values for all parent meeting topics

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get200_response_inner import RestV11ProjectsProjectIdMeetingTopicsMeetingTopicIdParentMinutesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    meeting_id = 56 # int | ID of the meeting
    meeting_topic_id = 56 # int | ID of the meeting topic

    try:
        # Get the minutes and date created for all parent topics
        api_response = api_instance.rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get(procore_company_id, project_id, meeting_id, meeting_topic_id)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_meeting_topic_id_parent_minutes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **meeting_id** | **int**| ID of the meeting | 
 **meeting_topic_id** | **int**| ID of the meeting topic | 

### Return type

[**List[RestV11ProjectsProjectIdMeetingTopicsMeetingTopicIdParentMinutesGet200ResponseInner]**](RestV11ProjectsProjectIdMeetingTopicsMeetingTopicIdParentMinutesGet200ResponseInner.md)

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
**403** | User does not have the right permissions to view the meeting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_meeting_topics_post**
> RestV11ProjectsProjectIdMeetingTopicsPost201Response rest_v11_projects_project_id_meeting_topics_post(procore_company_id, project_id, body65)

Create meeting topic

Creates Meeting Topic.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body65 import Body65
from procore_sdk.models.rest_v11_projects_project_id_meeting_topics_post201_response import RestV11ProjectsProjectIdMeetingTopicsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingTopicsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body65 = procore_sdk.Body65() # Body65 | 

    try:
        # Create meeting topic
        api_response = api_instance.rest_v11_projects_project_id_meeting_topics_post(procore_company_id, project_id, body65)
        print("The response of ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingTopicsApi->rest_v11_projects_project_id_meeting_topics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body65** | [**Body65**](Body65.md)|  | 

### Return type

[**RestV11ProjectsProjectIdMeetingTopicsPost201Response**](RestV11ProjectsProjectIdMeetingTopicsPost201Response.md)

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

