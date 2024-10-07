# procore_sdk.QualitySafetyIncidentsIncidentAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_incident_id_attachments_post**](QualitySafetyIncidentsIncidentAttachmentsApi.md#rest_v10_projects_project_id_incidents_incident_id_attachments_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/{incident_id}/attachments | Create Attachment


# **rest_v10_projects_project_id_incidents_incident_id_attachments_post**
> IncidentAttachment1 rest_v10_projects_project_id_incidents_incident_id_attachments_post(procore_company_id, project_id, incident_id, attachment, run_configurable_validations=run_configurable_validations)

Create Attachment

Creates an attachment for the specified Incident.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_attachment1 import IncidentAttachment1
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID
    attachment = None # bytearray | Incident Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type  with the `attachment` file. 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Create Attachment
        api_response = api_instance.rest_v10_projects_project_id_incidents_incident_id_attachments_post(procore_company_id, project_id, incident_id, attachment, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsIncidentAttachmentsApi->rest_v10_projects_project_id_incidents_incident_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentAttachmentsApi->rest_v10_projects_project_id_incidents_incident_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID | 
 **attachment** | **bytearray**| Incident Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type  with the &#x60;attachment&#x60; file.  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**IncidentAttachment1**](IncidentAttachment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

