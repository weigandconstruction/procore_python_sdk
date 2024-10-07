# procore_sdk.ProjectManagementModelsBIMModelRevisionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_bim_model_revisions_get**](ProjectManagementModelsBIMModelRevisionsApi.md#rest_v10_bim_model_revisions_get) | **GET** /rest/v1.0/bim_model_revisions | List BIM Model Revisions
[**rest_v10_bim_model_revisions_id_delete**](ProjectManagementModelsBIMModelRevisionsApi.md#rest_v10_bim_model_revisions_id_delete) | **DELETE** /rest/v1.0/bim_model_revisions/{id} | Delete BIM Model Revision
[**rest_v10_bim_model_revisions_id_get**](ProjectManagementModelsBIMModelRevisionsApi.md#rest_v10_bim_model_revisions_id_get) | **GET** /rest/v1.0/bim_model_revisions/{id} | Show BIM Model Revision
[**rest_v10_bim_model_revisions_id_patch**](ProjectManagementModelsBIMModelRevisionsApi.md#rest_v10_bim_model_revisions_id_patch) | **PATCH** /rest/v1.0/bim_model_revisions/{id} | Update BIM Model Revision
[**rest_v10_bim_model_revisions_post**](ProjectManagementModelsBIMModelRevisionsApi.md#rest_v10_bim_model_revisions_post) | **POST** /rest/v1.0/bim_model_revisions | Create BIM Model Revision


# **rest_v10_bim_model_revisions_get**
> List[RestV10BimModelRevisionsGet200ResponseInner] rest_v10_bim_model_revisions_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_bim_model_id=filters_bim_model_id, filters_publish_status=filters_publish_status, sort=sort)

List BIM Model Revisions

Lists BIM Model Revisions associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_model_revisions_get200_response_inner import RestV10BimModelRevisionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The compact view contains only ids. The normal view does not include the attribute 'published_model', and contains 'bim_gridline_id' instead of object. The extended view contains the response shown below. The default view is normal. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)
    filters_bim_model_id = 56 # int | Filter item(s) with matching Bim Model ids. (optional)
    filters_publish_status = 'filters_publish_status_example' # str | Filter item(s) by publish status (optional)
    sort = 'sort_example' # str | Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character '-' (optional)

    try:
        # List BIM Model Revisions
        api_response = api_instance.rest_v10_bim_model_revisions_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filters_id=filters_id, filters_bim_file_id=filters_bim_file_id, filters_bim_model_id=filters_bim_model_id, filters_publish_status=filters_publish_status, sort=sort)
        print("The response of ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The compact view contains only ids. The normal view does not include the attribute &#39;published_model&#39;, and contains &#39;bim_gridline_id&#39; instead of object. The extended view contains the response shown below. The default view is normal. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 
 **filters_bim_model_id** | **int**| Filter item(s) with matching Bim Model ids. | [optional] 
 **filters_publish_status** | **str**| Filter item(s) by publish status | [optional] 
 **sort** | **str**| Sort item(s) by an attribute. The default sort is ascending. To sort in descending order, prepend the sort value with a hyphen character &#39;-&#39; | [optional] 

### Return type

[**List[RestV10BimModelRevisionsGet200ResponseInner]**](RestV10BimModelRevisionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BIM Model Revisions listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | User does not have permission to view BIM Model Revisions |  -  |
**403** | User does not have permission to view BIM Model Revisions |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_bim_model_revisions_id_delete**
> rest_v10_bim_model_revisions_id_delete(procore_company_id, id, project_id)

Delete BIM Model Revision

Delete a BIM Model Revision from the system.

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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete BIM Model Revision
        api_instance.rest_v10_bim_model_revisions_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision ID | 
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

# **rest_v10_bim_model_revisions_id_get**
> RestV10BimModelRevisionsGet200ResponseInner rest_v10_bim_model_revisions_id_get(procore_company_id, id, project_id, view=view)

Show BIM Model Revision

Return a single BIM Model Revision.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_bim_model_revisions_get200_response_inner import RestV10BimModelRevisionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | The compact view contains only ids. The normal view does not include the attribute 'published_model', and contains 'bim_gridline_id' instead of object. The extended view contains the response shown below. The default view is normal. (optional)

    try:
        # Show BIM Model Revision
        api_response = api_instance.rest_v10_bim_model_revisions_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| The compact view contains only ids. The normal view does not include the attribute &#39;published_model&#39;, and contains &#39;bim_gridline_id&#39; instead of object. The extended view contains the response shown below. The default view is normal. | [optional] 

### Return type

[**RestV10BimModelRevisionsGet200ResponseInner**](RestV10BimModelRevisionsGet200ResponseInner.md)

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

# **rest_v10_bim_model_revisions_id_patch**
> RestV10BimModelRevisionsGet200ResponseInner rest_v10_bim_model_revisions_id_patch(procore_company_id, id, body131)

Update BIM Model Revision

Update a BIM Model Revision. The attributes `published_model_upload_uuid` and `object_definition_upload_uuid` should only be provided if the model is not associated to any upload. If a model is already associated to an upload, providing these attributes will cause error response.   For 3d files converted to Procore's format using BIM File Extractions API, the `geometry_file_id` can be retrieved via [BIM File Extraction API](https://developers.procore.com/reference/rest/v1/bim-file-extractions?version=1.0#show-bim-file-extraction) using the following JSONPath:      $.extraction_items.artifact.mobile_format.id  In a similar manner, the `property_file_id` can be retrieved via [BIM File Extraction API](https://developers.procore.com/reference/rest/v1/bim-file-extractions?version=1.0#show-bim-file-extraction) using the following JSONPath:      $.extraction_items.artifact.properties.id    Note that in the response for this BIM Model Revision endpoint, `geometry_file_id` will be designated as `published_model.id`, and `property_file_id` will be designated as `object_definition.id`.

### Example


```python
import procore_sdk
from procore_sdk.models.body131 import Body131
from procore_sdk.models.rest_v10_bim_model_revisions_get200_response_inner import RestV10BimModelRevisionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | BIM Model Revision ID
    body131 = procore_sdk.Body131() # Body131 | 

    try:
        # Update BIM Model Revision
        api_response = api_instance.rest_v10_bim_model_revisions_id_patch(procore_company_id, id, body131)
        print("The response of ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| BIM Model Revision ID | 
 **body131** | [**Body131**](Body131.md)|  | 

### Return type

[**RestV10BimModelRevisionsGet200ResponseInner**](RestV10BimModelRevisionsGet200ResponseInner.md)

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

# **rest_v10_bim_model_revisions_post**
> RestV10BimModelRevisionsGet200ResponseInner rest_v10_bim_model_revisions_post(procore_company_id, body130)

Create BIM Model Revision

Create a Revision for a BIM Model. If a set of upload UUIDs or model artifact references are not provided, the revision will be created with 'unpublished' publish status.   For 3d files converted to Procore's format using BIM File Extractions API, the `geometry_file_id` can be retrieved via [BIM File Extraction API](https://developers.procore.com/reference/rest/v1/bim-file-extractions?version=1.0#show-bim-file-extraction) using the following JSONPath:      $.extraction_items.artifact.mobile_format.id  In a similar manner, the `property_file_id` can be retrieved via [BIM File Extraction API](https://developers.procore.com/reference/rest/v1/bim-file-extractions?version=1.0#show-bim-file-extraction) using the following JSONPath:      $.extraction_items.artifact.properties.id    Note that in the response for this BIM Model Revision endpoint, `geometry_file_id` will be designated as `published_model.id`, and `property_file_id` will be designated as `object_definition.id`.

### Example


```python
import procore_sdk
from procore_sdk.models.body130 import Body130
from procore_sdk.models.rest_v10_bim_model_revisions_get200_response_inner import RestV10BimModelRevisionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementModelsBIMModelRevisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body130 = procore_sdk.Body130() # Body130 | 

    try:
        # Create BIM Model Revision
        api_response = api_instance.rest_v10_bim_model_revisions_post(procore_company_id, body130)
        print("The response of ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementModelsBIMModelRevisionsApi->rest_v10_bim_model_revisions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body130** | [**Body130**](Body130.md)|  | 

### Return type

[**RestV10BimModelRevisionsGet200ResponseInner**](RestV10BimModelRevisionsGet200ResponseInner.md)

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

