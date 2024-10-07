# procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/bulk_create | Bulk Create Action Plan Item Assignees
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/bulk_update | Bulk Update Action Plan Item Assignees
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_get**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees | List Action Plan Item Assignees
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{id} | Delete Action Plan Item Assignee
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{id} | Show Action Plan Item Assignee
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees/{id} | Update Action Plan Item Assignee
[**rest_v10_projects_project_id_action_plans_plan_item_assignees_post**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_item_assignees_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_item_assignees | Create Action Plan Item Assignee
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_item_assignees | List Recycled Action Plan Item Assignees
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get**](QualitySafetyActionPlansActionPlanItemAssigneesApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_item_assignees/{id} | Show Recycled Action Plan Item Assignee


# **rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]] rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request, completion_mode=completion_mode)

Bulk Create Action Plan Item Assignees

Creates multiple Action Plan Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Create Action Plan Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkCreatePostRequest.md)|  | 
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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]] rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch_request, completion_mode=completion_mode)

Bulk Update Action Plan Item Assignees

Updates multiple Action Plan Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkUpdatePatchRequest() # RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkUpdatePatchRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Update Action Plan Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_item_assignees_bulk_update_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkUpdatePatchRequest**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesBulkUpdatePatchRequest.md)|  | 
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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_get**
> List[RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_item_assignees_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Action Plan Item Assignees

List of all Action Plan Item Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Action Plan Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_plan_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Item ID(s). | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete**
> rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete(procore_company_id, project_id, id)

Delete Action Plan Item Assignee

Delete an Action Plan Item Assignee

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item Assignee ID

    try:
        # Delete Action Plan Item Assignee
        api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item Assignee ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get**
> RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get(procore_company_id, project_id, id)

Show Action Plan Item Assignee

Details of a single Action Plan Item Assignee

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item Assignee ID

    try:
        # Show Action Plan Item Assignee
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item Assignee ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch**
> RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request)

Update Action Plan Item Assignee

Updates a single Action Plan Item Assignee

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item Assignee ID
    rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequest() # RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequest | 

    try:
        # Update Action Plan Item Assignee
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item Assignee ID | 
 **rest_v10_projects_project_id_action_plans_plan_item_assignees_id_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequest**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_item_assignees_post**
> RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_item_assignees_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request)

Create Action Plan Item Assignee

Create an Action Plan Item Assignee. NOTE: Though both body `party_id` and `role` parameters are marked as required below, at least one of the two needs to be passed in (i.e., if you pass in a `role` then you do not need to also pass in a `party_id`, and vice versa, though you can pass in both parameters)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request import RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequest() # RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequest | 

    try:
        # Create Action Plan Item Assignee
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_item_assignees_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_item_assignees_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_item_assignees_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequest**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemAssigneesGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Recycled Action Plan Item Assignees

List of all Recycled Action Plan Item Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Recycled Action Plan Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_plan_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Item ID(s). | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Item Assignee

Details of a single Recycled Action Plan Item Assignee

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item Assignee ID

    try:
        # Show Recycled Action Plan Item Assignee
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemAssigneesApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_item_assignees_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item Assignee ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemAssigneesGet200ResponseInner.md)

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

