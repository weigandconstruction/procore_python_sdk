# procore_sdk.CoreProjectLinksLinksApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_links_get**](CoreProjectLinksLinksApi.md#rest_v10_links_get) | **GET** /rest/v1.0/links | List links
[**rest_v10_links_id_delete**](CoreProjectLinksLinksApi.md#rest_v10_links_id_delete) | **DELETE** /rest/v1.0/links/{id} | Delete link
[**rest_v10_links_id_get**](CoreProjectLinksLinksApi.md#rest_v10_links_id_get) | **GET** /rest/v1.0/links/{id} | Show link
[**rest_v10_links_id_patch**](CoreProjectLinksLinksApi.md#rest_v10_links_id_patch) | **PATCH** /rest/v1.0/links/{id} | Update link
[**rest_v10_links_id_restore_patch**](CoreProjectLinksLinksApi.md#rest_v10_links_id_restore_patch) | **PATCH** /rest/v1.0/links/{id}/restore | Retrieve recycled link
[**rest_v10_links_post**](CoreProjectLinksLinksApi.md#rest_v10_links_post) | **POST** /rest/v1.0/links | Create link
[**rest_v10_links_recycle_bin_get**](CoreProjectLinksLinksApi.md#rest_v10_links_recycle_bin_get) | **GET** /rest/v1.0/links/recycle_bin | List recycled links


# **rest_v10_links_get**
> List[RestV10LinksGet200ResponseInner] rest_v10_links_get(procore_company_id, project_id, page=page, per_page=per_page)

List links

Returns a list of Project Home Links on a given project.  This endpoint will be deprecated; please use the [V2](https://developers.procore.com/reference/rest/v2/links?version=2.0#list-project-links) endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_get200_response_inner import RestV10LinksGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List links
        api_response = api_instance.rest_v10_links_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10LinksGet200ResponseInner]**](RestV10LinksGet200ResponseInner.md)

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

# **rest_v10_links_id_delete**
> rest_v10_links_id_delete(procore_company_id, project_id, id)

Delete link

Send a specific Project Home Link to the recycle bin. Note: Requires either Company Admin or Project Home Admin permission. This endpoint will be deprecated; please use the [V2](https://developers.procore.com/reference/rest/v2/links?version=2.0#delete-a-link) endpoint.

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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Link ID

    try:
        # Delete link
        api_instance.rest_v10_links_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Link ID | 

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

# **rest_v10_links_id_get**
> RestV10LinksPost201Response rest_v10_links_id_get(procore_company_id, project_id, id)

Show link

Show detailed information for a specific Project Home Link

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_post201_response import RestV10LinksPost201Response
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Link ID

    try:
        # Show link
        api_response = api_instance.rest_v10_links_id_get(procore_company_id, project_id, id)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Link ID | 

### Return type

[**RestV10LinksPost201Response**](RestV10LinksPost201Response.md)

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

# **rest_v10_links_id_patch**
> RestV10LinksPost201Response rest_v10_links_id_patch(procore_company_id, project_id, id, rest_v10_links_post_request)

Update link

Update one or more attributes of a specific Project Home Link. Note: Requires either Company Admin or Project Home Admin permission. This endpoint will be deprecated; please use the [V2](https://developers.procore.com/reference/rest/v2/links?version=2.0#bulk-update-links) endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_post201_response import RestV10LinksPost201Response
from procore_sdk.models.rest_v10_links_post_request import RestV10LinksPostRequest
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Link ID
    rest_v10_links_post_request = procore_sdk.RestV10LinksPostRequest() # RestV10LinksPostRequest | 

    try:
        # Update link
        api_response = api_instance.rest_v10_links_id_patch(procore_company_id, project_id, id, rest_v10_links_post_request)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Link ID | 
 **rest_v10_links_post_request** | [**RestV10LinksPostRequest**](RestV10LinksPostRequest.md)|  | 

### Return type

[**RestV10LinksPost201Response**](RestV10LinksPost201Response.md)

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

# **rest_v10_links_id_restore_patch**
> RestV10LinksPost201Response rest_v10_links_id_restore_patch(procore_company_id, project_id, id)

Retrieve recycled link

Retrieves and restores a specific Project Home Link from the recycle bin. Note: Requires either Company Admin or Project Home Admin permission.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_post201_response import RestV10LinksPost201Response
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Link ID

    try:
        # Retrieve recycled link
        api_response = api_instance.rest_v10_links_id_restore_patch(procore_company_id, project_id, id)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Link ID | 

### Return type

[**RestV10LinksPost201Response**](RestV10LinksPost201Response.md)

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

# **rest_v10_links_post**
> RestV10LinksPost201Response rest_v10_links_post(procore_company_id, project_id, rest_v10_links_post_request)

Create link

Creates a Project Home Link on a given project. Note: Requires either Company Admin or Project Home Admin permission. This endpoint will be deprecated; please use the [V2](https://developers.procore.com/reference/rest/v2/links?version=2.0#bulk-update-links) endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_post201_response import RestV10LinksPost201Response
from procore_sdk.models.rest_v10_links_post_request import RestV10LinksPostRequest
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_links_post_request = procore_sdk.RestV10LinksPostRequest() # RestV10LinksPostRequest | 

    try:
        # Create link
        api_response = api_instance.rest_v10_links_post(procore_company_id, project_id, rest_v10_links_post_request)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_links_post_request** | [**RestV10LinksPostRequest**](RestV10LinksPostRequest.md)|  | 

### Return type

[**RestV10LinksPost201Response**](RestV10LinksPost201Response.md)

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

# **rest_v10_links_recycle_bin_get**
> List[RestV10LinksRecycleBinGet200ResponseInner] rest_v10_links_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page)

List recycled links

Returns a list of all Project Home Links in the recycle bin for a specific project. Note: Requires either Company Admin or Project Home Admin permission.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_links_recycle_bin_get200_response_inner import RestV10LinksRecycleBinGet200ResponseInner
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
    api_instance = procore_sdk.CoreProjectLinksLinksApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List recycled links
        api_response = api_instance.rest_v10_links_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectLinksLinksApi->rest_v10_links_recycle_bin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectLinksLinksApi->rest_v10_links_recycle_bin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10LinksRecycleBinGet200ResponseInner]**](RestV10LinksRecycleBinGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

