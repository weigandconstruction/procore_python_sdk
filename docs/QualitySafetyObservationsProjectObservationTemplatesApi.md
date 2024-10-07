# procore_sdk.QualitySafetyObservationsProjectObservationTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_observation_templates_bulk_update_patch**](QualitySafetyObservationsProjectObservationTemplatesApi.md#rest_v10_projects_project_id_observation_templates_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/observation_templates/bulk_update | Bulk Update Project Observation Templates


# **rest_v10_projects_project_id_observation_templates_bulk_update_patch**
> List[ProjectObservationTemplate1] rest_v10_projects_project_id_observation_templates_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_observation_templates_bulk_update_patch_request, observation_template_ids=observation_template_ids)

Bulk Update Project Observation Templates

Updates multiple Project Observation Templates

### Example


```python
import procore_sdk
from procore_sdk.models.project_observation_template1 import ProjectObservationTemplate1
from procore_sdk.models.rest_v10_projects_project_id_observation_templates_bulk_update_patch_request import RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyObservationsProjectObservationTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_observation_templates_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest() # RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest | 
    observation_template_ids = [56] # List[int] | IDs of all Project Observation Templates specified for bulk update (optional)

    try:
        # Bulk Update Project Observation Templates
        api_response = api_instance.rest_v10_projects_project_id_observation_templates_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_observation_templates_bulk_update_patch_request, observation_template_ids=observation_template_ids)
        print("The response of QualitySafetyObservationsProjectObservationTemplatesApi->rest_v10_projects_project_id_observation_templates_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsProjectObservationTemplatesApi->rest_v10_projects_project_id_observation_templates_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_observation_templates_bulk_update_patch_request** | [**RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest**](RestV10ProjectsProjectIdObservationTemplatesBulkUpdatePatchRequest.md)|  | 
 **observation_template_ids** | [**List[int]**](int.md)| IDs of all Project Observation Templates specified for bulk update | [optional] 

### Return type

[**List[ProjectObservationTemplate1]**](ProjectObservationTemplate1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

