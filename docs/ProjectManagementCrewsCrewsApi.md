# procore_sdk.ProjectManagementCrewsCrewsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_crews_get**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_get) | **GET** /rest/v1.0/projects/{project_id}/crews | List all Project Crews
[**rest_v10_projects_project_id_crews_id_delete**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/crews/{id} | Delete a Crew
[**rest_v10_projects_project_id_crews_id_get**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_id_get) | **GET** /rest/v1.0/projects/{project_id}/crews/{id} | Show A Crew
[**rest_v10_projects_project_id_crews_id_patch**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/crews/{id} | Update a Crew
[**rest_v10_projects_project_id_crews_ids_get**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_ids_get) | **GET** /rest/v1.0/projects/{project_id}/crews/ids | List all Project Crew Ids
[**rest_v10_projects_project_id_crews_post**](ProjectManagementCrewsCrewsApi.md#rest_v10_projects_project_id_crews_post) | **POST** /rest/v1.0/projects/{project_id}/crews | Create a new Crew


# **rest_v10_projects_project_id_crews_get**
> List[TimecardEntry8Crew] rest_v10_projects_project_id_crews_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List all Project Crews

Return a list of all Crews with details for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.timecard_entry8_crew import TimecardEntry8Crew
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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all Project Crews
        api_response = api_instance.rest_v10_projects_project_id_crews_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[TimecardEntry8Crew]**](TimecardEntry8Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_crews_id_delete**
> rest_v10_projects_project_id_crews_id_delete(procore_company_id, project_id, id, crew_body)

Delete a Crew

Deleting a Crew associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.crew_body import CrewBody
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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Crew
    crew_body = procore_sdk.CrewBody() # CrewBody | 

    try:
        # Delete a Crew
        api_instance.rest_v10_projects_project_id_crews_id_delete(procore_company_id, project_id, id, crew_body)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Crew | 
 **crew_body** | [**CrewBody**](CrewBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crew Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_crews_id_get**
> TimecardEntry8Crew rest_v10_projects_project_id_crews_id_get(procore_company_id, project_id, id)

Show A Crew

Return Crew detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.timecard_entry8_crew import TimecardEntry8Crew
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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show A Crew
        api_response = api_instance.rest_v10_projects_project_id_crews_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**TimecardEntry8Crew**](TimecardEntry8Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_crews_id_patch**
> TimecardEntry8Crew rest_v10_projects_project_id_crews_id_patch(procore_company_id, project_id, id, crew_body)

Update a Crew

Updating a Crew associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.crew_body import CrewBody
from procore_sdk.models.timecard_entry8_crew import TimecardEntry8Crew
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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Crew
    crew_body = procore_sdk.CrewBody() # CrewBody | 

    try:
        # Update a Crew
        api_response = api_instance.rest_v10_projects_project_id_crews_id_patch(procore_company_id, project_id, id, crew_body)
        print("The response of ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Crew | 
 **crew_body** | [**CrewBody**](CrewBody.md)|  | 

### Return type

[**TimecardEntry8Crew**](TimecardEntry8Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crew Updated |  -  |
**422** | Error creating a Crew |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_crews_ids_get**
> List[int] rest_v10_projects_project_id_crews_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List all Project Crew Ids

Return a list of all Crew Ids with details for a specified Project.

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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all Project Crew Ids
        api_response = api_instance.rest_v10_projects_project_id_crews_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_ids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_crews_post**
> TimecardEntry8Crew rest_v10_projects_project_id_crews_post(procore_company_id, project_id, crew_body)

Create a new Crew

Create a new Crew associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.crew_body import CrewBody
from procore_sdk.models.timecard_entry8_crew import TimecardEntry8Crew
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
    api_instance = procore_sdk.ProjectManagementCrewsCrewsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    crew_body = procore_sdk.CrewBody() # CrewBody | 

    try:
        # Create a new Crew
        api_response = api_instance.rest_v10_projects_project_id_crews_post(procore_company_id, project_id, crew_body)
        print("The response of ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCrewsCrewsApi->rest_v10_projects_project_id_crews_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **crew_body** | [**CrewBody**](CrewBody.md)|  | 

### Return type

[**TimecardEntry8Crew**](TimecardEntry8Crew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Crew Created Succesfully |  -  |
**422** | Error creating a Crew |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

