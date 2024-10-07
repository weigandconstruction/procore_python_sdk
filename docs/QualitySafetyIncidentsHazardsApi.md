# procore_sdk.QualitySafetyIncidentsHazardsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_hazards_bulk_update_patch**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/hazards/bulk_update | Bulk Update Hazards
[**rest_v10_companies_company_id_hazards_get**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_get) | **GET** /rest/v1.0/companies/{company_id}/hazards | List Hazards
[**rest_v10_companies_company_id_hazards_id_delete**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/hazards/{id} | Delete Hazard
[**rest_v10_companies_company_id_hazards_id_get**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_id_get) | **GET** /rest/v1.0/companies/{company_id}/hazards/{id} | Show Hazard
[**rest_v10_companies_company_id_hazards_id_patch**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/hazards/{id} | Update Hazard
[**rest_v10_companies_company_id_hazards_post**](QualitySafetyIncidentsHazardsApi.md#rest_v10_companies_company_id_hazards_post) | **POST** /rest/v1.0/companies/{company_id}/hazards | Create Hazard


# **rest_v10_companies_company_id_hazards_bulk_update_patch**
> List[Hazard1] rest_v10_companies_company_id_hazards_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_hazards_bulk_update_patch_request)

Bulk Update Hazards

Update multiple Hazards with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.hazard1 import Hazard1
from procore_sdk.models.rest_v10_companies_company_id_hazards_bulk_update_patch_request import RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_hazards_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest | 

    try:
        # Bulk Update Hazards
        api_response = api_instance.rest_v10_companies_company_id_hazards_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_hazards_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_hazards_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdHazardsBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[Hazard1]**](Hazard1.md)

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

# **rest_v10_companies_company_id_hazards_get**
> List[Hazard1] rest_v10_companies_company_id_hazards_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)

List Hazards

Return a list of all active Hazards associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.hazard1 import Hazard1
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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    all = True # bool | Both active and inactive Hazards (optional)

    try:
        # List Hazards
        api_response = api_instance.rest_v10_companies_company_id_hazards_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, all=all)
        print("The response of QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_get: %s\n" % e)
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
 **all** | **bool**| Both active and inactive Hazards | [optional] 

### Return type

[**List[Hazard1]**](Hazard1.md)

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

# **rest_v10_companies_company_id_hazards_id_delete**
> rest_v10_companies_company_id_hazards_id_delete(procore_company_id, company_id, id)

Delete Hazard

Deletes a Hazard. Note that Procore provided Hazards cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Hazard ID

    try:
        # Delete Hazard
        api_instance.rest_v10_companies_company_id_hazards_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Hazard ID | 

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

# **rest_v10_companies_company_id_hazards_id_get**
> Hazard1 rest_v10_companies_company_id_hazards_id_get(procore_company_id, company_id, id)

Show Hazard

Returns the details for a specified Hazard.

### Example


```python
import procore_sdk
from procore_sdk.models.hazard1 import Hazard1
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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Hazard ID

    try:
        # Show Hazard
        api_response = api_instance.rest_v10_companies_company_id_hazards_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Hazard ID | 

### Return type

[**Hazard1**](Hazard1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_hazards_id_patch**
> Hazard1 rest_v10_companies_company_id_hazards_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_hazards_id_patch_request)

Update Hazard

Updates a Hazard. Note that Procore provided Hazards' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.hazard1 import Hazard1
from procore_sdk.models.rest_v10_companies_company_id_hazards_id_patch_request import RestV10CompaniesCompanyIdHazardsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Hazard ID
    rest_v10_companies_company_id_hazards_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdHazardsIdPatchRequest() # RestV10CompaniesCompanyIdHazardsIdPatchRequest | 

    try:
        # Update Hazard
        api_response = api_instance.rest_v10_companies_company_id_hazards_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_hazards_id_patch_request)
        print("The response of QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Hazard ID | 
 **rest_v10_companies_company_id_hazards_id_patch_request** | [**RestV10CompaniesCompanyIdHazardsIdPatchRequest**](RestV10CompaniesCompanyIdHazardsIdPatchRequest.md)|  | 

### Return type

[**Hazard1**](Hazard1.md)

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

# **rest_v10_companies_company_id_hazards_post**
> Hazard1 rest_v10_companies_company_id_hazards_post(procore_company_id, company_id, rest_v10_companies_company_id_hazards_post_request)

Create Hazard

Creates a Hazard with the specified name.

### Example


```python
import procore_sdk
from procore_sdk.models.hazard1 import Hazard1
from procore_sdk.models.rest_v10_companies_company_id_hazards_post_request import RestV10CompaniesCompanyIdHazardsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsHazardsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_hazards_post_request = procore_sdk.RestV10CompaniesCompanyIdHazardsPostRequest() # RestV10CompaniesCompanyIdHazardsPostRequest | 

    try:
        # Create Hazard
        api_response = api_instance.rest_v10_companies_company_id_hazards_post(procore_company_id, company_id, rest_v10_companies_company_id_hazards_post_request)
        print("The response of QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsHazardsApi->rest_v10_companies_company_id_hazards_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_hazards_post_request** | [**RestV10CompaniesCompanyIdHazardsPostRequest**](RestV10CompaniesCompanyIdHazardsPostRequest.md)|  | 

### Return type

[**Hazard1**](Hazard1.md)

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

