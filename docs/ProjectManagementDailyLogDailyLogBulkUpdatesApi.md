# procore_sdk.ProjectManagementDailyLogDailyLogBulkUpdatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch**](ProjectManagementDailyLogDailyLogBulkUpdatesApi.md#rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/daily_logs/bulk_updates/bulk_update | Bulk Updates for Daily Logs


# **rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch**
> List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch200ResponseInner] rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request)

Bulk Updates for Daily Logs

Updates multiple daily logs with single request. Currently only status update is available. 300 logs maximum is allowed per request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch200_response_inner import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request import RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogBulkUpdatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest() # RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest | 

    try:
        # Bulk Updates for Daily Logs
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request)
        print("The response of ProjectManagementDailyLogDailyLogBulkUpdatesApi->rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogBulkUpdatesApi->rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_daily_logs_bulk_updates_bulk_update_patch_request** | [**RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch200ResponseInner]**](RestV10ProjectsProjectIdDailyLogsBulkUpdatesBulkUpdatePatch200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

