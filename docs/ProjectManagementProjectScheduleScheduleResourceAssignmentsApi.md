# procore_sdk.ProjectManagementProjectScheduleScheduleResourceAssignmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v11_projects_project_id_schedule_resource_assignments_id_get**](ProjectManagementProjectScheduleScheduleResourceAssignmentsApi.md#rest_v11_projects_project_id_schedule_resource_assignments_id_get) | **GET** /rest/v1.1/projects/{project_id}/schedule/resource_assignments/{id} | Show resource assignment


# **rest_v11_projects_project_id_schedule_resource_assignments_id_get**
> ResourceAssignment rest_v11_projects_project_id_schedule_resource_assignments_id_get(procore_company_id, project_id, id)

Show resource assignment

Show detail on the specified Resource Assignment.

### Example


```python
import procore_sdk
from procore_sdk.models.resource_assignment import ResourceAssignment
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleResourceAssignmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the resource

    try:
        # Show resource assignment
        api_response = api_instance.rest_v11_projects_project_id_schedule_resource_assignments_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementProjectScheduleScheduleResourceAssignmentsApi->rest_v11_projects_project_id_schedule_resource_assignments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleResourceAssignmentsApi->rest_v11_projects_project_id_schedule_resource_assignments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the resource | 

### Return type

[**ResourceAssignment**](ResourceAssignment.md)

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

