# procore_sdk.QualitySafetyIncidentsActionTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_action_types_bulk_update_patch**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_bulk_update_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/action_types/bulk_update | Bulk Update Incident Action Types
[**rest_v10_companies_company_id_incidents_action_types_get**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/action_types | List Incident Action Types
[**rest_v10_companies_company_id_incidents_action_types_id_delete**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/incidents/action_types/{id} | Delete Incident Action Type
[**rest_v10_companies_company_id_incidents_action_types_id_get**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/action_types/{id} | Show Incident Action Type
[**rest_v10_companies_company_id_incidents_action_types_id_patch**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/action_types/{id} | Update Incident Action Type
[**rest_v10_companies_company_id_incidents_action_types_post**](QualitySafetyIncidentsActionTypesApi.md#rest_v10_companies_company_id_incidents_action_types_post) | **POST** /rest/v1.0/companies/{company_id}/incidents/action_types | Create Incident Action Type


# **rest_v10_companies_company_id_incidents_action_types_bulk_update_patch**
> List[ActionType] rest_v10_companies_company_id_incidents_action_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_action_types_bulk_update_patch_request)

Bulk Update Incident Action Types

Update multiple Incident Action Types with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.action_type import ActionType
from procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_bulk_update_patch_request import RestV10CompaniesCompanyIdIncidentsActionTypesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_action_types_bulk_update_patch_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsActionTypesBulkUpdatePatchRequest() # RestV10CompaniesCompanyIdIncidentsActionTypesBulkUpdatePatchRequest | 

    try:
        # Bulk Update Incident Action Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_action_types_bulk_update_patch(procore_company_id, company_id, rest_v10_companies_company_id_incidents_action_types_bulk_update_patch_request)
        print("The response of QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_action_types_bulk_update_patch_request** | [**RestV10CompaniesCompanyIdIncidentsActionTypesBulkUpdatePatchRequest**](RestV10CompaniesCompanyIdIncidentsActionTypesBulkUpdatePatchRequest.md)|  | 

### Return type

[**List[ActionType]**](ActionType.md)

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

# **rest_v10_companies_company_id_incidents_action_types_get**
> List[ActionType] rest_v10_companies_company_id_incidents_action_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Incident Action Types

Return a list of all Incident Action Types associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.action_type import ActionType
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_active = True # bool | If true, returns item(s) with a status of 'active'. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Incident Action Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_action_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_active=filters_active, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_get: %s\n" % e)
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

### Return type

[**List[ActionType]**](ActionType.md)

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

# **rest_v10_companies_company_id_incidents_action_types_id_delete**
> rest_v10_companies_company_id_incidents_action_types_id_delete(procore_company_id, company_id, id)

Delete Incident Action Type

Deletes an Incident Action Type. Note that Procore provided Incident Action Types cannot be deleted.

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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Incident Action Type ID

    try:
        # Delete Incident Action Type
        api_instance.rest_v10_companies_company_id_incidents_action_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Incident Action Type ID | 

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

# **rest_v10_companies_company_id_incidents_action_types_id_get**
> ActionType rest_v10_companies_company_id_incidents_action_types_id_get(procore_company_id, company_id, id)

Show Incident Action Type

Returns the specified Incident Action Type.

### Example


```python
import procore_sdk
from procore_sdk.models.action_type import ActionType
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Incident Action Type ID

    try:
        # Show Incident Action Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_action_types_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Incident Action Type ID | 

### Return type

[**ActionType**](ActionType.md)

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

# **rest_v10_companies_company_id_incidents_action_types_id_patch**
> ActionType rest_v10_companies_company_id_incidents_action_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_action_types_post_request)

Update Incident Action Type

Updates a specified Incident Action Type. Note that Procore provided Incident Action Types' names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.action_type import ActionType
from procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request import RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Incident Action Type ID
    rest_v10_companies_company_id_incidents_action_types_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest() # RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest | 

    try:
        # Update Incident Action Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_action_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_action_types_post_request)
        print("The response of QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Incident Action Type ID | 
 **rest_v10_companies_company_id_incidents_action_types_post_request** | [**RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest**](RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest.md)|  | 

### Return type

[**ActionType**](ActionType.md)

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

# **rest_v10_companies_company_id_incidents_action_types_post**
> ActionType rest_v10_companies_company_id_incidents_action_types_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_action_types_post_request)

Create Incident Action Type

Creates an Incident Action Type with the specified name.

### Example


```python
import procore_sdk
from procore_sdk.models.action_type import ActionType
from procore_sdk.models.rest_v10_companies_company_id_incidents_action_types_post_request import RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_incidents_action_types_post_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest() # RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest | 

    try:
        # Create Incident Action Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_action_types_post(procore_company_id, company_id, rest_v10_companies_company_id_incidents_action_types_post_request)
        print("The response of QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionTypesApi->rest_v10_companies_company_id_incidents_action_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_incidents_action_types_post_request** | [**RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest**](RestV10CompaniesCompanyIdIncidentsActionTypesPostRequest.md)|  | 

### Return type

[**ActionType**](ActionType.md)

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

