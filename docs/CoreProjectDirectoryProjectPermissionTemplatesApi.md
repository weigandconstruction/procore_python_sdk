# procore_sdk.CoreProjectDirectoryProjectPermissionTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_permission_templates_get**](CoreProjectDirectoryProjectPermissionTemplatesApi.md#rest_v10_projects_project_id_permission_templates_get) | **GET** /rest/v1.0/projects/{project_id}/permission_templates | List all available permission templates for a Project


# **rest_v10_projects_project_id_permission_templates_get**
> List[RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner] rest_v10_projects_project_id_permission_templates_get(procore_company_id, project_id, filters_assignables_only=filters_assignables_only)

List all available permission templates for a Project

Returns the name, id, and project specific status for all Permission Templates available to use on the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_permission_templates_get200_response_inner import RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectPermissionTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_assignables_only = True # bool | Returns user's assignable permission templates (optional)

    try:
        # List all available permission templates for a Project
        api_response = api_instance.rest_v10_projects_project_id_permission_templates_get(procore_company_id, project_id, filters_assignables_only=filters_assignables_only)
        print("The response of CoreProjectDirectoryProjectPermissionTemplatesApi->rest_v10_projects_project_id_permission_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectPermissionTemplatesApi->rest_v10_projects_project_id_permission_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_assignables_only** | **bool**| Returns user&#39;s assignable permission templates | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdPermissionTemplatesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

