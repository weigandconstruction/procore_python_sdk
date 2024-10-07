# procore_sdk.QualitySafetyActionPlansActionPlansApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plans_create_from_template_post**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_create_from_template_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plans/create_from_template | Create an Action Plan from a Plan Template.
[**rest_v10_projects_project_id_action_plans_plans_get**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plans | List Action Plans
[**rest_v10_projects_project_id_action_plans_plans_id_delete**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plans/{id} | Delete Action Plan
[**rest_v10_projects_project_id_action_plans_plans_id_get**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plans/{id} | Show Action Plan
[**rest_v10_projects_project_id_action_plans_plans_id_patch**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plans/{id} | Update Action Plan
[**rest_v10_projects_project_id_action_plans_plans_id_publish_post**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_id_publish_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plans/{id}/publish | Move Action Plan into \&quot;In Progress\&quot;
[**rest_v10_projects_project_id_action_plans_plans_id_revise_post**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_id_revise_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plans/{id}/revise | Move Action Plan back into \&quot;Draft\&quot;
[**rest_v10_projects_project_id_action_plans_plans_post**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_action_plans_plans_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plans | Create Action Plan
[**rest_v10_projects_project_id_recycle_bin_action_plans_plans_get**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plans_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plans | List Recycled Action Plan
[**rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plans/{id} | Show Recycled Action Plan
[**rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch**](QualitySafetyActionPlansActionPlansApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plans/{id}/restore | Restore Recycled Action Plan


# **rest_v10_projects_project_id_action_plans_plans_create_from_template_post**
> RestV10ProjectsProjectIdActionPlansPlansCreateFromTemplatePost201Response rest_v10_projects_project_id_action_plans_plans_create_from_template_post(procore_company_id, project_id, plan_template_id)

Create an Action Plan from a Plan Template.

Create an Action Plan from a Plan Template. In addition to creating the plan itself, this action will also create sections, items, assignees, references and test record requests from the template.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_create_from_template_post201_response import RestV10ProjectsProjectIdActionPlansPlansCreateFromTemplatePost201Response
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    plan_template_id = 56 # int | Action Plan Template ID

    try:
        # Create an Action Plan from a Plan Template.
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plans_create_from_template_post(procore_company_id, project_id, plan_template_id)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_create_from_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_create_from_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **plan_template_id** | **int**| Action Plan Template ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlansCreateFromTemplatePost201Response**](RestV10ProjectsProjectIdActionPlansPlansCreateFromTemplatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **rest_v10_projects_project_id_action_plans_plans_get**
> List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner] rest_v10_projects_project_id_action_plans_plans_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_manager_id=filters_manager_id, filters_plan_type_id=filters_plan_type_id, filters_template_id=filters_template_id, filters_updated_at=filters_updated_at, sort=sort)

List Action Plans

List of all Action Plans

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_manager_id = [56] # List[int] | Return item(s) with a specific Manager ID or a range of Manager ID(s). (optional)
    filters_plan_type_id = [56] # List[int] | Action Plan Type ID. Returns item(s) with the specified Action Plan Type ID(s). (optional)
    filters_template_id = [56] # List[int] | Return Action Plan(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Action Plans
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plans_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_manager_id=filters_manager_id, filters_plan_type_id=filters_plan_type_id, filters_template_id=filters_template_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_get: %s\n" % e)
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
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_manager_id** | [**List[int]**](int.md)| Return item(s) with a specific Manager ID or a range of Manager ID(s). | [optional] 
 **filters_plan_type_id** | [**List[int]**](int.md)| Action Plan Type ID. Returns item(s) with the specified Action Plan Type ID(s). | [optional] 
 **filters_template_id** | [**List[int]**](int.md)| Return Action Plan(s) associated with the specified Action Plan Template ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plans_id_delete**
> rest_v10_projects_project_id_action_plans_plans_id_delete(procore_company_id, project_id, id)

Delete Action Plan

Delete an Action Plan

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Delete Action Plan
        api_instance.rest_v10_projects_project_id_action_plans_plans_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

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

# **rest_v10_projects_project_id_action_plans_plans_id_get**
> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner rest_v10_projects_project_id_action_plans_plans_id_get(procore_company_id, project_id, id)

Show Action Plan

Details of a single Action Plan

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Show Action Plan
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plans_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plans_id_patch**
> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner rest_v10_projects_project_id_action_plans_plans_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plans_id_patch_request)

Update Action Plan

Update an Action Plan

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_id_patch_request import RestV10ProjectsProjectIdActionPlansPlansIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID
    rest_v10_projects_project_id_action_plans_plans_id_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlansIdPatchRequest() # RestV10ProjectsProjectIdActionPlansPlansIdPatchRequest | 

    try:
        # Update Action Plan
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plans_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plans_id_patch_request)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 
 **rest_v10_projects_project_id_action_plans_plans_id_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlansIdPatchRequest**](RestV10ProjectsProjectIdActionPlansPlansIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plans_id_publish_post**
> rest_v10_projects_project_id_action_plans_plans_id_publish_post(procore_company_id, project_id, id)

Move Action Plan into \"In Progress\"

Move Action Plan into \"In Progress\". This will set the status of the Plan to \"in_progress\". Once in this state, only specific updates to the Plan are allowed.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Move Action Plan into \"In Progress\"
        api_instance.rest_v10_projects_project_id_action_plans_plans_id_publish_post(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plans_id_revise_post**
> rest_v10_projects_project_id_action_plans_plans_id_revise_post(procore_company_id, project_id, id)

Move Action Plan back into \"Draft\"

Move Action Plan Back into \"Draft\". This will remove approver and receiver signatures from the Plan, and set the status to \"draft\". Once in this state, the Plan is able to be updated.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Move Action Plan back into \"Draft\"
        api_instance.rest_v10_projects_project_id_action_plans_plans_id_revise_post(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_id_revise_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plans_post**
> RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner rest_v10_projects_project_id_action_plans_plans_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plans_post_request)

Create Action Plan

Create an Action Plan

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_post_request import RestV10ProjectsProjectIdActionPlansPlansPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plans_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlansPostRequest() # RestV10ProjectsProjectIdActionPlansPlansPostRequest | 

    try:
        # Create Action Plan
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plans_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plans_post_request)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_action_plans_plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plans_post_request** | [**RestV10ProjectsProjectIdActionPlansPlansPostRequest**](RestV10ProjectsProjectIdActionPlansPlansPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_action_plans_plans_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plans_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_deleted_by_id=filters_deleted_by_id, filters_id=filters_id, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_manager_id=filters_manager_id, filters_plan_type_id=filters_plan_type_id, filters_updated_at=filters_updated_at, sort=sort)

List Recycled Action Plan

Returns a list of Recycled Action Plans for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_deleted_by_id = [56] # List[int] | Return item(s) with a specific Deleted By ID or a range of Deleted By IDs. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_manager_id = [56] # List[int] | Return item(s) with a specific Manager ID or a range of Manager ID(s). (optional)
    filters_plan_type_id = [56] # List[int] | Action Plan Type ID. Returns item(s) with the specified Action Plan Type ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Recycled Action Plan
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plans_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_deleted_by_id=filters_deleted_by_id, filters_id=filters_id, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_manager_id=filters_manager_id, filters_plan_type_id=filters_plan_type_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_recycle_bin_action_plans_plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_recycle_bin_action_plans_plans_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_deleted_by_id** | [**List[int]**](int.md)| Return item(s) with a specific Deleted By ID or a range of Deleted By IDs. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_manager_id** | [**List[int]**](int.md)| Return item(s) with a specific Manager ID or a range of Manager ID(s). | [optional] 
 **filters_plan_type_id** | [**List[int]**](int.md)| Action Plan Type ID. Returns item(s) with the specified Action Plan Type ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan

Returns the specified Recycled Action Plan.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plans_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Show Recycled Action Plan
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlansGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch(procore_company_id, project_id, id)

Restore Recycled Action Plan

Restores the specified Action Plan from Recycle Bin.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlansApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan ID

    try:
        # Restore Recycled Action Plan
        api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlansApi->rest_v10_projects_project_id_recycle_bin_action_plans_plans_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan ID | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

