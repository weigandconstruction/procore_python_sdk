# procore_sdk.CoreProjectDirectoryProjectVendorsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_vendors_get**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_get) | **GET** /rest/v1.0/projects/{project_id}/vendors | List project vendors
[**rest_v10_projects_project_id_vendors_id_actions_add_post**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_id_actions_add_post) | **POST** /rest/v1.0/projects/{project_id}/vendors/{id}/actions/add | Add to project
[**rest_v10_projects_project_id_vendors_id_actions_remove_delete**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_id_actions_remove_delete) | **DELETE** /rest/v1.0/projects/{project_id}/vendors/{id}/actions/remove | Delete from project
[**rest_v10_projects_project_id_vendors_id_get**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_id_get) | **GET** /rest/v1.0/projects/{project_id}/vendors/{id} | Show project vendor
[**rest_v10_projects_project_id_vendors_id_patch**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/vendors/{id} | Update project vendor
[**rest_v10_projects_project_id_vendors_post**](CoreProjectDirectoryProjectVendorsApi.md#rest_v10_projects_project_id_vendors_post) | **POST** /rest/v1.0/projects/{project_id}/vendors | Create project vendor
[**rest_v11_projects_project_id_vendors_get**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_get) | **GET** /rest/v1.1/projects/{project_id}/vendors | List project vendors
[**rest_v11_projects_project_id_vendors_id_actions_add_post**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_id_actions_add_post) | **POST** /rest/v1.1/projects/{project_id}/vendors/{id}/actions/add | Add to project
[**rest_v11_projects_project_id_vendors_id_actions_remove_delete**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_id_actions_remove_delete) | **DELETE** /rest/v1.1/projects/{project_id}/vendors/{id}/actions/remove | Delete from project
[**rest_v11_projects_project_id_vendors_id_get**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_id_get) | **GET** /rest/v1.1/projects/{project_id}/vendors/{id} | Show project vendor
[**rest_v11_projects_project_id_vendors_id_patch**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/vendors/{id} | Update project vendor
[**rest_v11_projects_project_id_vendors_post**](CoreProjectDirectoryProjectVendorsApi.md#rest_v11_projects_project_id_vendors_post) | **POST** /rest/v1.1/projects/{project_id}/vendors | Create project vendor


# **rest_v10_projects_project_id_vendors_get**
> List[RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf] rest_v10_projects_project_id_vendors_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_search=filters_search, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, filters_abbreviated_name=filters_abbreviated_name, sort=sort)

List project vendors

Return a list of Vendors associated with a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_search = 'filters_search_example' # str | Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number (optional)
    filters_standard_cost_code_id = [56] # List[int] | Returns vendors associated with the specified standard cost code id(s) (optional)
    filters_trade_id = [56] # List[int] | Returns vendors associated with the specified trade id(s) (optional)
    filters_id = [56] # List[int] | Returns vendors with the specified id(s) (optional)
    filters_parent_id = [56] # List[int] | Returns vendors with the specified parent id(s) (optional)
    filters_abbreviated_name = ['filters_abbreviated_name_example'] # List[str] | Return vendors(s) matching any of the specified abbreviated names in the abbreviated_name filter. (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List project vendors
        api_response = api_instance.rest_v10_projects_project_id_vendors_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_search=filters_search, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, filters_abbreviated_name=filters_abbreviated_name, sort=sort)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_search** | **str**| Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number | [optional] 
 **filters_standard_cost_code_id** | [**List[int]**](int.md)| Returns vendors associated with the specified standard cost code id(s) | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Returns vendors associated with the specified trade id(s) | [optional] 
 **filters_id** | [**List[int]**](int.md)| Returns vendors with the specified id(s) | [optional] 
 **filters_parent_id** | [**List[int]**](int.md)| Returns vendors with the specified parent id(s) | [optional] 
 **filters_abbreviated_name** | [**List[str]**](str.md)| Return vendors(s) matching any of the specified abbreviated names in the abbreviated_name filter. | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf]**](RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf.md)

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

# **rest_v10_projects_project_id_vendors_id_actions_add_post**
> RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf rest_v10_projects_project_id_vendors_id_actions_add_post(procore_company_id, project_id, id, view=view)

Add to project

