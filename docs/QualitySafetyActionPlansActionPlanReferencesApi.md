# procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_references/bulk_create | Bulk Create Action Plan References
[**rest_v10_projects_project_id_action_plans_plan_references_get**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_action_plans_plan_references_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_references | List Action Plan References
[**rest_v10_projects_project_id_action_plans_plan_references_id_delete**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_action_plans_plan_references_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_references/{id} | Delete Action Plan Reference
[**rest_v10_projects_project_id_action_plans_plan_references_id_get**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_action_plans_plan_references_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_references/{id} | Show Action Plan Reference
[**rest_v10_projects_project_id_action_plans_plan_references_post**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_action_plans_plan_references_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_references | Create Action Plan Reference
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_references | List Recycled Action Plan References
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get**](QualitySafetyActionPlansActionPlanReferencesApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_references/{id} | Show Recycled Action Plan Reference


# **rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]] rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post_request, completion_mode=completion_mode)

Bulk Create Action Plan References

Creates multiple Action References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanReferencesBulkCreatePostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanReferencesBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanReferencesBulkCreatePostRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Create Action Plan References
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_references_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanReferencesBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanReferencesBulkCreatePostRequest.md)|  | 
 **completion_mode** | **str**| Whether to update what can be or nothing if one can not be updated. Defaults to \&quot;all_or_nothing\&quot; | [optional] 

### Return type

**List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]]**

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_references_get**
> List[RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_references_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_item_id=filters_plan_item_id, filters_plan_id=filters_plan_id, sort=sort)

List Action Plan References

List of all Action Plan References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Action Plan References
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_references_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_item_id=filters_plan_item_id, filters_plan_id=filters_plan_id, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_plan_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Item ID(s). | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_references_id_delete**
> rest_v10_projects_project_id_action_plans_plan_references_id_delete(procore_company_id, project_id, id)

Delete Action Plan Reference

Deletes an Action Plan Reference

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Reference ID

    try:
        # Delete Action Plan Reference
        api_instance.rest_v10_projects_project_id_action_plans_plan_references_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Reference ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_references_id_get**
> RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_references_id_get(procore_company_id, project_id, id)

Show Action Plan Reference

Returns an Action Plan Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Reference ID

    try:
        # Show Action Plan Reference
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_references_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Reference ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_references_post**
> RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_references_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_references_post_request)

Create Action Plan Reference

Create an Action Plan Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_post_request import RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_references_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest() # RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest | 

    try:
        # Create Action Plan Reference
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_references_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_references_post_request)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_action_plans_plan_references_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_references_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest**](RestV10ProjectsProjectIdActionPlansPlanReferencesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get**
> List[RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_item_id=filters_plan_item_id, filters_plan_id=filters_plan_id, sort=sort)

List Recycled Action Plan References

List of all Recycled Action Plan References

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Recycled Action Plan References
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_updated_at=filters_updated_at, filters_plan_item_id=filters_plan_item_id, filters_plan_id=filters_plan_id, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_plan_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Item ID(s). | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get**
> RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Reference

Returns a Recycled Action Plan Reference

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_references_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReferencesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Reference ID

    try:
        # Show Recycled Action Plan Reference
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReferencesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_references_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Reference ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanReferencesGet200ResponseInner.md)

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

