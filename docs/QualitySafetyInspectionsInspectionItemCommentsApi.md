# procore_sdk.QualitySafetyInspectionsInspectionItemCommentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_inspections_inspection_id_comments_post**](QualitySafetyInspectionsInspectionItemCommentsApi.md#rest_v10_projects_project_id_inspections_inspection_id_comments_post) | **POST** /rest/v1.0/projects/{project_id}/inspections/{inspection_id}/comments | Creates an Inspection Item Comment


# **rest_v10_projects_project_id_inspections_inspection_id_comments_post**
> ChecklistComment rest_v10_projects_project_id_inspections_inspection_id_comments_post(procore_company_id, project_id, inspection_id)

Creates an Inspection Item Comment

Adds a new Comment for a specified Inspection Item on a given Project

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_comment import ChecklistComment
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionItemCommentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    inspection_id = 56 # int | Unique identifier for the inspection.

    try:
        # Creates an Inspection Item Comment
        api_response = api_instance.rest_v10_projects_project_id_inspections_inspection_id_comments_post(procore_company_id, project_id, inspection_id)
        print("The response of QualitySafetyInspectionsInspectionItemCommentsApi->rest_v10_projects_project_id_inspections_inspection_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionItemCommentsApi->rest_v10_projects_project_id_inspections_inspection_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **inspection_id** | **int**| Unique identifier for the inspection. | 

### Return type

[**ChecklistComment**](ChecklistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

