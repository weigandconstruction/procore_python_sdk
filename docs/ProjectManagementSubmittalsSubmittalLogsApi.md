# procore_sdk.ProjectManagementSubmittalsSubmittalLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_submittal_logs_get**](ProjectManagementSubmittalsSubmittalLogsApi.md#rest_v10_submittal_logs_get) | **GET** /rest/v1.0/submittal_logs | List Submittals
[**rest_v10_submittal_logs_id_get**](ProjectManagementSubmittalsSubmittalLogsApi.md#rest_v10_submittal_logs_id_get) | **GET** /rest/v1.0/submittal_logs/{id} | Show Submittal


# **rest_v10_submittal_logs_get**
> List[RestV10SubmittalLogsGet200ResponseInner] rest_v10_submittal_logs_get(procore_company_id, project_id, filters_approved_id=filters_approved_id, filters_ball_in_court=filters_ball_in_court, filters_date_range=filters_date_range, filters_due_by=filters_due_by, filters_end_date=filters_end_date, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_only_current_revision=filters_only_current_revision, filters_query=filters_query, filters_received_from_id=filters_received_from_id, filters_response=filters_response, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_spec_division=filters_spec_division, filters_spec_section_id=filters_spec_section_id, filters_start_date=filters_start_date, filters_status=filters_status, filters_submittal_type=filters_submittal_type, filters_submittal_package_id=filters_submittal_package_id, page=page, per_page=per_page)

List Submittals

This is a deprecated endpoint. Please use /submittals endpoint.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_submittal_logs_get200_response_inner import RestV10SubmittalLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_approved_id = 'filters_approved_id_example' # str |  (optional)
    filters_ball_in_court = 'filters_ball_in_court_example' # str |  (optional)
    filters_date_range = 'filters_date_range_example' # str |  (optional)
    filters_due_by = '2013-10-20' # date |  (optional)
    filters_end_date = '2013-10-20' # date |  (optional)
    filters_include_sublocations = False # bool | Use together with `filters[location_id]`  (optional) (default to False)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_only_current_revision = 56 # int |  (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    filters_received_from_id = 56 # int | Received From ID (optional)
    filters_response = 'filters_response_example' # str |  (optional)
    filters_responsible_contractor_id = 56 # int | Responsible Contractor ID (optional)
    filters_spec_division = 'filters_spec_division_example' # str |  (optional)
    filters_spec_section_id = 'filters_spec_section_id_example' # str |  (optional)
    filters_start_date = '2013-10-20' # date |  (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_submittal_type = 'filters_submittal_type_example' # str |  (optional)
    filters_submittal_package_id = [56] # List[int] | Array of Submittal Package IDs. Returns item(s) associated with the specified Submittal Package IDs. A single integer value is also accepted. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Submittals
        api_response = api_instance.rest_v10_submittal_logs_get(procore_company_id, project_id, filters_approved_id=filters_approved_id, filters_ball_in_court=filters_ball_in_court, filters_date_range=filters_date_range, filters_due_by=filters_due_by, filters_end_date=filters_end_date, filters_include_sublocations=filters_include_sublocations, filters_location_id=filters_location_id, filters_only_current_revision=filters_only_current_revision, filters_query=filters_query, filters_received_from_id=filters_received_from_id, filters_response=filters_response, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_spec_division=filters_spec_division, filters_spec_section_id=filters_spec_section_id, filters_start_date=filters_start_date, filters_status=filters_status, filters_submittal_type=filters_submittal_type, filters_submittal_package_id=filters_submittal_package_id, page=page, per_page=per_page)
        print("The response of ProjectManagementSubmittalsSubmittalLogsApi->rest_v10_submittal_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalLogsApi->rest_v10_submittal_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_approved_id** | **str**|  | [optional] 
 **filters_ball_in_court** | **str**|  | [optional] 
 **filters_date_range** | **str**|  | [optional] 
 **filters_due_by** | **date**|  | [optional] 
 **filters_end_date** | **date**|  | [optional] 
 **filters_include_sublocations** | **bool**| Use together with &#x60;filters[location_id]&#x60;  | [optional] [default to False]
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_only_current_revision** | **int**|  | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **filters_received_from_id** | **int**| Received From ID | [optional] 
 **filters_response** | **str**|  | [optional] 
 **filters_responsible_contractor_id** | **int**| Responsible Contractor ID | [optional] 
 **filters_spec_division** | **str**|  | [optional] 
 **filters_spec_section_id** | **str**|  | [optional] 
 **filters_start_date** | **date**|  | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_submittal_type** | **str**|  | [optional] 
 **filters_submittal_package_id** | [**List[int]**](int.md)| Array of Submittal Package IDs. Returns item(s) associated with the specified Submittal Package IDs. A single integer value is also accepted. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10SubmittalLogsGet200ResponseInner]**](RestV10SubmittalLogsGet200ResponseInner.md)

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
**401** | Unauthorized access |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_submittal_logs_id_get**
> RestV10SubmittalLogsIdGet200Response rest_v10_submittal_logs_id_get(procore_company_id, id, project_id)

Show Submittal

This is a deprecated endpoint. Please use /submittals/{id} endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response import RestV10SubmittalLogsIdGet200Response
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
    api_instance = procore_sdk.ProjectManagementSubmittalsSubmittalLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of Submittal
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Submittal
        api_response = api_instance.rest_v10_submittal_logs_id_get(procore_company_id, id, project_id)
        print("The response of ProjectManagementSubmittalsSubmittalLogsApi->rest_v10_submittal_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsSubmittalLogsApi->rest_v10_submittal_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of Submittal | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10SubmittalLogsIdGet200Response**](RestV10SubmittalLogsIdGet200Response.md)

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
**401** | Unauthorized access |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

