# procore_sdk.CoreProjectDirectoryProjectDistributionGroupsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete**](CoreProjectDirectoryProjectDistributionGroupsApi.md#rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/distribution_groups/{distribution_group_id} | Delete Project Distribution Group
[**rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch**](CoreProjectDirectoryProjectDistributionGroupsApi.md#rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/distribution_groups/{distribution_group_id} | Update Project Distribution Group
[**rest_v10_projects_project_id_distribution_groups_get**](CoreProjectDirectoryProjectDistributionGroupsApi.md#rest_v10_projects_project_id_distribution_groups_get) | **GET** /rest/v1.0/projects/{project_id}/distribution_groups | List Project Distribution Groups
[**rest_v10_projects_project_id_distribution_groups_post**](CoreProjectDirectoryProjectDistributionGroupsApi.md#rest_v10_projects_project_id_distribution_groups_post) | **POST** /rest/v1.0/projects/{project_id}/distribution_groups | Create Project Distribution Group


# **rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete**
> rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete(procore_company_id, project_id, distribution_group_id)

Delete Project Distribution Group

Delete a Distribution Group associated with the given Project.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDistributionGroupsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    distribution_group_id = 56 # int | Unique identifier for the distribution group.

    try:
        # Delete Project Distribution Group
        api_instance.rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete(procore_company_id, project_id, distribution_group_id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_distribution_group_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **distribution_group_id** | **int**| Unique identifier for the distribution group. | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch**
> RestV10ProjectsProjectIdDistributionGroupsPost200Response rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch(procore_company_id, project_id, distribution_group_id, update_distribution_group_body, idempotency_token=idempotency_token)

Update Project Distribution Group

Update a Distribution Group associated with the given Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_post200_response import RestV10ProjectsProjectIdDistributionGroupsPost200Response
from procore_sdk.models.update_distribution_group_body import UpdateDistributionGroupBody
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDistributionGroupsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    distribution_group_id = 56 # int | Unique identifier for the distribution group.
    update_distribution_group_body = procore_sdk.UpdateDistributionGroupBody() # UpdateDistributionGroupBody | 
    idempotency_token = 'idempotency_token_example' # str | Unique idempotent token (optional)

    try:
        # Update Project Distribution Group
        api_response = api_instance.rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch(procore_company_id, project_id, distribution_group_id, update_distribution_group_body, idempotency_token=idempotency_token)
        print("The response of CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_distribution_group_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **distribution_group_id** | **int**| Unique identifier for the distribution group. | 
 **update_distribution_group_body** | [**UpdateDistributionGroupBody**](UpdateDistributionGroupBody.md)|  | 
 **idempotency_token** | **str**| Unique idempotent token | [optional] 

### Return type

[**RestV10ProjectsProjectIdDistributionGroupsPost200Response**](RestV10ProjectsProjectIdDistributionGroupsPost200Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_distribution_groups_get**
> List[RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner] rest_v10_projects_project_id_distribution_groups_get(procore_company_id, project_id, page=page, per_page=per_page, filters_search=filters_search, sort=sort, view=view, include_ancestors=include_ancestors, domain_id=domain_id, min_ual=min_ual)

List Project Distribution Groups

Return a list of all Distribution Groups associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_get200_response_inner import RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDistributionGroupsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)
    view = 'view_example' # str | Parameter affecting what level of detail will be returned from the endpoint. 'extended' will include the users included in each distribution group. (optional)
    include_ancestors = true # bool | Parameter affecting the scope for the Distribution Groups, by default is 'false' to only return the Distribution Groups at Project level. Setting it to 'true' will also include Distribution Groups at Company level. (optional)
    domain_id = 9 # int | Parameter affecting the scope for the Distribution Groups, by default it is the Domain ID of the Submittals Tool. Will return only Distributions Groups who users that have access to the Tool specified by the domain_id. Only applies to requests that also have include_ancestors set to 'true'. (optional)
    min_ual = 2 # int | Parameter affecting the scope for the Distribution Groups, by default it is the 'read' user access level. Will return only Distributions Groups who users that have the min ual specified by the 'min_ual'. Only applies to requests that also have include_ancestors set to 'true'. (optional)

    try:
        # List Project Distribution Groups
        api_response = api_instance.rest_v10_projects_project_id_distribution_groups_get(procore_company_id, project_id, page=page, per_page=per_page, filters_search=filters_search, sort=sort, view=view, include_ancestors=include_ancestors, domain_id=domain_id, min_ual=min_ual)
        print("The response of CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 
 **view** | **str**| Parameter affecting what level of detail will be returned from the endpoint. &#39;extended&#39; will include the users included in each distribution group. | [optional] 
 **include_ancestors** | **bool**| Parameter affecting the scope for the Distribution Groups, by default is &#39;false&#39; to only return the Distribution Groups at Project level. Setting it to &#39;true&#39; will also include Distribution Groups at Company level. | [optional] 
 **domain_id** | **int**| Parameter affecting the scope for the Distribution Groups, by default it is the Domain ID of the Submittals Tool. Will return only Distributions Groups who users that have access to the Tool specified by the domain_id. Only applies to requests that also have include_ancestors set to &#39;true&#39;. | [optional] 
 **min_ual** | **int**| Parameter affecting the scope for the Distribution Groups, by default it is the &#39;read&#39; user access level. Will return only Distributions Groups who users that have the min ual specified by the &#39;min_ual&#39;. Only applies to requests that also have include_ancestors set to &#39;true&#39;. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner]**](RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_distribution_groups_post**
> RestV10ProjectsProjectIdDistributionGroupsPost200Response rest_v10_projects_project_id_distribution_groups_post(procore_company_id, project_id, create_distribution_group_body, idempotency_token=idempotency_token)

Create Project Distribution Group

Create a new Distribution Group associated with the given Project.

### Example


```python
import procore_sdk
from procore_sdk.models.create_distribution_group_body import CreateDistributionGroupBody
from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_post200_response import RestV10ProjectsProjectIdDistributionGroupsPost200Response
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectDistributionGroupsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    create_distribution_group_body = procore_sdk.CreateDistributionGroupBody() # CreateDistributionGroupBody | 
    idempotency_token = 'idempotency_token_example' # str | Unique idempotent token (optional)

    try:
        # Create Project Distribution Group
        api_response = api_instance.rest_v10_projects_project_id_distribution_groups_post(procore_company_id, project_id, create_distribution_group_body, idempotency_token=idempotency_token)
        print("The response of CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectDistributionGroupsApi->rest_v10_projects_project_id_distribution_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **create_distribution_group_body** | [**CreateDistributionGroupBody**](CreateDistributionGroupBody.md)|  | 
 **idempotency_token** | **str**| Unique idempotent token | [optional] 

### Return type

[**RestV10ProjectsProjectIdDistributionGroupsPost200Response**](RestV10ProjectsProjectIdDistributionGroupsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Duplicate Idempotency-token header) |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

