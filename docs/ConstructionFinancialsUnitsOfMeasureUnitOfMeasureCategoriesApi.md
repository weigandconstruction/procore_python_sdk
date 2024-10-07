# procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitOfMeasureCategoriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_uom_categories_get**](ConstructionFinancialsUnitsOfMeasureUnitOfMeasureCategoriesApi.md#rest_v10_companies_company_id_uom_categories_get) | **GET** /rest/v1.0/companies/{company_id}/uom_categories | List Unit of Measure Categories


# **rest_v10_companies_company_id_uom_categories_get**
> List[RestV10CompaniesCompanyIdUomCategoriesGet200ResponseInner] rest_v10_companies_company_id_uom_categories_get(procore_company_id, company_id)

List Unit of Measure Categories

Returns a list of all Unit of Measure (UOM) Categories.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_uom_categories_get200_response_inner import RestV10CompaniesCompanyIdUomCategoriesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsUnitsOfMeasureUnitOfMeasureCategoriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List Unit of Measure Categories
        api_response = api_instance.rest_v10_companies_company_id_uom_categories_get(procore_company_id, company_id)
        print("The response of ConstructionFinancialsUnitsOfMeasureUnitOfMeasureCategoriesApi->rest_v10_companies_company_id_uom_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsUnitsOfMeasureUnitOfMeasureCategoriesApi->rest_v10_companies_company_id_uom_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdUomCategoriesGet200ResponseInner]**](RestV10CompaniesCompanyIdUomCategoriesGet200ResponseInner.md)

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

