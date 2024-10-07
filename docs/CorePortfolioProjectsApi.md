# procore_sdk.CorePortfolioProjectsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_get**](CorePortfolioProjectsApi.md#rest_v10_projects_get) | **GET** /rest/v1.0/projects | List projects
[**rest_v10_projects_id_filters_filter_name_get**](CorePortfolioProjectsApi.md#rest_v10_projects_id_filters_filter_name_get) | **GET** /rest/v1.0/projects/{id}/filters/{filter_name} | List possible Tool filter values
[**rest_v10_projects_id_filters_get**](CorePortfolioProjectsApi.md#rest_v10_projects_id_filters_get) | **GET** /rest/v1.0/projects/{id}/filters | List filters
[**rest_v10_projects_id_get**](CorePortfolioProjectsApi.md#rest_v10_projects_id_get) | **GET** /rest/v1.0/projects/{id} | Show project
[**rest_v10_projects_id_logo_delete**](CorePortfolioProjectsApi.md#rest_v10_projects_id_logo_delete) | **DELETE** /rest/v1.0/projects/{id}/logo | Delete the project logo
[**rest_v10_projects_id_logo_post**](CorePortfolioProjectsApi.md#rest_v10_projects_id_logo_post) | **POST** /rest/v1.0/projects/{id}/logo | Create a project logo
[**rest_v10_projects_id_patch**](CorePortfolioProjectsApi.md#rest_v10_projects_id_patch) | **PATCH** /rest/v1.0/projects/{id} | Update project
[**rest_v10_projects_post**](CorePortfolioProjectsApi.md#rest_v10_projects_post) | **POST** /rest/v1.0/projects | Create project
[**rest_v10_projects_sync_patch**](CorePortfolioProjectsApi.md#rest_v10_projects_sync_patch) | **PATCH** /rest/v1.0/projects/sync | Sync projects
[**rest_v11_projects_get**](CorePortfolioProjectsApi.md#rest_v11_projects_get) | **GET** /rest/v1.1/projects | List projects


# **rest_v10_projects_get**
> List[Project1] rest_v10_projects_get(procore_company_id, company_id, page=page, per_page=per_page, filters_by_status=filters_by_status, filters_name=filters_name, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, filters_id=filters_id, filters_synced=filters_synced, filters_vendor_id=filters_vendor_id, filters_custom_fields=filters_custom_fields, serializer_view=serializer_view, sort=sort)

List projects

Return a list of active Projects.  If the authenticated user has full company admin permissions the request will return all of the projects in the company. If the user does not have full company admin permissions, the request will only return the projects that the user has been added to.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.project1 import Project1
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_by_status = 'filters_by_status_example' # str | Filters on project status. Must be one of Active, Inactive, or All. (optional)
    filters_name = 'filters_name_example' # str | Filters projects to those matching the given string. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_synced = True # bool | If true, returns only item(s) with a `synced` status. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_custom_fields = {'key': {"1": true, "5": [4,3] }} # object | JSON object returns project with matching custom_field_values (optional)
    serializer_view = 'serializer_view_example' # str | The 'compact' view only returns id, name and display_name. Passing any other value (or passing no value at all) will result in the more complete list of attributes shown below. (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List projects
        api_response = api_instance.rest_v10_projects_get(procore_company_id, company_id, page=page, per_page=per_page, filters_by_status=filters_by_status, filters_name=filters_name, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, filters_id=filters_id, filters_synced=filters_synced, filters_vendor_id=filters_vendor_id, filters_custom_fields=filters_custom_fields, serializer_view=serializer_view, sort=sort)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_by_status** | **str**| Filters on project status. Must be one of Active, Inactive, or All. | [optional] 
 **filters_name** | **str**| Filters projects to those matching the given string. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_synced** | **bool**| If true, returns only item(s) with a &#x60;synced&#x60; status. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_custom_fields** | [**object**](.md)| JSON object returns project with matching custom_field_values | [optional] 
 **serializer_view** | **str**| The &#39;compact&#39; view only returns id, name and display_name. Passing any other value (or passing no value at all) will result in the more complete list of attributes shown below. | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[Project1]**](Project1.md)

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

# **rest_v10_projects_id_filters_filter_name_get**
> List[RestV10ProjectsIdFiltersFilterNameGet200ResponseInner] rest_v10_projects_id_filters_filter_name_get(procore_company_id, id, filter_name, tool, tab)

List possible Tool filter values

List all possible values customer can apply to a filter

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_id_filters_filter_name_get200_response_inner import RestV10ProjectsIdFiltersFilterNameGet200ResponseInner
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.
    filter_name = 'date_search' # str | Filter name
    tool = 'direct_costs' # str | Tool name
    tab = 'summary' # str | Tab name

    try:
        # List possible Tool filter values
        api_response = api_instance.rest_v10_projects_id_filters_filter_name_get(procore_company_id, id, filter_name, tool, tab)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_filters_filter_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_filters_filter_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 
 **filter_name** | **str**| Filter name | 
 **tool** | **str**| Tool name | 
 **tab** | **str**| Tab name | 

### Return type

[**List[RestV10ProjectsIdFiltersFilterNameGet200ResponseInner]**](RestV10ProjectsIdFiltersFilterNameGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_id_filters_get**
> RestV10ProjectsIdFiltersGet200Response rest_v10_projects_id_filters_get(procore_company_id, id, tool, tab)

List filters

List all filters customer can use for the project and tool

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_id_filters_get200_response import RestV10ProjectsIdFiltersGet200Response
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.
    tool = 'direct_costs' # str | Tool name
    tab = 'summary' # str | Tab name

    try:
        # List filters
        api_response = api_instance.rest_v10_projects_id_filters_get(procore_company_id, id, tool, tab)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 
 **tool** | **str**| Tool name | 
 **tab** | **str**| Tab name | 

### Return type

[**RestV10ProjectsIdFiltersGet200Response**](RestV10ProjectsIdFiltersGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_id_get**
> Project3 rest_v10_projects_id_get(procore_company_id, id, company_id)

Show project

Show details for the specified project in Procore.

### Example


```python
import procore_sdk
from procore_sdk.models.project3 import Project3
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show project
        api_response = api_instance.rest_v10_projects_id_get(procore_company_id, id, company_id)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**Project3**](Project3.md)

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

# **rest_v10_projects_id_logo_delete**
> Project3 rest_v10_projects_id_logo_delete(procore_company_id, id)

Delete the project logo

Updates the project setting the logo reference to null

### Example


```python
import procore_sdk
from procore_sdk.models.project3 import Project3
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.

    try:
        # Delete the project logo
        api_response = api_instance.rest_v10_projects_id_logo_delete(procore_company_id, id)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_logo_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_logo_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 

### Return type

[**Project3**](Project3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **rest_v10_projects_id_logo_post**
> Project3 rest_v10_projects_id_logo_post(procore_company_id, id, body32)

Create a project logo

Updates the project logo from a upload and returns the updated project.

### Example


```python
import procore_sdk
from procore_sdk.models.body32 import Body32
from procore_sdk.models.project3 import Project3
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.
    body32 = procore_sdk.Body32() # Body32 | 

    try:
        # Create a project logo
        api_response = api_instance.rest_v10_projects_id_logo_post(procore_company_id, id, body32)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_logo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_logo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 
 **body32** | [**Body32**](Body32.md)|  | 

### Return type

[**Project3**](Project3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_id_patch**
> Project3 rest_v10_projects_id_patch(procore_company_id, id, body31, run_configurable_validations=run_configurable_validations)

Update project

Update information for an existing project.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.body31 import Body31
from procore_sdk.models.project3 import Project3
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the project.
    body31 = procore_sdk.Body31() # Body31 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update project
        api_response = api_instance.rest_v10_projects_id_patch(procore_company_id, id, body31, run_configurable_validations=run_configurable_validations)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the project. | 
 **body31** | [**Body31**](Body31.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Project3**](Project3.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_post**
> Project3 rest_v10_projects_post(procore_company_id, body30, run_configurable_validations=run_configurable_validations)

Create project

Create a new Project in a Procore account. The new project is active by default.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information. #### Recommendation For accounts creating a significant number of projects (more than 300),  schedule these operations during non-business hours (5 P.M PST - 7 A.M PST) to optimize efficiency. Coordinate the timing with your solution architect for insights into system load and effective resource utilization.

### Example


```python
import procore_sdk
from procore_sdk.models.body30 import Body30
from procore_sdk.models.project3 import Project3
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body30 = procore_sdk.Body30() # Body30 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create project
        api_response = api_instance.rest_v10_projects_post(procore_company_id, body30, run_configurable_validations=run_configurable_validations)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body30** | [**Body30**](Body30.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**Project3**](Project3.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_sync_patch**
> ArrayOfProjects rest_v10_projects_sync_patch(procore_company_id, rest_v10_projects_sync_patch_request, company_id=company_id, run_configurable_validations=run_configurable_validations)

Sync projects

Create or update a batch of projects. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information. #### Recommendation Please be advised to not use the sync endpoint for bulk project creation due to potential performance bottlenecks.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_projects import ArrayOfProjects
from procore_sdk.models.rest_v10_projects_sync_patch_request import RestV10ProjectsSyncPatchRequest
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_projects_sync_patch_request = procore_sdk.RestV10ProjectsSyncPatchRequest() # RestV10ProjectsSyncPatchRequest | 
    company_id = 56 # int | Unique identifier for the company. (optional)
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Sync projects
        api_response = api_instance.rest_v10_projects_sync_patch(procore_company_id, rest_v10_projects_sync_patch_request, company_id=company_id, run_configurable_validations=run_configurable_validations)
        print("The response of CorePortfolioProjectsApi->rest_v10_projects_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v10_projects_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_projects_sync_patch_request** | [**RestV10ProjectsSyncPatchRequest**](RestV10ProjectsSyncPatchRequest.md)|  | 
 **company_id** | **int**| Unique identifier for the company. | [optional] 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**ArrayOfProjects**](ArrayOfProjects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of projects |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_get**
> List[RestV11ProjectsGet200ResponseInner] rest_v11_projects_get(procore_company_id, company_id, page=page, per_page=per_page, filters_by_status=filters_by_status, filters_name=filters_name, filters_project_number=filters_project_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, filters_id=filters_id, filters_synced=filters_synced, filters_vendor_id=filters_vendor_id, filters_is_demo=filters_is_demo, filters_custom_fields=filters_custom_fields, filters_template=filters_template, filters_by_owner_type=filters_by_owner_type, filters_by_department=filters_by_department, filters_by_region=filters_by_region, filters_by_office=filters_by_office, filters_by_program=filters_by_program, filters_by_stage=filters_by_stage, filters_by_type=filters_by_type, filters_by_bid_type=filters_by_bid_type, view=view, sort=sort)

List projects

Return a list of active Projects.  If the authenticated user has full company admin permissions the request will return all of the projects in the company. If the user does not have full company admin permissions, the request will only return the projects that the user has been added to. The default pagination is 100 projects per page. The max page size is 300 projects due to the size of the data in the response.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_get200_response_inner import RestV11ProjectsGet200ResponseInner
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
    api_instance = procore_sdk.CorePortfolioProjectsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_by_status = 'filters_by_status_example' # str | Filters on project status. Must be one of Active, Inactive, or All. (optional)
    filters_name = 'filters_name_example' # str | Filters projects to those matching the given string. (optional)
    filters_project_number = 'filters_project_number_example' # str | Filters on project number. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_synced = True # bool | If true, returns only item(s) with a `synced` status. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_is_demo = True # bool | Filters on project is_demo attribute, which indicates whether project is for demonstration purposes.  (optional)
    filters_custom_fields = {'key': {"1": true, "5": [4,3] }} # object | JSON object returns project with matching custom_field_values (optional)
    filters_template = True # bool | Filters on project template attribute, which indicates whether project is a template  (optional)
    filters_by_owner_type = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project owner type ID(s). (optional)
    filters_by_department = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified department ID(s). (optional)
    filters_by_region = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project region ID(s). (optional)
    filters_by_office = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified office ID(s). (optional)
    filters_by_program = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project program ID(s). (optional)
    filters_by_stage = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project stage ID(s). (optional)
    filters_by_type = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project type ID(s). (optional)
    filters_by_bid_type = procore_sdk.RestV11ProjectsGetFiltersByOwnerTypeParameter() # RestV11ProjectsGetFiltersByOwnerTypeParameter | Return item(s) with the specified project bid type ID(s). (optional)
    view = 'view_example' # str | The view determines which fields are returned. 'compact' will only return id and name. 'normal' returns more fields, while 'extended' returns all the project information (optional)
    sort = 'sort_example' # str | Return items with the specified sort. (optional)

    try:
        # List projects
        api_response = api_instance.rest_v11_projects_get(procore_company_id, company_id, page=page, per_page=per_page, filters_by_status=filters_by_status, filters_name=filters_name, filters_project_number=filters_project_number, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, filters_id=filters_id, filters_synced=filters_synced, filters_vendor_id=filters_vendor_id, filters_is_demo=filters_is_demo, filters_custom_fields=filters_custom_fields, filters_template=filters_template, filters_by_owner_type=filters_by_owner_type, filters_by_department=filters_by_department, filters_by_region=filters_by_region, filters_by_office=filters_by_office, filters_by_program=filters_by_program, filters_by_stage=filters_by_stage, filters_by_type=filters_by_type, filters_by_bid_type=filters_by_bid_type, view=view, sort=sort)
        print("The response of CorePortfolioProjectsApi->rest_v11_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorePortfolioProjectsApi->rest_v11_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_by_status** | **str**| Filters on project status. Must be one of Active, Inactive, or All. | [optional] 
 **filters_name** | **str**| Filters projects to those matching the given string. | [optional] 
 **filters_project_number** | **str**| Filters on project number. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_synced** | **bool**| If true, returns only item(s) with a &#x60;synced&#x60; status. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_is_demo** | **bool**| Filters on project is_demo attribute, which indicates whether project is for demonstration purposes.  | [optional] 
 **filters_custom_fields** | [**object**](.md)| JSON object returns project with matching custom_field_values | [optional] 
 **filters_template** | **bool**| Filters on project template attribute, which indicates whether project is a template  | [optional] 
 **filters_by_owner_type** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project owner type ID(s). | [optional] 
 **filters_by_department** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified department ID(s). | [optional] 
 **filters_by_region** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project region ID(s). | [optional] 
 **filters_by_office** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified office ID(s). | [optional] 
 **filters_by_program** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project program ID(s). | [optional] 
 **filters_by_stage** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project stage ID(s). | [optional] 
 **filters_by_type** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project type ID(s). | [optional] 
 **filters_by_bid_type** | [**RestV11ProjectsGetFiltersByOwnerTypeParameter**](.md)| Return item(s) with the specified project bid type ID(s). | [optional] 
 **view** | **str**| The view determines which fields are returned. &#39;compact&#39; will only return id and name. &#39;normal&#39; returns more fields, while &#39;extended&#39; returns all the project information | [optional] 
 **sort** | **str**| Return items with the specified sort. | [optional] 

### Return type

[**List[RestV11ProjectsGet200ResponseInner]**](RestV11ProjectsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

