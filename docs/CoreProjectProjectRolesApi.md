# procore_sdk.CoreProjectProjectRolesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_project_roles_get**](CoreProjectProjectRolesApi.md#rest_v10_project_roles_get) | **GET** /rest/v1.0/project_roles | List Project Roles
[**rest_v10_project_roles_id_delete**](CoreProjectProjectRolesApi.md#rest_v10_project_roles_id_delete) | **DELETE** /rest/v1.0/project_roles/{id} | Delete Project Role
[**rest_v10_project_roles_post**](CoreProjectProjectRolesApi.md#rest_v10_project_roles_post) | **POST** /rest/v1.0/project_roles | Create Project Role


# **rest_v10_project_roles_get**
> List[ProjectRole] rest_v10_project_roles_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at)

List Project Roles

Return a list of all relationships between Users and Roles in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.project_role import ProjectRole
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
    api_instance = procore_sdk.CoreProjectProjectRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) created within the specified ISO 8601 datetime range. (optional)

    try:
        # List Project Roles
        api_response = api_instance.rest_v10_project_roles_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at)
        print("The response of CoreProjectProjectRolesApi->rest_v10_project_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectRolesApi->rest_v10_project_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **datetime**| Return item(s) created within the specified ISO 8601 datetime range. | [optional] 

### Return type

[**List[ProjectRole]**](ProjectRole.md)

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

# **rest_v10_project_roles_id_delete**
> rest_v10_project_roles_id_delete(procore_company_id, id, project_id)

Delete Project Role

Remove a relationship between a User and a Role in a specified Project.

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
    api_instance = procore_sdk.CoreProjectProjectRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Project Role
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Project Role
        api_instance.rest_v10_project_roles_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling CoreProjectProjectRolesApi->rest_v10_project_roles_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Project Role | 
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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_project_roles_post**
> ProjectRole rest_v10_project_roles_post(procore_company_id, body36)

Create Project Role

Create a relationship between a User and a Role in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body36 import Body36
from procore_sdk.models.project_role import ProjectRole
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
    api_instance = procore_sdk.CoreProjectProjectRolesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body36 = procore_sdk.Body36() # Body36 | 

    try:
        # Create Project Role
        api_response = api_instance.rest_v10_project_roles_post(procore_company_id, body36)
        print("The response of CoreProjectProjectRolesApi->rest_v10_project_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectProjectRolesApi->rest_v10_project_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body36** | [**Body36**](Body36.md)|  | 

### Return type

[**ProjectRole**](ProjectRole.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

