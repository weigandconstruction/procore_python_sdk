# procore_sdk.QualitySafetyIncidentsFilingTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_injury_filing_types_get**](QualitySafetyIncidentsFilingTypesApi.md#rest_v10_companies_company_id_incidents_injury_filing_types_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/injury_filing_types | List Incident Filing Types
[**rest_v10_companies_company_id_incidents_injury_filing_types_id_get**](QualitySafetyIncidentsFilingTypesApi.md#rest_v10_companies_company_id_incidents_injury_filing_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/injury_filing_types/{id} | Show Filing Type
[**rest_v10_companies_company_id_incidents_injury_filing_types_id_patch**](QualitySafetyIncidentsFilingTypesApi.md#rest_v10_companies_company_id_incidents_injury_filing_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/injury_filing_types/{id} | Update Filing Type


# **rest_v10_companies_company_id_incidents_injury_filing_types_get**
> List[IncidentFilingType] rest_v10_companies_company_id_incidents_injury_filing_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)

List Incident Filing Types

Return a list of all Filing Types associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_filing_type import IncidentFilingType
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
    api_instance = procore_sdk.QualitySafetyIncidentsFilingTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Incident Filing Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_injury_filing_types_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[IncidentFilingType]**](IncidentFilingType.md)

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

# **rest_v10_companies_company_id_incidents_injury_filing_types_id_get**
> IncidentFilingType rest_v10_companies_company_id_incidents_injury_filing_types_id_get(procore_company_id, company_id, id)

Show Filing Type

Returns the specified Filing Type.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_filing_type import IncidentFilingType
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
    api_instance = procore_sdk.QualitySafetyIncidentsFilingTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Filing Type ID

    try:
        # Show Filing Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_injury_filing_types_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Filing Type ID | 

### Return type

[**IncidentFilingType**](IncidentFilingType.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_incidents_injury_filing_types_id_patch**
> IncidentFilingType rest_v10_companies_company_id_incidents_injury_filing_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_injury_filing_types_id_patch_request)

Update Filing Type

Updates a specified Filing Type. Note that Procore provided Filing Type names cannot be changed.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_filing_type import IncidentFilingType
from procore_sdk.models.rest_v10_companies_company_id_incidents_injury_filing_types_id_patch_request import RestV10CompaniesCompanyIdIncidentsInjuryFilingTypesIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsFilingTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Filing Type ID
    rest_v10_companies_company_id_incidents_injury_filing_types_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsInjuryFilingTypesIdPatchRequest() # RestV10CompaniesCompanyIdIncidentsInjuryFilingTypesIdPatchRequest | 

    try:
        # Update Filing Type
        api_response = api_instance.rest_v10_companies_company_id_incidents_injury_filing_types_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_injury_filing_types_id_patch_request)
        print("The response of QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsFilingTypesApi->rest_v10_companies_company_id_incidents_injury_filing_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Filing Type ID | 
 **rest_v10_companies_company_id_incidents_injury_filing_types_id_patch_request** | [**RestV10CompaniesCompanyIdIncidentsInjuryFilingTypesIdPatchRequest**](RestV10CompaniesCompanyIdIncidentsInjuryFilingTypesIdPatchRequest.md)|  | 

### Return type

[**IncidentFilingType**](IncidentFilingType.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

