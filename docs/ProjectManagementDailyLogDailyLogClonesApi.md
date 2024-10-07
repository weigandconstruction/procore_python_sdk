# procore_sdk.ProjectManagementDailyLogDailyLogClonesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_logs_clones_post**](ProjectManagementDailyLogDailyLogClonesApi.md#rest_v10_projects_project_id_daily_logs_clones_post) | **POST** /rest/v1.0/projects/{project_id}/daily_logs/clones | Clones Daily Logs from one Date to another Date


# **rest_v10_projects_project_id_daily_logs_clones_post**
> rest_v10_projects_project_id_daily_logs_clones_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_clones_post_request, idempotency_token=idempotency_token)

Clones Daily Logs from one Date to another Date

Clones Daily Logs of the given log_types from the from_date to the to_date. 

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_clones_post_request import RestV10ProjectsProjectIdDailyLogsClonesPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogDailyLogClonesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_daily_logs_clones_post_request = procore_sdk.RestV10ProjectsProjectIdDailyLogsClonesPostRequest() # RestV10ProjectsProjectIdDailyLogsClonesPostRequest | 
    idempotency_token = 'idempotency_token_example' # str | Unique idempotent token (optional)

    try:
        # Clones Daily Logs from one Date to another Date
        api_instance.rest_v10_projects_project_id_daily_logs_clones_post(procore_company_id, project_id, rest_v10_projects_project_id_daily_logs_clones_post_request, idempotency_token=idempotency_token)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogDailyLogClonesApi->rest_v10_projects_project_id_daily_logs_clones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_daily_logs_clones_post_request** | [**RestV10ProjectsProjectIdDailyLogsClonesPostRequest**](RestV10ProjectsProjectIdDailyLogsClonesPostRequest.md)|  | 
 **idempotency_token** | **str**| Unique idempotent token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (Duplicate Idempotency-token header) |  -  |
**201** | The copy succeeded. |  -  |
**400** | Request is invalid. The dates may be out-of-order or in the future, or the log types might be invalid. |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

