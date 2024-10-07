# procore_sdk.QualitySafetyInspectionsAlternativeResponseSetsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_checklist_alternative_response_sets_get**](QualitySafetyInspectionsAlternativeResponseSetsApi.md#rest_v10_companies_company_id_checklist_alternative_response_sets_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/alternative_response_sets | List Alternative Response Sets
[**rest_v10_companies_company_id_checklist_alternative_response_sets_id_get**](QualitySafetyInspectionsAlternativeResponseSetsApi.md#rest_v10_companies_company_id_checklist_alternative_response_sets_id_get) | **GET** /rest/v1.0/companies/{company_id}/checklist/alternative_response_sets/{id} | Show Alternative Response Set


# **rest_v10_companies_company_id_checklist_alternative_response_sets_get**
> List[ChecklistAlternativeResponseSetFull] rest_v10_companies_company_id_checklist_alternative_response_sets_get(procore_company_id, company_id)

List Alternative Response Sets

Lists Alternative Response Sets for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_alternative_response_set_full import ChecklistAlternativeResponseSetFull
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
    api_instance = procore_sdk.QualitySafetyInspectionsAlternativeResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List Alternative Response Sets
        api_response = api_instance.rest_v10_companies_company_id_checklist_alternative_response_sets_get(procore_company_id, company_id)
        print("The response of QualitySafetyInspectionsAlternativeResponseSetsApi->rest_v10_companies_company_id_checklist_alternative_response_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsAlternativeResponseSetsApi->rest_v10_companies_company_id_checklist_alternative_response_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[ChecklistAlternativeResponseSetFull]**](ChecklistAlternativeResponseSetFull.md)

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

# **rest_v10_companies_company_id_checklist_alternative_response_sets_id_get**
> ChecklistAlternativeResponseSetFull rest_v10_companies_company_id_checklist_alternative_response_sets_id_get(procore_company_id, id, company_id)

Show Alternative Response Set

Returns a specified Alternative Response Set. The set includes alternative terms to represent conforming and deficient item responses, e.g. \"Safe\" instead of \"Pass\" for an item with an internal status of \"yes\". The global attribute indicates whether a response set has been provided by Procore.

### Example


```python
import procore_sdk
from procore_sdk.models.checklist_alternative_response_set_full import ChecklistAlternativeResponseSetFull
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
    api_instance = procore_sdk.QualitySafetyInspectionsAlternativeResponseSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Alternative Response Set ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Alternative Response Set
        api_response = api_instance.rest_v10_companies_company_id_checklist_alternative_response_sets_id_get(procore_company_id, id, company_id)
        print("The response of QualitySafetyInspectionsAlternativeResponseSetsApi->rest_v10_companies_company_id_checklist_alternative_response_sets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsAlternativeResponseSetsApi->rest_v10_companies_company_id_checklist_alternative_response_sets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Alternative Response Set ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**ChecklistAlternativeResponseSetFull**](ChecklistAlternativeResponseSetFull.md)

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

