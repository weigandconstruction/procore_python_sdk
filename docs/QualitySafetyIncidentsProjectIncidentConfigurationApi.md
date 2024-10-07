# procore_sdk.QualitySafetyIncidentsProjectIncidentConfigurationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_configuration_get**](QualitySafetyIncidentsProjectIncidentConfigurationApi.md#rest_v10_projects_project_id_incidents_configuration_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/configuration | Get Project Incident Configuration
[**rest_v10_projects_project_id_incidents_configuration_patch**](QualitySafetyIncidentsProjectIncidentConfigurationApi.md#rest_v10_projects_project_id_incidents_configuration_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/configuration | Update Project Incident Configuration


# **rest_v10_projects_project_id_incidents_configuration_get**
> ProjectIncidentConfiguration rest_v10_projects_project_id_incidents_configuration_get(procore_company_id, project_id)

Get Project Incident Configuration

Return the selected project Incident configuration values

### Example


```python
import procore_sdk
from procore_sdk.models.project_incident_configuration import ProjectIncidentConfiguration
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
    api_instance = procore_sdk.QualitySafetyIncidentsProjectIncidentConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Project Incident Configuration
        api_response = api_instance.rest_v10_projects_project_id_incidents_configuration_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsProjectIncidentConfigurationApi->rest_v10_projects_project_id_incidents_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsProjectIncidentConfigurationApi->rest_v10_projects_project_id_incidents_configuration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**ProjectIncidentConfiguration**](ProjectIncidentConfiguration.md)

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

# **rest_v10_projects_project_id_incidents_configuration_patch**
> ProjectIncidentConfiguration rest_v10_projects_project_id_incidents_configuration_patch(procore_company_id, project_id, rest_v10_projects_project_id_incidents_configuration_patch_request)

Update Project Incident Configuration

Update the selected project Incident configuration values

### Example


```python
import procore_sdk
from procore_sdk.models.project_incident_configuration import ProjectIncidentConfiguration
from procore_sdk.models.rest_v10_projects_project_id_incidents_configuration_patch_request import RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsProjectIncidentConfigurationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_configuration_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest() # RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest | 

    try:
        # Update Project Incident Configuration
        api_response = api_instance.rest_v10_projects_project_id_incidents_configuration_patch(procore_company_id, project_id, rest_v10_projects_project_id_incidents_configuration_patch_request)
        print("The response of QualitySafetyIncidentsProjectIncidentConfigurationApi->rest_v10_projects_project_id_incidents_configuration_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsProjectIncidentConfigurationApi->rest_v10_projects_project_id_incidents_configuration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_configuration_patch_request** | [**RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest**](RestV10ProjectsProjectIdIncidentsConfigurationPatchRequest.md)|  | 

### Return type

[**ProjectIncidentConfiguration**](ProjectIncidentConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

