# procore_sdk.ProjectManagementMeetingsMeetingCategoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_meeting_categories_get**](ProjectManagementMeetingsMeetingCategoriesApi.md#rest_v10_meeting_categories_get) | **GET** /rest/v1.0/meeting_categories | List meeting categories
[**rest_v10_meeting_categories_id_patch**](ProjectManagementMeetingsMeetingCategoriesApi.md#rest_v10_meeting_categories_id_patch) | **PATCH** /rest/v1.0/meeting_categories/{id} | Update meeting category
[**rest_v10_meeting_categories_post**](ProjectManagementMeetingsMeetingCategoriesApi.md#rest_v10_meeting_categories_post) | **POST** /rest/v1.0/meeting_categories | Create meeting category


# **rest_v10_meeting_categories_get**
> List[RestV10MeetingCategoriesGet200ResponseInner] rest_v10_meeting_categories_get(procore_company_id, project_id, meeting_id, page=page, per_page=per_page)

List meeting categories

Returns all Meeting Categories for a given Meeting.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_meeting_categories_get200_response_inner import RestV10MeetingCategoriesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    meeting_id = 56 # int | ID of the meeting
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List meeting categories
        api_response = api_instance.rest_v10_meeting_categories_get(procore_company_id, project_id, meeting_id, page=page, per_page=per_page)
        print("The response of ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **meeting_id** | **int**| ID of the meeting | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10MeetingCategoriesGet200ResponseInner]**](RestV10MeetingCategoriesGet200ResponseInner.md)

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

# **rest_v10_meeting_categories_id_patch**
> RestV10MeetingCategoriesPost201Response rest_v10_meeting_categories_id_patch(procore_company_id, id, body67)

Update meeting category

Update a Meeting Category.

### Example


```python
import procore_sdk
from procore_sdk.models.body67 import Body67
from procore_sdk.models.rest_v10_meeting_categories_post201_response import RestV10MeetingCategoriesPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the meeting category
    body67 = procore_sdk.Body67() # Body67 | 

    try:
        # Update meeting category
        api_response = api_instance.rest_v10_meeting_categories_id_patch(procore_company_id, id, body67)
        print("The response of ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the meeting category | 
 **body67** | [**Body67**](Body67.md)|  | 

### Return type

[**RestV10MeetingCategoriesPost201Response**](RestV10MeetingCategoriesPost201Response.md)

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

# **rest_v10_meeting_categories_post**
> RestV10MeetingCategoriesPost201Response rest_v10_meeting_categories_post(procore_company_id, body67)

Create meeting category

Create a new Meeting Category.

### Example


```python
import procore_sdk
from procore_sdk.models.body67 import Body67
from procore_sdk.models.rest_v10_meeting_categories_post201_response import RestV10MeetingCategoriesPost201Response
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
    api_instance = procore_sdk.ProjectManagementMeetingsMeetingCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body67 = procore_sdk.Body67() # Body67 | 

    try:
        # Create meeting category
        api_response = api_instance.rest_v10_meeting_categories_post(procore_company_id, body67)
        print("The response of ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementMeetingsMeetingCategoriesApi->rest_v10_meeting_categories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body67** | [**Body67**](Body67.md)|  | 

### Return type

[**RestV10MeetingCategoriesPost201Response**](RestV10MeetingCategoriesPost201Response.md)

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

