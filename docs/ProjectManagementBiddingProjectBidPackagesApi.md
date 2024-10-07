# procore_sdk.ProjectManagementBiddingProjectBidPackagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/correspondences | List Correspondences
[**rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{bid_package_id}/correspondences/{id} | Show Correspondence
[**rest_v10_projects_project_id_bid_packages_id_get**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v10_projects_project_id_bid_packages_id_get) | **GET** /rest/v1.0/projects/{project_id}/bid_packages/{id} | Show Bid Package
[**rest_v10_projects_project_id_bid_packages_id_patch**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v10_projects_project_id_bid_packages_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/bid_packages/{id} | Update Bid Package
[**rest_v10_projects_project_id_bid_packages_post**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v10_projects_project_id_bid_packages_post) | **POST** /rest/v1.0/projects/{project_id}/bid_packages | Create Bid Package
[**rest_v11_projects_project_id_bid_packages_get**](ProjectManagementBiddingProjectBidPackagesApi.md#rest_v11_projects_project_id_bid_packages_get) | **GET** /rest/v1.1/projects/{project_id}/bid_packages | List Bid Packages


# **rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get**
> List[RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner] rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get(procore_company_id, project_id, bid_package_id, page=page, per_page=per_page)

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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Correspondences
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get(procore_company_id, project_id, bid_package_id, page=page, per_page=per_page)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_get: %s\n" % e)
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

# **rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get**
> RestV10ProjectsProjectIdBidPackagesBidPackageIdCorrespondencesGet200ResponseInner rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get(procore_company_id, project_id, bid_package_id, id)

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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    bid_package_id = 56 # int | Bid Package ID
    id = 56 # int | Correspondence ID

    try:
        # Show Correspondence
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get(procore_company_id, project_id, bid_package_id, id)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_bid_package_id_correspondences_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_projects_project_id_bid_packages_id_get**
> RestV10ProjectsProjectIdBidPackagesPost201Response rest_v10_projects_project_id_bid_packages_id_get(procore_company_id, project_id, id)

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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show Bid Package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
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

# **rest_v10_projects_project_id_bid_packages_id_patch**
> RestV10ProjectsProjectIdBidPackagesPost201Response rest_v10_projects_project_id_bid_packages_id_patch(procore_company_id, project_id, id, body42)

Update Bid Package

Update a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.body42 import Body42
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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    body42 = procore_sdk.Body42() # Body42 | 

    try:
        # Update Bid Package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_id_patch(procore_company_id, project_id, id, body42)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **body42** | [**Body42**](Body42.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBidPackagesPost201Response**](RestV10ProjectsProjectIdBidPackagesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_bid_packages_post**
> RestV10ProjectsProjectIdBidPackagesPost201Response rest_v10_projects_project_id_bid_packages_post(procore_company_id, project_id, body42)

Create Bid Package

Create a Bid Package.

### Example


```python
import procore_sdk
from procore_sdk.models.body42 import Body42
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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body42 = procore_sdk.Body42() # Body42 | 

    try:
        # Create Bid Package
        api_response = api_instance.rest_v10_projects_project_id_bid_packages_post(procore_company_id, project_id, body42)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v10_projects_project_id_bid_packages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body42** | [**Body42**](Body42.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBidPackagesPost201Response**](RestV10ProjectsProjectIdBidPackagesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_bid_packages_get**
> List[RestV11ProjectsProjectIdBidPackagesGet200ResponseInner] rest_v11_projects_project_id_bid_packages_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filter=filter, sort=sort)

List Bid Packages

Return a list of all Bid Packages for a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_get200_response_inner import RestV11ProjectsProjectIdBidPackagesGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementBiddingProjectBidPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | When set to all, both open and closed bid packages will be returned. When set to internal, more keys will be made available for each bid package. When set to use_previous_bidders, a key will be made available that will provide information on whether the bid package has bid forms (optional)
    filter = 'filter_example' # str | Filters down list of bid packages for a project. (optional)
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. Only applies when view=internal. (optional)

    try:
        # List Bid Packages
        api_response = api_instance.rest_v11_projects_project_id_bid_packages_get(procore_company_id, project_id, page=page, per_page=per_page, view=view, filter=filter, sort=sort)
        print("The response of ProjectManagementBiddingProjectBidPackagesApi->rest_v11_projects_project_id_bid_packages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementBiddingProjectBidPackagesApi->rest_v11_projects_project_id_bid_packages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| When set to all, both open and closed bid packages will be returned. When set to internal, more keys will be made available for each bid package. When set to use_previous_bidders, a key will be made available that will provide information on whether the bid package has bid forms | [optional] 
 **filter** | **str**| Filters down list of bid packages for a project. | [optional] 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. Only applies when view&#x3D;internal. | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdBidPackagesGet200ResponseInner]**](RestV11ProjectsProjectIdBidPackagesGet200ResponseInner.md)

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

