# procore_sdk.QualitySafetyPunchListPunchItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_punch_items_add_punch_item_attachments_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_add_punch_item_attachments_post) | **POST** /rest/v1.0/punch_items/add_punch_item_attachments | Add Attachments to Punch Item
[**rest_v10_punch_items_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_get) | **GET** /rest/v1.0/punch_items | List Punch Items
[**rest_v10_punch_items_id_comments_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_id_comments_post) | **POST** /rest/v1.0/punch_items/{id}/comments | Create Punch Item Comment
[**rest_v10_punch_items_id_delete**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_id_delete) | **DELETE** /rest/v1.0/punch_items/{id} | Delete Punch Item
[**rest_v10_punch_items_id_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_id_get) | **GET** /rest/v1.0/punch_items/{id} | Show Punch Item
[**rest_v10_punch_items_id_patch**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_id_patch) | **PATCH** /rest/v1.0/punch_items/{id} | Update Punch Item
[**rest_v10_punch_items_id_send_email_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_id_send_email_post) | **POST** /rest/v1.0/punch_items/{id}/send_email | Send Punch Item Email
[**rest_v10_punch_items_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_post) | **POST** /rest/v1.0/punch_items | Create Punch Item
[**rest_v10_punch_items_recycle_bin_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_recycle_bin_get) | **GET** /rest/v1.0/punch_items/recycle_bin | List Deleted Punch Items
[**rest_v10_punch_items_send_all_unsent_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_send_all_unsent_post) | **POST** /rest/v1.0/punch_items/send_all_unsent | Send All Unsent Punch Item Emails
[**rest_v10_punch_items_send_unsent_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_items_send_unsent_post) | **POST** /rest/v1.0/punch_items/send_unsent | Send unsent Punch Items
[**rest_v10_punch_list_default_distribution_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v10_punch_list_default_distribution_get) | **GET** /rest/v1.0/punch_list/default_distribution | List Punch Item Default Distribution List
[**rest_v11_punch_items_add_punch_item_attachments_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_add_punch_item_attachments_post) | **POST** /rest/v1.1/punch_items/add_punch_item_attachments | Add Attachments to Punch Item
[**rest_v11_punch_items_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_get) | **GET** /rest/v1.1/punch_items | List Punch Items
[**rest_v11_punch_items_id_delete**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_id_delete) | **DELETE** /rest/v1.1/punch_items/{id} | Delete Punch Item
[**rest_v11_punch_items_id_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_id_get) | **GET** /rest/v1.1/punch_items/{id} | Show Punch Item
[**rest_v11_punch_items_id_patch**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_id_patch) | **PATCH** /rest/v1.1/punch_items/{id} | Update Punch Item
[**rest_v11_punch_items_id_send_email_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_id_send_email_post) | **POST** /rest/v1.1/punch_items/{id}/send_email | Send Punch Item Email
[**rest_v11_punch_items_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_post) | **POST** /rest/v1.1/punch_items | Create Punch Item
[**rest_v11_punch_items_recycle_bin_get**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_recycle_bin_get) | **GET** /rest/v1.1/punch_items/recycle_bin | List Deleted Punch Items
[**rest_v11_punch_items_send_all_unsent_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_send_all_unsent_post) | **POST** /rest/v1.1/punch_items/send_all_unsent | Send All Unsent Punch Item Emails
[**rest_v11_punch_items_send_unsent_post**](QualitySafetyPunchListPunchItemsApi.md#rest_v11_punch_items_send_unsent_post) | **POST** /rest/v1.1/punch_items/send_unsent | Send unsent Punch Items


# **rest_v10_punch_items_add_punch_item_attachments_post**
> RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner rest_v10_punch_items_add_punch_item_attachments_post(procore_company_id, id, project_id, attachments=attachments)

Add Attachments to Punch Item

Add Attachments to Punch Item #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | ID of the project
    attachments = ['attachments_example'] # List[str] | Punch Item Assignment attachments. To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files. (optional)

    try:
        # Add Attachments to Punch Item
        api_response = api_instance.rest_v10_punch_items_add_punch_item_attachments_post(procore_company_id, id, project_id, attachments=attachments)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_add_punch_item_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_add_punch_item_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **project_id** | **int**| ID of the project | 
 **attachments** | [**List[str]**](str.md)| Punch Item Assignment attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_items_get**
> List[PunchItem6] rest_v10_punch_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_priority=filters_priority, filters_punch_item_type_id=filters_punch_item_type_id, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_approver_login_information_id=filters_approver_login_information_id, filters_vendor_id=filters_vendor_id, filters_assignee_response=filters_assignee_response, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_query=filters_query, filters_updated_at=filters_updated_at)

