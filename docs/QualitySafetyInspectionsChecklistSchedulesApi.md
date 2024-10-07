# procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/calculate_first_inspection_created_at | Calculate when the first Inspection of an Inspection Schedule will be created
[**rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/calculate_total_inspections_count | Calculate number of Inspections to create based on Schedule
[**rest_v10_projects_project_id_checklist_schedules_get**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules | List Checklist (Inspection) Schedules
[**rest_v10_projects_project_id_checklist_schedules_id_delete**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/schedules/{id} | Delete Checklist Schedule
[**rest_v10_projects_project_id_checklist_schedules_id_get**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_id_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/{id} | Show Checklist Schedule
[**rest_v10_projects_project_id_checklist_schedules_id_patch**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/checklist/schedules/{id} | Update a Checklist (Inspection) Schedule
[**rest_v10_projects_project_id_checklist_schedules_post**](QualitySafetyInspectionsChecklistSchedulesApi.md#rest_v10_projects_project_id_checklist_schedules_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/schedules | Create a Checklist (Inspection) Schedule


# **rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get**
> RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet200Response rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get(procore_company_id, project_id, rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request)

Calculate when the first Inspection of an Inspection Schedule will be created

Calculates the creation date for the first Inspection to be created based on an Inspection Schedule's temporal attributes.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get200_response import RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet200Response
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request import RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request = procore_sdk.RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest() # RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest | 

    try:
        # Calculate when the first Inspection of an Inspection Schedule will be created
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get(procore_company_id, project_id, rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_checklist_schedules_calculate_first_inspection_created_at_get_request** | [**RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest**](RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGetRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet200Response**](RestV10ProjectsProjectIdChecklistSchedulesCalculateFirstInspectionCreatedAtGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get**
> TotalInspections rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get(procore_company_id, project_id, rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get_request)

Calculate number of Inspections to create based on Schedule

Calculates the total number of Inspections to create based on Schedule parameters.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get_request import RestV10ProjectsProjectIdChecklistSchedulesCalculateTotalInspectionsCountGetRequest
from procore_sdk.models.total_inspections import TotalInspections
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get_request = procore_sdk.RestV10ProjectsProjectIdChecklistSchedulesCalculateTotalInspectionsCountGetRequest() # RestV10ProjectsProjectIdChecklistSchedulesCalculateTotalInspectionsCountGetRequest | 

    try:
        # Calculate number of Inspections to create based on Schedule
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get(procore_company_id, project_id, rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get_request)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_checklist_schedules_calculate_total_inspections_count_get_request** | [**RestV10ProjectsProjectIdChecklistSchedulesCalculateTotalInspectionsCountGetRequest**](RestV10ProjectsProjectIdChecklistSchedulesCalculateTotalInspectionsCountGetRequest.md)|  | 

### Return type

[**TotalInspections**](TotalInspections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_get**
> List[ChecklistSchedule] rest_v10_projects_project_id_checklist_schedules_get(procore_company_id, project_id, filters_updated_at=filters_updated_at, filters_inspection_type_id=filters_inspection_type_id, filters_frequency=filters_frequency, filters_location_id=filters_location_id, filters_list_template_id=filters_list_template_id, filters_assignee_id=filters_assignee_id, filters_first_inspection_due_at=filters_first_inspection_due_at, filters_ends_at=filters_ends_at, filters_ended=filters_ended, sort=sort, page=page, per_page=per_page)

List Checklist (Inspection) Schedules

Returns the Checklist Schedules from Checklists (Inspections) on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule import ChecklistSchedule
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_inspection_type_id = [56] # List[int] | Return schedule(s) with the specified Checklist Type IDs (optional)
    filters_frequency = ['filters_frequency_example'] # List[str] | Return schedule(s) with the specified Frequency Types (optional)
    filters_location_id = [56] # List[int] | Return schedule(s) with the specified Location IDs (optional)
    filters_list_template_id = [56] # List[int] | Return schedule(s) with the specified Inspection Template IDs (optional)
    filters_assignee_id = [56] # List[int] | Return schedule(s) with the specified Assignee IDs (optional)
    filters_first_inspection_due_at = ['2013-10-20'] # List[date] | Return schedule(s) with the specified First Inspection Due Date (optional)
    filters_ends_at = ['2013-10-20'] # List[date] | Return schedule(s) with the specified Last Inspection Due Date. (optional)
    filters_ended = True # bool | Return schedule(s) that are finished when true, returns unfinished schedule(s) otherwise (optional)
    sort = 'sort_example' # str | Sort schedule(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Checklist (Inspection) Schedules
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_get(procore_company_id, project_id, filters_updated_at=filters_updated_at, filters_inspection_type_id=filters_inspection_type_id, filters_frequency=filters_frequency, filters_location_id=filters_location_id, filters_list_template_id=filters_list_template_id, filters_assignee_id=filters_assignee_id, filters_first_inspection_due_at=filters_first_inspection_due_at, filters_ends_at=filters_ends_at, filters_ended=filters_ended, sort=sort, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_inspection_type_id** | [**List[int]**](int.md)| Return schedule(s) with the specified Checklist Type IDs | [optional] 
 **filters_frequency** | [**List[str]**](str.md)| Return schedule(s) with the specified Frequency Types | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return schedule(s) with the specified Location IDs | [optional] 
 **filters_list_template_id** | [**List[int]**](int.md)| Return schedule(s) with the specified Inspection Template IDs | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Return schedule(s) with the specified Assignee IDs | [optional] 
 **filters_first_inspection_due_at** | [**List[date]**](date.md)| Return schedule(s) with the specified First Inspection Due Date | [optional] 
 **filters_ends_at** | [**List[date]**](date.md)| Return schedule(s) with the specified Last Inspection Due Date. | [optional] 
 **filters_ended** | **bool**| Return schedule(s) that are finished when true, returns unfinished schedule(s) otherwise | [optional] 
 **sort** | **str**| Sort schedule(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistSchedule]**](ChecklistSchedule.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_id_delete**
> rest_v10_projects_project_id_checklist_schedules_id_delete(procore_company_id, project_id, id)

Delete Checklist Schedule

Delete a Checklist Schedule in a specified Project.

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Schedule ID

    try:
        # Delete Checklist Schedule
        api_instance.rest_v10_projects_project_id_checklist_schedules_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Schedule ID | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_id_get**
> ChecklistSchedule rest_v10_projects_project_id_checklist_schedules_id_get(procore_company_id, project_id, id)

Show Checklist Schedule

Retrieves Checklist Schedule in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule import ChecklistSchedule
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Schedule ID

    try:
        # Show Checklist Schedule
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Schedule ID | 

### Return type

[**ChecklistSchedule**](ChecklistSchedule.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_id_patch**
> ChecklistSchedule rest_v10_projects_project_id_checklist_schedules_id_patch(procore_company_id, project_id, id, checklist_schedule_body1=checklist_schedule_body1)

Update a Checklist (Inspection) Schedule

Updates a Checklist (Inspection) Schedule in a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule import ChecklistSchedule
from procore_sdk.models.checklist_schedule_body1 import ChecklistScheduleBody1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Checklist Schedule ID
    checklist_schedule_body1 = procore_sdk.ChecklistScheduleBody1() # ChecklistScheduleBody1 |  (optional)

    try:
        # Update a Checklist (Inspection) Schedule
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_id_patch(procore_company_id, project_id, id, checklist_schedule_body1=checklist_schedule_body1)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Checklist Schedule ID | 
 **checklist_schedule_body1** | [**ChecklistScheduleBody1**](ChecklistScheduleBody1.md)|  | [optional] 

### Return type

[**ChecklistSchedule**](ChecklistSchedule.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_post**
> ChecklistSchedule rest_v10_projects_project_id_checklist_schedules_post(procore_company_id, project_id, checklist_schedule_body=checklist_schedule_body)

Create a Checklist (Inspection) Schedule

Creates a Checklist Schedule from a Checklist (Inspection) Template on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule import ChecklistSchedule
from procore_sdk.models.checklist_schedule_body import ChecklistScheduleBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistSchedulesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    checklist_schedule_body = procore_sdk.ChecklistScheduleBody() # ChecklistScheduleBody |  (optional)

    try:
        # Create a Checklist (Inspection) Schedule
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_post(procore_company_id, project_id, checklist_schedule_body=checklist_schedule_body)
        print("The response of QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistSchedulesApi->rest_v10_projects_project_id_checklist_schedules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_schedule_body** | [**ChecklistScheduleBody**](ChecklistScheduleBody.md)|  | [optional] 

### Return type

[**ChecklistSchedule**](ChecklistSchedule.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

