# procore_sdk.QualitySafetyIncidentsAfflictionTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/affliction_types/bulk_update | Bulk Update Affliction Types
[**rest_v10_companies_company_id_incidents_affliction_types_get**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/affliction_types | List Affliction Types
[**rest_v10_companies_company_id_incidents_affliction_types_id_delete**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/incidents/affliction_types/{id} | Delete Affliction Type
[**rest_v10_companies_company_id_incidents_affliction_types_id_get**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/affliction_types/{id} | Show Affliction Type
[**rest_v10_companies_company_id_incidents_affliction_types_id_patch**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/affliction_types/{id} | Update Affliction Type
[**rest_v10_companies_company_id_incidents_affliction_types_post**](QualitySafetyIncidentsAfflictionTypesApi.md#rest_v10_companies_company_id_incidents_affliction_types_post) | **POST** /rest/v1.0/companies/{company_id}/incidents/affliction_types | Create Affliction Type


# **rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch**
> List[AfflictionType1] rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request)

Bulk Update Affliction Types

Update multiple Affliction Types with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.affliction_type1 import AfflictionType1
from procore_sdk.models.rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request import RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequest | 

    try:
        # Bulk Update Affliction Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_affliction_types_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdIncidentsAfflictionTypesBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[AfflictionType1]**](AfflictionType1.md)

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

# **rest_v10_companies_company_id_incidents_affliction_types_get**
> List[AfflictionType1] rest_v10_companies_company_id_incidents_affliction_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Affliction Types

Return a list of all Affliction Types associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.affliction_type1 import AfflictionType1
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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str | Affliction Types (optional)

    try:
        # List Affliction Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_affliction_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_active** | **bool**| If true, returns item(s) with a status of &#39;active&#39;. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**| Affliction Types | [optional] 

### Return type

[**List[AfflictionType1]**](AfflictionType1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_incidents_affliction_types_id_delete**
> rest_v10_companies_company_id_incidents_affliction_types_id_delete(procore_company_id, company_id, id)

Delete Affliction Type

Deletes an Affliction Type. Note that Procore provided Affliction Types cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Affliction Type ID

    try:
        # Delete Affliction Type
        api_instance.rest_v10_companies_company_id_incidents_affliction_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Affliction Type ID | 

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_incidents_affliction_types_id_get**
> AfflictionType1 rest_v10_companies_company_id_incidents_affliction_types_id_get(procore_company_id, company_id, id)

Show Affliction Type

Returns the specified Affliction Type.

### Example


```python
import procore_sdk
from procore_sdk.models.affliction_type1 import AfflictionType1
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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Affliction Type ID

    try:
        # Show Affliction Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_affliction_types_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Affliction Type ID | 

### Return type

[**AfflictionType1**](AfflictionType1.md)

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

# **rest_v10_companies_company_id_incidents_affliction_types_id_patch**
> AfflictionType1 rest_v10_companies_company_id_incidents_affliction_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_affliction_types_post_request)

Update Affliction Type

Updates a specified Affliction Type. Note that Procore provided Affliction Types' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.affliction_type1 import AfflictionType1
from procore_sdk.models.rest_v10_companies_company_id_incidents_affliction_types_post_request import RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Affliction Type ID
    rest_v10_companies_company_id_incidents_affliction_types_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest() # RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest | 

    try:
        # Update Affliction Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_affliction_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_affliction_types_post_request)
        print("The response of QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Affliction Type ID | 
 **rest_v10_companies_company_id_incidents_affliction_types_post_request** | [**RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest**](RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest.md)|  | 

### Return type

[**AfflictionType1**](AfflictionType1.md)

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

# **rest_v10_companies_company_id_incidents_affliction_types_post**
> AfflictionType1 rest_v10_companies_company_id_incidents_affliction_types_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_affliction_types_post_request)

Create Affliction Type

Creates a Affliction Type with the specified name.

### Example


```python
import procore_sdk
from procore_sdk.models.affliction_type1 import AfflictionType1
from procore_sdk.models.rest_v10_companies_company_id_incidents_affliction_types_post_request import RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsAfflictionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_affliction_types_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest() # RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest | 

    try:
        # Create Affliction Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_affliction_types_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_affliction_types_post_request)
        print("The response of QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAfflictionTypesApi->rest_v10_companies_company_id_incidents_affliction_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_affliction_types_post_request** | [**RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest**](RestV10CompaniesCompanyIdIncidentsAfflictionTypesPostRequest.md)|  | 

### Return type

[**AfflictionType1**](AfflictionType1.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

