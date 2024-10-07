# procore_sdk.ProjectManagementBiddingBidsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_bids_get**](ProjectManagementBiddingBidsApi.md#rest_v10_companies_company_id_bids_get) | **GET** /rest/v1.0/companies/{company_id}/bids | List Bids within a Company
[**rest_v10_companies_company_id_bids_id_get**](ProjectManagementBiddingBidsApi.md#rest_v10_companies_company_id_bids_id_get) | **GET** /rest/v1.0/companies/{company_id}/bids/{id} | Show a Bid Within a Company
[**rest_v10_companies_company_id_bids_id_patch**](ProjectManagementBiddingBidsApi.md#rest_v10_companies_company_id_bids_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/bids/{id} | Update a Bid within a Company
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bids | List Bids within a Bid Package
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bids/{id} | Show Bids within a Bid package
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bids/{id} | Update a Bid from a Bid Package
[**rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post) | **POST** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/bids | Create bid
[**rest_v10_projects_project_id_bids_get**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bids_get) | **GET** /rest/v1.0/projects/{project_id}/bids | List Bids within a Project
[**rest_v10_projects_project_id_bids_id_get**](ProjectManagementBiddingBidsApi.md#rest_v10_projects_project_id_bids_id_get) | **GET** /rest/v1.0/projects/{project_id}/bids/{id} | Show a Bid within a Project
[**rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch**](ProjectManagementBiddingBidsApi.md#rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/bid_packages/{bid_package_id}/bids/{id} | Update a Bid from a Bid Package


# **rest_v10_companies_company_id_bids_get**
> List[RestV10CompaniesCompanyIdBidsGet200ResponseInner] rest_v10_companies_company_id_bids_get(procore_company_id, company_id, page=page, per_page=per_page)

List Bids within a Company

Return a list of your assigned Bids within a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bids_get200_response_inner import RestV10CompaniesCompanyIdBidsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Bids within a Company
        api_response = api_instance.rest_v10_companies_company_id_bids_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdBidsGet200ResponseInner]**](RestV10CompaniesCompanyIdBidsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_bids_id_get**
> Bid rest_v10_companies_company_id_bids_id_get(procore_company_id, id, company_id)

Show a Bid Within a Company

Return detailed information about a specified Bid.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show a Bid Within a Company
        api_response = api_instance.rest_v10_companies_company_id_bids_id_get(procore_company_id, id, company_id)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**Bid**](Bid.md)

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

# **rest_v10_companies_company_id_bids_id_patch**
> Bid rest_v10_companies_company_id_bids_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_bids_id_patch_request)

Update a Bid within a Company

Update a Bid at a company level.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
from procore_sdk.models.rest_v10_companies_company_id_bids_id_patch_request import RestV10CompaniesCompanyIdBidsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_bids_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdBidsIdPatchRequest() # RestV10CompaniesCompanyIdBidsIdPatchRequest | 

    try:
        # Update a Bid within a Company
        api_response = api_instance.rest_v10_companies_company_id_bids_id_patch(procore_company_id, id, company_id, rest_v10_companies_company_id_bids_id_patch_request)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_companies_company_id_bids_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_bids_id_patch_request** | [**RestV10CompaniesCompanyIdBidsIdPatchRequest**](RestV10CompaniesCompanyIdBidsIdPatchRequest.md)|  | 

### Return type

[**Bid**](Bid.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get**
> List[RestV10CompaniesCompanyIdBidsGet200ResponseInner] rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get(procore_company_id, project_id, bid_package_id, page=page, per_page=per_page)

List Bids within a Bid Package

Return a list of your assigned Bids within a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bids_get200_response_inner import RestV10CompaniesCompanyIdBidsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Bids within a Bid Package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get(procore_company_id, project_id, bid_package_id, page=page, per_page=per_page)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdBidsGet200ResponseInner]**](RestV10CompaniesCompanyIdBidsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get**
> Bid rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get(procore_company_id, project_id, bid_package_id, id)

Show Bids within a Bid package

Return information on a Bid from a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    id = 56 # int | ID

    try:
        # Show Bids within a Bid package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get(procore_company_id, project_id, bid_package_id, id)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **id** | **int**| ID | 

### Return type

[**Bid**](Bid.md)

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

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch**
> Bid rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch(procore_company_id, project_id, bid_package_id, id, rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request)

Update a Bid from a Bid Package

Update a Bid with a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    id = 56 # int | ID
    rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request = procore_sdk.RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest() # RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest | 

    try:
        # Update a Bid from a Bid Package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch(procore_company_id, project_id, bid_package_id, id, rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **id** | **int**| ID | 
 **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request** | [**RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest**](RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest.md)|  | 

### Return type

[**Bid**](Bid.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post**
> Bid rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post(procore_company_id, project_id, bid_package_id, rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request)

Create bid

Create a Bid within a Bid Package. To submit a bid in Bid Management 2.0, a bid form must exist since the bid will be submitted against the bid form.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request = procore_sdk.RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest() # RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest | 

    try:
        # Create bid
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post(procore_company_id, project_id, bid_package_id, rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request** | [**RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest**](RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequest.md)|  | 

### Return type

[**Bid**](Bid.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bids_get**
> List[RestV10CompaniesCompanyIdBidsGet200ResponseInner] rest_v10_projects_project_id_bids_get(procore_company_id, project_id, page=page, per_page=per_page)

List Bids within a Project

Return a list of your assigned Bids within a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_bids_get200_response_inner import RestV10CompaniesCompanyIdBidsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Bids within a Project
        api_response = api_instance.rest_v10_projects_project_id_bids_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdBidsGet200ResponseInner]**](RestV10CompaniesCompanyIdBidsGet200ResponseInner.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bids_id_get**
> Bid rest_v10_projects_project_id_bids_id_get(procore_company_id, project_id, id)

Show a Bid within a Project

Return information on a Bid from a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show a Bid within a Project
        api_response = api_instance.rest_v10_projects_project_id_bids_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bids_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v10_projects_project_id_bids_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**Bid**](Bid.md)

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

# **rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch**
> Bid rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch(procore_company_id, project_id, bid_package_id, id, rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request)

Update a Bid from a Bid Package

Update a Bid with a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.bid import Bid
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request import RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest
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
    api_instance = procore_sdk.ProjectManagementBiddingBidsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    id = 56 # int | ID
    rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request = procore_sdk.RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest() # RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest | 

    try:
        # Update a Bid from a Bid Package
        api_response = api_instance.rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch(procore_company_id, project_id, bid_package_id, id, rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request)
        print("The response of ProjectManagementBiddingBidsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingBidsApi->rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **bid_package_id** | **int**| Bid Package ID | 
 **id** | **int**| ID | 
 **rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request** | [**RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest**](RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequest.md)|  | 

### Return type

[**Bid**](Bid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

