# procore_sdk.ProjectManagementPhotosImagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_images_get**](ProjectManagementPhotosImagesApi.md#rest_v10_images_get) | **GET** /rest/v1.0/images | List images
[**rest_v10_images_id_delete**](ProjectManagementPhotosImagesApi.md#rest_v10_images_id_delete) | **DELETE** /rest/v1.0/images/{id} | Delete image
[**rest_v10_images_id_get**](ProjectManagementPhotosImagesApi.md#rest_v10_images_id_get) | **GET** /rest/v1.0/images/{id} | Show image
[**rest_v10_images_id_patch**](ProjectManagementPhotosImagesApi.md#rest_v10_images_id_patch) | **PATCH** /rest/v1.0/images/{id} | Update image
[**rest_v10_images_post**](ProjectManagementPhotosImagesApi.md#rest_v10_images_post) | **POST** /rest/v1.0/images | Create image


# **rest_v10_images_get**
> List[Image] rest_v10_images_get(procore_company_id, project_id, image_category_id=image_category_id, page=page, per_page=per_page, filters_log_date=filters_log_date, filters_private=filters_private, filters_starred=filters_starred, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_trade_ids=filters_trade_ids, filters_query=filters_query, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_id=filters_id, sort=sort, serializer_view=serializer_view)

List images

Return a list of all Images from a Project's Photo Album (Image Category).  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.image import Image
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
    api_instance = procore_sdk.ProjectManagementPhotosImagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    image_category_id = 56 # int | Optional. ID of the image category to filter the images by. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_log_date = '2013-10-20' # date | Date of Photos added to the Daily Log in the format \"YYYY-MM-DD\", or a range of dates in the format \"YYYY-MM-DD...YYYY-MM-DD\". (optional)
    filters_private = False # bool | If true, returns only item(s) with a `private` status. (optional) (default to False)
    filters_starred = False # bool | If true, returns only item(s) with a `starred` status. (optional) (default to False)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_trade_ids = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    sort = 'sort_example' # str | Field to sort by. If the field is passed with a - (EX: -created_at) it is sorted in reverse order (optional)
    serializer_view = 'serializer_view_example' # str | The data set that should be returned from the serializer. The normal view includes default fields, plus links, comments_count, trades. The android view includes default fields, plus trades, comments. The mobile view include default fields, plus log_date, trades, comments. The mobile_feed view includes default fields, plus comments. The prostore_file view includes default fields, plus images. The ids_only view does not include default fields, response returns strictly an array of image ids. Default view is normal. (optional)

    try:
        # List images
        api_response = api_instance.rest_v10_images_get(procore_company_id, project_id, image_category_id=image_category_id, page=page, per_page=per_page, filters_log_date=filters_log_date, filters_private=filters_private, filters_starred=filters_starred, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_trade_ids=filters_trade_ids, filters_query=filters_query, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_id=filters_id, sort=sort, serializer_view=serializer_view)
        print("The response of ProjectManagementPhotosImagesApi->rest_v10_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImagesApi->rest_v10_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **image_category_id** | **int**| Optional. ID of the image category to filter the images by. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_log_date** | **date**| Date of Photos added to the Daily Log in the format \&quot;YYYY-MM-DD\&quot;, or a range of dates in the format \&quot;YYYY-MM-DD...YYYY-MM-DD\&quot;. | [optional] 
 **filters_private** | **bool**| If true, returns only item(s) with a &#x60;private&#x60; status. | [optional] [default to False]
 **filters_starred** | **bool**| If true, returns only item(s) with a &#x60;starred&#x60; status. | [optional] [default to False]
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_trade_ids** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **sort** | **str**| Field to sort by. If the field is passed with a - (EX: -created_at) it is sorted in reverse order | [optional] 
 **serializer_view** | **str**| The data set that should be returned from the serializer. The normal view includes default fields, plus links, comments_count, trades. The android view includes default fields, plus trades, comments. The mobile view include default fields, plus log_date, trades, comments. The mobile_feed view includes default fields, plus comments. The prostore_file view includes default fields, plus images. The ids_only view does not include default fields, response returns strictly an array of image ids. Default view is normal. | [optional] 

### Return type

[**List[Image]**](Image.md)

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

# **rest_v10_images_id_delete**
> rest_v10_images_id_delete(procore_company_id, id, project_id, permanent=permanent)

Delete image

Remove an Image from a Project.

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
    api_instance = procore_sdk.ProjectManagementPhotosImagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image
    project_id = 56 # int | Unique identifier for the project.
    permanent = True # bool | If true, permanently deletes the image. (optional)

    try:
        # Delete image
        api_instance.rest_v10_images_id_delete(procore_company_id, id, project_id, permanent=permanent)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImagesApi->rest_v10_images_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image | 
 **project_id** | **int**| Unique identifier for the project. | 
 **permanent** | **bool**| If true, permanently deletes the image. | [optional] 

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

# **rest_v10_images_id_get**
> Image rest_v10_images_id_get(procore_company_id, id, project_id)

Show image

Show detailed information for a specified Image in a Project's Photo Album (Image Category).

### Example


```python
import procore_sdk
from procore_sdk.models.image import Image
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
    api_instance = procore_sdk.ProjectManagementPhotosImagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show image
        api_response = api_instance.rest_v10_images_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementPhotosImagesApi->rest_v10_images_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImagesApi->rest_v10_images_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Image**](Image.md)

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

# **rest_v10_images_id_patch**
> Image rest_v10_images_id_patch(procore_company_id, id, project_id, body79)

Update image

Update an existing Image in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body79 import Body79
from procore_sdk.models.image import Image
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
    api_instance = procore_sdk.ProjectManagementPhotosImagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the image
    project_id = 56 # int | Unique identifier for the project.
    body79 = procore_sdk.Body79() # Body79 | 

    try:
        # Update image
        api_response = api_instance.rest_v10_images_id_patch(procore_company_id, id, project_id, body79)
        print("The response of ProjectManagementPhotosImagesApi->rest_v10_images_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImagesApi->rest_v10_images_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the image | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body79** | [**Body79**](Body79.md)|  | 

### Return type

[**Image**](Image.md)

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

# **rest_v10_images_post**
> Image rest_v10_images_post(procore_company_id, project_id, image_name, image, upload_uuid=upload_uuid)

Create image

Upload and add a new Image to a Project's Photo Album (Image Category).

### Example


```python
import procore_sdk
from procore_sdk.models.image import Image
from procore_sdk.models.image1 import Image1
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
    api_instance = procore_sdk.ProjectManagementPhotosImagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    image_name = 'image_name_example' # str | The name of the image file to be uploaded. Required when using an upload_uuid to upload the image.
    image = procore_sdk.Image1() # Image1 | 
    upload_uuid = 'upload_uuid_example' # str | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. (optional)

    try:
        # Create image
        api_response = api_instance.rest_v10_images_post(procore_company_id, project_id, image_name, image, upload_uuid=upload_uuid)
        print("The response of ProjectManagementPhotosImagesApi->rest_v10_images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementPhotosImagesApi->rest_v10_images_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **image_name** | **str**| The name of the image file to be uploaded. Required when using an upload_uuid to upload the image. | 
 **image** | [**Image1**](Image1.md)|  | 
 **upload_uuid** | **str**| UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

