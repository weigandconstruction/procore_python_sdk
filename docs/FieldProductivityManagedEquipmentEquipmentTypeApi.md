# procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_types/bulk_update | Bulk Update Managed Equipment types
[**rest_v10_companies_company_id_managed_equipment_types_get**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_types | List all equipment types
[**rest_v10_companies_company_id_managed_equipment_types_id_delete**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_types/{id} | Delete a equipment type
[**rest_v10_companies_company_id_managed_equipment_types_id_get**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_types/{id} | Show an equipment type
[**rest_v10_companies_company_id_managed_equipment_types_id_patch**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_types/{id} | Update an equipment type
[**rest_v10_companies_company_id_managed_equipment_types_post**](FieldProductivityManagedEquipmentEquipmentTypeApi.md#rest_v10_companies_company_id_managed_equipment_types_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_types | Create an equipment type


# **rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch**
> List[ManagedEquipmentType] rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request)

Bulk Update Managed Equipment types

Update multiple Managed Equipment types entries is_active property with one request

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request import RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequest | 

    try:
        # Bulk Update Managed Equipment types
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_types_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdManagedEquipmentTypesBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[ManagedEquipmentType]**](ManagedEquipmentType.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_types_get**
> List[ManagedEquipmentType] rest_v10_companies_company_id_managed_equipment_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List all equipment types

Return a list of all equipment types

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all equipment types
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ManagedEquipmentType]**](ManagedEquipmentType.md)

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

# **rest_v10_companies_company_id_managed_equipment_types_id_delete**
> ManagedEquipmentType rest_v10_companies_company_id_managed_equipment_types_id_delete(procore_company_id, id, company_id)

Delete a equipment type

Detete a specific equipment type

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the types for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete a equipment type
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_id_delete(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the types for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**ManagedEquipmentType**](ManagedEquipmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_types_id_get**
> ManagedEquipmentType rest_v10_companies_company_id_managed_equipment_types_id_get(procore_company_id, id, company_id)

Show an equipment type

Return detailed information about a specific equipment type

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the types for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show an equipment type
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the types for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**ManagedEquipmentType**](ManagedEquipmentType.md)

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

# **rest_v10_companies_company_id_managed_equipment_types_id_patch**
> ManagedEquipmentType rest_v10_companies_company_id_managed_equipment_types_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_types_post_request=rest_v10_companies_company_id_managed_equipment_types_post_request)

Update an equipment type

Update a specified equipment type

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_post_request import RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the types for
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_types_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest |  (optional)

    try:
        # Update an equipment type
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_types_post_request=rest_v10_companies_company_id_managed_equipment_types_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the types for | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_types_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentType**](ManagedEquipmentType.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_managed_equipment_types_post**
> ManagedEquipmentType rest_v10_companies_company_id_managed_equipment_types_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_types_post_request=rest_v10_companies_company_id_managed_equipment_types_post_request)

Create an equipment type

Create a new Equipment Type Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_type import ManagedEquipmentType
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_post_request import RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_types_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest |  (optional)

    try:
        # Create an equipment type
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_types_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_types_post_request=rest_v10_companies_company_id_managed_equipment_types_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentTypeApi->rest_v10_companies_company_id_managed_equipment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_types_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentType**](ManagedEquipmentType.md)

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

