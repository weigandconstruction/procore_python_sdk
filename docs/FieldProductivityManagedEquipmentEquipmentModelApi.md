# procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_models/bulk_update | Bulk Update Managed Equipment models
[**rest_v10_companies_company_id_managed_equipment_models_get**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_models | List all equipment models
[**rest_v10_companies_company_id_managed_equipment_models_id_delete**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_models/{id} | Delete an equipment model
[**rest_v10_companies_company_id_managed_equipment_models_id_get**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_models/{id} | Show an equipment model
[**rest_v10_companies_company_id_managed_equipment_models_id_patch**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_models/{id} | Update an equipment model
[**rest_v10_companies_company_id_managed_equipment_models_post**](FieldProductivityManagedEquipmentEquipmentModelApi.md#rest_v10_companies_company_id_managed_equipment_models_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_models | Create an equipment Model


# **rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch**
> List[ManagedEquipmentModel] rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request)

Bulk Update Managed Equipment models

Update multiple Managed Equipment model entries is_active property with one request

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request import RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequest | 

    try:
        # Bulk Update Managed Equipment models
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[ManagedEquipmentModel]**](ManagedEquipmentModel.md)

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

# **rest_v10_companies_company_id_managed_equipment_models_get**
> List[ManagedEquipmentModel] rest_v10_companies_company_id_managed_equipment_models_get(procore_company_id, company_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List all equipment models

Return a list of all equipment models

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all equipment models
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_get(procore_company_id, company_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ManagedEquipmentModel]**](ManagedEquipmentModel.md)

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

# **rest_v10_companies_company_id_managed_equipment_models_id_delete**
> ManagedEquipmentModel rest_v10_companies_company_id_managed_equipment_models_id_delete(procore_company_id, id, company_id)

Delete an equipment model

Detete a specific equipment model

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the models for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete an equipment model
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_id_delete(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the models for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**ManagedEquipmentModel**](ManagedEquipmentModel.md)

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

# **rest_v10_companies_company_id_managed_equipment_models_id_get**
> ManagedEquipmentModel rest_v10_companies_company_id_managed_equipment_models_id_get(procore_company_id, id, company_id)

Show an equipment model

Return detailed information about a specific equipment model

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the models for
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show an equipment model
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_id_get(procore_company_id, id, company_id)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the models for | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**ManagedEquipmentModel**](ManagedEquipmentModel.md)

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

# **rest_v10_companies_company_id_managed_equipment_models_id_patch**
> ManagedEquipmentModel rest_v10_companies_company_id_managed_equipment_models_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_models_post_request=rest_v10_companies_company_id_managed_equipment_models_post_request)

Update an equipment model

Update a specified equipment model

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_post_request import RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the company to get the models for
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_models_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest |  (optional)

    try:
        # Update an equipment model
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_managed_equipment_models_post_request=rest_v10_companies_company_id_managed_equipment_models_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the company to get the models for | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_models_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentModel**](ManagedEquipmentModel.md)

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

# **rest_v10_companies_company_id_managed_equipment_models_post**
> ManagedEquipmentModel rest_v10_companies_company_id_managed_equipment_models_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_models_post_request=rest_v10_companies_company_id_managed_equipment_models_post_request)

Create an equipment Model

Create a new equipment model entry

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_model import ManagedEquipmentModel
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_post_request import RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentModelApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_models_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest |  (optional)

    try:
        # Create an equipment Model
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_models_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_models_post_request=rest_v10_companies_company_id_managed_equipment_models_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentModelApi->rest_v10_companies_company_id_managed_equipment_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_models_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentModelsPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentModel**](ManagedEquipmentModel.md)

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

