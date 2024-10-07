# procore_sdk.QualitySafetyInspectionsChecklistAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete**](QualitySafetyInspectionsChecklistAttachmentsApi.md#rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/lists/{list_id}/attachments/{id} | Delete Attachment
[**rest_v10_projects_project_id_checklist_lists_list_id_attachments_post**](QualitySafetyInspectionsChecklistAttachmentsApi.md#rest_v10_projects_project_id_checklist_lists_list_id_attachments_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/lists/{list_id}/attachments | Create Attachment


# **rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete**
> rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete(procore_company_id, project_id, list_id, id)

Delete Attachment

Deletes the specified Attachment

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    list_id = 56 # int | Checklist (Inspection) ID
    id = 56 # int | Attachment ID

    try:
        # Delete Attachment
        api_instance.rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete(procore_company_id, project_id, list_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistAttachmentsApi->rest_v10_projects_project_id_checklist_lists_list_id_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **list_id** | **int**| Checklist (Inspection) ID | 
 **id** | **int**| Attachment ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_checklist_lists_list_id_attachments_post**
> ChecklistInspectionAttachment1 rest_v10_projects_project_id_checklist_lists_list_id_attachments_post(procore_company_id, project_id, list_id, attachment)

Create Attachment

Creates an attachment for the specified Checklist (Inspection).

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_inspection_attachment1 import ChecklistInspectionAttachment1
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    list_id = 56 # int | Checklist (Inspection) ID
    attachment = None # bytearray | Checklist (Inspection) Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type with the `attachment` file.

    try:
        # Create Attachment
        api_response = api_instance.rest_v10_projects_project_id_checklist_lists_list_id_attachments_post(procore_company_id, project_id, list_id, attachment)
        print("The response of QualitySafetyInspectionsChecklistAttachmentsApi->rest_v10_projects_project_id_checklist_lists_list_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistAttachmentsApi->rest_v10_projects_project_id_checklist_lists_list_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **list_id** | **int**| Checklist (Inspection) ID | 
 **attachment** | **bytearray**| Checklist (Inspection) Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type with the &#x60;attachment&#x60; file. | 

### Return type

[**ChecklistInspectionAttachment1**](ChecklistInspectionAttachment1.md)

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

