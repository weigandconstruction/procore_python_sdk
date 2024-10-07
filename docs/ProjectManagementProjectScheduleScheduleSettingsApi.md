# procore_sdk.ProjectManagementProjectScheduleScheduleSettingsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_schedule_settings_get**](ProjectManagementProjectScheduleScheduleSettingsApi.md#rest_v10_projects_project_id_schedule_settings_get) | **GET** /rest/v1.0/projects/{project_id}/schedule/settings | Show Project Schedule Settings


# **rest_v10_projects_project_id_schedule_settings_get**
> RestV10ProjectsProjectIdScheduleSettingsGet200Response rest_v10_projects_project_id_schedule_settings_get(procore_company_id, project_id)

Show Project Schedule Settings

Return the Schedule tool settings for the given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_schedule_settings_get200_response import RestV10ProjectsProjectIdScheduleSettingsGet200Response
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleSettingsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Project Schedule Settings
        api_response = api_instance.rest_v10_projects_project_id_schedule_settings_get(procore_company_id, project_id)
        print("The response of ProjectManagementProjectScheduleScheduleSettingsApi->rest_v10_projects_project_id_schedule_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleSettingsApi->rest_v10_projects_project_id_schedule_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdScheduleSettingsGet200Response**](RestV10ProjectsProjectIdScheduleSettingsGet200Response.md)

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
**403** | User does not have right permissions |  -  |
**404** | Endpoint not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

