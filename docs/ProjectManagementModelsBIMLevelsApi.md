# procore_sdk.ProjectManagementModelsBIMLevelsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_levels_get**](ProjectManagementModelsBIMLevelsApi.md#rest_v10_bim_levels_get) | **GET** /rest/v1.0/bim_levels | List BIM Levels
[**rest_v10_bim_levels_id_delete**](ProjectManagementModelsBIMLevelsApi.md#rest_v10_bim_levels_id_delete) | **DELETE** /rest/v1.0/bim_levels/{id} | Delete BIM Level
[**rest_v10_bim_levels_id_get**](ProjectManagementModelsBIMLevelsApi.md#rest_v10_bim_levels_id_get) | **GET** /rest/v1.0/bim_levels/{id} | Show BIM Level
[**rest_v10_bim_levels_id_patch**](ProjectManagementModelsBIMLevelsApi.md#rest_v10_bim_levels_id_patch) | **PATCH** /rest/v1.0/bim_levels/{id} | Update BIM Level
[**rest_v10_bim_levels_post**](ProjectManagementModelsBIMLevelsApi.md#rest_v10_bim_levels_post) | **POST** /rest/v1.0/bim_levels | Create BIM Level


# **rest_v10_bim_levels_get**
> List[RestV10BimLevelsGet200ResponseInner] rest_v10_bim_levels_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_location_id=filters_location_id, sort=sort)

List BIM Levels

Lists BIM Levels associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner import RestV10BimLevelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'bim_file_id', 'location_id', and 'created_by_id' instead of embedded objects. The default view is normal. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)

    try:
        # List BIM Levels
        api_response = api_instance.rest_v10_bim_levels_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_location_id=filters_location_id, sort=sort)
        print("The response of ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;bim_file_id&#39;, &#39;location_id&#39;, and &#39;created_by_id&#39; instead of embedded objects. The default view is normal. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 

### Return type

[**List[RestV10BimLevelsGet200ResponseInner]**](RestV10BimLevelsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Levels listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view BIM Levels |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_levels_id_delete**
> rest_v10_bim_levels_id_delete(procore_company_id, id, project_id)

Delete BIM Level

Delete a BIM Level from the system. A BIM Level can only be deleted if it is not associated with published models.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Level ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete BIM Level
        api_instance.rest_v10_bim_levels_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Level ID | 
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

# **rest_v10_bim_levels_id_get**
> RestV10BimLevelsGet200ResponseInner rest_v10_bim_levels_id_get(procore_company_id, id, project_id, view=view)

Show BIM Level

Return a single BIM Level item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner import RestV10BimLevelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Level ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'bim_file_id', 'location_id', and 'created_by_id' instead of embedded objects. The default view is normal. (optional)

    try:
        # Show BIM Level
        api_response = api_instance.rest_v10_bim_levels_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Level ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;bim_file_id&#39;, &#39;location_id&#39;, and &#39;created_by_id&#39; instead of embedded objects. The default view is normal. | [optional] 

### Return type

[**RestV10BimLevelsGet200ResponseInner**](RestV10BimLevelsGet200ResponseInner.md)

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

# **rest_v10_bim_levels_id_patch**
> RestV10BimLevelsGet200ResponseInner rest_v10_bim_levels_id_patch(procore_company_id, id, body137)

Update BIM Level

Update a BIM Level item

### Example


```python
import procore_sdk
from procore_sdk.models.body137 import Body137
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner import RestV10BimLevelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Level ID
    body137 = procore_sdk.Body137() # Body137 | 

    try:
        # Update BIM Level
        api_response = api_instance.rest_v10_bim_levels_id_patch(procore_company_id, id, body137)
        print("The response of ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Level ID | 
 **body137** | [**Body137**](Body137.md)|  | 

### Return type

[**RestV10BimLevelsGet200ResponseInner**](RestV10BimLevelsGet200ResponseInner.md)

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

# **rest_v10_bim_levels_post**
> RestV10BimLevelsGet200ResponseInner rest_v10_bim_levels_post(procore_company_id, body136)

Create BIM Level

Create a BIM Level in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.body136 import Body136
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner import RestV10BimLevelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body136 = procore_sdk.Body136() # Body136 | 

    try:
        # Create BIM Level
        api_response = api_instance.rest_v10_bim_levels_post(procore_company_id, body136)
        print("The response of ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMLevelsApi->rest_v10_bim_levels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body136** | [**Body136**](Body136.md)|  | 

### Return type

[**RestV10BimLevelsGet200ResponseInner**](RestV10BimLevelsGet200ResponseInner.md)

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

