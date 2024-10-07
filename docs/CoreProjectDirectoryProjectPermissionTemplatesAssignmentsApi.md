# procore_sdk.CoreProjectDirectoryProjectPermissionTemplatesAssignmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_permission_template_assignments_patch**](CoreProjectDirectoryProjectPermissionTemplatesAssignmentsApi.md#rest_v10_projects_project_id_permission_template_assignments_patch) | **PATCH** /rest/v1.0/projects/{project_id}/permission_template_assignments | Update a permission template assignment for a user on a project


# **rest_v10_projects_project_id_permission_template_assignments_patch**
> RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatch200Response rest_v10_projects_project_id_permission_template_assignments_patch(procore_company_id, project_id, rest_v10_projects_project_id_permission_template_assignments_patch_request)

Update a permission template assignment for a user on a project

Returns the user_id and permission_template_id for the new permission template assignment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_permission_template_assignments_patch200_response import RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatch200Response
from procore_sdk.models.rest_v10_projects_project_id_permission_template_assignments_patch_request import RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatchRequest
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectPermissionTemplatesAssignmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_permission_template_assignments_patch_request = procore_sdk.RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatchRequest() # RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatchRequest | 

    try:
        # Update a permission template assignment for a user on a project
        api_response = api_instance.rest_v10_projects_project_id_permission_template_assignments_patch(procore_company_id, project_id, rest_v10_projects_project_id_permission_template_assignments_patch_request)
        print("The response of CoreProjectDirectoryProjectPermissionTemplatesAssignmentsApi->rest_v10_projects_project_id_permission_template_assignments_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectPermissionTemplatesAssignmentsApi->rest_v10_projects_project_id_permission_template_assignments_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_permission_template_assignments_patch_request** | [**RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatchRequest**](RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatch200Response**](RestV10ProjectsProjectIdPermissionTemplateAssignmentsPatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

