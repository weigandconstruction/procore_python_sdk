# procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_action_plans_plan_test_records_get**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_action_plans_plan_test_records_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_test_records | List Action Plan Test Records
[**rest_v10_projects_project_id_action_plans_plan_test_records_id_delete**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_action_plans_plan_test_records_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/action_plans/plan_test_records/{id} | Delete Action Plan Test Record
[**rest_v10_projects_project_id_action_plans_plan_test_records_id_get**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_action_plans_plan_test_records_id_get) | **GET** /rest/v1.0/projects/{project_id}/action_plans/plan_test_records/{id} | View an Action Plan Test Record
[**rest_v10_projects_project_id_action_plans_plan_test_records_post**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_action_plans_plan_test_records_post) | **POST** /rest/v1.0/projects/{project_id}/action_plans/plan_test_records | Create Action Plan Test Record
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_test_records | List Recyled Action Plan Test Records
[**rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get**](QualitySafetyActionPlansActionPlanTestRecordsApi.md#rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/action_plans/plan_test_records/{id} | Show Recycled Action Plan Test Record


# **rest_v10_projects_project_id_action_plans_plan_test_records_get**
> List[RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner] rest_v10_projects_project_id_action_plans_plan_test_records_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Action Plan Test Records

List of all Action Plan Test Records

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_plan_test_record_request_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Test Record Request ID(s). (optional)
    filters_type = ['filters_type_example'] # List[str] | Return item(s) associated with the specified Action Plan Test Record Types. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Action Plan Test Records
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_test_records_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_get: %s\n" % e)
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
 **filters_plan_test_record_request_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Test Record Request ID(s). | [optional] 
 **filters_type** | [**List[str]**](str.md)| Return item(s) associated with the specified Action Plan Test Record Types. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner]**](RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_test_records_id_delete**
> rest_v10_projects_project_id_action_plans_plan_test_records_id_delete(procore_company_id, project_id, id)

Delete Action Plan Test Record

Deletes an Action Plan Test Record

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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Test Record ID

    try:
        # Delete Action Plan Test Record
        api_instance.rest_v10_projects_project_id_action_plans_plan_test_records_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Test Record ID | 

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

# **rest_v10_projects_project_id_action_plans_plan_test_records_id_get**
> RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_test_records_id_get(procore_company_id, project_id, id)

View an Action Plan Test Record

Returns the details of an Action Plan Test Record

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Test Record ID

    try:
        # View an Action Plan Test Record
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_test_records_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Test Record ID | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_action_plans_plan_test_records_post**
> RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner rest_v10_projects_project_id_action_plans_plan_test_records_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_test_records_post_request)

Create Action Plan Test Record

Create an Action Plan Test Record  Action Plan Test Records can have one of the following payload formats (checklist_id, form_id, generic_tool_id, meeting_id, submittal_log_id, observation_item_id, attachment) Attachment payloads must be a binary file or contain an attachment_id.  A specific Action Plan Test Record Type can only leverage its corresponding format.  *For instance, Checklist Test Records can only leverage checklist_id while Attachment/Photo Test Records can only leverage attachment.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_test_records_post_request import RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_action_plans_plan_test_records_post_request = procore_sdk.RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest() # RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest | 

    try:
        # Create Action Plan Test Record
        api_response = api_instance.rest_v10_projects_project_id_action_plans_plan_test_records_post(procore_company_id, project_id, rest_v10_projects_project_id_action_plans_plan_test_records_post_request)
        print("The response of QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_action_plans_plan_test_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_action_plans_plan_test_records_post_request** | [**RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest**](RestV10ProjectsProjectIdActionPlansPlanTestRecordsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner**](RestV10ProjectsProjectIdActionPlansPlanTestRecordsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get**
> List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)

List Recyled Action Plan Test Records

List of all Recycled Action Plan Test Records

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_plan_item_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Item ID(s). (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_plan_id = [56] # List[int] | Return item(s) associated with the specified Action Plan ID(s) (optional)
    filters_plan_test_record_request_id = [56] # List[int] | Return item(s) associated with the specified Action Plan Test Record Request ID(s). (optional)
    filters_type = ['filters_type_example'] # List[str] | Return item(s) associated with the specified Action Plan Test Record Type(s). (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Recyled Action Plan Test Records
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get(procore_company_id, project_id, filters_plan_item_id=filters_plan_item_id, filters_created_at=filters_created_at, filters_id=filters_id, filters_plan_id=filters_plan_id, filters_plan_test_record_request_id=filters_plan_test_record_request_id, filters_type=filters_type, filters_updated_at=filters_updated_at, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get: %s\n" % e)
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
 **filters_plan_test_record_request_id** | [**List[int]**](int.md)| Return item(s) associated with the specified Action Plan Test Record Request ID(s). | [optional] 
 **filters_type** | [**List[str]**](str.md)| Return item(s) associated with the specified Action Plan Test Record Type(s). | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner]**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get**
> RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get(procore_company_id, project_id, id)

Show Recycled Action Plan Test Record

Returns a Recycled Action Plan Test Record

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_get200_response_inner import RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyActionPlansActionPlanTestRecordsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action Plan Test Record ID

    try:
        # Show Recycled Action Plan Test Record
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyActionPlansActionPlanTestRecordsApi->rest_v10_projects_project_id_recycle_bin_action_plans_plan_test_records_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action Plan Test Record ID | 

### Return type

[**RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner**](RestV10ProjectsProjectIdRecycleBinActionPlansPlanTestRecordsGet200ResponseInner.md)

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

