# procore_sdk.QualitySafetyObservationsObservationsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_observations_category_configurable_field_sets_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_category_configurable_field_sets_get) | **GET** /rest/v1.0/observations/category_configurable_field_sets | List Observation Category Configurable Field Sets
[**rest_v10_observations_default_distribution_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_default_distribution_get) | **GET** /rest/v1.0/observations/default_distribution | List Observation Default Distribution Members
[**rest_v10_observations_items_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_get) | **GET** /rest/v1.0/observations/items | List Observation Items
[**rest_v10_observations_items_id_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_id_get) | **GET** /rest/v1.0/observations/items/{id} | Show Observation Item
[**rest_v10_observations_items_id_patch**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_id_patch) | **PATCH** /rest/v1.0/observations/items/{id} | Update Observation Item
[**rest_v10_observations_items_id_pdf_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_id_pdf_get) | **GET** /rest/v1.0/observations/items/{id}/pdf | Get Observation Item PDF url
[**rest_v10_observations_items_id_send_email_post**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_id_send_email_post) | **POST** /rest/v1.0/observations/items/{id}/send_email | Send Observation Item Email
[**rest_v10_observations_items_item_id_response_logs_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_item_id_response_logs_get) | **GET** /rest/v1.0/observations/items/{item_id}/response_logs | List Observation Item Response Logs
[**rest_v10_observations_items_item_id_response_logs_post**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_item_id_response_logs_post) | **POST** /rest/v1.0/observations/items/{item_id}/response_logs | Create Observation Item Response Log
[**rest_v10_observations_items_next_available_number_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_next_available_number_get) | **GET** /rest/v1.0/observations/items/next_available_number | Show Next Available Number for Observation Items
[**rest_v10_observations_items_post**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_post) | **POST** /rest/v1.0/observations/items | Create Observation Item
[**rest_v10_observations_items_send_unsent_post**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_items_send_unsent_post) | **POST** /rest/v1.0/observations/items/send_unsent | Send unsent Observation Items
[**rest_v10_observations_potential_distribution_members_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_potential_distribution_members_get) | **GET** /rest/v1.0/observations/potential_distribution_members | List Observation Potential Distribution Members
[**rest_v10_observations_types_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_observations_types_get) | **GET** /rest/v1.0/observations/types | List Observation Types
[**rest_v10_projects_project_id_observations_items_id_delete**](QualitySafetyObservationsObservationsApi.md#rest_v10_projects_project_id_observations_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/observations/items/{id} | Delete Observation Item
[**rest_v10_projects_project_id_observations_response_logs_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_projects_project_id_observations_response_logs_get) | **GET** /rest/v1.0/projects/{project_id}/observations/response_logs | List Observations Response Logs
[**rest_v10_projects_project_id_recycle_bin_observations_items_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_projects_project_id_recycle_bin_observations_items_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/observations/items | List Recycled Observation Items
[**rest_v10_projects_project_id_recycle_bin_observations_items_id_get**](QualitySafetyObservationsObservationsApi.md#rest_v10_projects_project_id_recycle_bin_observations_items_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/observations/items/{id} | Show Recycled Observation
[**rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch**](QualitySafetyObservationsObservationsApi.md#rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/observations/items/{id}/restore | Retrieve Recycled Observation


# **rest_v10_observations_category_configurable_field_sets_get**
> List[ObservationCategoryConfigurableFieldSets] rest_v10_observations_category_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page)

List Observation Category Configurable Field Sets

Returns a collection of Observation Category Configurable Field Sets from the Project

### Example


```python
import procore_sdk
from procore_sdk.models.observation_category_configurable_field_sets import ObservationCategoryConfigurableFieldSets
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Category Configurable Field Sets
        api_response = api_instance.rest_v10_observations_category_configurable_field_sets_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_category_configurable_field_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_category_configurable_field_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationCategoryConfigurableFieldSets]**](ObservationCategoryConfigurableFieldSets.md)

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

# **rest_v10_observations_default_distribution_get**
> List[ObservationItemDefaultDistribution] rest_v10_observations_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)

List Observation Default Distribution Members

Returns a collection of Users that are of the Observations Default Distribution list

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_default_distribution import ObservationItemDefaultDistribution
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Default Distribution Members
        api_response = api_instance.rest_v10_observations_default_distribution_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_default_distribution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_default_distribution_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationItemDefaultDistribution]**](ObservationItemDefaultDistribution.md)

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

# **rest_v10_observations_items_get**
> List[ObservationItem] rest_v10_observations_items_get(procore_company_id, project_id, filters_assignee_company_id=filters_assignee_company_id, filters_checklist_list_id=filters_checklist_list_id, filters_created_by_id=filters_created_by_id, filters_id=filters_id, filters_location_id=filters_location_id, filters_assignee_id=filters_assignee_id, filters_checklist_item_id=filters_checklist_item_id, filters_priority=filters_priority, filters_search=filters_search, filters_status=filters_status, filters_type_id=filters_type_id, filters_trade_ids=filters_trade_ids, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List Observation Items

Returns a collection of Observation Items. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item import ObservationItem
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_assignee_company_id = [56] # List[int] | Array of Vendor IDs. Returns item(s) where the assignee is associated to the specified Vendor ID. (optional)
    filters_checklist_list_id = ['filters_checklist_list_id_example'] # List[str] | Array of Checklist List IDs. Return item(s) associated with the specified Checklist List IDs. (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)
    filters_assignee_id = [56] # List[int] | Return item(s) assigned to the specified User ID. (optional)
    filters_checklist_item_id = 56 # int | Return Observations(s) originating from the specified Checklist Item(s). (optional)
    filters_priority = ['filters_priority_example'] # List[str] | Return item(s) with the specified priorities.  (optional)
    filters_search = 'filters_search_example' # str | Return item(s) matching the specified Search query. (optional)
    filters_status = [56] # List[int] | Return item(s) with the specified status values. The mapping is as follows: ```   0: Initiated   1: Ready For reviewed   2: Not Accepted   3: Closed ``` (optional)
    filters_type_id = [56] # List[int] | Return item(s) with the specified Observation Type ID. (optional)
    filters_trade_ids = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Items
        api_response = api_instance.rest_v10_observations_items_get(procore_company_id, project_id, filters_assignee_company_id=filters_assignee_company_id, filters_checklist_list_id=filters_checklist_list_id, filters_created_by_id=filters_created_by_id, filters_id=filters_id, filters_location_id=filters_location_id, filters_assignee_id=filters_assignee_id, filters_checklist_item_id=filters_checklist_item_id, filters_priority=filters_priority, filters_search=filters_search, filters_status=filters_status, filters_type_id=filters_type_id, filters_trade_ids=filters_trade_ids, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_assignee_company_id** | [**List[int]**](int.md)| Array of Vendor IDs. Returns item(s) where the assignee is associated to the specified Vendor ID. | [optional] 
 **filters_checklist_list_id** | [**List[str]**](str.md)| Array of Checklist List IDs. Return item(s) associated with the specified Checklist List IDs. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Return item(s) assigned to the specified User ID. | [optional] 
 **filters_checklist_item_id** | **int**| Return Observations(s) originating from the specified Checklist Item(s). | [optional] 
 **filters_priority** | [**List[str]**](str.md)| Return item(s) with the specified priorities.  | [optional] 
 **filters_search** | **str**| Return item(s) matching the specified Search query. | [optional] 
 **filters_status** | [**List[int]**](int.md)| Return item(s) with the specified status values. The mapping is as follows: &#x60;&#x60;&#x60;   0: Initiated   1: Ready For reviewed   2: Not Accepted   3: Closed &#x60;&#x60;&#x60; | [optional] 
 **filters_type_id** | [**List[int]**](int.md)| Return item(s) with the specified Observation Type ID. | [optional] 
 **filters_trade_ids** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationItem]**](ObservationItem.md)

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

# **rest_v10_observations_items_id_get**
> ObservationItem1 rest_v10_observations_items_id_get(procore_company_id, id, project_id)

Show Observation Item

Returns an Observation Item.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item1 import ObservationItem1
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Observation Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Observation Item
        api_response = api_instance.rest_v10_observations_items_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Observation Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ObservationItem1**](ObservationItem1.md)

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

# **rest_v10_observations_items_id_patch**
> ObservationItem1 rest_v10_observations_items_id_patch(procore_company_id, id, body56)

Update Observation Item

Updates an Observation Item.

### Example


```python
import procore_sdk
from procore_sdk.models.body56 import Body56
from procore_sdk.models.observation_item1 import ObservationItem1
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Observation Item ID
    body56 = procore_sdk.Body56() # Body56 | 

    try:
        # Update Observation Item
        api_response = api_instance.rest_v10_observations_items_id_patch(procore_company_id, id, body56)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Observation Item ID | 
 **body56** | [**Body56**](Body56.md)|  | 

### Return type

[**ObservationItem1**](ObservationItem1.md)

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

# **rest_v10_observations_items_id_pdf_get**
> ObservationItemPDF rest_v10_observations_items_id_pdf_get(procore_company_id, id, project_id)

Get Observation Item PDF url

Return the PDF url for a specified Observation Item

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_pdf import ObservationItemPDF
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Observation Item ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Observation Item PDF url
        api_response = api_instance.rest_v10_observations_items_id_pdf_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Observation Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ObservationItemPDF**](ObservationItemPDF.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_observations_items_id_send_email_post**
> rest_v10_observations_items_id_send_email_post(procore_company_id, id, project_id, body58)

Send Observation Item Email

Sends an email for an Observation Item in a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body58 import Body58
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Observation Item ID
    project_id = 56 # int | Project ID
    body58 = procore_sdk.Body58() # Body58 | 

    try:
        # Send Observation Item Email
        api_instance.rest_v10_observations_items_id_send_email_post(procore_company_id, id, project_id, body58)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_id_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Observation Item ID | 
 **project_id** | **int**| Project ID | 
 **body58** | [**Body58**](Body58.md)|  | 

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

# **rest_v10_observations_items_item_id_response_logs_get**
> List[ObservationItemResponseLog] rest_v10_observations_items_item_id_response_logs_get(procore_company_id, item_id, project_id, page=page, per_page=per_page)

List Observation Item Response Logs

Returns a collection of Response Logs for a given Observation Item.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_response_log import ObservationItemResponseLog
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    item_id = 56 # int | Observation Item ID
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Item Response Logs
        api_response = api_instance.rest_v10_observations_items_item_id_response_logs_get(procore_company_id, item_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_item_id_response_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_item_id_response_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **item_id** | **int**| Observation Item ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationItemResponseLog]**](ObservationItemResponseLog.md)

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

# **rest_v10_observations_items_item_id_response_logs_post**
> ObservationItemResponseLog rest_v10_observations_items_item_id_response_logs_post(procore_company_id, item_id, observation_item_response_log_body, run_configurable_validations=run_configurable_validations)

Create Observation Item Response Log

Creates a new Response Log for a given Observation Item.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_response_log import ObservationItemResponseLog
from procore_sdk.models.observation_item_response_log_body import ObservationItemResponseLogBody
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    item_id = 56 # int | Observation Item ID
    observation_item_response_log_body = procore_sdk.ObservationItemResponseLogBody() # ObservationItemResponseLogBody | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Observation Items Category Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/observations#list-observation-category-configurable-field-sets) for a list of Observation Category configurable validations enabled on this project. (optional)

    try:
        # Create Observation Item Response Log
        api_response = api_instance.rest_v10_observations_items_item_id_response_logs_post(procore_company_id, item_id, observation_item_response_log_body, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_item_id_response_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_item_id_response_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **item_id** | **int**| Observation Item ID | 
 **observation_item_response_log_body** | [**ObservationItemResponseLogBody**](ObservationItemResponseLogBody.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Observation Items Category Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/observations#list-observation-category-configurable-field-sets) for a list of Observation Category configurable validations enabled on this project. | [optional] 

### Return type

[**ObservationItemResponseLog**](ObservationItemResponseLog.md)

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

# **rest_v10_observations_items_next_available_number_get**
> RestV10ObservationsItemsNextAvailableNumberGet200Response rest_v10_observations_items_next_available_number_get(procore_company_id, project_id)

Show Next Available Number for Observation Items

Returns the next available number for an observation item in the current Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_observations_items_next_available_number_get200_response import RestV10ObservationsItemsNextAvailableNumberGet200Response
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Next Available Number for Observation Items
        api_response = api_instance.rest_v10_observations_items_next_available_number_get(procore_company_id, project_id)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_next_available_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_next_available_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ObservationsItemsNextAvailableNumberGet200Response**](RestV10ObservationsItemsNextAvailableNumberGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Next available number returned successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_observations_items_post**
> ObservationItem1 rest_v10_observations_items_post(procore_company_id, body54, run_configurable_validations=run_configurable_validations)

Create Observation Item

Creates an Observation Item.

### Example


```python
import procore_sdk
from procore_sdk.models.body54 import Body54
from procore_sdk.models.observation_item1 import ObservationItem1
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body54 = procore_sdk.Body54() # Body54 | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Observation Items Category Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/observations#list-observation-category-configurable-field-sets) for a list of Observation Category configurable validations enabled on this project. (optional)

    try:
        # Create Observation Item
        api_response = api_instance.rest_v10_observations_items_post(procore_company_id, body54, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body54** | [**Body54**](Body54.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Observation Items Category Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/observations#list-observation-category-configurable-field-sets) for a list of Observation Category configurable validations enabled on this project. | [optional] 

### Return type

[**ObservationItem1**](ObservationItem1.md)

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

# **rest_v10_observations_items_send_unsent_post**
> List[ObservationItem] rest_v10_observations_items_send_unsent_post(procore_company_id, rest_v10_observations_items_send_unsent_post_request)

Send unsent Observation Items

Sends email notifications for unsent Observation Items.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item import ObservationItem
from procore_sdk.models.rest_v10_observations_items_send_unsent_post_request import RestV10ObservationsItemsSendUnsentPostRequest
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_observations_items_send_unsent_post_request = procore_sdk.RestV10ObservationsItemsSendUnsentPostRequest() # RestV10ObservationsItemsSendUnsentPostRequest | 

    try:
        # Send unsent Observation Items
        api_response = api_instance.rest_v10_observations_items_send_unsent_post(procore_company_id, rest_v10_observations_items_send_unsent_post_request)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_items_send_unsent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_items_send_unsent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_observations_items_send_unsent_post_request** | [**RestV10ObservationsItemsSendUnsentPostRequest**](RestV10ObservationsItemsSendUnsentPostRequest.md)|  | 

### Return type

[**List[ObservationItem]**](ObservationItem.md)

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

# **rest_v10_observations_potential_distribution_members_get**
> List[ObservationItemDefaultDistribution] rest_v10_observations_potential_distribution_members_get(procore_company_id, project_id, page=page, per_page=per_page)

List Observation Potential Distribution Members

Returns a collection of Potential Users for the Observations Distribution List

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_default_distribution import ObservationItemDefaultDistribution
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Potential Distribution Members
        api_response = api_instance.rest_v10_observations_potential_distribution_members_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_potential_distribution_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_potential_distribution_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationItemDefaultDistribution]**](ObservationItemDefaultDistribution.md)

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

# **rest_v10_observations_types_get**
> List[ObservationType] rest_v10_observations_types_get(procore_company_id, project_id, company_id, page=page, per_page=per_page)

List Observation Types

Returns a collection of Observation Types from the Project's Company or from the Company, depending on which query parameter is used.  NOTE: Though both query parameters are marked as required below, only one of the two needs to be passed in (i.e., if you pass in a project_id then you do not need to also pass in a company_id, and vice versa).

### Example


```python
import procore_sdk
from procore_sdk.models.observation_type import ObservationType
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Observation Types
        api_response = api_instance.rest_v10_observations_types_get(procore_company_id, project_id, company_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_observations_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_observations_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ObservationType]**](ObservationType.md)

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

# **rest_v10_projects_project_id_observations_items_id_delete**
> rest_v10_projects_project_id_observations_items_id_delete(procore_company_id, project_id, id)

Delete Observation Item

Sends the specified Observation Item to the recycle bin.

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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Observation ID

    try:
        # Delete Observation Item
        api_instance.rest_v10_projects_project_id_observations_items_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_observations_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Observation ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_observations_response_logs_get**
> List[ObservationItemResponseLog] rest_v10_projects_project_id_observations_response_logs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at)

List Observations Response Logs

Returns a collection of Response Logs scoped to viewable Observations  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item_response_log import ObservationItemResponseLog
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Observations Response Logs
        api_response = api_instance.rest_v10_projects_project_id_observations_response_logs_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_observations_response_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_observations_response_logs_get: %s\n" % e)
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

### Return type

[**List[ObservationItemResponseLog]**](ObservationItemResponseLog.md)

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

# **rest_v10_projects_project_id_recycle_bin_observations_items_get**
> List[ObservationItem] rest_v10_projects_project_id_recycle_bin_observations_items_get(procore_company_id, project_id, filters_type_id=filters_type_id, filters_trade_ids=filters_trade_ids, filters_assignee_id=filters_assignee_id, filters_status=filters_status, filters_priority=filters_priority, filters_location_id=filters_location_id, filters_created_by_id=filters_created_by_id, filters_assignee_company_id=filters_assignee_company_id, filters_updated_at=filters_updated_at)

List Recycled Observation Items

Returns a collection of Recycled Observation Items. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item import ObservationItem
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_type_id = [56] # List[int] | Return item(s) with the specified Observation Type ID. (optional)
    filters_trade_ids = [56] # List[int] | Array of Trade IDs. Returns item(s) with the specified Trade IDs. (optional)
    filters_assignee_id = [56] # List[int] | Return item(s) assigned to the specified User ID. (optional)
    filters_status = [56] # List[int] | Return item(s) with the specified status values. The mapping is as follows: ```   0: Initiated   1: Ready For reviewed   2: Not Accepted   3: Closed ``` (optional)
    filters_priority = ['filters_priority_example'] # List[str] | Return item(s) with the specified priorities.  (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_assignee_company_id = [56] # List[int] | Array of Vendor IDs. Returns item(s) where the assignee is associated to the specified Vendor ID. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Observation Items
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_observations_items_get(procore_company_id, project_id, filters_type_id=filters_type_id, filters_trade_ids=filters_trade_ids, filters_assignee_id=filters_assignee_id, filters_status=filters_status, filters_priority=filters_priority, filters_location_id=filters_location_id, filters_created_by_id=filters_created_by_id, filters_assignee_company_id=filters_assignee_company_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_type_id** | [**List[int]**](int.md)| Return item(s) with the specified Observation Type ID. | [optional] 
 **filters_trade_ids** | [**List[int]**](int.md)| Array of Trade IDs. Returns item(s) with the specified Trade IDs. | [optional] 
 **filters_assignee_id** | [**List[int]**](int.md)| Return item(s) assigned to the specified User ID. | [optional] 
 **filters_status** | [**List[int]**](int.md)| Return item(s) with the specified status values. The mapping is as follows: &#x60;&#x60;&#x60;   0: Initiated   1: Ready For reviewed   2: Not Accepted   3: Closed &#x60;&#x60;&#x60; | [optional] 
 **filters_priority** | [**List[str]**](str.md)| Return item(s) with the specified priorities.  | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_assignee_company_id** | [**List[int]**](int.md)| Array of Vendor IDs. Returns item(s) where the assignee is associated to the specified Vendor ID. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[ObservationItem]**](ObservationItem.md)

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

# **rest_v10_projects_project_id_recycle_bin_observations_items_id_get**
> ObservationItem1 rest_v10_projects_project_id_recycle_bin_observations_items_id_get(procore_company_id, project_id, id)

Show Recycled Observation

Returns the specified Recycled Observation.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item1 import ObservationItem1
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Observation ID

    try:
        # Show Recycled Observation
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_observations_items_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Observation ID | 

### Return type

[**ObservationItem1**](ObservationItem1.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch**
> ObservationItem1 rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch(procore_company_id, project_id, id)

Retrieve Recycled Observation

Retrieves the specified Observation from Recycle Bin.

### Example


```python
import procore_sdk
from procore_sdk.models.observation_item1 import ObservationItem1
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
    api_instance = procore_sdk.QualitySafetyObservationsObservationsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Observation ID

    try:
        # Retrieve Recycled Observation
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch(procore_company_id, project_id, id)
        print("The response of QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsObservationsApi->rest_v10_projects_project_id_recycle_bin_observations_items_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Observation ID | 

### Return type

[**ObservationItem1**](ObservationItem1.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

