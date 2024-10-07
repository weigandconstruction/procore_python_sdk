# procore_sdk.ProjectManagementModelsBIMModelsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_models_get**](ProjectManagementModelsBIMModelsApi.md#rest_v10_bim_models_get) | **GET** /rest/v1.0/bim_models | List BIM Models
[**rest_v10_bim_models_id_delete**](ProjectManagementModelsBIMModelsApi.md#rest_v10_bim_models_id_delete) | **DELETE** /rest/v1.0/bim_models/{id} | Delete BIM Model
[**rest_v10_bim_models_id_get**](ProjectManagementModelsBIMModelsApi.md#rest_v10_bim_models_id_get) | **GET** /rest/v1.0/bim_models/{id} | Show BIM Model
[**rest_v10_bim_models_id_patch**](ProjectManagementModelsBIMModelsApi.md#rest_v10_bim_models_id_patch) | **PATCH** /rest/v1.0/bim_models/{id} | Update BIM Model
[**rest_v10_bim_models_post**](ProjectManagementModelsBIMModelsApi.md#rest_v10_bim_models_post) | **POST** /rest/v1.0/bim_models | Create BIM Model


# **rest_v10_bim_models_get**
> List[RestV10BimModelsGet200ResponseInner] rest_v10_bim_models_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_has_revisions=filters_has_revisions, filters_search=filters_search, sort=sort)

List BIM Models

Lists BIM Models associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_models_get200_response_inner import RestV10BimModelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'current_revision_id' instead of an embedded object 'current_revision' The default view is normal. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)
    filters_has_revisions = True # bool | Filter item(s) with or without revisions. (optional)
    filters_search = 'filters_search_example' # str | Filter item(s) with the matching search query. The search is performed on title. (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)

    try:
        # List BIM Models
        api_response = api_instance.rest_v10_bim_models_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_has_revisions=filters_has_revisions, filters_search=filters_search, sort=sort)
        print("The response of ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;current_revision_id&#39; instead of an embedded object &#39;current_revision&#39; The default view is normal. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 
 **filters_has_revisions** | **bool**| Filter item(s) with or without revisions. | [optional] 
 **filters_search** | **str**| Filter item(s) with the matching search query. The search is performed on title. | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 

### Return type

[**List[RestV10BimModelsGet200ResponseInner]**](RestV10BimModelsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Models listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have permission to view BIM Models |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_models_id_delete**
> rest_v10_bim_models_id_delete(procore_company_id, id, project_id)

Delete BIM Model

Delete a BIM Model from the system. A BIM Model with revisions cannot be deleted.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete BIM Model
        api_instance.rest_v10_bim_models_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model ID | 
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

# **rest_v10_bim_models_id_get**
> RestV10BimModelsGet200ResponseInner rest_v10_bim_models_id_get(procore_company_id, id, project_id, view=view)

Show BIM Model

Return a single BIM Model item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_models_get200_response_inner import RestV10BimModelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The extended view contains the response shown below. The normal view contains 'current_revision_id' instead of an embedded object 'current_revision' The default view is normal. (optional)

    try:
        # Show BIM Model
        api_response = api_instance.rest_v10_bim_models_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The extended view contains the response shown below. The normal view contains &#39;current_revision_id&#39; instead of an embedded object &#39;current_revision&#39; The default view is normal. | [optional] 

### Return type

[**RestV10BimModelsGet200ResponseInner**](RestV10BimModelsGet200ResponseInner.md)

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

# **rest_v10_bim_models_id_patch**
> RestV10BimModelsGet200ResponseInner rest_v10_bim_models_id_patch(procore_company_id, id, body129)

Update BIM Model

Update a BIM Model item

### Example


```python
import procore_sdk
from procore_sdk.models.body129 import Body129
from procore_sdk.models.rest_v10_bim_models_get200_response_inner import RestV10BimModelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model ID
    body129 = procore_sdk.Body129() # Body129 | 

    try:
        # Update BIM Model
        api_response = api_instance.rest_v10_bim_models_id_patch(procore_company_id, id, body129)
        print("The response of ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model ID | 
 **body129** | [**Body129**](Body129.md)|  | 

### Return type

[**RestV10BimModelsGet200ResponseInner**](RestV10BimModelsGet200ResponseInner.md)

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

# **rest_v10_bim_models_post**
> RestV10BimModelsGet200ResponseInner rest_v10_bim_models_post(procore_company_id, body128)

Create BIM Model

Create a BIM Model in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.body128 import Body128
from procore_sdk.models.rest_v10_bim_models_get200_response_inner import RestV10BimModelsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body128 = procore_sdk.Body128() # Body128 | 

    try:
        # Create BIM Model
        api_response = api_instance.rest_v10_bim_models_post(procore_company_id, body128)
        print("The response of ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelsApi->rest_v10_bim_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body128** | [**Body128**](Body128.md)|  | 

### Return type

[**RestV10BimModelsGet200ResponseInner**](RestV10BimModelsGet200ResponseInner.md)

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

