# procore_sdk.ProjectManagementBiddingBidPackageDocumentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get**](ProjectManagementBiddingBidPackageDocumentsApi.md#rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get) | **GET** /rest/v1.0/companies/{company_id}/planroom/bid_packages/{bid_package_id}/documents | Gets documents attached to Bid Package


# **rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get**
> RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get(procore_company_id, company_id, bid_package_id)

Gets documents attached to Bid Package

Returns list of all documents attached to Bid Package, with meta information about all drawings

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get200_response import RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingBidPackageDocumentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    bid_package_id = 56 # int | Bid Package ID

    try:
        # Gets documents attached to Bid Package
        api_response = api_instance.rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get(procore_company_id, company_id, bid_package_id)
        print("The response of ProjectManagementBiddingBidPackageDocumentsApi->rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidPackageDocumentsApi->rest_v10_companies_company_id_planroom_bid_packages_bid_package_id_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **bid_package_id** | **int**| Bid Package ID | 

### Return type

[**RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response**](RestV10CompaniesCompanyIdPlanroomBidPackagesBidPackageIdDocumentsGet200Response.md)

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
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

