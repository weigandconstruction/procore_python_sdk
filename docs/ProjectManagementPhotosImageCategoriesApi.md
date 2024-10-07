# procore_sdk.ProjectManagementPhotosImageCategoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_image_categories_get**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_get) | **GET** /rest/v1.0/image_categories | List image categories
[**rest_v10_image_categories_id_delete**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_id_delete) | **DELETE** /rest/v1.0/image_categories/{id} | Delete image category
[**rest_v10_image_categories_id_get**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_id_get) | **GET** /rest/v1.0/image_categories/{id} | Show image category
[**rest_v10_image_categories_id_patch**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_id_patch) | **PATCH** /rest/v1.0/image_categories/{id} | Update image category
[**rest_v10_image_categories_ids_with_images_get**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_ids_with_images_get) | **GET** /rest/v1.0/image_categories/ids_with_images | List Image Category IDs That Contain Images
[**rest_v10_image_categories_post**](ProjectManagementPhotosImageCategoriesApi.md#rest_v10_image_categories_post) | **POST** /rest/v1.0/image_categories | Create image category


# **rest_v10_image_categories_get**
> List[ImageCategory] rest_v10_image_categories_get(procore_company_id, project_id, page=page, per_page=per_page)

List image categories

Return a list of all Photo Albums (Image Categories) in a specified project.

### Example


```python
import procore_sdk
from procore_sdk.models.image_category import ImageCategory
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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List image categories
        api_response = api_instance.rest_v10_image_categories_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ImageCategory]**](ImageCategory.md)

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

# **rest_v10_image_categories_id_delete**
> rest_v10_image_categories_id_delete(procore_company_id, id, project_id)

Delete image category

Delete a Photo Album (Image Category) from a specified Project.

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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image category
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete image category
        api_instance.rest_v10_image_categories_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image category | 
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

# **rest_v10_image_categories_id_get**
> ImageCategory2 rest_v10_image_categories_id_get(procore_company_id, id, project_id)

Show image category

Return detail information about the specified Photo Album (Image Category).

### Example


```python
import procore_sdk
from procore_sdk.models.image_category2 import ImageCategory2
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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image category
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show image category
        api_response = api_instance.rest_v10_image_categories_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image category | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ImageCategory2**](ImageCategory2.md)

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

# **rest_v10_image_categories_id_patch**
> ImageCategory2 rest_v10_image_categories_id_patch(procore_company_id, id, project_id, body80)

Update image category

Update a Photo Album (Image Category) in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body80 import Body80
from procore_sdk.models.image_category2 import ImageCategory2
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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image category
    project_id = 56 # int | Unique identifier for the project.
    body80 = procore_sdk.Body80() # Body80 | 

    try:
        # Update image category
        api_response = api_instance.rest_v10_image_categories_id_patch(procore_company_id, id, project_id, body80)
        print("The response of ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image category | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body80** | [**Body80**](Body80.md)|  | 

### Return type

[**ImageCategory2**](ImageCategory2.md)

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

# **rest_v10_image_categories_ids_with_images_get**
> List[int] rest_v10_image_categories_ids_with_images_get(procore_company_id, project_id, filters_updated_at=filters_updated_at)

List Image Category IDs That Contain Images

Return an array of Image Category IDs for a specified Project that contain Images See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_updated_at = 'filters_updated_at_example' # str | Return Image Categories that contain Images that are within a specific updated_at date-time range. (optional)

    try:
        # List Image Category IDs That Contain Images
        api_response = api_instance.rest_v10_image_categories_ids_with_images_get(procore_company_id, project_id, filters_updated_at=filters_updated_at)
        print("The response of ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_ids_with_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_ids_with_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_updated_at** | **str**| Return Image Categories that contain Images that are within a specific updated_at date-time range. | [optional] 

### Return type

**List[int]**

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

# **rest_v10_image_categories_post**
> ImageCategory2 rest_v10_image_categories_post(procore_company_id, project_id, body80)

Create image category

Create a new Photo Album (Category) for Images.

### Example


```python
import procore_sdk
from procore_sdk.models.body80 import Body80
from procore_sdk.models.image_category2 import ImageCategory2
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
    api_instance = procore_sdk.ProjectManagementPhotosImageCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body80 = procore_sdk.Body80() # Body80 | 

    try:
        # Create image category
        api_response = api_instance.rest_v10_image_categories_post(procore_company_id, project_id, body80)
        print("The response of ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImageCategoriesApi->rest_v10_image_categories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body80** | [**Body80**](Body80.md)|  | 

### Return type

[**ImageCategory2**](ImageCategory2.md)

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

