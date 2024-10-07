# procore_sdk.QualitySafetyInspectionsChecklistScheduleChangeHistoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get**](QualitySafetyInspectionsChecklistScheduleChangeHistoriesApi.md#rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/{schedule_id}/change_history | List Checklist Schedule Change Histories


# **rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get**
> List[ChecklistScheduleChangeHistory] rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get(procore_company_id, project_id, schedule_id, page=page, per_page=per_page)

List Checklist Schedule Change Histories

Lists Checklist Schedule Change Histories for given Project and Schedule

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule_change_history import ChecklistScheduleChangeHistory
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleChangeHistoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_id = 56 # int | Checklist Schedule ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Checklist Schedule Change Histories
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get(procore_company_id, project_id, schedule_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsChecklistScheduleChangeHistoriesApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleChangeHistoriesApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_change_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **schedule_id** | **int**| Checklist Schedule ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ChecklistScheduleChangeHistory]**](ChecklistScheduleChangeHistory.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

