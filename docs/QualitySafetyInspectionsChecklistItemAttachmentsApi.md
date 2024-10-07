# procore_sdk.QualitySafetyInspectionsChecklistItemAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post**](QualitySafetyInspectionsChecklistItemAttachmentsApi.md#rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/list_item_attachments/bulk_create | Bulk Create Checklist (Inspections) Item Attachments
[**rest_v10_projects_project_id_checklist_list_item_attachments_get**](QualitySafetyInspectionsChecklistItemAttachmentsApi.md#rest_v10_projects_project_id_checklist_list_item_attachments_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_item_attachments | List Checklist (Inspections) Item Attachments
[**rest_v10_projects_project_id_checklist_list_item_attachments_id_delete**](QualitySafetyInspectionsChecklistItemAttachmentsApi.md#rest_v10_projects_project_id_checklist_list_item_attachments_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/list_item_attachments/{id} | Delete Checklist (Inspections) Item Attachment
[**rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get**](QualitySafetyInspectionsChecklistItemAttachmentsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/list_item_attachments | List Recycled Checklist (Inspections) Item Attachments


# **rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post**
> List[ChecklistItemAttachment1] rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post(procore_company_id, project_id, checklist_item_attachments)

Bulk Create Checklist (Inspections) Item Attachments

Uploads Attachments to the specified Checklist Item for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_attachment1 import ChecklistItemAttachment1
from procore_sdk.models.checklist_item_attachments import ChecklistItemAttachments
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    checklist_item_attachments = procore_sdk.ChecklistItemAttachments() # ChecklistItemAttachments | 

    try:
        # Bulk Create Checklist (Inspections) Item Attachments
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post(procore_company_id, project_id, checklist_item_attachments)
        print("The response of QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_checklist_list_item_attachments_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_item_attachments** | [**ChecklistItemAttachments**](ChecklistItemAttachments.md)|  | 

### Return type

[**List[ChecklistItemAttachment1]**](ChecklistItemAttachment1.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_item_attachments_get**
> List[ChecklistItemAttachment1] rest_v10_projects_project_id_checklist_list_item_attachments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_item_id=filters_item_id)

List Checklist (Inspections) Item Attachments

Lists Checklist (Inspections) Item Attachments in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_attachment1 import ChecklistItemAttachment1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_item_id = [56] # List[int] | Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. (optional)

    try:
        # List Checklist (Inspections) Item Attachments
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_item_attachments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_item_id=filters_item_id)
        print("The response of QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_checklist_list_item_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_checklist_list_item_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_item_id** | [**List[int]**](int.md)| Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. | [optional] 

### Return type

[**List[ChecklistItemAttachment1]**](ChecklistItemAttachment1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_item_attachments_id_delete**
> rest_v10_projects_project_id_checklist_list_item_attachments_id_delete(procore_company_id, project_id, id)

Delete Checklist (Inspections) Item Attachment

Removes the Attachment for a specified Checklist Item on a given Project

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Item ID

    try:
        # Delete Checklist (Inspections) Item Attachment
        api_instance.rest_v10_projects_project_id_checklist_list_item_attachments_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_checklist_list_item_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Item ID | 

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
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get**
> List[ChecklistItemAttachment1] rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_item_id=filters_item_id)

List Recycled Checklist (Inspections) Item Attachments

Lists Checklist (Inspections) Item Attachments from deleted inspections in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_attachment1 import ChecklistItemAttachment1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_item_id = [56] # List[int] | Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. (optional)

    try:
        # List Recycled Checklist (Inspections) Item Attachments
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_item_id=filters_item_id)
        print("The response of QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemAttachmentsApi->rest_v10_projects_project_id_recycle_bin_checklist_list_item_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_item_id** | [**List[int]**](int.md)| Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. | [optional] 

### Return type

[**List[ChecklistItemAttachment1]**](ChecklistItemAttachment1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