Add a specified vendor to a Project from the Company Directory.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The name view is a minimal view only including the name and id. The default view is normal. (optional)

    try:
        # Add to project
        api_response = api_instance.rest_v10_projects_project_id_vendors_id_actions_add_post(procore_company_id, project_id, id, view=view)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_actions_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_actions_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The name view is a minimal view only including the name and id. The default view is normal. | [optional] 

### Return type

[**RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf**](RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_vendors_id_actions_remove_delete**
> rest_v10_projects_project_id_vendors_id_actions_remove_delete(procore_company_id, project_id, id)

Delete from project

Remove a specified Vendor from a Project.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor

    try:
        # Delete from project
        api_instance.rest_v10_projects_project_id_vendors_id_actions_remove_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_actions_remove_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 

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

# **rest_v10_projects_project_id_vendors_id_get**
> RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf rest_v10_projects_project_id_vendors_id_get(procore_company_id, project_id, id, view=view)

Show project vendor

Show detail on a specified Project Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)

    try:
        # Show project vendor
        api_response = api_instance.rest_v10_projects_project_id_vendors_id_get(procore_company_id, project_id, id, view=view)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 

### Return type

[**RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf**](RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_vendors_id_patch**
> RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf rest_v10_projects_project_id_vendors_id_patch(procore_company_id, project_id, id, project_vendor_body1, view=view, run_configurable_validations=run_configurable_validations)

Update project vendor

Update a specified Project Vendor.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.project_vendor_body1 import ProjectVendorBody1
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    project_vendor_body1 = procore_sdk.ProjectVendorBody1() # ProjectVendorBody1 | 
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update project vendor
        api_response = api_instance.rest_v10_projects_project_id_vendors_id_patch(procore_company_id, project_id, id, project_vendor_body1, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **project_vendor_body1** | [**ProjectVendorBody1**](ProjectVendorBody1.md)|  | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf**](RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_vendors_post**
> RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf rest_v10_projects_project_id_vendors_post(procore_company_id, project_id, project_vendor_body, view=view, run_configurable_validations=run_configurable_validations)

Create project vendor

Create a new Project Vendor.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.project_vendor_body import ProjectVendorBody
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    project_vendor_body = procore_sdk.ProjectVendorBody() # ProjectVendorBody | 
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create project vendor
        api_response = api_instance.rest_v10_projects_project_id_vendors_post(procore_company_id, project_id, project_vendor_body, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v10_projects_project_id_vendors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **project_vendor_body** | [**ProjectVendorBody**](ProjectVendorBody.md)|  | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf**](RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf.md)

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

# **rest_v11_projects_project_id_vendors_get**
> List[RestV11ProjectsProjectIdVendorsGet200ResponseInner] rest_v11_projects_project_id_vendors_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_search=filters_search, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, sort=sort)

List project vendors

Return a list of Vendors associated with a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner import RestV11ProjectsProjectIdVendorsGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to ids_only, name, and minimal views. If a valid view is not provided, it will return the default view: minimal for users without read permissions and normal otherwise. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_search = 'filters_search_example' # str | Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number (optional)
    filters_standard_cost_code_id = [56] # List[int] | Returns vendors associated with the specified standard cost code id(s) (optional)
    filters_trade_id = [56] # List[int] | Returns vendors associated with the specified trade id(s) (optional)
    filters_id = [56] # List[int] | Returns vendors with the specified id(s) (optional)
    filters_parent_id = [56] # List[int] | Returns vendors with the specified parent id(s) (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List project vendors
        api_response = api_instance.rest_v11_projects_project_id_vendors_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_search=filters_search, filters_standard_cost_code_id=filters_standard_cost_code_id, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_parent_id=filters_parent_id, sort=sort)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). Users without read permissions to Directory are limited to ids_only, name, and minimal views. If a valid view is not provided, it will return the default view: minimal for users without read permissions and normal otherwise. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_search** | **str**| Return vendors where the search string matches the vendor name, keywords, origin_code, or ABN/EIN number | [optional] 
 **filters_standard_cost_code_id** | [**List[int]**](int.md)| Returns vendors associated with the specified standard cost code id(s) | [optional] 
 **filters_trade_id** | [**List[int]**](int.md)| Returns vendors associated with the specified trade id(s) | [optional] 
 **filters_id** | [**List[int]**](int.md)| Returns vendors with the specified id(s) | [optional] 
 **filters_parent_id** | [**List[int]**](int.md)| Returns vendors with the specified parent id(s) | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdVendorsGet200ResponseInner]**](RestV11ProjectsProjectIdVendorsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_vendors_id_actions_add_post**
> RestV11ProjectsProjectIdVendorsPost201Response rest_v11_projects_project_id_vendors_id_actions_add_post(procore_company_id, project_id, id, view=view)

Add to project

Add a specified vendor to a Project from the Company Directory.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_post201_response import RestV11ProjectsProjectIdVendorsPost201Response
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)

    try:
        # Add to project
        api_response = api_instance.rest_v11_projects_project_id_vendors_id_actions_add_post(procore_company_id, project_id, id, view=view)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_actions_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_actions_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 

