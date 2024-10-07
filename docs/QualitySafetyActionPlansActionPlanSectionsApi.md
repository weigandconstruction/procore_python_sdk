# procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_sections/create_from_section | Create a copy of the Action Plan Section in the Action Plan of the Section.
[**rest_v10_projects_project_id_action_plans_plan_sections_get**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_sections | List Action Plan Sections
[**rest_v10_projects_project_id_action_plans_plan_sections_id_delete**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_sections/{id} | Delete Action Plan Section
[**rest_v10_projects_project_id_action_plans_plan_sections_id_get**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_sections/{id} | Show Action Plan Section
[**rest_v10_projects_project_id_action_plans_plan_sections_id_move_post**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_id_move_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_sections/{id}/move | Move Action Plan Section
[**rest_v10_projects_project_id_action_plans_plan_sections_id_patch**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_sections/{id} | Update Action Plan Section
[**rest_v10_projects_project_id_action_plans_plan_sections_post**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_action_plans_plan_sections_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_sections | Create Action Plan Section
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_sections | List Recycled Action Plan Sections
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get**](QualitySafetyActionPlansActionPlanSectionsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_sections/{id} | Show Recycled Action Plan Section


# **rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post**
> RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post_request)

Create a copy of the Action Plan Section in the Action Plan of the Section.

Create a copy of the Action Plan Section in the Action Plan of the Section.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post_request import RestV10ProjectsProjectIdActionPlansPlanSectionsCreateFromSectionPostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanSectionsCreateFromSectionPostRequest() # RestV10ProjectsProjectIdActionPlansPlanSectionsCreateFromSectionPostRequest | 

    try:
        # Create a copy of the Action Plan Section in the Action Plan of the Section.
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post_request)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_sections_create_from_section_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanSectionsCreateFromSectionPostRequest**](RestV10ProjectsProjectIdActionPlansPlanSectionsCreateFromSectionPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_sections_get**
> List[RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)

List Action Plan Sections

Returns all Action Plan Sections for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Action Plan Sections
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_get: %s\n" % e)
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
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_sections_id_delete**
> rest_v10_projects_project_id_action_plans_plan_sections_id_delete(procore_company_id, project_id, id)

Delete Action Plan Section

Deletes an Action Plan Section

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Section ID

    try:
        # Delete Action Plan Section
        api_instance.rest_v10_projects_project_id_action_plans_plan_sections_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Section ID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_sections_id_get**
> RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_sections_id_get(procore_company_id, project_id, id)

Show Action Plan Section

Returns an Action Plan Section

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Section ID

    try:
        # Show Action Plan Section
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_sections_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Section ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_sections_id_move_post**
> rest_v10_projects_project_id_action_plans_plan_sections_id_move_post(procore_company_id, project_id, id, next_section_id=next_section_id)

Move Action Plan Section

Moves the Action Plan Section.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Section ID
    next_section_id = 56 # int | ID of the Action Plan Section that will follow the newly moved Section. When moving an Action Plan Section to the last position of the Action Plan, do not provide this parameter. (optional)

    try:
        # Move Action Plan Section
        api_instance.rest_v10_projects_project_id_action_plans_plan_sections_id_move_post(procore_company_id, project_id, id, next_section_id=next_section_id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Section ID | 
 **next_section_id** | **int**| ID of the Action Plan Section that will follow the newly moved Section. When moving an Action Plan Section to the last position of the Action Plan, do not provide this parameter. | [optional] 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_action_plans_plan_sections_id_patch**
> RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_sections_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_sections_id_patch_request)

Update Action Plan Section

Updates an Action Plan Section

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_id_patch_request import RestV10ProjectsProjectIdActionPlansPlanSectionsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Section ID
    rest_v10_projects_project_id_action_plans_plan_sections_id_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanSectionsIdPatchRequest() # RestV10ProjectsProjectIdActionPlansPlanSectionsIdPatchRequest | 

    try:
        # Update Action Plan Section
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_sections_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_sections_id_patch_request)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Section ID | 
 **rest_v10_projects_project_id_action_plans_plan_sections_id_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanSectionsIdPatchRequest**](RestV10ProjectsProjectIdActionPlansPlanSectionsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_sections_post**
> RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_sections_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_sections_post_request)

Create Action Plan Section

Creates an Action Plan Section for a given Action Plan.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_post_request import RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_sections_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest() # RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest | 

    try:
        # Create Action Plan Section
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_sections_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_sections_post_request)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_action_plans_plan_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_sections_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest**](RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanSectionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)

List Recycled Action Plan Sections

Returns all Recycled Action Plan Sections for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Action Plan Sections
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get: %s\n" % e)
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
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Section

Returns a Recycled Action Plan Section

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Section ID

    try:
        # Show Recycled Action Plan Section
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanSectionsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_sections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Section ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanSectionsGet200ResponseInner.md)

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

