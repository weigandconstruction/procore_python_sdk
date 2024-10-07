# procore_sdk.QualitySafetyInspectionsChecklistScheduleFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get**](QualitySafetyInspectionsChecklistScheduleFilterOptionsApi.md#rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/filter_options/assignees | Checklist Schedule Assignee Filter Options
[**rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get**](QualitySafetyInspectionsChecklistScheduleFilterOptionsApi.md#rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/filter_options/inspection_templates | Checklist Schedule Inspection Template Filter Options
[**rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get**](QualitySafetyInspectionsChecklistScheduleFilterOptionsApi.md#rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/filter_options/locations | Checklist Schedule Location Filter Options
[**rest_v10_projects_project_id_checklist_schedules_filter_options_types_get**](QualitySafetyInspectionsChecklistScheduleFilterOptionsApi.md#rest_v10_projects_project_id_checklist_schedules_filter_options_types_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/filter_options/types | Checklist Schedule Inspection Type Filter Options


# **rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get**
> List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner] rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get(procore_company_id, project_id)

Checklist Schedule Assignee Filter Options

Returns assignees of the checklist schedule

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get200_response_inner import RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Checklist Schedule Assignee Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get**
> List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner] rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get(procore_company_id, project_id)

Checklist Schedule Inspection Template Filter Options

Returns inspection templates associated to the inspections schedule

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get200_response_inner import RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Checklist Schedule Inspection Template Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_inspection_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get**
> List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner] rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get(procore_company_id, project_id)

Checklist Schedule Location Filter Options

Returns locations associated to the inspection schedules

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get200_response_inner import RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Checklist Schedule Location Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_schedules_filter_options_types_get**
> List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner] rest_v10_projects_project_id_checklist_schedules_filter_options_types_get(procore_company_id, project_id)

Checklist Schedule Inspection Type Filter Options

Returns Inspection types associated to inspection schedules

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_checklist_schedules_filter_options_assignees_get200_response_inner import RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Checklist Schedule Inspection Type Filter Options
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_filter_options_types_get(procore_company_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleFilterOptionsApi->rest_v10_projects_project_id_checklist_schedules_filter_options_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdChecklistSchedulesFilterOptionsAssigneesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

