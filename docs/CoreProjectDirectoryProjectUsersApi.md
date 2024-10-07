# procore_sdk.CoreProjectDirectoryProjectUsersApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_users_get**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_get) | **GET** /rest/v1.0/projects/{project_id}/users | List Project Users
[**rest_v10_projects_project_id_users_id_actions_add_post**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_id_actions_add_post) | **POST** /rest/v1.0/projects/{project_id}/users/{id}/actions/add | Add company user to project
[**rest_v10_projects_project_id_users_id_actions_remove_delete**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_id_actions_remove_delete) | **DELETE** /rest/v1.0/projects/{project_id}/users/{id}/actions/remove | Remove a user from the project
[**rest_v10_projects_project_id_users_id_get**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_id_get) | **GET** /rest/v1.0/projects/{project_id}/users/{id} | Show project user
[**rest_v10_projects_project_id_users_id_patch**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/users/{id} | Update project user
[**rest_v10_projects_project_id_users_post**](CoreProjectDirectoryProjectUsersApi.md#rest_v10_projects_project_id_users_post) | **POST** /rest/v1.0/projects/{project_id}/users | Create project user


# **rest_v10_projects_project_id_users_get**
> List[RestV10ProjectsProjectIdUsersGet200ResponseInner] rest_v10_projects_project_id_users_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_permission_template=filters_permission_template, filters_vendor_id=filters_vendor_id, filters_origin_id=filters_origin_id, filters_trade_id=filters_trade_id, filters_search=filters_search, filters_employee=filters_employee, filters_id=filters_id, sort=sort)

List Project Users

Returns a list of active users associated with a project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_users_get200_response_inner import RestV10ProjectsProjectIdUsersGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to the compact view. Otherwise, the default view is normal. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_permission_template = 56 # int | Permission Template ID. Returns item(s) assiociated with the specified Permission Template ID. (optional)
    filters_vendor_id = [56] # List[int] | Return item(s) with the specified Vendor IDs. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_trade_id = [56] # List[int] | Returns users whose vendor record is associated with the specified trade id(s). (optional)
    filters_search = 'filters_search_example' # str | Returns users where the search string matches the user's first name, last name, email address, keywords, job title, or company name (optional)
    filters_employee = True # bool | Returns users whose is_employee attribute matches the parameter. (optional)
    filters_id = 56 # int | Returns users whose id attribute matches the parameter. (optional)
    sort = 'sort_example' # str | Returns items with the specified sort. (optional)

    try:
        # List Project Users
        api_response = api_instance.rest_v10_projects_project_id_users_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_permission_template=filters_permission_template, filters_vendor_id=filters_vendor_id, filters_origin_id=filters_origin_id, filters_trade_id=filters_trade_id, filters_search=filters_search, filters_employee=filters_employee, filters_id=filters_id, sort=sort)
        print("The response of CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to the compact view. Otherwise, the default view is normal. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_permission_template** | **int**| Permission Template ID. Returns item(s) assiociated with the specified Permission Template ID. | [optional] 
 **filters_vendor_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor IDs. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Returns users whose vendor record is associated with the specified trade id(s). | [optional] 
 **filters_search** | **str**| Returns users where the search string matches the user&#39;s first name, last name, email address, keywords, job title, or company name | [optional] 
 **filters_employee** | **bool**| Returns users whose is_employee attribute matches the parameter. | [optional] 
 **filters_id** | **int**| Returns users whose id attribute matches the parameter. | [optional] 
 **sort** | **str**| Returns items with the specified sort. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdUsersGet200ResponseInner]**](RestV10ProjectsProjectIdUsersGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_users_id_actions_add_post**
> NormalView rest_v10_projects_project_id_users_id_actions_add_post(procore_company_id, project_id, id, rest_v10_projects_project_id_users_id_actions_add_post_request=rest_v10_projects_project_id_users_id_actions_add_post_request)

Add company user to project

Adds a user from the Company Directory to the Project Directory. #### Created Response For null values, the key won't be returned   

### Example


```python
import procore_sdk
from procore_sdk.models.normal_view import NormalView
from procore_sdk.models.rest_v10_projects_project_id_users_id_actions_add_post_request import RestV10ProjectsProjectIdUsersIdActionsAddPostRequest
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the user
    rest_v10_projects_project_id_users_id_actions_add_post_request = procore_sdk.RestV10ProjectsProjectIdUsersIdActionsAddPostRequest() # RestV10ProjectsProjectIdUsersIdActionsAddPostRequest |  (optional)

    try:
        # Add company user to project
        api_response = api_instance.rest_v10_projects_project_id_users_id_actions_add_post(procore_company_id, project_id, id, rest_v10_projects_project_id_users_id_actions_add_post_request=rest_v10_projects_project_id_users_id_actions_add_post_request)
        print("The response of CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_actions_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_actions_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the user | 
 **rest_v10_projects_project_id_users_id_actions_add_post_request** | [**RestV10ProjectsProjectIdUsersIdActionsAddPostRequest**](RestV10ProjectsProjectIdUsersIdActionsAddPostRequest.md)|  | [optional] 

### Return type

[**NormalView**](NormalView.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_users_id_actions_remove_delete**
> rest_v10_projects_project_id_users_id_actions_remove_delete(procore_company_id, project_id, id)

Remove a user from the project

Removes a specified user from a project.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the user

    try:
        # Remove a user from the project
        api_instance.rest_v10_projects_project_id_users_id_actions_remove_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_actions_remove_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the user | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_users_id_get**
> User rest_v10_projects_project_id_users_id_get(procore_company_id, project_id, id)

Show project user

Show detail on a specified Project User.  #### OK Response For null values, the key won't be returned

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the user

    try:
        # Show project user
        api_response = api_instance.rest_v10_projects_project_id_users_id_get(procore_company_id, project_id, id)
        print("The response of CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_get: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_users_id_patch**
> User rest_v10_projects_project_id_users_id_patch(procore_company_id, project_id, id, project_user_body1, run_configurable_validations=run_configurable_validations)

Update project user

Updates the specified project user. The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information. For OK responses with null values, the key will not be returned.  Note: The `is_active` parameter value requires a boolean value to be passed in. Setting this parameter to false deactivates the user. If you have deactivated a user by setting `is_active` to false and then try to reactivate the user by setting `is_active` to true, you will receive an error message. To reactivate the user via API, you need to call the [Sync Company Users](/reference/rest/v1/company-users#sync-company-users) method. 

### Example


```python
import procore_sdk
from procore_sdk.models.project_user_body1 import ProjectUserBody1
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the user
    project_user_body1 = procore_sdk.ProjectUserBody1() # ProjectUserBody1 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update project user
        api_response = api_instance.rest_v10_projects_project_id_users_id_patch(procore_company_id, project_id, id, project_user_body1, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the user | 
 **project_user_body1** | [**ProjectUserBody1**](ProjectUserBody1.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**User**](User.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_users_post**
> User rest_v10_projects_project_id_users_post(procore_company_id, project_id, project_user_body, run_configurable_validations=run_configurable_validations)

Create project user

Creates a new user in the specified project.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.  #### Created Response For null values, the key won't be returned

### Example


```python
import procore_sdk
from procore_sdk.models.project_user_body import ProjectUserBody
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectUsersApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    project_user_body = procore_sdk.ProjectUserBody() # ProjectUserBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create project user
        api_response = api_instance.rest_v10_projects_project_id_users_post(procore_company_id, project_id, project_user_body, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectUsersApi->rest_v10_projects_project_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **project_user_body** | [**ProjectUserBody**](ProjectUserBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**User**](User.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

