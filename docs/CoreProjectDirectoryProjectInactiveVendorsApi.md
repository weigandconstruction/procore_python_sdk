# procore_sdk.CoreProjectDirectoryProjectInactiveVendorsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_vendors_inactive_get**](CoreProjectDirectoryProjectInactiveVendorsApi.md#rest_v10_projects_project_id_vendors_inactive_get) | **GET** /rest/v1.0/projects/{project_id}/vendors/inactive | List Project Inactive Vendors
[**rest_v10_projects_project_id_vendors_inactive_id_patch**](CoreProjectDirectoryProjectInactiveVendorsApi.md#rest_v10_projects_project_id_vendors_inactive_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/vendors/inactive/{id} | Reactivate project vendor


# **rest_v10_projects_project_id_vendors_inactive_get**
> List[RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner] rest_v10_projects_project_id_vendors_inactive_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, sort=sort)

List Project Inactive Vendors

Return a list of all Inactive Vendors associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_vendors_inactive_get200_response_inner import RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInactiveVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Return items with the specified sort (optional)

    try:
        # List Project Inactive Vendors
        api_response = api_instance.rest_v10_projects_project_id_vendors_inactive_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, sort=sort)
        print("The response of CoreProjectDirectoryProjectInactiveVendorsApi->rest_v10_projects_project_id_vendors_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInactiveVendorsApi->rest_v10_projects_project_id_vendors_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Return items with the specified sort | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner]**](RestV10ProjectsProjectIdVendorsInactiveGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_vendors_inactive_id_patch**
> NormalView1 rest_v10_projects_project_id_vendors_inactive_id_patch(procore_company_id, project_id, id, view=view)

Reactivate project vendor

Reactivate a specified Project Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.normal_view1 import NormalView1
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInactiveVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)

    try:
        # Reactivate project vendor
        api_response = api_instance.rest_v10_projects_project_id_vendors_inactive_id_patch(procore_company_id, project_id, id, view=view)
        print("The response of CoreProjectDirectoryProjectInactiveVendorsApi->rest_v10_projects_project_id_vendors_inactive_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInactiveVendorsApi->rest_v10_projects_project_id_vendors_inactive_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 

### Return type

[**NormalView1**](NormalView1.md)

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