List Punch Items

Return a list of all Punch Items for a specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item6 import PunchItem6
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Punch Item Status - 'open' or 'closed'. (optional)
    filters_priority = 'filters_priority_example' # str | Return item(s) with the specified Punch Item Priority -  'low', 'medium', 'high' (optional)
    filters_punch_item_type_id = 56 # int | Return item(s) with the specified Punch Item Type ID. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_approver_login_information_id = 56 # int | User ID. Returns item(s) where the specified User ID is an approver. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_assignee_response = False # bool | If true, returns item(s) with the specified assignee response approved status. (optional) (default to False)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified Punch Item ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Punch Items
        api_response = api_instance.rest_v10_punch_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_priority=filters_priority, filters_punch_item_type_id=filters_punch_item_type_id, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_approver_login_information_id=filters_approver_login_information_id, filters_vendor_id=filters_vendor_id, filters_assignee_response=filters_assignee_response, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_query=filters_query, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_status** | **str**| Return item(s) with the specified Punch Item Status - &#39;open&#39; or &#39;closed&#39;. | [optional] 
 **filters_priority** | **str**| Return item(s) with the specified Punch Item Priority -  &#39;low&#39;, &#39;medium&#39;, &#39;high&#39; | [optional] 
 **filters_punch_item_type_id** | **int**| Return item(s) with the specified Punch Item Type ID. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_approver_login_information_id** | **int**| User ID. Returns item(s) where the specified User ID is an approver. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_assignee_response** | **bool**| If true, returns item(s) with the specified assignee response approved status. | [optional] [default to False]
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified Punch Item ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[PunchItem6]**](PunchItem6.md)

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

# **rest_v10_punch_items_id_comments_post**
> PunchItemComment rest_v10_punch_items_id_comments_post(procore_company_id, id, project_id, punch_item_comment_body)

Create Punch Item Comment

Create a new Punch Item Comment in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item_comment import PunchItemComment
from procore_sdk.models.punch_item_comment_body import PunchItemCommentBody
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | Unique identifier for the project.
    punch_item_comment_body = procore_sdk.PunchItemCommentBody() # PunchItemCommentBody | 

    try:
        # Create Punch Item Comment
        api_response = api_instance.rest_v10_punch_items_id_comments_post(procore_company_id, id, project_id, punch_item_comment_body)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **project_id** | **int**| Unique identifier for the project. | 
 **punch_item_comment_body** | [**PunchItemCommentBody**](PunchItemCommentBody.md)|  | 

### Return type

[**PunchItemComment**](PunchItemComment.md)

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

# **rest_v10_punch_items_id_delete**
> rest_v10_punch_items_id_delete(procore_company_id, id, project_id)

Delete Punch Item

Delete a specific Punch Item.

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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Punch Item
        api_instance.rest_v10_punch_items_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_items_id_get**
> PunchItem3 rest_v10_punch_items_id_get(procore_company_id, id, project_id)

Show Punch Item

Return detailed information about a specific Punch Item in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Punch Item
        api_response = api_instance.rest_v10_punch_items_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**PunchItem3**](PunchItem3.md)

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

# **rest_v10_punch_items_id_patch**
> PunchItem3 rest_v10_punch_items_id_patch(procore_company_id, id, punch_item_body6, run_configurable_validations=run_configurable_validations)

