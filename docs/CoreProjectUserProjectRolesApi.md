# procore_sdk.CoreProjectUserProjectRolesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_user_project_roles_id_patch**](CoreProjectUserProjectRolesApi.md#rest_v10_projects_project_id_user_project_roles_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/user_project_roles/{id} | Update User Project Roles


# **rest_v10_projects_project_id_user_project_roles_id_patch**
> UserProjectRole rest_v10_projects_project_id_user_project_roles_id_patch(procore_company_id, id, project_id, body6=body6)

Update User Project Roles

Set which Users are associated with a specific Project Role. Will remove any users associated with the role if they are not included in the `user_ids` parameter.

### Example


```python
import procore_sdk
from procore_sdk.models.body6 import Body6
from procore_sdk.models.user_project_role import UserProjectRole
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
    api_instance = procore_sdk.CoreProjectUserProjectRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Company Role
    project_id = 56 # int | Unique identifier for the project.
    body6 = procore_sdk.Body6() # Body6 |  (optional)

    try:
        # Update User Project Roles
        api_response = api_instance.rest_v10_projects_project_id_user_project_roles_id_patch(procore_company_id, id, project_id, body6=body6)
        print("The response of CoreProjectUserProjectRolesApi->rest_v10_projects_project_id_user_project_roles_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectUserProjectRolesApi->rest_v10_projects_project_id_user_project_roles_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Company Role | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body6** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**UserProjectRole**](UserProjectRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

