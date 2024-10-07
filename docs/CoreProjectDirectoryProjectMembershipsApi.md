# procore_sdk.CoreProjectDirectoryProjectMembershipsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_project_memberships_bulk_add_post**](CoreProjectDirectoryProjectMembershipsApi.md#rest_v10_projects_project_id_project_memberships_bulk_add_post) | **POST** /rest/v1.0/projects/{project_id}/project_memberships/bulk_add | Bulk Create Project Memberships
[**rest_v10_projects_project_id_project_memberships_get**](CoreProjectDirectoryProjectMembershipsApi.md#rest_v10_projects_project_id_project_memberships_get) | **GET** /rest/v1.0/projects/{project_id}/project_memberships | List Project Memberships
[**rest_v10_projects_project_id_project_memberships_id_delete**](CoreProjectDirectoryProjectMembershipsApi.md#rest_v10_projects_project_id_project_memberships_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/project_memberships/{id} | Delete Project Membership
[**rest_v10_projects_project_id_project_memberships_post**](CoreProjectDirectoryProjectMembershipsApi.md#rest_v10_projects_project_id_project_memberships_post) | **POST** /rest/v1.0/projects/{project_id}/project_memberships | Create Project Membership


# **rest_v10_projects_project_id_project_memberships_bulk_add_post**
> List[int] rest_v10_projects_project_id_project_memberships_bulk_add_post(procore_company_id, project_id, bulk_create_project_membership_body)

Bulk Create Project Memberships

Bulk Create Project Memberships for many parties on the given Project.  This endpoint can currently only be used to add reference users to a project. It cannot be used to add a user who has a login or to add vendors.

### Example


```python
import procore_sdk
from procore_sdk.models.bulk_create_project_membership_body import BulkCreateProjectMembershipBody
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectMembershipsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bulk_create_project_membership_body = procore_sdk.BulkCreateProjectMembershipBody() # BulkCreateProjectMembershipBody | 

    try:
        # Bulk Create Project Memberships
        api_response = api_instance.rest_v10_projects_project_id_project_memberships_bulk_add_post(procore_company_id, project_id, bulk_create_project_membership_body)
        print("The response of CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_bulk_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_bulk_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bulk_create_project_membership_body** | [**BulkCreateProjectMembershipBody**](BulkCreateProjectMembershipBody.md)|  | 

### Return type

**List[int]**

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

# **rest_v10_projects_project_id_project_memberships_get**
> List[ProjectMembership] rest_v10_projects_project_id_project_memberships_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Memberships

List all Project Memberships on a given Project.  This endpoint returns all Memberships, including inactive Users/Vendors.

### Example


```python
import procore_sdk
from procore_sdk.models.project_membership import ProjectMembership
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectMembershipsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Memberships
        api_response = api_instance.rest_v10_projects_project_id_project_memberships_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectMembership]**](ProjectMembership.md)

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

# **rest_v10_projects_project_id_project_memberships_id_delete**
> rest_v10_projects_project_id_project_memberships_id_delete(procore_company_id, project_id, id, party_id)

Delete Project Membership

Delete a Project Membership for a party on the given Project.  This endpoint can currently only be used to delete reference users from a project. It cannot be used to delete a user who has a login or to delete vendors.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectMembershipsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | The ID of the Project Membership
    party_id = 56 # int | The ID of the Party (reference user)

    try:
        # Delete Project Membership
        api_instance.rest_v10_projects_project_id_project_memberships_id_delete(procore_company_id, project_id, id, party_id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| The ID of the Project Membership | 
 **party_id** | **int**| The ID of the Party (reference user) | 

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
**204** | Deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_project_memberships_post**
> List[float] rest_v10_projects_project_id_project_memberships_post(procore_company_id, project_id, project_membership_body)

Create Project Membership

Create a Project Membership for a party on the given Project.  This endpoint can currently only be used to add reference users to a project. It cannot be used to add a user who has a login or to add vendors.

### Example


```python
import procore_sdk
from procore_sdk.models.project_membership_body import ProjectMembershipBody
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectMembershipsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    project_membership_body = procore_sdk.ProjectMembershipBody() # ProjectMembershipBody | 

    try:
        # Create Project Membership
        api_response = api_instance.rest_v10_projects_project_id_project_memberships_post(procore_company_id, project_id, project_membership_body)
        print("The response of CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectMembershipsApi->rest_v10_projects_project_id_project_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **project_membership_body** | [**ProjectMembershipBody**](ProjectMembershipBody.md)|  | 

### Return type

**List[float]**

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