Update Punch Item

Update a specific Punch Item in a Project.  #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `punch_item[images][]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
from procore_sdk.models.punch_item_body6 import PunchItemBody6
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    punch_item_body6 = procore_sdk.PunchItemBody6() # PunchItemBody6 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Punch Item
        api_response = api_instance.rest_v10_punch_items_id_patch(procore_company_id, id, punch_item_body6, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **punch_item_body6** | [**PunchItemBody6**](PunchItemBody6.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**PunchItem3**](PunchItem3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_items_id_send_email_post**
> object rest_v10_punch_items_id_send_email_post(procore_company_id, id, body29)

Send Punch Item Email

Send an email for a Punch Item in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body29 import Body29
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    body29 = procore_sdk.Body29() # Body29 | 

    try:
        # Send Punch Item Email
        api_response = api_instance.rest_v10_punch_items_id_send_email_post(procore_company_id, id, body29)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **body29** | [**Body29**](Body29.md)|  | 

### Return type

**object**

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

# **rest_v10_punch_items_post**
> PunchItem3 rest_v10_punch_items_post(procore_company_id, punch_item_body4, run_configurable_validations=run_configurable_validations)

Create Punch Item

Create a new Punch Item in a Project.  #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `punch_item[images][]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
from procore_sdk.models.punch_item_body4 import PunchItemBody4
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    punch_item_body4 = procore_sdk.PunchItemBody4() # PunchItemBody4 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Punch Item
        api_response = api_instance.rest_v10_punch_items_post(procore_company_id, punch_item_body4, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **punch_item_body4** | [**PunchItemBody4**](PunchItemBody4.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**PunchItem3**](PunchItem3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_items_recycle_bin_get**
> PunchItem6 rest_v10_punch_items_recycle_bin_get(procore_company_id, project_id)

List Deleted Punch Items

Return an array of Deleted Punch objects for a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item6 import PunchItem6
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Deleted Punch Items
        api_response = api_instance.rest_v10_punch_items_recycle_bin_get(procore_company_id, project_id)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_recycle_bin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_recycle_bin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**PunchItem6**](PunchItem6.md)

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

# **rest_v10_punch_items_send_all_unsent_post**
> object rest_v10_punch_items_send_all_unsent_post(procore_company_id, project_id, body28)

Send All Unsent Punch Item Emails

Send all unsent Punch Item emails in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body28 import Body28
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body28 = procore_sdk.Body28() # Body28 | 

    try:
        # Send All Unsent Punch Item Emails
        api_response = api_instance.rest_v10_punch_items_send_all_unsent_post(procore_company_id, project_id, body28)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_send_all_unsent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_send_all_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body28** | [**Body28**](Body28.md)|  | 

### Return type

**object**

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

# **rest_v10_punch_items_send_unsent_post**
> rest_v10_punch_items_send_unsent_post(procore_company_id, rest_v11_punch_items_send_unsent_post_request)

Send unsent Punch Items

Sends email notifications for unsent Punch Items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_punch_items_send_unsent_post_request import RestV11PunchItemsSendUnsentPostRequest
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v11_punch_items_send_unsent_post_request = procore_sdk.RestV11PunchItemsSendUnsentPostRequest() # RestV11PunchItemsSendUnsentPostRequest | 

    try:
        # Send unsent Punch Items
        api_instance.rest_v10_punch_items_send_unsent_post(procore_company_id, rest_v11_punch_items_send_unsent_post_request)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_items_send_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v11_punch_items_send_unsent_post_request** | [**RestV11PunchItemsSendUnsentPostRequest**](RestV11PunchItemsSendUnsentPostRequest.md)|  | 

### Return type

void (empty response body)

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

# **rest_v10_punch_list_default_distribution_get**
> List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] rest_v10_punch_list_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)

List Punch Item Default Distribution List

Returns a collection of Default Distribution Members for a given Punch Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Punch Item Default Distribution List
        api_response = api_instance.rest_v10_punch_list_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v10_punch_list_default_distribution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v10_punch_list_default_distribution_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md)

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

