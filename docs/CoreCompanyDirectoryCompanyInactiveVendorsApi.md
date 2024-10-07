# procore_sdk.CoreCompanyDirectoryCompanyInactiveVendorsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_vendors_inactive_get**](CoreCompanyDirectoryCompanyInactiveVendorsApi.md#rest_v10_companies_company_id_vendors_inactive_get) | **GET** /rest/v1.0/companies/{company_id}/vendors/inactive | List company Inactive Vendors
[**rest_v10_companies_company_id_vendors_inactive_id_patch**](CoreCompanyDirectoryCompanyInactiveVendorsApi.md#rest_v10_companies_company_id_vendors_inactive_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/vendors/inactive/{id} | Reactivate company vendor


# **rest_v10_companies_company_id_vendors_inactive_get**
> List[RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner] rest_v10_companies_company_id_vendors_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, sort=sort)

List company Inactive Vendors

Return a list of all Inactive Vendors associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_vendors_inactive_get200_response_inner import RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyInactiveVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)
    sort = 'sort_example' # str | Return items with the specified sort (optional)

    try:
        # List company Inactive Vendors
        api_response = api_instance.rest_v10_companies_company_id_vendors_inactive_get(procore_company_id, company_id, page=page, per_page=per_page, view=view, sort=sort)
        print("The response of CoreCompanyDirectoryCompanyInactiveVendorsApi->rest_v10_companies_company_id_vendors_inactive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyInactiveVendorsApi->rest_v10_companies_company_id_vendors_inactive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 
 **sort** | **str**| Return items with the specified sort | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner]**](RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_vendors_inactive_id_patch**
> RestV10VendorsGet200ResponseInner rest_v10_companies_company_id_vendors_inactive_id_patch(procore_company_id, company_id, id, view=view)

Reactivate company vendor

Reactivate a specified Company Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_vendors_get200_response_inner import RestV10VendorsGet200ResponseInner
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
    api_instance = procore_sdk.CoreCompanyDirectoryCompanyInactiveVendorsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the vendor
    view = 'view_example' # str | Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. (optional)

    try:
        # Reactivate company vendor
        api_response = api_instance.rest_v10_companies_company_id_vendors_inactive_id_patch(procore_company_id, company_id, id, view=view)
        print("The response of CoreCompanyDirectoryCompanyInactiveVendorsApi->rest_v10_companies_company_id_vendors_inactive_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyDirectoryCompanyInactiveVendorsApi->rest_v10_companies_company_id_vendors_inactive_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the vendor | 
 **view** | **str**| Specifies which view of the resource to return (which attributes should be present in the response). The default view is extended. | [optional] 

### Return type

[**RestV10VendorsGet200ResponseInner**](RestV10VendorsGet200ResponseInner.md)

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

