# procore_sdk.QualitySafetyActionPlansActionPlanReceiversApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_receivers_get**](QualitySafetyActionPlansActionPlanReceiversApi.md#rest_v10_projects_project_id_action_plans_plan_receivers_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_receivers | List Action Plan Receivers


# **rest_v10_projects_project_id_action_plans_plan_receivers_get**
> List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner] rest_v10_projects_project_id_action_plans_plan_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)

List Action Plan Receivers

Returns all Action Plan Receivers for a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plans_get200_response_inner_plan_receivers_inner import RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanReceiversApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Action Plan Receivers
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_receivers_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyActionPlansActionPlanReceiversApi->rest_v10_projects_project_id_action_plans_plan_receivers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanReceiversApi->rest_v10_projects_project_id_action_plans_plan_receivers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_plan_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan ID(s) | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner]**](RestV10ProjectsProjectIdActionPlansPlansGet200ResponseInnerPlanReceiversInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