### Return type

[**RestV11ProjectsProjectIdVendorsPost201Response**](RestV11ProjectsProjectIdVendorsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_vendors_id_actions_remove_delete**
> rest_v11_projects_project_id_vendors_id_actions_remove_delete(procore_company_id, project_id, id)

Delete from project

Remove a specified Vendor from a Project.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor

    try:
        # Delete from project
        api_instance.rest_v11_projects_project_id_vendors_id_actions_remove_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_actions_remove_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 

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

# **rest_v11_projects_project_id_vendors_id_get**
> RestV11ProjectsProjectIdVendorsPost201Response rest_v11_projects_project_id_vendors_id_get(procore_company_id, project_id, id, view=view)

Show project vendor

Show detail on a specified Project Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_vendors_post201_response import RestV11ProjectsProjectIdVendorsPost201Response
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)

    try:
        # Show project vendor
        api_response = api_instance.rest_v11_projects_project_id_vendors_id_get(procore_company_id, project_id, id, view=view)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 

### Return type

[**RestV11ProjectsProjectIdVendorsPost201Response**](RestV11ProjectsProjectIdVendorsPost201Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_vendors_id_patch**
> RestV11ProjectsProjectIdVendorsPost201Response rest_v11_projects_project_id_vendors_id_patch(procore_company_id, project_id, id, project_vendor_body1, view=view, run_configurable_validations=run_configurable_validations)

Update project vendor

Update a specified Project Vendor.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.project_vendor_body1 import ProjectVendorBody1
from procore_sdk.models.rest_v11_projects_project_id_vendors_post201_response import RestV11ProjectsProjectIdVendorsPost201Response
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the vendor
    project_vendor_body1 = procore_sdk.ProjectVendorBody1() # ProjectVendorBody1 | 
    view = 'view_example' # str | The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update project vendor
        api_response = api_instance.rest_v11_projects_project_id_vendors_id_patch(procore_company_id, project_id, id, project_vendor_body1, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the vendor | 
 **project_vendor_body1** | [**ProjectVendorBody1**](ProjectVendorBody1.md)|  | 
 **view** | **str**| The normal view provides what is shown below. The extended view is the same as the normal view but includes children_count, legal_name, parent, and bidding. The default view is normal. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdVendorsPost201Response**](RestV11ProjectsProjectIdVendorsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_vendors_post**
> RestV11ProjectsProjectIdVendorsPost201Response rest_v11_projects_project_id_vendors_post(procore_company_id, project_id, project_vendor_body, view=view, run_configurable_validations=run_configurable_validations)

Create project vendor

Create a new Project Vendor.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.project_vendor_body import ProjectVendorBody
from procore_sdk.models.rest_v11_projects_project_id_vendors_post201_response import RestV11ProjectsProjectIdVendorsPost201Response
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    project_vendor_body = procore_sdk.ProjectVendorBody() # ProjectVendorBody | 
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is normal. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create project vendor
        api_response = api_instance.rest_v11_projects_project_id_vendors_post(procore_company_id, project_id, project_vendor_body, view=view, run_configurable_validations=run_configurable_validations)
        print("The response of CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorsApi->rest_v11_projects_project_id_vendors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **project_vendor_body** | [**ProjectVendorBody**](ProjectVendorBody.md)|  | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is normal. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdVendorsPost201Response**](RestV11ProjectsProjectIdVendorsPost201Response.md)

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

