# procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers/bulk_create | Bulk Create Action Plan Template Approvers
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers/bulk_destroy | Bulk Destroy Action Plan Template Approvers
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_get**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers | List Action Plan Template Approvers
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers/{id} | Delete Action Plan Template Approver
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers/{id} | Show Action Plan Template Approver
[**rest_v10_projects_project_id_action_plans_plan_template_approvers_post**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_action_plans_plan_template_approvers_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_approvers | Create Action Plan Template Approver
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_template_approvers | List Recycled Action Plan Template Approvers
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get**](QualitySafetyActionPlansProjectActionPlanTemplateApproversApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_template_approvers/{id} | Show Recycled Action Plan Template Approver


# **rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post_request)

Bulk Create Action Plan Template Approvers

Bulk Create Action Plan Template Approvers for a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkCreatePostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkCreatePostRequest | 

    try:
        # Bulk Create Action Plan Template Approvers
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post_request)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkCreatePostRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete**
> rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete_request)

Bulk Destroy Action Plan Template Approvers

Bulk Destroy Action Plan Template Approvers from a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete_request import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkDestroyDeleteRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkDestroyDeleteRequest | 

    try:
        # Bulk Destroy Action Plan Template Approvers
        api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete_request)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_approvers_bulk_destroy_delete_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkDestroyDeleteRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversBulkDestroyDeleteRequest.md)|  | 

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

# **rest_v10_projects_project_id_action_plans_plan_template_approvers_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_approvers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id)

List Action Plan Template Approvers

Returns all Action Plan Template Approvers for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)

    try:
        # List Action Plan Template Approvers
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_get: %s\n" % e)
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

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete**
> rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete(procore_company_id, project_id, id)

Delete Action Plan Template Approver

Deletes an Action Plan Template Approver

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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Approver ID

    try:
        # Delete Action Plan Template Approver
        api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Approver ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get**
> RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get(procore_company_id, project_id, id)

Show Action Plan Template Approver

Returns an Action Plan Template Approver

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Approver ID

    try:
        # Show Action Plan Template Approver
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Approver ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_approvers_post**
> RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_template_approvers_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_post_request)

Create Action Plan Template Approver

Creates an Action Plan Template Approver for a given Project Action Plan Template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_approvers_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateApproversPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_approvers_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateApproversPostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateApproversPostRequest | 

    try:
        # Create Action Plan Template Approver
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_approvers_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_approvers_post_request)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_action_plans_plan_template_approvers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_approvers_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateApproversPostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)

List Recycled Action Plan Template Approvers

Returns all Recycled Action Plan Template Approvers for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Action Plan Template Approvers
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get: %s\n" % e)
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

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Template Approver

Returns a Recycled Action Plan Template Approver

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateApproversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Template Approver ID

    try:
        # Show Recycled Action Plan Template Approver
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateApproversApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_template_approvers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Template Approver ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTemplateApproversGet200ResponseInner.md)

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

