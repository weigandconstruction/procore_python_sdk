# procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers/bulk_create | Bulk Create Action Plan Template Receivers
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers/bulk_destroy | Bulk Destroy Action Plan Template Receivers
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_get**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers | List Action Plan Template Receivers
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers/{id} | Delete Action Plan Template Receiver
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers/{id} | Show Action Plan Template Receiver
[**rest_v10_projects_project_id_action_plans_plan_template_receivers_post**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_template_receivers_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_receivers | Create Action Plan Template Receiver
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_template_receivers | List Recycled Action Plan Template Receivers
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get**](QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_template_receivers/{id} | Show Recycled Action Plan Template Receiver


# **rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post_request)

Bulk Create Action Plan Template Receivers

Bulk Create Action Plan Template Receivers for a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkCreatePostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkCreatePostRequest | 

    try:
        # Bulk Create Action Plan Template Receivers
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post_request)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkCreatePostRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete**
> rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete_request)

Bulk Destroy Action Plan Template Receivers

Bulk Destroy Action Plan Template Receivers from a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete_request import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkDestroyDeleteRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkDestroyDeleteRequest | 

    try:
        # Bulk Destroy Action Plan Template Receivers
        api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete_request)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_receivers_bulk_destroy_delete_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkDestroyDeleteRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversBulkDestroyDeleteRequest.md)|  | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_template_receivers_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)

List Action Plan Template Receivers

Returns all Action Plan Template Receivers for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Action Plan Template Receivers
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_template_id** | [**List[int]**](int.md)| Return section(s) associated with the specified Action Plan Template ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete**
> rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete(procore_company_id, project_id, id)

Delete Action Plan Template Receiver

Deletes an Action Plan Template Receiver

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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Receiver ID

    try:
        # Delete Action Plan Template Receiver
        api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Receiver ID | 

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get**
> RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get(procore_company_id, project_id, id)

Show Action Plan Template Receiver

Returns an Action Plan Template Receiver

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Receiver ID

    try:
        # Show Action Plan Template Receiver
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Receiver ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_receivers_post**
> RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_template_receivers_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request)

Create Action Plan Template Receiver

Creates an Action Plan Template Receiver for a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequest | 

    try:
        # Create Action Plan Template Receiver
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_receivers_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_action_plans_plan_template_receivers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversGet200ResponseInner.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)

List Recycled Action Plan Template Receivers

Returns all Recycled Action Plan Template Receivers for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Action Plan Template Receivers
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_template_id** | [**List[int]**](int.md)| Return section(s) associated with the specified Action Plan Template ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Template Receiver

Returns a Recycled Action Plan Template Receiver

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Receiver ID

    try:
        # Show Recycled Action Plan Template Receiver
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateReceiversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_receivers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Receiver ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateReceiversGet200ResponseInner.md)

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

