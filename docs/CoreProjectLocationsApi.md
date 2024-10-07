# procore_sdk.CoreProjectLocationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_locations_get**](CoreProjectLocationsApi.md#rest_v10_locations_get) | **GET** /rest/v1.0/locations | List locations
[**rest_v10_locations_id_delete**](CoreProjectLocationsApi.md#rest_v10_locations_id_delete) | **DELETE** /rest/v1.0/locations/{id} | Delete location
[**rest_v10_locations_id_get**](CoreProjectLocationsApi.md#rest_v10_locations_id_get) | **GET** /rest/v1.0/locations/{id} | Show location
[**rest_v10_locations_id_patch**](CoreProjectLocationsApi.md#rest_v10_locations_id_patch) | **PATCH** /rest/v1.0/locations/{id} | Update Location
[**rest_v10_locations_post**](CoreProjectLocationsApi.md#rest_v10_locations_post) | **POST** /rest/v1.0/locations | Create location
[**rest_v10_projects_project_id_locations_find_or_create_by_path_post**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_find_or_create_by_path_post) | **POST** /rest/v1.0/projects/{project_id}/locations/find_or_create_by_path | Find or Create Location(s) by Path
[**rest_v10_projects_project_id_locations_get**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_get) | **GET** /rest/v1.0/projects/{project_id}/locations | List Project Locations
[**rest_v10_projects_project_id_locations_location_id_delete**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_location_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/locations/{location_id} | Delete Project Location
[**rest_v10_projects_project_id_locations_location_id_get**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_location_id_get) | **GET** /rest/v1.0/projects/{project_id}/locations/{location_id} | Show Project Location
[**rest_v10_projects_project_id_locations_location_id_patch**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_location_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/locations/{location_id} | Update Project Location
[**rest_v10_projects_project_id_locations_post**](CoreProjectLocationsApi.md#rest_v10_projects_project_id_locations_post) | **POST** /rest/v1.0/projects/{project_id}/locations | Create Location (Admin)
[**rest_v11_projects_project_id_locations_location_id_delete**](CoreProjectLocationsApi.md#rest_v11_projects_project_id_locations_location_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/locations/{location_id} | Delete Project Location


# **rest_v10_locations_get**
> List[Location1] rest_v10_locations_get(procore_company_id, project_id, page=page, per_page=per_page)

List locations

Return a list of Locations associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List locations
        api_response = api_instance.rest_v10_locations_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectLocationsApi->rest_v10_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Location1]**](Location1.md)

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

# **rest_v10_locations_id_delete**
> rest_v10_locations_id_delete(procore_company_id, id, project_id)

Delete location

Delete the specified Location.

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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the location
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete location
        api_instance.rest_v10_locations_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_locations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the location | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_locations_id_get**
> Location1 rest_v10_locations_id_get(procore_company_id, id, project_id)

Show location

Show detail on the specified Location.

### Example


```python
import procore_sdk
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the location
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show location
        api_response = api_instance.rest_v10_locations_id_get(procore_company_id, id, project_id)
        print("The response of CoreProjectLocationsApi->rest_v10_locations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_locations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the location | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v10_locations_id_patch**
> Location1 rest_v10_locations_id_patch(procore_company_id, id, body70)

Update Location

Update the specified Location.

### Example


```python
import procore_sdk
from procore_sdk.models.body70 import Body70
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the location
    body70 = procore_sdk.Body70() # Body70 | 

    try:
        # Update Location
        api_response = api_instance.rest_v10_locations_id_patch(procore_company_id, id, body70)
        print("The response of CoreProjectLocationsApi->rest_v10_locations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_locations_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the location | 
 **body70** | [**Body70**](Body70.md)|  | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v10_locations_post**
> Location1 rest_v10_locations_post(procore_company_id, body69)

Create location

Create a new Location for the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body69 import Body69
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body69 = procore_sdk.Body69() # Body69 | 

    try:
        # Create location
        api_response = api_instance.rest_v10_locations_post(procore_company_id, body69)
        print("The response of CoreProjectLocationsApi->rest_v10_locations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_locations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body69** | [**Body69**](Body69.md)|  | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v10_projects_project_id_locations_find_or_create_by_path_post**
> Location1 rest_v10_projects_project_id_locations_find_or_create_by_path_post(procore_company_id, project_id, body72)

Find or Create Location(s) by Path

Retrieves a Location corresponding to the provided path, or creates Location(s) representing the path.

### Example


```python
import procore_sdk
from procore_sdk.models.body72 import Body72
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body72 = procore_sdk.Body72() # Body72 | 

    try:
        # Find or Create Location(s) by Path
        api_response = api_instance.rest_v10_projects_project_id_locations_find_or_create_by_path_post(procore_company_id, project_id, body72)
        print("The response of CoreProjectLocationsApi->rest_v10_projects_project_id_locations_find_or_create_by_path_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_find_or_create_by_path_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body72** | [**Body72**](Body72.md)|  | 

### Return type

[**Location1**](Location1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_locations_get**
> List[Location1] rest_v10_projects_project_id_locations_get(procore_company_id, project_id, filters_id=filters_id, filters_parent_id=filters_parent_id, filters_code=filters_code, filters_search=filters_search, filters_search_with_code=filters_search_with_code, filters_superlocations_for=filters_superlocations_for, filters_sublocations_for=filters_sublocations_for, filters_updated_at=filters_updated_at, sort=sort, page=page, per_page=per_page, filters_depth_range=filters_depth_range)

List Project Locations

Return a list of Locations associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_parent_id = 56 # int | Return location(s) with the specified parent_ids. (optional)
    filters_code = ['filters_code_example'] # List[str] | Return location(s) matching any of the specified codes in the search term. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    filters_search_with_code = 'filters_search_with_code_example' # str | Return item(s) where the location code or the location name match the search term (optional)
    filters_superlocations_for = 56 # int | Return superlocations (ancestors) of the specified location ids. (optional)
    filters_sublocations_for = 56 # int | Return sublocations (descendants) of the specified location ids. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_depth_range = '0...1' # str | Return item(s) with a tree depth within the specified range.  Examples: `0...1` - Parents and children `0...2` - Parents, children, and grandchildren `1...2` - Children and grandchildren (optional)

    try:
        # List Project Locations
        api_response = api_instance.rest_v10_projects_project_id_locations_get(procore_company_id, project_id, filters_id=filters_id, filters_parent_id=filters_parent_id, filters_code=filters_code, filters_search=filters_search, filters_search_with_code=filters_search_with_code, filters_superlocations_for=filters_superlocations_for, filters_sublocations_for=filters_sublocations_for, filters_updated_at=filters_updated_at, sort=sort, page=page, per_page=per_page, filters_depth_range=filters_depth_range)
        print("The response of CoreProjectLocationsApi->rest_v10_projects_project_id_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_parent_id** | **int**| Return location(s) with the specified parent_ids. | [optional] 
 **filters_code** | [**List[str]**](str.md)| Return location(s) matching any of the specified codes in the search term. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **filters_search_with_code** | **str**| Return item(s) where the location code or the location name match the search term | [optional] 
 **filters_superlocations_for** | **int**| Return superlocations (ancestors) of the specified location ids. | [optional] 
 **filters_sublocations_for** | **int**| Return sublocations (descendants) of the specified location ids. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_depth_range** | **str**| Return item(s) with a tree depth within the specified range.  Examples: &#x60;0...1&#x60; - Parents and children &#x60;0...2&#x60; - Parents, children, and grandchildren &#x60;1...2&#x60; - Children and grandchildren | [optional] 

### Return type

[**List[Location1]**](Location1.md)

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

# **rest_v10_projects_project_id_locations_location_id_delete**
> rest_v10_projects_project_id_locations_location_id_delete(procore_company_id, project_id, location_id)

Delete Project Location

Deletes a specified Location.

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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    location_id = 56 # int | ID of the location

    try:
        # Delete Project Location
        api_instance.rest_v10_projects_project_id_locations_location_id_delete(procore_company_id, project_id, location_id)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_location_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **location_id** | **int**| ID of the location | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_locations_location_id_get**
> Location1 rest_v10_projects_project_id_locations_location_id_get(procore_company_id, project_id, location_id)

Show Project Location

Retrieves a Location for a specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    location_id = 56 # int | ID of the location

    try:
        # Show Project Location
        api_response = api_instance.rest_v10_projects_project_id_locations_location_id_get(procore_company_id, project_id, location_id)
        print("The response of CoreProjectLocationsApi->rest_v10_projects_project_id_locations_location_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_location_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **location_id** | **int**| ID of the location | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v10_projects_project_id_locations_location_id_patch**
> Location1 rest_v10_projects_project_id_locations_location_id_patch(procore_company_id, project_id, location_id, body71)

Update Project Location

Update the specified Location.

### Example


```python
import procore_sdk
from procore_sdk.models.body71 import Body71
from procore_sdk.models.location1 import Location1
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    location_id = 56 # int | ID of the location
    body71 = procore_sdk.Body71() # Body71 | 

    try:
        # Update Project Location
        api_response = api_instance.rest_v10_projects_project_id_locations_location_id_patch(procore_company_id, project_id, location_id, body71)
        print("The response of CoreProjectLocationsApi->rest_v10_projects_project_id_locations_location_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_location_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **location_id** | **int**| ID of the location | 
 **body71** | [**Body71**](Body71.md)|  | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v10_projects_project_id_locations_post**
> Location1 rest_v10_projects_project_id_locations_post(procore_company_id, project_id, rest_v10_projects_project_id_locations_post_request)

Create Location (Admin)

Create a new Location for the specified Project. Note: This endpoint requires Project Admin permissions and does not respect the \"Disable Dynamic Location Creation\" project configuration.

### Example


```python
import procore_sdk
from procore_sdk.models.location1 import Location1
from procore_sdk.models.rest_v10_projects_project_id_locations_post_request import RestV10ProjectsProjectIdLocationsPostRequest
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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_locations_post_request = procore_sdk.RestV10ProjectsProjectIdLocationsPostRequest() # RestV10ProjectsProjectIdLocationsPostRequest | 

    try:
        # Create Location (Admin)
        api_response = api_instance.rest_v10_projects_project_id_locations_post(procore_company_id, project_id, rest_v10_projects_project_id_locations_post_request)
        print("The response of CoreProjectLocationsApi->rest_v10_projects_project_id_locations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v10_projects_project_id_locations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_locations_post_request** | [**RestV10ProjectsProjectIdLocationsPostRequest**](RestV10ProjectsProjectIdLocationsPostRequest.md)|  | 

### Return type

[**Location1**](Location1.md)

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

# **rest_v11_projects_project_id_locations_location_id_delete**
> rest_v11_projects_project_id_locations_location_id_delete(procore_company_id, project_id, location_id)

Delete Project Location

Deletes a specified Location.

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
    api_instance = procore_sdk.CoreProjectLocationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    location_id = 56 # int | ID of the location

    try:
        # Delete Project Location
        api_instance.rest_v11_projects_project_id_locations_location_id_delete(procore_company_id, project_id, location_id)
    except Exception as e:
        print("Exception when calling CoreProjectLocationsApi->rest_v11_projects_project_id_locations_location_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **location_id** | **int**| ID of the location | 

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
**204** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

