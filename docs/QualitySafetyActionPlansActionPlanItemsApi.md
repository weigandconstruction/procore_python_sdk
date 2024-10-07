# procore_sdk.QualitySafetyActionPlansActionPlanItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_items/bulk_update | Bulk Update Action Plan Item
[**rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_items/create_from_item | Create a copy of the Action Plan Item in the Item&#39;s Section.
[**rest_v10_projects_project_id_action_plans_plan_items_get**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_items | List Action Plan Items
[**rest_v10_projects_project_id_action_plans_plan_items_id_delete**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_items/{id} | Delete Action Plan Item
[**rest_v10_projects_project_id_action_plans_plan_items_id_get**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_items/{id} | Show Action Plan Item
[**rest_v10_projects_project_id_action_plans_plan_items_id_move_post**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_id_move_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_items/{id}/move | Move Action Plan Item within or across Sections
[**rest_v10_projects_project_id_action_plans_plan_items_id_patch**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_items/{id} | Update Action Plan Item
[**rest_v10_projects_project_id_action_plans_plan_items_post**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_action_plans_plan_items_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_items | Create Action Plan Item
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_items | List Recycled Action Plan Items
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get**](QualitySafetyActionPlansActionPlanItemsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_items/{id} | Show Recycled Action Plan Item


# **rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch**
> List[RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request)

Bulk Update Action Plan Item

Updates multiple Action Plan Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest() # RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest | 

    try:
        # Bulk Update Action Plan Item
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest**](RestV10ProjectsProjectIdActionPlansPlanItemsBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post**
> RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request)

Create a copy of the Action Plan Item in the Item's Section.

Create a copy of the Action Plan Item in the Item's Section.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request import RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest() # RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest | 

    try:
        # Create a copy of the Action Plan Item in the Item's Section.
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest**](RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_items_get**
> List[RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_section_id=filters_plan_section_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, filters_query=filters_query, filters_due_at=filters_due_at, filters_assignee_party_id_or_role_id=filters_assignee_party_id_or_role_id, filters_attachment_id=filters_attachment_id, filters_drawing_revision_id=filters_drawing_revision_id, filters_file_version_id=filters_file_version_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_specification_section_id=filters_specification_section_id, filters_verification_method_id=filters_verification_method_id, filters_generic_tool_item_id=filters_generic_tool_item_id, filters_form_id=filters_form_id, filters_meeting_id=filters_meeting_id, filters_observation_item_id=filters_observation_item_id, filters_submittal_log_id=filters_submittal_log_id, filters_record_checklist_template_id=filters_record_checklist_template_id, filters_record_generic_tool_id=filters_record_generic_tool_id, filters_reference_type=filters_reference_type)

List Action Plan Items

Returns all Action Plan Items for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_section_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Section(s). (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_due_at = '2013-10-20T19:20:30+01:00' # datetime | Return item(s) due within the specified date range. (optional)
    filters_assignee_party_id_or_role_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Assignee party ID(s) or role ID(s) (optional)
    filters_attachment_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference attachment ID(s) (optional)
    filters_drawing_revision_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference drawing revision ID(s) (optional)
    filters_file_version_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference file version ID(s) (optional)
    filters_plan_test_record_request_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Test Record Request ID(s). (optional)
    filters_specification_section_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference specification section id ID(s) (optional)
    filters_verification_method_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Assignee verification method ID(s) (optional)
    filters_generic_tool_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference Generic Tool Item ID(s) (optional)
    filters_form_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference Form ID(s) (optional)
    filters_meeting_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference Meeting ID(s) (optional)
    filters_observation_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference Observation Item ID(s) (optional)
    filters_submittal_log_id = [56] # List[int] | Return item(s) associated with the specified Action Plan reference submittal log ID(s) (optional)
    filters_record_checklist_template_id = 56 # int | Return item(s) with the specified checklist template id. (optional)
    filters_record_generic_tool_id = 56 # int | Return item(s) with the specified Generic Tool ID. (optional)
    filters_reference_type = ['filters_reference_type_example'] # List[str] | Return item(s) associated with the specified Action Plan reference type(s) (optional)

    try:
        # List Action Plan Items
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_section_id=filters_plan_section_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, filters_query=filters_query, filters_due_at=filters_due_at, filters_assignee_party_id_or_role_id=filters_assignee_party_id_or_role_id, filters_attachment_id=filters_attachment_id, filters_drawing_revision_id=filters_drawing_revision_id, filters_file_version_id=filters_file_version_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_specification_section_id=filters_specification_section_id, filters_verification_method_id=filters_verification_method_id, filters_generic_tool_item_id=filters_generic_tool_item_id, filters_form_id=filters_form_id, filters_meeting_id=filters_meeting_id, filters_observation_item_id=filters_observation_item_id, filters_submittal_log_id=filters_submittal_log_id, filters_record_checklist_template_id=filters_record_checklist_template_id, filters_record_generic_tool_id=filters_record_generic_tool_id, filters_reference_type=filters_reference_type)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_get: %s\n" % e)
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
 **filters_plan_section_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Section(s). | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_due_at** | **datetime**| Return item(s) due within the specified date range. | [optional] 
 **filters_assignee_party_id_or_role_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Assignee party ID(s) or role ID(s) | [optional] 
 **filters_attachment_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference attachment ID(s) | [optional] 
 **filters_drawing_revision_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference drawing revision ID(s) | [optional] 
 **filters_file_version_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference file version ID(s) | [optional] 
 **filters_plan_test_record_request_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Test Record Request ID(s). | [optional] 
 **filters_specification_section_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference specification section id ID(s) | [optional] 
 **filters_verification_method_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Assignee verification method ID(s) | [optional] 
 **filters_generic_tool_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference Generic Tool Item ID(s) | [optional] 
 **filters_form_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference Form ID(s) | [optional] 
 **filters_meeting_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference Meeting ID(s) | [optional] 
 **filters_observation_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference Observation Item ID(s) | [optional] 
 **filters_submittal_log_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan reference submittal log ID(s) | [optional] 
 **filters_record_checklist_template_id** | **int**| Return item(s) with the specified checklist template id. | [optional] 
 **filters_record_generic_tool_id** | **int**| Return item(s) with the specified Generic Tool ID. | [optional] 
 **filters_reference_type** | [**List[str]**](str.md)| Return item(s) associated with the specified Action Plan reference type(s) | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_items_id_delete**
> rest_v10_projects_project_id_action_plans_plan_items_id_delete(procore_company_id, project_id, id)

Delete Action Plan Item

Deletes an Action Plan Item

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item ID

    try:
        # Delete Action Plan Item
        api_instance.rest_v10_projects_project_id_action_plans_plan_items_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_items_id_get**
> RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_items_id_get(procore_company_id, project_id, id)

Show Action Plan Item

Returns an Action Plan Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item ID

    try:
        # Show Action Plan Item
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_items_id_move_post**
> rest_v10_projects_project_id_action_plans_plan_items_id_move_post(procore_company_id, project_id, id, plan_section_id, next_plan_item_id=next_plan_item_id)

Move Action Plan Item within or across Sections

Move Action Plan Item within or across Action Plan Sections.

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item ID
    plan_section_id = 56 # int | ID of the Action Plan Section the Item will move within or to
    next_plan_item_id = 56 # int | ID of the Action Plan Item that will follow the newly moved Item. When moving an Item to the last position of the Section, do not provide this parameter. (optional)

    try:
        # Move Action Plan Item within or across Sections
        api_instance.rest_v10_projects_project_id_action_plans_plan_items_id_move_post(procore_company_id, project_id, id, plan_section_id, next_plan_item_id=next_plan_item_id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item ID | 
 **plan_section_id** | **int**| ID of the Action Plan Section the Item will move within or to | 
 **next_plan_item_id** | **int**| ID of the Action Plan Item that will follow the newly moved Item. When moving an Item to the last position of the Section, do not provide this parameter. | [optional] 

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

# **rest_v10_projects_project_id_action_plans_plan_items_id_patch**
> RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_items_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_items_id_patch_request)

Update Action Plan Item

Updates an Action Plan Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_id_patch_request import RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item ID
    rest_v10_projects_project_id_action_plans_plan_items_id_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest() # RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest | 

    try:
        # Update Action Plan Item
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_action_plans_plan_items_id_patch_request)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item ID | 
 **rest_v10_projects_project_id_action_plans_plan_items_id_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest**](RestV10ProjectsProjectIdActionPlansPlanItemsIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_items_post**
> RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_items_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_post_request)

Create Action Plan Item

Creates an Action Plan Item for a given Action Plan Section.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_post_request import RestV10ProjectsProjectIdActionPlansPlanItemsPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_items_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanItemsPostRequest() # RestV10ProjectsProjectIdActionPlansPlanItemsPostRequest | 

    try:
        # Create Action Plan Item
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_items_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_items_post_request)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_action_plans_plan_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_items_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanItemsPostRequest**](RestV10ProjectsProjectIdActionPlansPlanItemsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_section_id=filters_plan_section_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, filters_query=filters_query)

List Recycled Action Plan Items

Returns all Recycled Action Plan Items for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_section_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Section(s). (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)

    try:
        # List Recycled Action Plan Items
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_section_id=filters_plan_section_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at, filters_query=filters_query)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get: %s\n" % e)
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
 **filters_plan_section_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Section(s). | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Item

Returns a Specific Recycled Action Plan Item for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Item ID

    try:
        # Show Recycled Action Plan Item
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanItemsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Item ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanItemsGet200ResponseInner.md)

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

