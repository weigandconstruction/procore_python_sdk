# procore_sdk.QualitySafetyInspectionsChecklistCommentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_checklist_lists_list_id_comments_id_get**](QualitySafetyInspectionsChecklistCommentsApi.md#rest_v10_checklist_lists_list_id_comments_id_get) | **GET** /rest/v1.0/checklist/lists/{list_id}/comments/{id} | Show Checklist Comment
[**rest_v10_checklist_lists_list_id_comments_post**](QualitySafetyInspectionsChecklistCommentsApi.md#rest_v10_checklist_lists_list_id_comments_post) | **POST** /rest/v1.0/checklist/lists/{list_id}/comments | Create Checklist Comment
[**rest_v10_projects_project_id_checklist_list_item_comments_get**](QualitySafetyInspectionsChecklistCommentsApi.md#rest_v10_projects_project_id_checklist_list_item_comments_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/list_item_comments | List Checklist (Inspection) Comments
[**rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get**](QualitySafetyInspectionsChecklistCommentsApi.md#rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/checklist/list_item_comments | List Recycled Checklist (Inspection) Comments


# **rest_v10_checklist_lists_list_id_comments_id_get**
> ChecklistComment rest_v10_checklist_lists_list_id_comments_id_get(procore_company_id, list_id, id, project_id)

Show Checklist Comment

Retrieves Checklist Comment in a specified Checklist.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_comment import ChecklistComment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    id = 56 # int | Comment ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Checklist Comment
        api_response = api_instance.rest_v10_checklist_lists_list_id_comments_id_get(procore_company_id, list_id, id, project_id)
        print("The response of QualitySafetyInspectionsChecklistCommentsApi->rest_v10_checklist_lists_list_id_comments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistCommentsApi->rest_v10_checklist_lists_list_id_comments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **id** | **int**| Comment ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ChecklistComment**](ChecklistComment.md)

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

# **rest_v10_checklist_lists_list_id_comments_post**
> ChecklistComment rest_v10_checklist_lists_list_id_comments_post(procore_company_id, list_id, checklist_comment_body)

Create Checklist Comment

Creates Checklist Comment in a specified Checklist

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_comment import ChecklistComment
from procore_sdk.models.checklist_comment_body import ChecklistCommentBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    list_id = 56 # int | Checklist ID
    checklist_comment_body = procore_sdk.ChecklistCommentBody() # ChecklistCommentBody | 

    try:
        # Create Checklist Comment
        api_response = api_instance.rest_v10_checklist_lists_list_id_comments_post(procore_company_id, list_id, checklist_comment_body)
        print("The response of QualitySafetyInspectionsChecklistCommentsApi->rest_v10_checklist_lists_list_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistCommentsApi->rest_v10_checklist_lists_list_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **list_id** | **int**| Checklist ID | 
 **checklist_comment_body** | [**ChecklistCommentBody**](ChecklistCommentBody.md)|  | 

### Return type

[**ChecklistComment**](ChecklistComment.md)

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

# **rest_v10_projects_project_id_checklist_list_item_comments_get**
> List[ChecklistComment] rest_v10_projects_project_id_checklist_list_item_comments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_item_id=filters_item_id, filters_updated_at=filters_updated_at, sort=sort)

List Checklist (Inspection) Comments

Returns the Checklist Comments from Checklists (Inspections) on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_comment import ChecklistComment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_item_id = [56] # List[int] | Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Checklist (Inspection) Comments
        api_response = api_instance.rest_v10_projects_project_id_checklist_list_item_comments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_item_id=filters_item_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistCommentsApi->rest_v10_projects_project_id_checklist_list_item_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistCommentsApi->rest_v10_projects_project_id_checklist_list_item_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_item_id** | [**List[int]**](int.md)| Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[ChecklistComment]**](ChecklistComment.md)

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

# **rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get**
> List[ChecklistComment] rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_item_id=filters_item_id, filters_updated_at=filters_updated_at, sort=sort)

List Recycled Checklist (Inspection) Comments

Returns the Checklist Comments from recycled Checklists (Inspections) on the Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_comment import ChecklistComment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_item_id = [56] # List[int] | Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Checklist (Inspection) Comments
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_item_id=filters_item_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyInspectionsChecklistCommentsApi->rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistCommentsApi->rest_v10_projects_project_id_recycle_bin_checklist_list_item_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_item_id** | [**List[int]**](int.md)| Array of Checklist Item IDs. Return item(s) associated with the specified Checklist Item IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[ChecklistComment]**](ChecklistComment.md)

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

