# procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete**](FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment/{id}/managed_equipment_attachments/bulk_destroy | Bulk Delete Managed Equipment Attachment
[**rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete**](FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi.md#rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment/{managed_equipment_id}/managed_equipment_attachments/{id} | Delete Managed Equipment Attachment


# **rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete**
> List[ManagedEquipmentAttachment] rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request)

Bulk Delete Managed Equipment Attachment

Delete multiple Managed Equipment Attachments with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_attachment import ManagedEquipmentAttachment
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request import RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID
    rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequest() # RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Managed Equipment Attachment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi->rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi->rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 
 **rest_v10_companies_company_id_managed_equipment_id_managed_equipment_attachments_bulk_destroy_delete_request** | [**RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequest**](RestV10CompaniesCompanyIdManagedEquipmentIdManagedEquipmentAttachmentsBulkDestroyDeleteRequest.md)|  | 

### Return type

[**List[ManagedEquipmentAttachment]**](ManagedEquipmentAttachment.md)

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

# **rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete**
> ManagedEquipmentAttachment rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete(procore_company_id, company_id, managed_equipment_id, id)

Delete Managed Equipment Attachment

Deleting an attachment from a Managed Equipment

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_attachment import ManagedEquipmentAttachment
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    managed_equipment_id = 56 # int | Id of the Equipment
    id = 56 # int | Id of the Managed Equipment Attachment

    try:
        # Delete Managed Equipment Attachment
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete(procore_company_id, company_id, managed_equipment_id, id)
        print("The response of FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi->rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentManagedEquipmentAttachmentApi->rest_v10_companies_company_id_managed_equipment_managed_equipment_id_managed_equipment_attachments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **managed_equipment_id** | **int**| Id of the Equipment | 
 **id** | **int**| Id of the Managed Equipment Attachment | 

### Return type

[**ManagedEquipmentAttachment**](ManagedEquipmentAttachment.md)

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

