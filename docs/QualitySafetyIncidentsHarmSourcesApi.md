# procore_sdk.QualitySafetyIncidentsHarmSourcesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/harm_sources/bulk_update | Bulk Update Harm Sources
[**rest_v10_companies_company_id_incidents_harm_sources_get**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/harm_sources | List Harm Sources
[**rest_v10_companies_company_id_incidents_harm_sources_id_delete**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/incidents/harm_sources/{id} | Delete Harm Source
[**rest_v10_companies_company_id_incidents_harm_sources_id_get**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/harm_sources/{id} | Show Harm Source
[**rest_v10_companies_company_id_incidents_harm_sources_id_patch**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/harm_sources/{id} | Update Harm Source
[**rest_v10_companies_company_id_incidents_harm_sources_post**](QualitySafetyIncidentsHarmSourcesApi.md#rest_v10_companies_company_id_incidents_harm_sources_post) | **POST** /rest/v1.0/companies/{company_id}/incidents/harm_sources | Create Harm Source


# **rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch**
> List[HarmSource1] rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request)

Bulk Update Harm Sources

Update multiple Harm Sources with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.harm_source1 import HarmSource1
from procore_sdk.models.rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request import RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequest | 

    try:
        # Bulk Update Harm Sources
        api_response = api_instance.rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_harm_sources_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdIncidentsHarmSourcesBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[HarmSource1]**](HarmSource1.md)

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

# **rest_v10_companies_company_id_incidents_harm_sources_get**
> List[HarmSource1] rest_v10_companies_company_id_incidents_harm_sources_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort, all=all)

List Harm Sources

Return a list of all Harm Sources associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.harm_source1 import HarmSource1
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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)
    all = True # bool | Harm Sources (optional)

    try:
        # List Harm Sources
        api_response = api_instance.rest_v10_companies_company_id_incidents_harm_sources_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort, all=all)
        print("The response of QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_get: %s\n" % e)
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
 **sort** | **str**|  | [optional] 
 **all** | **bool**| Harm Sources | [optional] 

### Return type

[**List[HarmSource1]**](HarmSource1.md)

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

# **rest_v10_companies_company_id_incidents_harm_sources_id_delete**
> rest_v10_companies_company_id_incidents_harm_sources_id_delete(procore_company_id, company_id, id)

Delete Harm Source

Deletes a Harm Source. Note that Procore provided Harm Sources cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Harm Source ID

    try:
        # Delete Harm Source
        api_instance.rest_v10_companies_company_id_incidents_harm_sources_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Harm Source ID | 

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

# **rest_v10_companies_company_id_incidents_harm_sources_id_get**
> HarmSource1 rest_v10_companies_company_id_incidents_harm_sources_id_get(procore_company_id, company_id, id)

Show Harm Source

Returns the specified Harm Source.

### Example


```python
import procore_sdk
from procore_sdk.models.harm_source1 import HarmSource1
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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Harm Source ID

    try:
        # Show Harm Source
        api_response = api_instance.rest_v10_companies_company_id_incidents_harm_sources_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Harm Source ID | 

### Return type

[**HarmSource1**](HarmSource1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_incidents_harm_sources_id_patch**
> HarmSource1 rest_v10_companies_company_id_incidents_harm_sources_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_harm_sources_post_request)

Update Harm Source

Updates a specified Harm Source. Note that Procore provided Harm Sources' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.harm_source1 import HarmSource1
from procore_sdk.models.rest_v10_companies_company_id_incidents_harm_sources_post_request import RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Harm Source ID
    rest_v10_companies_company_id_incidents_harm_sources_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest() # RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest | 

    try:
        # Update Harm Source
        api_response = api_instance.rest_v10_companies_company_id_incidents_harm_sources_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_harm_sources_post_request)
        print("The response of QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Harm Source ID | 
 **rest_v10_companies_company_id_incidents_harm_sources_post_request** | [**RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest**](RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest.md)|  | 

### Return type

[**HarmSource1**](HarmSource1.md)

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

# **rest_v10_companies_company_id_incidents_harm_sources_post**
> HarmSource1 rest_v10_companies_company_id_incidents_harm_sources_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_harm_sources_post_request)

Create Harm Source

Creates a Harm Source with the specified name

### Example


```python
import procore_sdk
from procore_sdk.models.harm_source1 import HarmSource1
from procore_sdk.models.rest_v10_companies_company_id_incidents_harm_sources_post_request import RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHarmSourcesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_harm_sources_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest() # RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest | 

    try:
        # Create Harm Source
        api_response = api_instance.rest_v10_companies_company_id_incidents_harm_sources_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_harm_sources_post_request)
        print("The response of QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHarmSourcesApi->rest_v10_companies_company_id_incidents_harm_sources_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_harm_sources_post_request** | [**RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest**](RestV10CompaniesCompanyIdIncidentsHarmSourcesPostRequest.md)|  | 

### Return type

[**HarmSource1**](HarmSource1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

