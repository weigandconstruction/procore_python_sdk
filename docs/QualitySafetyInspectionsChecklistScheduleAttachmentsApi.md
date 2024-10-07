# procore_sdk.QualitySafetyInspectionsChecklistScheduleAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get**](QualitySafetyInspectionsChecklistScheduleAttachmentsApi.md#rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get) | **GET** /rest/v1.0/projects/{project_id}/checklist/schedules/{schedule_id}/attachments | List Checklist Schedule Attachments
[**rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete**](QualitySafetyInspectionsChecklistScheduleAttachmentsApi.md#rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/checklist/schedules/{schedule_id}/attachments/{id} | Delete Checklist Schedule Attachment
[**rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post**](QualitySafetyInspectionsChecklistScheduleAttachmentsApi.md#rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post) | **POST** /rest/v1.0/projects/{project_id}/checklist/schedules/{schedule_id}/attachments | Create Checklist Schedule Attachment


# **rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get**
> List[ChecklistScheduleAttachment] rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get(procore_company_id, project_id, schedule_id, page=page, per_page=per_page)

List Checklist Schedule Attachments

Lists Checklist Schedule Attachments for given Project and Schedule

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule_attachment import ChecklistScheduleAttachment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_id = 56 # int | Checklist Schedule ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Checklist Schedule Attachments
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get(procore_company_id, project_id, schedule_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsChecklistScheduleAttachmentsApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleAttachmentsApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_get: %s\n" % e)
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

[**List[ChecklistScheduleAttachment]**](ChecklistScheduleAttachment.md)

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

# **rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete**
> rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete(procore_company_id, project_id, schedule_id, id)

Delete Checklist Schedule Attachment

Delete the attachment pertaining to the Checklist Schedule Attachment

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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_id = 56 # int | Checklist Schedule ID
    id = 56 # int | Checklist Schedule Attachment ID

    try:
        # Delete Checklist Schedule Attachment
        api_instance.rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete(procore_company_id, project_id, schedule_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleAttachmentsApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **schedule_id** | **int**| Checklist Schedule ID | 
 **id** | **int**| Checklist Schedule Attachment ID | 

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

# **rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post**
> ChecklistScheduleAttachment rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post(procore_company_id, project_id, schedule_id, attachment)

Create Checklist Schedule Attachment

Uploads an Attachment to the specified Checklist Schedule

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_schedule_attachment import ChecklistScheduleAttachment
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
    api_instance = procore_sdk.QualitySafetyInspectionsChecklistScheduleAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_id = 56 # int | Checklist Schedule ID
    attachment = None # bytearray | Checklist Schedule Attachment. To upload an attachment you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with the `attachment` file.

    try:
        # Create Checklist Schedule Attachment
        api_response = api_instance.rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post(procore_company_id, project_id, schedule_id, attachment)
        print("The response of QualitySafetyInspectionsChecklistScheduleAttachmentsApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsChecklistScheduleAttachmentsApi->rest_v10_projects_project_id_checklist_schedules_schedule_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **schedule_id** | **int**| Checklist Schedule ID | 
 **attachment** | **bytearray**| Checklist Schedule Attachment. To upload an attachment you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with the &#x60;attachment&#x60; file. | 

### Return type

[**ChecklistScheduleAttachment**](ChecklistScheduleAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

