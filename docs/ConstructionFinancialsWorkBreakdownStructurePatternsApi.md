# procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_work_breakdown_structure_patterns_get**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_companies_company_id_work_breakdown_structure_patterns_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/patterns | List Company WBS Patterns
[**rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put) | **PUT** /rest/v1.0/companies/{company_id}/work_breakdown_structure/patterns/update_segment_order | Update Company Pattern&#39;s Segment Order
[**rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put) | **PUT** /rest/v1.0/projects/{project_id}/work_breakdown_structure/patterns/add_segment | Add segment to the project pattern
[**rest_v10_projects_project_id_work_breakdown_structure_patterns_get**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_projects_project_id_work_breakdown_structure_patterns_get) | **GET** /rest/v1.0/projects/{project_id}/work_breakdown_structure/patterns | List Project WBS Patterns
[**rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put) | **PUT** /rest/v1.0/projects/{project_id}/work_breakdown_structure/patterns/remove_segment | Remove segment from the project pattern
[**rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put**](ConstructionFinancialsWorkBreakdownStructurePatternsApi.md#rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put) | **PUT** /rest/v1.0/projects/{project_id}/work_breakdown_structure/patterns/update_segment_order | Update Project Pattern&#39;s Segment Order


# **rest_v10_companies_company_id_work_breakdown_structure_patterns_get**
> RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGet200Response rest_v10_companies_company_id_work_breakdown_structure_patterns_get(procore_company_id, company_id)

List Company WBS Patterns

All patterns for a given company

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_patterns_get200_response import RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # List Company WBS Patterns
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_patterns_get(procore_company_id, company_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_companies_company_id_work_breakdown_structure_patterns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_companies_company_id_work_breakdown_structure_patterns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGet200Response**](RestV10CompaniesCompanyIdWorkBreakdownStructurePatternsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put**
> rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put(procore_company_id, company_id, update_segment_order_body)

Update Company Pattern's Segment Order

Updates the segment order on a company pattern

### Example


```python
import procore_sdk
from procore_sdk.models.update_segment_order_body import UpdateSegmentOrderBody
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    update_segment_order_body = procore_sdk.UpdateSegmentOrderBody() # UpdateSegmentOrderBody | 

    try:
        # Update Company Pattern's Segment Order
        api_instance.rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put(procore_company_id, company_id, update_segment_order_body)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_companies_company_id_work_breakdown_structure_patterns_update_segment_order_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **update_segment_order_body** | [**UpdateSegmentOrderBody**](UpdateSegmentOrderBody.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put**
> rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request)

Add segment to the project pattern

Add segment to the project pattern

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request import RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest() # RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest | 

    try:
        # Add segment to the project pattern
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest**](RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest.md)|  | 

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
**204** | No Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_patterns_get**
> RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response rest_v10_projects_project_id_work_breakdown_structure_patterns_get(procore_company_id, project_id)

List Project WBS Patterns

All patterns for a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_patterns_get200_response import RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Project WBS Patterns
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_patterns_get(procore_company_id, project_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_projects_project_id_work_breakdown_structure_patterns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_projects_project_id_work_breakdown_structure_patterns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response**](RestV10ProjectsProjectIdWorkBreakdownStructurePatternsGet200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put**
> rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request)

Remove segment from the project pattern

Remove segment from the project pattern

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request import RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest() # RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest | 

    try:
        # Remove segment from the project pattern
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_projects_project_id_work_breakdown_structure_patterns_remove_segment_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_work_breakdown_structure_patterns_add_segment_put_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest**](RestV10ProjectsProjectIdWorkBreakdownStructurePatternsAddSegmentPutRequest.md)|  | 

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
**204** | No Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put**
> rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put(procore_company_id, project_id, update_segment_order_body)

Update Project Pattern's Segment Order

Updates the segment order on a project pattern

### Example


```python
import procore_sdk
from procore_sdk.models.update_segment_order_body import UpdateSegmentOrderBody
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructurePatternsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    update_segment_order_body = procore_sdk.UpdateSegmentOrderBody() # UpdateSegmentOrderBody | 

    try:
        # Update Project Pattern's Segment Order
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put(procore_company_id, project_id, update_segment_order_body)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructurePatternsApi->rest_v10_projects_project_id_work_breakdown_structure_patterns_update_segment_order_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **update_segment_order_body** | [**UpdateSegmentOrderBody**](UpdateSegmentOrderBody.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

