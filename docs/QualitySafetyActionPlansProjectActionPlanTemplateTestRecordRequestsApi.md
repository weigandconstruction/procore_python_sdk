# procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post**](QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi.md#rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_template_test_record_requests/bulk_create | Bulk Create Action Plan Template Test Record Requests
[**rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get**](QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi.md#rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_template_test_record_requests | List Project Action Plan Template Test Record Requests


# **rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post**
> List[List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner]] rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post_request, completion_mode=completion_mode)

Bulk Create Action Plan Template Test Record Requests

Creates Multiple Project Action Plan Template Test Record Requests for selected Template item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post200_response_inner_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePost200ResponseInnerInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post_request import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePostRequest() # RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePostRequest | 
    completion_mode = 'completion_mode_example' # str | Whether to update what can be or nothing if one can not be updated. Defaults to \"all_or_nothing\" (optional)

    try:
        # Bulk Create Action Plan Template Test Record Requests
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post_request, completion_mode=completion_mode)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi->rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi->rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_bulk_create_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePostRequest**](RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsBulkCreatePostRequest.md)|  | 
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

# **rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get(procore_company_id, project_id, filters_plan_template_item_id=filters_plan_template_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Project Action Plan Template Test Record Requests

List of all Project Action Plan Template Test Record Requests

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_template_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Template Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_template_id = [56] # List[int] | Return section(s) associated with the specified Action Plan Template ID(s). (optional)
    filters_type = ['filters_type_example'] # List[str] | Return item(s) associated with the specified Record Type(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Project Action Plan Template Test Record Requests
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get(procore_company_id, project_id, filters_plan_template_item_id=filters_plan_template_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_template_id=filters_plan_template_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi->rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansProjectActionPlanTemplateTestRecordRequestsApi->rest_v10_projects_project_id_action_plans_plan_template_test_record_requests_get: %s\n" % e)
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
 **filters_type** | [**List[str]**](str.md)| Return item(s) associated with the specified Record Type(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTemplateTestRecordRequestsGet200ResponseInner.md)

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

