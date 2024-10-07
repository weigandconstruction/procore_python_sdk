# procore_sdk.CoreCompanyCompanyScheduleApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_schedule_summary_get**](CoreCompanyCompanyScheduleApi.md#rest_v10_companies_company_id_schedule_summary_get) | **GET** /rest/v1.0/companies/{company_id}/schedule/summary | Return company schedule summary


# **rest_v10_companies_company_id_schedule_summary_get**
> RestV10CompaniesCompanyIdScheduleSummaryGet200Response rest_v10_companies_company_id_schedule_summary_get(procore_company_id, company_id, after, before, limit_per_day=limit_per_day, project_ids=project_ids, project_stage_ids=project_stage_ids, project_type_ids=project_type_ids, project_department_ids=project_department_ids, project_office_ids=project_office_ids, project_region_ids=project_region_ids, project_owner_type_ids=project_owner_type_ids, program_ids=program_ids, resource_ids=resource_ids, sort_key=sort_key, sort_dir=sort_dir)

Return company schedule summary

Returns a list of the number of tasks and calendar items per project for each day in the specified date range. Tasks and calendar items whose start - finish overlap with the specified date range are included in the sums.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_schedule_summary_get200_response import RestV10CompaniesCompanyIdScheduleSummaryGet200Response
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
    api_instance = procore_sdk.CoreCompanyCompanyScheduleApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    after = 'after_example' # str | Beginning of date range to filter by.
    before = 'before_example' # str | End of date range to filter by
    limit_per_day = 4 # int | Number of results to return per day (optional) (default to 4)
    project_ids = [56] # List[int] | Filter by project IDs (optional)
    project_stage_ids = [56] # List[int] | Filter by project stage IDs (optional)
    project_type_ids = [56] # List[int] | Filter by project type IDs (optional)
    project_department_ids = [56] # List[int] | Filter by project department IDs (optional)
    project_office_ids = [56] # List[int] | Filter by project office IDs (optional)
    project_region_ids = [56] # List[int] | Filter by project region IDs (optional)
    project_owner_type_ids = [56] # List[int] | Filter by project owner type IDs (optional)
    program_ids = [56] # List[int] | Filter by project program IDs (optional)
    resource_ids = [56] # List[int] | Filter by resource IDs (optional)
    sort_key = 'sort_key_example' # str | Sort results by a property of projects. Defaults to descending project_event_count. (optional)
    sort_dir = 'sort_dir_example' # str | Sort results in ascending or descending order (optional)

    try:
        # Return company schedule summary
        api_response = api_instance.rest_v10_companies_company_id_schedule_summary_get(procore_company_id, company_id, after, before, limit_per_day=limit_per_day, project_ids=project_ids, project_stage_ids=project_stage_ids, project_type_ids=project_type_ids, project_department_ids=project_department_ids, project_office_ids=project_office_ids, project_region_ids=project_region_ids, project_owner_type_ids=project_owner_type_ids, program_ids=program_ids, resource_ids=resource_ids, sort_key=sort_key, sort_dir=sort_dir)
        print("The response of CoreCompanyCompanyScheduleApi->rest_v10_companies_company_id_schedule_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyScheduleApi->rest_v10_companies_company_id_schedule_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **after** | **str**| Beginning of date range to filter by. | 
 **before** | **str**| End of date range to filter by | 
 **limit_per_day** | **int**| Number of results to return per day | [optional] [default to 4]
 **project_ids** | [**List[int]**](int.md)| Filter by project IDs | [optional] 
 **project_stage_ids** | [**List[int]**](int.md)| Filter by project stage IDs | [optional] 
 **project_type_ids** | [**List[int]**](int.md)| Filter by project type IDs | [optional] 
 **project_department_ids** | [**List[int]**](int.md)| Filter by project department IDs | [optional] 
 **project_office_ids** | [**List[int]**](int.md)| Filter by project office IDs | [optional] 
 **project_region_ids** | [**List[int]**](int.md)| Filter by project region IDs | [optional] 
 **project_owner_type_ids** | [**List[int]**](int.md)| Filter by project owner type IDs | [optional] 
 **program_ids** | [**List[int]**](int.md)| Filter by project program IDs | [optional] 
 **resource_ids** | [**List[int]**](int.md)| Filter by resource IDs | [optional] 
 **sort_key** | **str**| Sort results by a property of projects. Defaults to descending project_event_count. | [optional] 
 **sort_dir** | **str**| Sort results in ascending or descending order | [optional] 

### Return type

[**RestV10CompaniesCompanyIdScheduleSummaryGet200Response**](RestV10CompaniesCompanyIdScheduleSummaryGet200Response.md)

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

