# procore_sdk.QualitySafetyInspectionsChecklistItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_lists_list_id_items_id_get**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_checklist_lists_list_id_items_id_get) | **GET** /rest/v1.0/checklist/lists/{list_id}/items/{id} | Show Checklist Item
[**rest_v10_checklist_lists_list_id_items_id_patch**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_checklist_lists_list_id_items_id_patch) | **PATCH** /rest/v1.0/checklist/lists/{list_id}/items/{id} | Update Checklist Item
[**rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post) | **POST** /rest/v1.0/checklist/lists/{list_id}/items/{item_id}/item_attachments | Create Checklist Item Attachment
[**rest_v10_projects_project_id_checklist_items_item_id_item_response_delete**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_projects_project_id_checklist_items_item_id_item_response_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/items/{item_id}/item_response | Delete Checklist Item Response
[**rest_v10_projects_project_id_checklist_items_item_id_item_response_get**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_projects_project_id_checklist_items_item_id_item_response_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/items/{item_id}/item_response | Show Checklist Item Response
[**rest_v10_projects_project_id_checklist_items_item_id_item_response_post**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_projects_project_id_checklist_items_item_id_item_response_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/items/{item_id}/item_response | Create Checklist Item Response
[**rest_v10_projects_project_id_checklist_list_items_get**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v10_projects_project_id_checklist_list_items_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_items | List Checklist (Inspections) Items
[**rest_v11_projects_project_id_checklist_list_items_get**](QualitySafetyInspectionsChecklistItemsApi.md#rest_v11_projects_project_id_checklist_list_items_get) | **GET** /rest/v1.1/projects/{project_id}/checklist/list_items | List Checklist (Inspections) Items


# **rest_v10_checklist_lists_list_id_items_id_get**
> ChecklistSectionItem1 rest_v10_checklist_lists_list_id_items_id_get(procore_company_id, list_id, id, project_id, section_id)

Show Checklist Item

Retrieves Checklist Item in a specified Checklist

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_section_item1 import ChecklistSectionItem1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Item ID
    project_id = 56 # int | Unique identifier for the project.
    section_id = 56 # int | Checklist Section ID

    try:
        # Show Checklist Item
        api_response = api_instance.rest_v10_checklist_lists_list_id_items_id_get(procore_company_id, list_id, id, project_id, section_id)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **section_id** | **int**| Checklist Section ID | 

### Return type

[**ChecklistSectionItem1**](ChecklistSectionItem1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unauthorized |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_checklist_lists_list_id_items_id_patch**
> ChecklistSectionItem1 rest_v10_checklist_lists_list_id_items_id_patch(procore_company_id, list_id, id, checklist_item_body)

Update Checklist Item

Updates Checklist Item in a specified Checklist

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_body import ChecklistItemBody
from procore_sdk.models.checklist_section_item1 import ChecklistSectionItem1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Item ID
    checklist_item_body = procore_sdk.ChecklistItemBody() # ChecklistItemBody | 

    try:
        # Update Checklist Item
        api_response = api_instance.rest_v10_checklist_lists_list_id_items_id_patch(procore_company_id, list_id, id, checklist_item_body)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Item ID | 
 **checklist_item_body** | [**ChecklistItemBody**](ChecklistItemBody.md)|  | 

### Return type

[**ChecklistSectionItem1**](ChecklistSectionItem1.md)

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

# **rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post**
> ChecklistItemAttachment rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post(procore_company_id, list_id, item_id, project_id, section_id, attachment)

Create Checklist Item Attachment

Uploads an Attachment to the specified Checklist Item

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_attachment import ChecklistItemAttachment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    item_id = 56 # int | Checklist Item ID
    project_id = 56 # int | The ID of the Project the Item belongs to
    section_id = 56 # int | The ID of the Section the Item belongs to
    attachment = None # bytearray | Item Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with the `attachment` file.

    try:
        # Create Checklist Item Attachment
        api_response = api_instance.rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post(procore_company_id, list_id, item_id, project_id, section_id, attachment)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_checklist_lists_list_id_items_item_id_item_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **item_id** | **int**| Checklist Item ID | 
 **project_id** | **int**| The ID of the Project the Item belongs to | 
 **section_id** | **int**| The ID of the Section the Item belongs to | 
 **attachment** | **bytearray**| Item Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with the &#x60;attachment&#x60; file. | 

### Return type

[**ChecklistItemAttachment**](ChecklistItemAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_items_item_id_item_response_delete**
> rest_v10_projects_project_id_checklist_items_item_id_item_response_delete(procore_company_id, item_id, project_id)

Delete Checklist Item Response

Removes the Checklist Item Response for a specified Checklist Item

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    item_id = 56 # int | Checklist Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Checklist Item Response
        api_instance.rest_v10_projects_project_id_checklist_items_item_id_item_response_delete(procore_company_id, item_id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_items_item_id_item_response_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **item_id** | **int**| Checklist Item ID | 
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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_items_item_id_item_response_get**
> ChecklistItemResponse2 rest_v10_projects_project_id_checklist_items_item_id_item_response_get(procore_company_id, item_id, project_id)

Show Checklist Item Response

Returns the Checklist Item Response for a specified Checklist Item

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response2 import ChecklistItemResponse2
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    item_id = 56 # int | Checklist Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist Item Response
        api_response = api_instance.rest_v10_projects_project_id_checklist_items_item_id_item_response_get(procore_company_id, item_id, project_id)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_items_item_id_item_response_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_items_item_id_item_response_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **item_id** | **int**| Checklist Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ChecklistItemResponse2**](ChecklistItemResponse2.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_items_item_id_item_response_post**
> ChecklistItemResponse2 rest_v10_projects_project_id_checklist_items_item_id_item_response_post(procore_company_id, item_id, project_id, checklist_item_response_body)

Create Checklist Item Response

Create Checklist Item Response for a specified Checklist Item  Checklist Item Response can have one of the following payload formats (text_value, number_value, date_value, response_option, status)  A specific Item Type can only leverage its corresponding format.  *For instance, Number Items can only leverage a number_value while Date Items can only leverage a date_value.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response2 import ChecklistItemResponse2
from procore_sdk.models.checklist_item_response_body import ChecklistItemResponseBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    item_id = 56 # int | Checklist Item ID
    project_id = 56 # int | Unique identifier for the project.
    checklist_item_response_body = procore_sdk.ChecklistItemResponseBody() # ChecklistItemResponseBody | 

    try:
        # Create Checklist Item Response
        api_response = api_instance.rest_v10_projects_project_id_checklist_items_item_id_item_response_post(procore_company_id, item_id, project_id, checklist_item_response_body)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_items_item_id_item_response_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_items_item_id_item_response_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **item_id** | **int**| Checklist Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **checklist_item_response_body** | [**ChecklistItemResponseBody**](ChecklistItemResponseBody.md)|  | 

### Return type

[**ChecklistItemResponse2**](ChecklistItemResponse2.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_list_items_get**
> List[ChecklistListItem1] rest_v10_projects_project_id_checklist_list_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_section_id=filters_section_id, filters_list_id=filters_list_id, filters_item_response_status=filters_item_response_status, sort=sort)

List Checklist (Inspections) Items

Lists Checklist (Inspections) Items in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_list_item1 import ChecklistListItem1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_section_id = [56] # List[int] | Return item(s) with the specified Checklist Section IDs (optional)
    filters_list_id = [56] # List[int] | Return item(s) with the specified Checklist List IDs (optional)
    filters_item_response_status = 'filters_item_response_status_example' # str | Filter item(s) with matching item_response status. (optional)
    sort = 'sort_example' # str | Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. (optional)

    try:
        # List Checklist (Inspections) Items
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_section_id=filters_section_id, filters_list_id=filters_list_id, filters_item_response_status=filters_item_response_status, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_list_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v10_projects_project_id_checklist_list_items_get: %s\n" % e)
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
 **filters_section_id** | [**List[int]**](int.md)| Return item(s) with the specified Checklist Section IDs | [optional] 
 **filters_list_id** | [**List[int]**](int.md)| Return item(s) with the specified Checklist List IDs | [optional] 
 **filters_item_response_status** | **str**| Filter item(s) with matching item_response status. | [optional] 
 **sort** | **str**| Sort item(s) by the chosen param; check below for a list of options. The direction of sorting is ascending by default; for descending sort, insert the - symbol before the param. | [optional] 

### Return type

[**List[ChecklistListItem1]**](ChecklistListItem1.md)

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

# **rest_v11_projects_project_id_checklist_list_items_get**
> List[ChecklistListItem] rest_v11_projects_project_id_checklist_list_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_section_id=filters_section_id, filters_list_id=filters_list_id)

List Checklist (Inspections) Items

Lists Checklist (Inspections) Items in a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_list_item import ChecklistListItem
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_section_id = [56] # List[int] | Return item(s) with the specified Checklist Section IDs (optional)
    filters_list_id = [56] # List[int] | Return item(s) with the specified Checklist List IDs (optional)

    try:
        # List Checklist (Inspections) Items
        api_response = api_instance.rest_v11_projects_project_id_checklist_list_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_section_id=filters_section_id, filters_list_id=filters_list_id)
        print("The response of QualitySafetyInspectionsChecklistItemsApi->rest_v11_projects_project_id_checklist_list_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistItemsApi->rest_v11_projects_project_id_checklist_list_items_get: %s\n" % e)
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
 **filters_section_id** | [**List[int]**](int.md)| Return item(s) with the specified Checklist Section IDs | [optional] 
 **filters_list_id** | [**List[int]**](int.md)| Return item(s) with the specified Checklist List IDs | [optional] 

### Return type

[**List[ChecklistListItem]**](ChecklistListItem.md)

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