# **rest_v11_punch_items_add_punch_item_attachments_post**
> RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner rest_v11_punch_items_add_punch_item_attachments_post(procore_company_id, id, project_id, attachments=attachments)

Add Attachments to Punch Item

Add Attachments to Punch Item #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get200_response_inner_attachments_inner import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | ID of the project
    attachments = ['attachments_example'] # List[str] | Punch Item Assignment attachments. To upload attachments you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `attachments[]` as files. (optional)

    try:
        # Add Attachments to Punch Item
        api_response = api_instance.rest_v11_punch_items_add_punch_item_attachments_post(procore_company_id, id, project_id, attachments=attachments)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_add_punch_item_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_add_punch_item_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **project_id** | **int**| ID of the project | 
 **attachments** | [**List[str]**](str.md)| Punch Item Assignment attachments. To upload attachments you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;attachments[]&#x60; as files. | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_punch_items_get**
> List[PunchItem] rest_v11_punch_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_priority=filters_priority, filters_punch_item_type_id=filters_punch_item_type_id, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_approver_login_information_id=filters_approver_login_information_id, filters_vendor_id=filters_vendor_id, filters_assignee_response=filters_assignee_response, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_query=filters_query, filters_updated_at=filters_updated_at)

List Punch Items

Return a list of all Punch Items for a specified Project. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item import PunchItem
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Punch Item Status - 'open' or 'closed'. (optional)
    filters_priority = 'filters_priority_example' # str | Return item(s) with the specified Punch Item Priority -  'low', 'medium', 'high' (optional)
    filters_punch_item_type_id = 56 # int | Return item(s) with the specified Punch Item Type ID. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_approver_login_information_id = 56 # int | User ID. Returns item(s) where the specified User ID is an approver. (optional)
    filters_vendor_id = 56 # int | Return item(s) with the specified Vendor ID. (optional)
    filters_assignee_response = False # bool | If true, returns item(s) with the specified assignee response approved status. (optional) (default to False)
    filters_trade_id = 56 # int | Trade ID (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified Punch Item ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Punch Items
        api_response = api_instance.rest_v11_punch_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_priority=filters_priority, filters_punch_item_type_id=filters_punch_item_type_id, filters_location_id=filters_location_id, filters_include_sublocations=filters_include_sublocations, filters_approver_login_information_id=filters_approver_login_information_id, filters_vendor_id=filters_vendor_id, filters_assignee_response=filters_assignee_response, filters_trade_id=filters_trade_id, filters_id=filters_id, filters_query=filters_query, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_status** | **str**| Return item(s) with the specified Punch Item Status - &#39;open&#39; or &#39;closed&#39;. | [optional] 
 **filters_priority** | **str**| Return item(s) with the specified Punch Item Priority -  &#39;low&#39;, &#39;medium&#39;, &#39;high&#39; | [optional] 
 **filters_punch_item_type_id** | **int**| Return item(s) with the specified Punch Item Type ID. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_approver_login_information_id** | **int**| User ID. Returns item(s) where the specified User ID is an approver. | [optional] 
 **filters_vendor_id** | **int**| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_assignee_response** | **bool**| If true, returns item(s) with the specified assignee response approved status. | [optional] [default to False]
 **filters_trade_id** | **int**| Trade ID | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified Punch Item ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[PunchItem]**](PunchItem.md)

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

# **rest_v11_punch_items_id_delete**
> rest_v11_punch_items_id_delete(procore_company_id, id, project_id)

Delete Punch Item

Delete a specific Punch Item.

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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Punch Item
        api_instance.rest_v11_punch_items_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_punch_items_id_get**
> PunchItem3 rest_v11_punch_items_id_get(procore_company_id, id, project_id)

Show Punch Item

Return detailed information about a specific Punch Item in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Punch Item
        api_response = api_instance.rest_v11_punch_items_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**PunchItem3**](PunchItem3.md)

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

