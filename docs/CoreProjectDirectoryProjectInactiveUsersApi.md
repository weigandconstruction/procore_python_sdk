# procore_sdk.CoreProjectDirectoryProjectInactiveUsersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_users_inactive_get**](CoreProjectDirectoryProjectInactiveUsersApi.md#rest_v10_projects_project_id_users_inactive_get) | **GET** /rest/v1.0/projects/{project_id}/users/inactive | List Project inactive users
[**rest_v10_projects_project_id_users_inactive_id_patch**](CoreProjectDirectoryProjectInactiveUsersApi.md#rest_v10_projects_project_id_users_inactive_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/users/inactive/{id} | Reactivate project user.


# **rest_v10_projects_project_id_users_inactive_get**
> List[InactiveUser] rest_v10_projects_project_id_users_inactive_get(procore_company_id, project_id, page=page, per_page=per_page, sort=sort)

List Project inactive users

Return a list of all Inactive Users associated with a Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.inactive_user import InactiveUser
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInactiveUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List Project inactive users
        api_response = api_instance.rest_v10_projects_project_id_users_inactive_get(procore_company_id, project_id, page=page, per_page=per_page, sort=sort)
        print("The response of CoreProjectDirectoryProjectInactiveUsersApi->rest_v10_projects_project_id_users_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInactiveUsersApi->rest_v10_projects_project_id_users_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[InactiveUser]**](InactiveUser.md)

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

# **rest_v10_projects_project_id_users_inactive_id_patch**
> User rest_v10_projects_project_id_users_inactive_id_patch(procore_company_id, project_id, id)

Reactivate project user.

Reactivate the specified User. #### OK Response For null values, the key won't be returned   

### Example


```python
import procore_sdk
from procore_sdk.models.user import User
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInactiveUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the user

    try:
        # Reactivate project user.
        api_response = api_instance.rest_v10_projects_project_id_users_inactive_id_patch(procore_company_id, project_id, id)
        print("The response of CoreProjectDirectoryProjectInactiveUsersApi->rest_v10_projects_project_id_users_inactive_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInactiveUsersApi->rest_v10_projects_project_id_users_inactive_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the user | 

### Return type

[**User**](User.md)

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

