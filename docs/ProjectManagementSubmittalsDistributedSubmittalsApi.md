# procore_sdk.ProjectManagementSubmittalsDistributedSubmittalsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch**](ProjectManagementSubmittalsDistributedSubmittalsApi.md#rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch) | **PATCH** /rest/v1.0/projects/{project_id}/submittal_logs/{id}/close_and_distribute | Close and Distribute a Submittal Log


# **rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch**
> RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request=rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request)

Close and Distribute a Submittal Log

Close and Distribute the specified Submittal Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch200_response import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response
from procore_sdk.models.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request import RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest
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
    api_instance = procore_sdk.ProjectManagementSubmittalsDistributedSubmittalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Submittal ID
    rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request = procore_sdk.RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest() # RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest |  (optional)

    try:
        # Close and Distribute a Submittal Log
        api_response = api_instance.rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request=rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request)
        print("The response of ProjectManagementSubmittalsDistributedSubmittalsApi->rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSubmittalsDistributedSubmittalsApi->rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Submittal ID | 
 **rest_v10_projects_project_id_submittal_logs_id_close_and_distribute_patch_request** | [**RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest**](RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatchRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response**](RestV10ProjectsProjectIdSubmittalLogsIdCloseAndDistributePatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

