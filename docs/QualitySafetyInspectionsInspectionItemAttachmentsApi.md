# procore_sdk.QualitySafetyInspectionsInspectionItemAttachmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete**](QualitySafetyInspectionsInspectionItemAttachmentsApi.md#rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/inspections/{inspection_id}/item_attachments/{id} | Delete an Inspection Item Attachment


# **rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete**
> rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete(procore_company_id, project_id, inspection_id, id)

Delete an Inspection Item Attachment

Removes the Attachment for a specified Inspection Item on a given Project

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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionItemAttachmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    inspection_id = 56 # int | Unique identifier for the inspection.
    id = 56 # int | Item Attachment ID

    try:
        # Delete an Inspection Item Attachment
        api_instance.rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete(procore_company_id, project_id, inspection_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionItemAttachmentsApi->rest_v10_projects_project_id_inspections_inspection_id_item_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **inspection_id** | **int**| Unique identifier for the inspection. | 
 **id** | **int**| Item Attachment ID | 

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

