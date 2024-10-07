# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_get**](ProjectManagementCoordinationIssuesCoordinationIssuesApi.md#rest_v10_coordination_issues_get) | **GET** /rest/v1.0/coordination_issues | List Coordination Issues
[**rest_v10_coordination_issues_id_delete**](ProjectManagementCoordinationIssuesCoordinationIssuesApi.md#rest_v10_coordination_issues_id_delete) | **DELETE** /rest/v1.0/coordination_issues/{id} | Delete Coordination Issue
[**rest_v10_coordination_issues_id_get**](ProjectManagementCoordinationIssuesCoordinationIssuesApi.md#rest_v10_coordination_issues_id_get) | **GET** /rest/v1.0/coordination_issues/{id} | Show Coordination Issue
[**rest_v10_coordination_issues_id_patch**](ProjectManagementCoordinationIssuesCoordinationIssuesApi.md#rest_v10_coordination_issues_id_patch) | **PATCH** /rest/v1.0/coordination_issues/{id} | Update Coordination Issue
[**rest_v10_coordination_issues_post**](ProjectManagementCoordinationIssuesCoordinationIssuesApi.md#rest_v10_coordination_issues_post) | **POST** /rest/v1.0/coordination_issues | Create Coordination Issue


# **rest_v10_coordination_issues_get**
> List[RestV10CoordinationIssuesGet200ResponseInner] rest_v10_coordination_issues_get(procore_company_id, project_id, page=page, per_page=per_page, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_created_by_id=filters_created_by_id, filters_created_from=filters_created_from, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_issue_type=filters_issue_type, filters_priority=filters_priority, filters_trade_id=filters_trade_id, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_created_at=filters_created_at, sort=sort, view=view, viewpoint_format=viewpoint_format, save_sticky_filters=save_sticky_filters)

List Coordination Issues

Lists Coordination Issues associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_assignee_company_id = [56] # List[int] | Filter item(s) with matching assignee vendor companies. (optional)
    filters_assignee_id = [56] # List[int] | Filter item(s) with matching assignees. (optional)
    filters_created_by_id = [56] # List[int] | Filter item(s) with matching User IDs. (optional)
    filters_created_from = ['filters_created_from_example'] # List[str] | Filter item(s) with matching creation source. (optional)
    filters_ids = [56] # List[int] | Filter item(s) with matching ids. (optional)
    filters_location_id = [56] # List[int] | Filter item(s) with matching locations. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_search = 'filters_search_example' # str | Filter item(s) with the matching search query. The search is performed on title and issue number. (optional)
    filters_coordination_issue_file_id = [56] # List[int] | Filter item(s) with the exact coordination issue file. (optional)
    filters_status = ['filters_status_example'] # List[str] | Filter item(s) with matching status. (optional)
    filters_issue_type = ['filters_issue_type_example'] # List[str] | Filter item(s) with matching issue_type. (optional)
    filters_priority = ['filters_priority_example'] # List[str] | Filter item(s) with matching priority. (optional)
    filters_trade_id = [56] # List[int] | Filter item(s) with matching trades. (optional)
    filters_updated_at = 'filters_updated_at_example' # str | Filter item(s) within a specific updated at iso8601 datetime range. (optional)
    filters_due_date = 'filters_due_date_example' # str | Filter item(s) within a specific due date iso8601 date range. (optional)
    filters_created_at = 'filters_created_at_example' # str | Filter item(s) within a specific created at iso8601 datetime range. (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)
    view = 'view_example' # str | The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. (optional)
    viewpoint_format = 'viewpoint_format_example' # str | Specify viewpoint data format. This parameter functions only when the query parameter view is 'extended' The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. (optional)
    save_sticky_filters = True # bool | Persists filter parameters for the requesting user and project. (optional)

    try:
        # List Coordination Issues
        api_response = api_instance.rest_v10_coordination_issues_get(procore_company_id, project_id, page=page, per_page=per_page, filters_assignee_company_id=filters_assignee_company_id, filters_assignee_id=filters_assignee_id, filters_created_by_id=filters_created_by_id, filters_created_from=filters_created_from, filters_ids=filters_ids, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_search=filters_search, filters_coordination_issue_file_id=filters_coordination_issue_file_id, filters_status=filters_status, filters_issue_type=filters_issue_type, filters_priority=filters_priority, filters_trade_id=filters_trade_id, filters_updated_at=filters_updated_at, filters_due_date=filters_due_date, filters_created_at=filters_created_at, sort=sort, view=view, viewpoint_format=viewpoint_format, save_sticky_filters=save_sticky_filters)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_assignee_company_id** | [**List[int]**](int.md)| Filter item(s) with matching assignee vendor companies. | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Filter item(s) with matching assignees. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Filter item(s) with matching User IDs. | [optional] 
 **filters_created_from** | [**List[str]**](str.md)| Filter item(s) with matching creation source. | [optional] 
 **filters_ids** | [**List[int]**](int.md)| Filter item(s) with matching ids. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Filter item(s) with matching locations. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_search** | **str**| Filter item(s) with the matching search query. The search is performed on title and issue number. | [optional] 
 **filters_coordination_issue_file_id** | [**List[int]**](int.md)| Filter item(s) with the exact coordination issue file. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Filter item(s) with matching status. | [optional] 
 **filters_issue_type** | [**List[str]**](str.md)| Filter item(s) with matching issue_type. | [optional] 
 **filters_priority** | [**List[str]**](str.md)| Filter item(s) with matching priority. | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Filter item(s) with matching trades. | [optional] 
 **filters_updated_at** | **str**| Filter item(s) within a specific updated at iso8601 datetime range. | [optional] 
 **filters_due_date** | **str**| Filter item(s) within a specific due date iso8601 date range. | [optional] 
 **filters_created_at** | **str**| Filter item(s) within a specific created at iso8601 datetime range. | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 
 **view** | **str**| The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. | [optional] 
 **viewpoint_format** | **str**| Specify viewpoint data format. This parameter functions only when the query parameter view is &#39;extended&#39; The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. | [optional] 
 **save_sticky_filters** | **bool**| Persists filter parameters for the requesting user and project. | [optional] 

### Return type

[**List[RestV10CoordinationIssuesGet200ResponseInner]**](RestV10CoordinationIssuesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coordination Issues listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view Coordination Issues |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_id_delete**
> rest_v10_coordination_issues_id_delete(procore_company_id, id, project_id)

Delete Coordination Issue

Delete a Coordination Issue from the system

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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Coordination Issue
        api_instance.rest_v10_coordination_issues_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_id_get**
> RestV10CoordinationIssuesGet200ResponseInner rest_v10_coordination_issues_id_get(procore_company_id, id, project_id, view=view, viewpoint_format=viewpoint_format)

Show Coordination Issue

Return a single Coordination Issue item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. (optional)
    viewpoint_format = 'viewpoint_format_example' # str | Specify viewpoint data format. This parameter functions only when the query parameter view is 'extended' The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. (optional)

    try:
        # Show Coordination Issue
        api_response = api_instance.rest_v10_coordination_issues_id_get(procore_company_id, id, project_id, view=view, viewpoint_format=viewpoint_format)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The normal view is a subset of the response shown below, and does not include attachments, viewpoints, linked items and updated_by The extended view contains the response shown below. The default view is normal. | [optional] 
 **viewpoint_format** | **str**| Specify viewpoint data format. This parameter functions only when the query parameter view is &#39;extended&#39; The default format returns the viewpoint content as saved. The procore format returns the viewpoint content converted to Procore format. If a valid conversion is not possible, empty viewpoint is returned. | [optional] 

### Return type

[**RestV10CoordinationIssuesGet200ResponseInner**](RestV10CoordinationIssuesGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_id_patch**
> RestV10CoordinationIssuesGet200ResponseInner rest_v10_coordination_issues_id_patch(procore_company_id, id, body105)

Update Coordination Issue

Update a Coordination Issue item

### Example


```python
import procore_sdk
from procore_sdk.models.body105 import Body105
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Coordination Issue ID
    body105 = procore_sdk.Body105() # Body105 | 

    try:
        # Update Coordination Issue
        api_response = api_instance.rest_v10_coordination_issues_id_patch(procore_company_id, id, body105)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Coordination Issue ID | 
 **body105** | [**Body105**](Body105.md)|  | 

### Return type

[**RestV10CoordinationIssuesGet200ResponseInner**](RestV10CoordinationIssuesGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_coordination_issues_post**
> RestV10CoordinationIssuesGet200ResponseInner rest_v10_coordination_issues_post(procore_company_id, body104)

Create Coordination Issue

Create a Coordination Issue in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.body104 import Body104
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner import RestV10CoordinationIssuesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssuesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body104 = procore_sdk.Body104() # Body104 | 

    try:
        # Create Coordination Issue
        api_response = api_instance.rest_v10_coordination_issues_post(procore_company_id, body104)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssuesApi->rest_v10_coordination_issues_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body104** | [**Body104**](Body104.md)|  | 

### Return type

[**RestV10CoordinationIssuesGet200ResponseInner**](RestV10CoordinationIssuesGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

