# procore_sdk.QualitySafetyInspectionsItemResponseSetsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_item_response_sets_get**](QualitySafetyInspectionsItemResponseSetsApi.md#rest_v10_companies_company_id_checklist_item_response_sets_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/item/response_sets | List Item Response Sets
[**rest_v10_companies_company_id_checklist_item_response_sets_id_delete**](QualitySafetyInspectionsItemResponseSetsApi.md#rest_v10_companies_company_id_checklist_item_response_sets_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{id} | Delete Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_id_get**](QualitySafetyInspectionsItemResponseSetsApi.md#rest_v10_companies_company_id_checklist_item_response_sets_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{id} | Show Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_id_patch**](QualitySafetyInspectionsItemResponseSetsApi.md#rest_v10_companies_company_id_checklist_item_response_sets_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/checklist/item/response_sets/{id} | Update Item Response Set
[**rest_v10_companies_company_id_checklist_item_response_sets_post**](QualitySafetyInspectionsItemResponseSetsApi.md#rest_v10_companies_company_id_checklist_item_response_sets_post) | **POST** /rest/v1.0/companies/{company_id}/checklist/item/response_sets | Create Item Response Set


# **rest_v10_companies_company_id_checklist_item_response_sets_get**
> List[ChecklistItemResponseSet1] rest_v10_companies_company_id_checklist_item_response_sets_get(procore_company_id, company_id, sort=sort, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_active=filters_active, page=page, per_page=per_page)

List Item Response Sets

List Checklist Item Response Sets for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response_set1 import ChecklistItemResponseSet1
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    sort = 'sort_example' # str |  (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Item Response Sets
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_get(procore_company_id, company_id, sort=sort, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_active=filters_active, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **sort** | **str**|  | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistItemResponseSet1]**](ChecklistItemResponseSet1.md)

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

# **rest_v10_companies_company_id_checklist_item_response_sets_id_delete**
> rest_v10_companies_company_id_checklist_item_response_sets_id_delete(procore_company_id, company_id, id)

Delete Item Response Set

Deletes a Company Checklist Item Response Set for a specified Company.

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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Item Response Set ID

    try:
        # Delete Item Response Set
        api_instance.rest_v10_companies_company_id_checklist_item_response_sets_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Item Response Set ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_id_get**
> ChecklistItemResponseSet1 rest_v10_companies_company_id_checklist_item_response_sets_id_get(procore_company_id, company_id, id)

Show Item Response Set

Returns a specified Checklist Item Response Set.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response_set1 import ChecklistItemResponseSet1
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Item Response Set ID

    try:
        # Show Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Item Response Set ID | 

### Return type

[**ChecklistItemResponseSet1**](ChecklistItemResponseSet1.md)

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

# **rest_v10_companies_company_id_checklist_item_response_sets_id_patch**
> ChecklistItemResponseSet1 rest_v10_companies_company_id_checklist_item_response_sets_id_patch(procore_company_id, company_id, id, checklist_item_response_set_body1)

Update Item Response Set

Updates a Company Checklist Item Response Set for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response_set1 import ChecklistItemResponseSet1
from procore_sdk.models.checklist_item_response_set_body1 import ChecklistItemResponseSetBody1
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Item Response Set ID
    checklist_item_response_set_body1 = procore_sdk.ChecklistItemResponseSetBody1() # ChecklistItemResponseSetBody1 | 

    try:
        # Update Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_id_patch(procore_company_id, company_id, id, checklist_item_response_set_body1)
        print("The response of QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Item Response Set ID | 
 **checklist_item_response_set_body1** | [**ChecklistItemResponseSetBody1**](ChecklistItemResponseSetBody1.md)|  | 

### Return type

[**ChecklistItemResponseSet1**](ChecklistItemResponseSet1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_checklist_item_response_sets_post**
> ChecklistItemResponseSet1 rest_v10_companies_company_id_checklist_item_response_sets_post(procore_company_id, company_id, checklist_item_response_set_body)

Create Item Response Set

Creates a Company Checklist Item Response Set for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_item_response_set1 import ChecklistItemResponseSet1
from procore_sdk.models.checklist_item_response_set_body import ChecklistItemResponseSetBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsItemResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    checklist_item_response_set_body = procore_sdk.ChecklistItemResponseSetBody() # ChecklistItemResponseSetBody | 

    try:
        # Create Item Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_item_response_sets_post(procore_company_id, company_id, checklist_item_response_set_body)
        print("The response of QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsItemResponseSetsApi->rest_v10_companies_company_id_checklist_item_response_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **checklist_item_response_set_body** | [**ChecklistItemResponseSetBody**](ChecklistItemResponseSetBody.md)|  | 

### Return type

[**ChecklistItemResponseSet1**](ChecklistItemResponseSet1.md)

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

