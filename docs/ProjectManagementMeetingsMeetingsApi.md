# procore_sdk.ProjectManagementMeetingsMeetingsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_meetings_ecrion_pdf_generation_data_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_ecrion_pdf_generation_data_get) | **GET** /rest/v1.0/meetings/ecrion_pdf_generation_data | List Ecrion Xml and Template for Meetings
[**rest_v10_meetings_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_get) | **GET** /rest/v1.0/meetings | List meetings
[**rest_v10_meetings_id_delete**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_id_delete) | **DELETE** /rest/v1.0/meetings/{id} | Delete meeting
[**rest_v10_meetings_id_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_id_get) | **GET** /rest/v1.0/meetings/{id} | Show meeting
[**rest_v10_meetings_id_patch**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_id_patch) | **PATCH** /rest/v1.0/meetings/{id} | Update meeting
[**rest_v10_meetings_post**](ProjectManagementMeetingsMeetingsApi.md#rest_v10_meetings_post) | **POST** /rest/v1.0/meetings | Create meeting
[**rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get) | **GET** /rest/v1.1/projects/{project_id}/meetings/ecrion_pdf_generation_data | List Ecrion Xml and Template for Meetings
[**rest_v11_projects_project_id_meetings_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_get) | **GET** /rest/v1.1/projects/{project_id}/meetings | List meetings
[**rest_v11_projects_project_id_meetings_id_delete**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/meetings/{id} | Delete meeting
[**rest_v11_projects_project_id_meetings_id_get**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_id_get) | **GET** /rest/v1.1/projects/{project_id}/meetings/{id} | Show meeting
[**rest_v11_projects_project_id_meetings_id_patch**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/meetings/{id} | Update meeting
[**rest_v11_projects_project_id_meetings_post**](ProjectManagementMeetingsMeetingsApi.md#rest_v11_projects_project_id_meetings_post) | **POST** /rest/v1.1/projects/{project_id}/meetings | Create meeting


# **rest_v10_meetings_ecrion_pdf_generation_data_get**
> RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response rest_v10_meetings_ecrion_pdf_generation_data_get(procore_company_id, project_id, page=page, per_page=per_page)

List Ecrion Xml and Template for Meetings

Returns Ecrion Xml and Template for all Meetings on the Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response import RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Ecrion Xml and Template for Meetings
        api_response = api_instance.rest_v10_meetings_ecrion_pdf_generation_data_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_ecrion_pdf_generation_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_ecrion_pdf_generation_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response**](RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ecrion Template and Xml returned successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_meetings_get**
> List[RestV10MeetingsGet200ResponseInner] rest_v10_meetings_get(procore_company_id, project_id, page=page, per_page=per_page, deleted_only=deleted_only, serializer_view=serializer_view)

List meetings

Returns a list of all Meetings for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_meetings_get200_response_inner import RestV10MeetingsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    deleted_only = True # bool | Indicates whether to only show deleted meetings. When this query parameter is passed the response body will be an array of meetings without grouping. i.e. { \"meetings\":[{Meeting_1}, {Meeting_2}] } (optional)
    serializer_view = 'serializer_view_example' # str | The data set that should be returned from the serializer. The normal view includes default fields. The extended view includes the default fields plus Meeting Template fields. Default view is normal. (optional)

    try:
        # List meetings
        api_response = api_instance.rest_v10_meetings_get(procore_company_id, project_id, page=page, per_page=per_page, deleted_only=deleted_only, serializer_view=serializer_view)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **deleted_only** | **bool**| Indicates whether to only show deleted meetings. When this query parameter is passed the response body will be an array of meetings without grouping. i.e. { \&quot;meetings\&quot;:[{Meeting_1}, {Meeting_2}] } | [optional] 
 **serializer_view** | **str**| The data set that should be returned from the serializer. The normal view includes default fields. The extended view includes the default fields plus Meeting Template fields. Default view is normal. | [optional] 

### Return type

[**List[RestV10MeetingsGet200ResponseInner]**](RestV10MeetingsGet200ResponseInner.md)

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

# **rest_v10_meetings_id_delete**
> rest_v10_meetings_id_delete(procore_company_id, id, project_id)

Delete meeting

Delete a specified meeting from the system

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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the meeting
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete meeting
        api_instance.rest_v10_meetings_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the meeting | 
 **project_id** | **int**| Unique identifier for the project. | 

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

# **rest_v10_meetings_id_get**
> RestV10MeetingsPost201Response rest_v10_meetings_id_get(procore_company_id, id, project_id)

Show meeting

Returns detailed information about a Meeting in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_meetings_post201_response import RestV10MeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the meeting
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show meeting
        api_response = api_instance.rest_v10_meetings_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the meeting | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10MeetingsPost201Response**](RestV10MeetingsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_meetings_id_patch**
> RestV10MeetingsPost201Response rest_v10_meetings_id_patch(procore_company_id, id, body64)

Update meeting

Update a Meeting.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body64 import Body64
from procore_sdk.models.rest_v10_meetings_post201_response import RestV10MeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the meeting
    body64 = procore_sdk.Body64() # Body64 | 

    try:
        # Update meeting
        api_response = api_instance.rest_v10_meetings_id_patch(procore_company_id, id, body64)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the meeting | 
 **body64** | [**Body64**](Body64.md)|  | 

### Return type

[**RestV10MeetingsPost201Response**](RestV10MeetingsPost201Response.md)

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

# **rest_v10_meetings_post**
> RestV10MeetingsPost201Response rest_v10_meetings_post(procore_company_id, body63)

Create meeting

Create a new Meeting.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body63 import Body63
from procore_sdk.models.rest_v10_meetings_post201_response import RestV10MeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body63 = procore_sdk.Body63() # Body63 | 

    try:
        # Create meeting
        api_response = api_instance.rest_v10_meetings_post(procore_company_id, body63)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v10_meetings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body63** | [**Body63**](Body63.md)|  | 

### Return type

[**RestV10MeetingsPost201Response**](RestV10MeetingsPost201Response.md)

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

# **rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get**
> RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get(procore_company_id, project_id, page=page, per_page=per_page)

List Ecrion Xml and Template for Meetings

Returns Ecrion Xml and Template for all Meetings on the Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response import RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Ecrion Xml and Template for Meetings
        api_response = api_instance.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response**](RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ecrion Template and Xml returned successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_meetings_get**
> RestV11ProjectsProjectIdMeetingsGet200Response rest_v11_projects_project_id_meetings_get(procore_company_id, project_id, page=page, per_page=per_page, deleted_only=deleted_only, filters_assignee_id=filters_assignee_id, filters_id=filters_id, serializer_view=serializer_view)

List meetings

Returns a list of all Meetings for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_meetings_get200_response import RestV11ProjectsProjectIdMeetingsGet200Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    deleted_only = True # bool | Indicates whether to only show deleted meetings. When this query parameter is passed the response body will be an array of meetings without grouping. i.e. { \"meetings\":[{Meeting_1}, {Meeting_2}] } (optional)
    filters_assignee_id = [56] # List[int] | Returns meeting(s) with the specified assignee (optional)
    filters_id = [56] # List[int] | Returns meeting(s) with the specified ID(s) (optional)
    serializer_view = 'serializer_view_example' # str | The data set that should be returned from the serializer. The normal view includes default fields. The extended view includes the default fields plus Meeting Template fields. Default view is normal. (optional)

    try:
        # List meetings
        api_response = api_instance.rest_v11_projects_project_id_meetings_get(procore_company_id, project_id, page=page, per_page=per_page, deleted_only=deleted_only, filters_assignee_id=filters_assignee_id, filters_id=filters_id, serializer_view=serializer_view)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **deleted_only** | **bool**| Indicates whether to only show deleted meetings. When this query parameter is passed the response body will be an array of meetings without grouping. i.e. { \&quot;meetings\&quot;:[{Meeting_1}, {Meeting_2}] } | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Returns meeting(s) with the specified assignee | [optional] 
 **filters_id** | [**List[int]**](int.md)| Returns meeting(s) with the specified ID(s) | [optional] 
 **serializer_view** | **str**| The data set that should be returned from the serializer. The normal view includes default fields. The extended view includes the default fields plus Meeting Template fields. Default view is normal. | [optional] 

### Return type

[**RestV11ProjectsProjectIdMeetingsGet200Response**](RestV11ProjectsProjectIdMeetingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_meetings_id_delete**
> rest_v11_projects_project_id_meetings_id_delete(procore_company_id, project_id, id)

Delete meeting

Delete a specified meeting from the system

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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the meeting

    try:
        # Delete meeting
        api_instance.rest_v11_projects_project_id_meetings_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the meeting | 

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

# **rest_v11_projects_project_id_meetings_id_get**
> RestV11ProjectsProjectIdMeetingsPost201Response rest_v11_projects_project_id_meetings_id_get(procore_company_id, project_id, id)

Show meeting

Returns detailed information about a Meeting in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response import RestV11ProjectsProjectIdMeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the meeting

    try:
        # Show meeting
        api_response = api_instance.rest_v11_projects_project_id_meetings_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the meeting | 

### Return type

[**RestV11ProjectsProjectIdMeetingsPost201Response**](RestV11ProjectsProjectIdMeetingsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_meetings_id_patch**
> RestV11ProjectsProjectIdMeetingsPost201Response rest_v11_projects_project_id_meetings_id_patch(procore_company_id, project_id, id, body62)

Update meeting

Update a Meeting.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body62 import Body62
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response import RestV11ProjectsProjectIdMeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the meeting
    body62 = procore_sdk.Body62() # Body62 | 

    try:
        # Update meeting
        api_response = api_instance.rest_v11_projects_project_id_meetings_id_patch(procore_company_id, project_id, id, body62)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the meeting | 
 **body62** | [**Body62**](Body62.md)|  | 

### Return type

[**RestV11ProjectsProjectIdMeetingsPost201Response**](RestV11ProjectsProjectIdMeetingsPost201Response.md)

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

# **rest_v11_projects_project_id_meetings_post**
> RestV11ProjectsProjectIdMeetingsPost201Response rest_v11_projects_project_id_meetings_post(procore_company_id, project_id, body61)

Create meeting

Create a new Meeting.  #### Uploading attachments To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.body61 import Body61
from procore_sdk.models.rest_v11_projects_project_id_meetings_post201_response import RestV11ProjectsProjectIdMeetingsPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body61 = procore_sdk.Body61() # Body61 | 

    try:
        # Create meeting
        api_response = api_instance.rest_v11_projects_project_id_meetings_post(procore_company_id, project_id, body61)
        print("The response of ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingsApi->rest_v11_projects_project_id_meetings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body61** | [**Body61**](Body61.md)|  | 

### Return type

[**RestV11ProjectsProjectIdMeetingsPost201Response**](RestV11ProjectsProjectIdMeetingsPost201Response.md)

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

