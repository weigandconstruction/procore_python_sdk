# procore_sdk.ProjectManagementBiddingCompanyBidPackagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get**](ProjectManagementBiddingCompanyBidPackagesApi.md#rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get) | **GET** /rest/v1.0/companies/{company_id}/bid_packages/{bid_package_id}/correspondences | List Correspondences
[**rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get**](ProjectManagementBiddingCompanyBidPackagesApi.md#rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get) | **GET** /rest/v1.0/companies/{company_id}/bid_packages/{bid_package_id}/correspondences/{id} | Show Correspondence
[**rest_v10_companies_company_id_bid_packages_get**](ProjectManagementBiddingCompanyBidPackagesApi.md#rest_v10_companies_company_id_bid_packages_get) | **GET** /rest/v1.0/companies/{company_id}/bid_packages | List Bid Packages
[**rest_v10_companies_company_id_bid_packages_id_get**](ProjectManagementBiddingCompanyBidPackagesApi.md#rest_v10_companies_company_id_bid_packages_id_get) | **GET** /rest/v1.0/companies/{company_id}/bid_packages/{id} | Show Bid Package


# **rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get**
> List[RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner] rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get(procore_company_id, company_id, bid_package_id, page=page, per_page=per_page)

List Correspondences

Return a list of all Correspondences for a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner import RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingCompanyBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    bid_package_id = 56 # int | Bid Package ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Correspondences
        api_response = api_instance.rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get(procore_company_id, company_id, bid_package_id, page=page, per_page=per_page)
        print("The response of ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner]**](RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner.md)

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
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get**
> RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get(procore_company_id, company_id, bid_package_id, id)

Show Correspondence

Return Correspondence detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get200_response_inner import RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingCompanyBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    bid_package_id = 56 # int | Bid Package ID
    id = 56 # int | Correspondence ID

    try:
        # Show Correspondence
        api_response = api_instance.rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get(procore_company_id, company_id, bid_package_id, id)
        print("The response of ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_bid_package_id_correspondences_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **id** | **int**| Correspondence ID | 

### Return type

[**RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner**](RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner.md)

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
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_bid_packages_get**
> RestV10CompaniesCompanyIdBidPackagesGet200Response rest_v10_companies_company_id_bid_packages_get(procore_company_id, company_id, page=page, per_page=per_page, sort=sort)

List Bid Packages

Return a list of Bid Packages for a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bid_packages_get200_response import RestV10CompaniesCompanyIdBidPackagesGet200Response
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
    api_instance = procore_sdk.ProjectManagementBiddingCompanyBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)

    try:
        # List Bid Packages
        api_response = api_instance.rest_v10_companies_company_id_bid_packages_get(procore_company_id, company_id, page=page, per_page=per_page, sort=sort)
        print("The response of ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 

### Return type

[**RestV10CompaniesCompanyIdBidPackagesGet200Response**](RestV10CompaniesCompanyIdBidPackagesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bid Packages listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_bid_packages_id_get**
> RestV10ProjectsProjectIdBidPackagesPost201Response rest_v10_companies_company_id_bid_packages_id_get(procore_company_id, company_id, id)

Show Bid Package

Return Bid Package detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response import RestV10ProjectsProjectIdBidPackagesPost201Response
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
    api_instance = procore_sdk.ProjectManagementBiddingCompanyBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID

    try:
        # Show Bid Package
        api_response = api_instance.rest_v10_companies_company_id_bid_packages_id_get(procore_company_id, company_id, id)
        print("The response of ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingCompanyBidPackagesApi->rest_v10_companies_company_id_bid_packages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdBidPackagesPost201Response**](RestV10ProjectsProjectIdBidPackagesPost201Response.md)

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
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

