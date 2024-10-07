# procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post**](QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_item_assignees/bulk_create | Bulk Create Action Plan Template Item Assignees
[**rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch**](QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_template_item_assignees/bulk_update | Bulk update Action Plan Template Item Assignees
[**rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get**](QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi.md#rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_item_assignees | List Action Plan Template Item Assignees


# **rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post_request, completion_mode=completion_mode)

Bulk Create Action Plan Template Item Assignees

Creates multiple Action Plan Template Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePostRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Create Action Plan Template Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePostRequest.md)|  | 
 **completion_mode** | **str**| Whether to update what can be or nothing if one can not be updated. Defaults to \&quot;all_or_nothing\&quot; | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkCreatePost200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request, completion_mode=completion_mode)

Bulk update Action Plan Template Item Assignees

Update multiple Action Plan Template Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk update Action Plan Template Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_item_assignees_bulk_update_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatchRequest.md)|  | 
 **completion_mode** | **str**| Whether to update what can be or nothing if one can not be updated. Defaults to \&quot;all_or_nothing\&quot; | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesBulkUpdatePatch200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get(procore_company_id, project_id, filters_plan_template_item_id=filters_plan_template_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Action Plan Template Item Assignees

List of all Action Plan Template Item Assignees

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_template_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Template Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Action Plan Template Item Assignees
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get(procore_company_id, project_id, filters_plan_template_item_id=filters_plan_template_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemAssigneesApi->rest_v10_projects_project_id_action_plans_plan_template_item_assignees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_plan_template_item_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Template Item ID(s). | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_template_id** | [**List[int]**](int.md)| Return section(s) associated with the specified Action Plan Template ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemAssigneesGet200ResponseInner.md)

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

