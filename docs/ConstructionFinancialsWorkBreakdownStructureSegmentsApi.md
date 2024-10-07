# procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_work_breakdown_structure_segments_get**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments | List Company WBS Segments
[**rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{id} | Delete WBS Segment
[**rest_v10_companies_company_id_work_breakdown_structure_segments_id_get**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_id_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{id} | Show Company WBS Segment
[**rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{id} | Update Company WBS Segment
[**rest_v10_companies_company_id_work_breakdown_structure_segments_post**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_post) | **POST** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments | Create a Company WBS Segment
[**rest_v10_projects_project_id_work_breakdown_structure_segments_get**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_get) | **GET** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments | List Project WBS Segments
[**rest_v10_projects_project_id_work_breakdown_structure_segments_id_get**](ConstructionFinancialsWorkBreakdownStructureSegmentsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_id_get) | **GET** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{id} | Show Project WBS Segment


# **rest_v10_companies_company_id_work_breakdown_structure_segments_get**
> List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner] rest_v10_companies_company_id_work_breakdown_structure_segments_get(procore_company_id, company_id)

List Company WBS Segments

All Segments for a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List Company WBS Segments
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_get(procore_company_id, company_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete**
> rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete(procore_company_id, company_id, id, segment_item_list_id=segment_item_list_id)

Delete WBS Segment

Delete WBS Segment

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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID
    segment_item_list_id = 56 # int | Segment Item List ID (optional)

    try:
        # Delete WBS Segment
        api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete(procore_company_id, company_id, id, segment_item_list_id=segment_item_list_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 
 **segment_item_list_id** | **int**| Segment Item List ID | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_id_get**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response rest_v10_companies_company_id_work_breakdown_structure_segments_id_get(procore_company_id, company_id, id, segment_item_list_id=segment_item_list_id)

Show Company WBS Segment

Show a company level segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_id_get200_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID
    segment_item_list_id = 56 # int | Segment Item List ID (optional)

    try:
        # Show Company WBS Segment
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_id_get(procore_company_id, company_id, id, segment_item_list_id=segment_item_list_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 
 **segment_item_list_id** | **int**| Segment Item List ID | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response.md)

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

# **rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch**
> rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch_request, segment_item_list_id=segment_item_list_id)

Update Company WBS Segment

Update company level WBS Segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdPatchRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdPatchRequest | 
    segment_item_list_id = 56 # int | Segment Item List ID (optional)

    try:
        # Update Company WBS Segment
        api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch_request, segment_item_list_id=segment_item_list_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_id_patch_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdPatchRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdPatchRequest.md)|  | 
 **segment_item_list_id** | **int**| Segment Item List ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_post**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner rest_v10_companies_company_id_work_breakdown_structure_segments_post(procore_company_id, company_id, rest_v10_companies_company_id_work_breakdown_structure_segments_post_request)

Create a Company WBS Segment

Create a new company level WBS Segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_post_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    rest_v10_companies_company_id_work_breakdown_structure_segments_post_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsPostRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsPostRequest | 

    try:
        # Create a Company WBS Segment
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_post(procore_company_id, company_id, rest_v10_companies_company_id_work_breakdown_structure_segments_post_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_post_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsPostRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_get**
> List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response] rest_v10_projects_project_id_work_breakdown_structure_segments_get(procore_company_id, project_id)

List Project WBS Segments

All Segments for a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_id_get200_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project WBS Segments
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_get(procore_company_id, project_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response.md)

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

# **rest_v10_projects_project_id_work_breakdown_structure_segments_id_get**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response rest_v10_projects_project_id_work_breakdown_structure_segments_id_get(procore_company_id, project_id, id, legacy_sub_job_id=legacy_sub_job_id)

Show Project WBS Segment

Show a project level segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_id_get200_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    legacy_sub_job_id = 56 # int | Legacy Sub_Job ID (optional)

    try:
        # Show Project WBS Segment
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_id_get(procore_company_id, project_id, id, legacy_sub_job_id=legacy_sub_job_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **legacy_sub_job_id** | **int**| Legacy Sub_Job ID | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsIdGet200Response.md)

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