# **rest_v11_punch_items_id_patch**
> PunchItem3 rest_v11_punch_items_id_patch(procore_company_id, id, punch_item_body2, run_configurable_validations=run_configurable_validations)

Update Punch Item

Update a specific Punch Item in a Project.  #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `punch_item[images][]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
from procore_sdk.models.punch_item_body2 import PunchItemBody2
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    punch_item_body2 = procore_sdk.PunchItemBody2() # PunchItemBody2 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Punch Item
        api_response = api_instance.rest_v11_punch_items_id_patch(procore_company_id, id, punch_item_body2, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **punch_item_body2** | [**PunchItemBody2**](PunchItemBody2.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**PunchItem3**](PunchItem3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_punch_items_id_send_email_post**
> object rest_v11_punch_items_id_send_email_post(procore_company_id, id, body29)

Send Punch Item Email

Send an email for a Punch Item in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body29 import Body29
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item
    body29 = procore_sdk.Body29() # Body29 | 

    try:
        # Send Punch Item Email
        api_response = api_instance.rest_v11_punch_items_id_send_email_post(procore_company_id, id, body29)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item | 
 **body29** | [**Body29**](Body29.md)|  | 

### Return type

**object**

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

# **rest_v11_punch_items_post**
> PunchItem3 rest_v11_punch_items_post(procore_company_id, punch_item_body, run_configurable_validations=run_configurable_validations)

Create Punch Item

Create a new Punch Item in a Project.  #### Uploading images To upload images you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `punch_item[images][]` as files.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item3 import PunchItem3
from procore_sdk.models.punch_item_body import PunchItemBody
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    punch_item_body = procore_sdk.PunchItemBody() # PunchItemBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Punch Item
        api_response = api_instance.rest_v11_punch_items_post(procore_company_id, punch_item_body, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **punch_item_body** | [**PunchItemBody**](PunchItemBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**PunchItem3**](PunchItem3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_punch_items_recycle_bin_get**
> PunchItem rest_v11_punch_items_recycle_bin_get(procore_company_id, project_id)

List Deleted Punch Items

Return an array of Deleted Punch objects for a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item import PunchItem
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Deleted Punch Items
        api_response = api_instance.rest_v11_punch_items_recycle_bin_get(procore_company_id, project_id)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_recycle_bin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_recycle_bin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**PunchItem**](PunchItem.md)

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

# **rest_v11_punch_items_send_all_unsent_post**
> object rest_v11_punch_items_send_all_unsent_post(procore_company_id, project_id, body28)

Send All Unsent Punch Item Emails

Send all unsent Punch Item emails in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body28 import Body28
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body28 = procore_sdk.Body28() # Body28 | 

    try:
        # Send All Unsent Punch Item Emails
        api_response = api_instance.rest_v11_punch_items_send_all_unsent_post(procore_company_id, project_id, body28)
        print("The response of QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_send_all_unsent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_send_all_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body28** | [**Body28**](Body28.md)|  | 

### Return type

**object**

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

# **rest_v11_punch_items_send_unsent_post**
> rest_v11_punch_items_send_unsent_post(procore_company_id, rest_v11_punch_items_send_unsent_post_request)

Send unsent Punch Items

Sends email notifications for unsent Punch Items.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_punch_items_send_unsent_post_request import RestV11PunchItemsSendUnsentPostRequest
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v11_punch_items_send_unsent_post_request = procore_sdk.RestV11PunchItemsSendUnsentPostRequest() # RestV11PunchItemsSendUnsentPostRequest | 

    try:
        # Send unsent Punch Items
        api_instance.rest_v11_punch_items_send_unsent_post(procore_company_id, rest_v11_punch_items_send_unsent_post_request)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemsApi->rest_v11_punch_items_send_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v11_punch_items_send_unsent_post_request** | [**RestV11PunchItemsSendUnsentPostRequest**](RestV11PunchItemsSendUnsentPostRequest.md)|  | 

### Return type

void (empty response body)

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

