# procore_sdk.QualitySafetyObservationsCompanyObservationTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_observation_types_get**](QualitySafetyObservationsCompanyObservationTypesApi.md#rest_v10_companies_company_id_observation_types_get) | **GET** /rest/v1.0/companies/{company_id}/observation_types | List Company Observation Types


# **rest_v10_companies_company_id_observation_types_get**
> List[CompanyObservationType] rest_v10_companies_company_id_observation_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List Company Observation Types

Returns a list of all Company Observation Types associated to a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.company_observation_type import CompanyObservationType
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
    api_instance = procore_sdk.QualitySafetyObservationsCompanyObservationTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Company Observation Types
        api_response = api_instance.rest_v10_companies_company_id_observation_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsCompanyObservationTypesApi->rest_v10_companies_company_id_observation_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsCompanyObservationTypesApi->rest_v10_companies_company_id_observation_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[CompanyObservationType]**](CompanyObservationType.md)

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

