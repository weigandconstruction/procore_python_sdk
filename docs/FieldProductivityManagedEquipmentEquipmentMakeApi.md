# procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_managed_equipment_makes_get**](FieldProductivityManagedEquipmentEquipmentMakeApi.md#rest_v10_companies_company_id_managed_equipment_makes_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_makes | List all equipment makes
[**rest_v10_companies_company_id_managed_equipment_makes_id_delete**](FieldProductivityManagedEquipmentEquipmentMakeApi.md#rest_v10_companies_company_id_managed_equipment_makes_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/managed_equipment_makes/{id} | Delete an equipment make
[**rest_v10_companies_company_id_managed_equipment_makes_id_get**](FieldProductivityManagedEquipmentEquipmentMakeApi.md#rest_v10_companies_company_id_managed_equipment_makes_id_get) | **GET** /rest/v1.0/companies/{company_id}/managed_equipment_makes/{id} | Show an equipment make
[**rest_v10_companies_company_id_managed_equipment_makes_id_patch**](FieldProductivityManagedEquipmentEquipmentMakeApi.md#rest_v10_companies_company_id_managed_equipment_makes_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/managed_equipment_makes/{id} | Update an equipment make
[**rest_v10_companies_company_id_managed_equipment_makes_post**](FieldProductivityManagedEquipmentEquipmentMakeApi.md#rest_v10_companies_company_id_managed_equipment_makes_post) | **POST** /rest/v1.0/companies/{company_id}/managed_equipment_makes | Create an equipment make


# **rest_v10_companies_company_id_managed_equipment_makes_get**
> List[ManagedEquipmentMake] rest_v10_companies_company_id_managed_equipment_makes_get(procore_company_id, company_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)

List all equipment makes

Return a list of all equipment makes.

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List all equipment makes
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_makes_get(procore_company_id, company_id, filters_updated_at=filters_updated_at, page=page, per_page=per_page)
        print("The response of FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_get: %s\n" % e)
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

[**List[ManagedEquipmentMake]**](ManagedEquipmentMake.md)

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

# **rest_v10_companies_company_id_managed_equipment_makes_id_delete**
> ManagedEquipmentMake rest_v10_companies_company_id_managed_equipment_makes_id_delete(procore_company_id, company_id, id)

Delete an equipment make

Detete a specific equipment make

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the equipment make

    try:
        # Delete an equipment make
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_makes_id_delete(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the equipment make | 

### Return type

[**ManagedEquipmentMake**](ManagedEquipmentMake.md)

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

# **rest_v10_companies_company_id_managed_equipment_makes_id_get**
> ManagedEquipmentMake rest_v10_companies_company_id_managed_equipment_makes_id_get(procore_company_id, company_id, id)

Show an equipment make

Return detailed information about a specific equipment make

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the equipment make

    try:
        # Show an equipment make
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_makes_id_get(procore_company_id, company_id, id)
        print("The response of FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the equipment make | 

### Return type

[**ManagedEquipmentMake**](ManagedEquipmentMake.md)

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

# **rest_v10_companies_company_id_managed_equipment_makes_id_patch**
> ManagedEquipmentMake rest_v10_companies_company_id_managed_equipment_makes_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_makes_post_request=rest_v10_companies_company_id_managed_equipment_makes_post_request)

Update an equipment make

Update a specified equipment make

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_makes_post_request import RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the equipment make
    rest_v10_companies_company_id_managed_equipment_makes_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest |  (optional)

    try:
        # Update an equipment make
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_makes_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_managed_equipment_makes_post_request=rest_v10_companies_company_id_managed_equipment_makes_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the equipment make | 
 **rest_v10_companies_company_id_managed_equipment_makes_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentMake**](ManagedEquipmentMake.md)

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

# **rest_v10_companies_company_id_managed_equipment_makes_post**
> ManagedEquipmentMake rest_v10_companies_company_id_managed_equipment_makes_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_makes_post_request=rest_v10_companies_company_id_managed_equipment_makes_post_request)

Create an equipment make

Create a new equipment make

### Example


```python
import procore_sdk
from procore_sdk.models.managed_equipment_make import ManagedEquipmentMake
from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_makes_post_request import RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest
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
    api_instance = procore_sdk.FieldProductivityManagedEquipmentEquipmentMakeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_managed_equipment_makes_post_request = procore_sdk.RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest() # RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest |  (optional)

    try:
        # Create an equipment make
        api_response = api_instance.rest_v10_companies_company_id_managed_equipment_makes_post(procore_company_id, company_id, rest_v10_companies_company_id_managed_equipment_makes_post_request=rest_v10_companies_company_id_managed_equipment_makes_post_request)
        print("The response of FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityManagedEquipmentEquipmentMakeApi->rest_v10_companies_company_id_managed_equipment_makes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_managed_equipment_makes_post_request** | [**RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest**](RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequest.md)|  | [optional] 

### Return type

[**ManagedEquipmentMake**](ManagedEquipmentMake.md)

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

