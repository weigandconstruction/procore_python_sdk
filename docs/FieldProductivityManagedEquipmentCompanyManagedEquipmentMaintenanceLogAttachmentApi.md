# procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete**](FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id}/attachments/{attachment_id} | Delete Managed Equipment Maintenance Log Attachment
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get**](FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id}/attachments/{attachment_id} | Show an individual managed equipment maintenance log attachment
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete**](FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id}/attachments/bulk_destroy | Bulk Delete Managed Equipment Maintenance Log Attachments
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get**](FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id}/attachments | List all maintenance logs attachment
[**rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post**](FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_maintenance_logs/{id}/attachments | Create maintenance log attachment.


# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete**
> ManagedEquipmentMaintenanceLogsAttachment rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete(procore_company_id, attachment_id, company_id, id)

Delete Managed Equipment Maintenance Log Attachment

Deleting an attachment from a Managed Equipment Maintenance Log

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    attachment_id = 56 # int | ID of the managed equipment maintenance log attachment
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the Managed Equipment Maintenance Log Attachment

    try:
        # Delete Managed Equipment Maintenance Log Attachment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete(procore_company_id, attachment_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **attachment_id** | **int**| ID of the managed equipment maintenance log attachment | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the Managed Equipment Maintenance Log Attachment | 

### Return type

[**ManagedEquipmentMaintenanceLogsAttachment**](ManagedEquipmentMaintenanceLogsAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get**
> ManagedEquipmentMaintenanceLogsAttachment rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get(procore_company_id, company_id, id, attachment_id)

Show an individual managed equipment maintenance log attachment

Return detailed information about a specific managed equipment maintenance log attachment

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the managed equipment maintenance log to get attachments from
    attachment_id = 56 # int | ID of the managed equipment maintenance log attachment

    try:
        # Show an individual managed equipment maintenance log attachment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get(procore_company_id, company_id, id, attachment_id)
        print("The response of FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_attachment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the managed equipment maintenance log to get attachments from | 
 **attachment_id** | **int**| ID of the managed equipment maintenance log attachment | 

### Return type

[**ManagedEquipmentMaintenanceLogsAttachment**](ManagedEquipmentMaintenanceLogsAttachment.md)

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

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete**
> List[ManagedEquipmentMaintenanceLogsAttachment] rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete_request)

Bulk Delete Managed Equipment Maintenance Log Attachments

Delete multiple Managed Equipment Maintenance Logs Attachments with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Managed Equipment Maintenance Log
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsBulkDestroyDeleteRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Managed Equipment Maintenance Log Attachments
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete_request)
        print("The response of FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Managed Equipment Maintenance Log | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_bulk_destroy_delete_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsBulkDestroyDeleteRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsBulkDestroyDeleteRequest.md)|  | 

### Return type

[**List[ManagedEquipmentMaintenanceLogsAttachment]**](ManagedEquipmentMaintenanceLogsAttachment.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get**
> List[ManagedEquipmentMaintenanceLogsAttachment] rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get(procore_company_id, company_id, id)

List all maintenance logs attachment

Return a list of all Maintenance Log attachments for the Maintenance Log the current user has access to.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # List all maintenance logs attachment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 

### Return type

[**List[ManagedEquipmentMaintenanceLogsAttachment]**](ManagedEquipmentMaintenanceLogsAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post**
> ManagedEquipmentMaintenanceLogsAttachment rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request)

Create maintenance log attachment.

Create a new maintenance log attachment.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_maintenance_logs_attachment import ManagedEquipmentMaintenanceLogsAttachment
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request import RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Id of the Managed Equipment Maintenance Log
    rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequest | 

    try:
        # Create maintenance log attachment.
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request)
        print("The response of FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentCompanyManagedEquipmentMaintenanceLogAttachmentApi->rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Id of the Managed Equipment Maintenance Log | 
 **rest_v10_companies_company_id_managed_equipment_maintenance_logs_id_attachments_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMaintenanceLogsIdAttachmentsPostRequest.md)|  | 

### Return type

[**ManagedEquipmentMaintenanceLogsAttachment**](ManagedEquipmentMaintenanceLogsAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

