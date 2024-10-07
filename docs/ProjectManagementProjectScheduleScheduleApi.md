# procore_sdk.ProjectManagementProjectScheduleScheduleApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_schedule_get**](ProjectManagementProjectScheduleScheduleApi.md#rest_v10_projects_project_id_schedule_get) | **GET** /rest/v1.0/projects/{project_id}/schedule | Get Schedule Metadata
[**rest_v10_projects_project_id_schedule_patch**](ProjectManagementProjectScheduleScheduleApi.md#rest_v10_projects_project_id_schedule_patch) | **PATCH** /rest/v1.0/projects/{project_id}/schedule | Update Schedule Metadata


# **rest_v10_projects_project_id_schedule_get**
> RestV10ProjectsProjectIdScheduleGet200Response rest_v10_projects_project_id_schedule_get(procore_company_id, project_id)

Get Schedule Metadata

Returns metadata about this Project's Schedule, including information about the Schedule integration configuration for the current project.  #### Schedule Types  | Type                                                 | Key                           | |------------------------------------------------------|-------------------------------| | File-based schedule integration via web browser      | \"Microsoft Project\"           | | File-based schedule integration via Procore Drive    | \"Microsoft Project 2010\"      | | File-based schedule integration via Procore Documents| \"Microsoft Project Documents\" | | Primavera P6 database integration via Procore Drive  | \"Primavera P6\"                |  Note that the schedule types listed as \"Microsoft Project\", \"Microsoft Project 2010\", and \"Microsoft Project Documents\" are functionally identical. In all cases Procore can consume any supported schedule file type and extract data from it, not just Microsoft Project. Schedule files can be uploaded either via Procore Drive, via the Procore Documents tool, or via the Procore Schedule tool, regardless of which of these three types is selected. Where Primavera P6 database integration via Procore Drive is in use, the `p6_id` attribute returned by this API indicates which P6 project Procore Drive is extracting data from. 

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response import RestV10ProjectsProjectIdScheduleGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Schedule Metadata
        api_response = api_instance.rest_v10_projects_project_id_schedule_get(procore_company_id, project_id)
        print("The response of ProjectManagementProjectScheduleScheduleApi->rest_v10_projects_project_id_schedule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleApi->rest_v10_projects_project_id_schedule_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdScheduleGet200Response**](RestV10ProjectsProjectIdScheduleGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule metadata |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_schedule_patch**
> RestV10ProjectsProjectIdScheduleGet200Response rest_v10_projects_project_id_schedule_patch(procore_company_id, project_id, body15)

Update Schedule Metadata

Updates the Schedule integration type for a project.  #### Schedule Types  | Type                                                 | Key                           | |------------------------------------------------------|-------------------------------| | File-based schedule integration via web browser      | \"Microsoft Project\"           | | File-based schedule integration via Procore Drive    | \"Microsoft Project 2010\"      | | File-based schedule integration via Procore Documents| \"Microsoft Project Documents\" | | Primavera P6 database integration via Procore Drive  | \"Primavera P6\"                |  Note that the schedule types listed as \"Microsoft Project\", \"Microsoft Project 2010\", and \"Microsoft Project Documents\" are functionally identical. In all cases Procore can consume any supported schedule file type and extract data from it, not just Microsoft Project. Schedule files can be uploaded either via Procore Drive, via the Procore Documents tool, or via the Procore Schedule tool, regardless of which of these three types is selected. Where Primavera P6 database integration via Procore Drive is in use, the `p6_id` attribute returned by this API indicates which P6 project Procore Drive is extracting data from. 

### Example


```python
import procore_sdk
from procore_sdk.models.body15 import Body15
from procore_sdk.models.rest_v10_projects_project_id_schedule_get200_response import RestV10ProjectsProjectIdScheduleGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body15 = procore_sdk.Body15() # Body15 | 

    try:
        # Update Schedule Metadata
        api_response = api_instance.rest_v10_projects_project_id_schedule_patch(procore_company_id, project_id, body15)
        print("The response of ProjectManagementProjectScheduleScheduleApi->rest_v10_projects_project_id_schedule_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleApi->rest_v10_projects_project_id_schedule_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body15** | [**Body15**](Body15.md)|  | 

### Return type

[**RestV10ProjectsProjectIdScheduleGet200Response**](RestV10ProjectsProjectIdScheduleGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule metadata |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

