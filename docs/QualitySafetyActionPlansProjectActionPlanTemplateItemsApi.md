# procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch**](QualitySafetyActionPlansProjectActionPlanTemplateItemsApi.md#rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/action_plans/plan_template_items/bulk_update | Bulk Update Action Plan Template Item
[**rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post**](QualitySafetyActionPlansProjectActionPlanTemplateItemsApi.md#rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_items/create_from_item | Create a copy of the Action Plan Template Item in the Item&#39;s Section.
[**rest_v10_projects_project_id_action_plans_plan_template_items_get**](QualitySafetyActionPlansProjectActionPlanTemplateItemsApi.md#rest_v10_projects_project_id_action_plans_plan_template_items_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_items | List Project Action Plan Template Items


# **rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner]] rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request, completion_mode=completion_mode)

Bulk Update Action Plan Template Item

Updates multiple Action Plan Template Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch200_response_inner_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Update Action Plan Template Item
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_items_bulk_update_patch_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatchRequest.md)|  | 
 **completion_mode** | **str**| Whether to update what can be or nothing if one can not be updated. Defaults to \&quot;all_or_nothing\&quot; | [optional] 

### Return type

**List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemsBulkUpdatePatch200ResponseInnerInner]]**

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

# **rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post**
> RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post_request)

Create a copy of the Action Plan Template Item in the Item's Section.

Create a copy of the Action Plan Template Item in the Item's Section.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsCreateFromItemPostRequest
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateItemsCreateFromItemPostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateItemsCreateFromItemPostRequest | 

    try:
        # Create a copy of the Action Plan Template Item in the Item's Section.
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post_request)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_items_create_from_item_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateItemsCreateFromItemPostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemsCreateFromItemPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_template_items_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_plan_template_section_id=filters_plan_template_section_id, filters_updated_at=filters_updated_at, sort=sort)

List Project Action Plan Template Items

Gets the list of Project Action Plan Template Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_items_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = 56 # int | Return item(s) associated with the specified Action Plan Template ID. (optional)
    filters_plan_template_section_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Template Section ID(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Project Action Plan Template Items
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_items_get(procore_company_id, project_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_plan_template_section_id=filters_plan_template_section_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateItemsApi->rest_v10_projects_project_id_action_plans_plan_template_items_get: %s\n" % e)
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
 **filters_plan_template_id** | **int**| Return item(s) associated with the specified Action Plan Template ID. | [optional] 
 **filters_plan_template_section_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Template Section ID(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateItemsGet200ResponseInner.md)

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

