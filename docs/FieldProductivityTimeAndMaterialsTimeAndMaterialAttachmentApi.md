# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi.md#rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_entry_attachments/bulk_destroy | Bulk Delete Time and Material Attachments
[**rest_v10_projects_project_id_time_and_material_entry_attachments_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi.md#rest_v10_projects_project_id_time_and_material_entry_attachments_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entry_attachments | List all attachments
[**rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi.md#rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_entry_attachments/{id} | Delete a Time and Material Attachment
[**rest_v10_projects_project_id_time_and_material_entry_attachments_id_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi.md#rest_v10_projects_project_id_time_and_material_entry_attachments_id_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_entry_attachments/{id} | Show an individual time and material attachment
[**rest_v10_projects_project_id_time_and_material_entry_attachments_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi.md#rest_v10_projects_project_id_time_and_material_entry_attachments_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_entry_attachments | Create attachment


# **rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner] rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request)

Bulk Delete Time and Material Attachments

Delete multiple Time and Material Attachments with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request import RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request = procore_sdk.RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequest() # RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Time and Material Attachments
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_time_and_material_entry_attachments_bulk_destroy_delete_request** | [**RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequest**](RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsBulkDestroyDeleteRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md)

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

# **rest_v10_projects_project_id_time_and_material_entry_attachments_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner] rest_v10_projects_project_id_time_and_material_entry_attachments_get(procore_company_id, project_id)

List all attachments

Return a list of all Time and Material attachments for the specified Project user has access to.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List all attachments
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entry_attachments_get(procore_company_id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md)

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

# **rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete(procore_company_id, project_id, id)

Delete a Time and Material Attachment

Deleting a Time and Material Attachment from a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the Time and Material Attachment

    try:
        # Delete a Time and Material Attachment
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the Time and Material Attachment | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_entry_attachments_id_get**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner rest_v10_projects_project_id_time_and_material_entry_attachments_id_get(procore_company_id, project_id, id)

Show an individual time and material attachment

Return detailed information about a specific time and material attachment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the time and material attachment

    try:
        # Show an individual time and material attachment
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entry_attachments_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the time and material attachment | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md)

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

# **rest_v10_projects_project_id_time_and_material_entry_attachments_post**
> RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner rest_v10_projects_project_id_time_and_material_entry_attachments_post(procore_company_id, project_id, rest_v10_projects_project_id_time_and_material_entry_attachments_post_request)

Create attachment

Create a new attachment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_time_and_material_entry_attachments_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entry_attachments_post_request import RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_time_and_material_entry_attachments_post_request = procore_sdk.RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest() # RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest | 

    try:
        # Create attachment
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_entry_attachments_post(procore_company_id, project_id, rest_v10_projects_project_id_time_and_material_entry_attachments_post_request)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialAttachmentApi->rest_v10_projects_project_id_time_and_material_entry_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_time_and_material_entry_attachments_post_request** | [**RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest**](RestV10ProjectsProjectIdTimeAndMaterialEntryAttachmentsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md)

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

