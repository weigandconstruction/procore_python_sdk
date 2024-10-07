# procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete) | **DELETE** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items/bulk_destroy | Bulk Delete Company Segment Items
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items | List Company Segment Items
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items/{id} | Delete Company Segment Item
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get) | **GET** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items/{id} | Show Company Segment Item
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items/{id} | Update Company Segment Item
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post) | **POST** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items | Create Company Segment Item
[**rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch) | **PATCH** /rest/v1.0/companies/{company_id}/work_breakdown_structure/segments/{segment_id}/segment_items/update_all | Update All Company Segment Items
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items/bulk_destroy | Bulk Delete Project Segment Items
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get) | **GET** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items | List Project Segment Items
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items/{id} | Delete Project Segment Item
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items/{id} | Update Project Segment Item
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post) | **POST** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items | Create Project Segment Item
[**rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch**](ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi.md#rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_breakdown_structure/segments/{segment_id}/segment_items/update_all | Update All Project Segment Items


# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request)

Bulk Delete Company Segment Items

Bulk Delete Company Segment Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Company Segment Items
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-Status |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get**
> List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner] rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get(procore_company_id, company_id, segment_id, segment_item_list_id=segment_item_list_id, page=page, per_page=per_page)

List Company Segment Items

List Segment Items for a specific segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    segment_item_list_id = 56 # int | Used to filter legacy segment items by list. Required for Cost Codes. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Company Segment Items
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get(procore_company_id, company_id, segment_id, segment_item_list_id=segment_item_list_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **segment_item_list_id** | **int**| Used to filter legacy segment items by list. Required for Cost Codes. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete**
> rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete(procore_company_id, company_id, segment_id, id)

Delete Company Segment Item

Delete a specific Company Segment Item.

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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    id = 56 # int | Segment Item ID

    try:
        # Delete Company Segment Item
        api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete(procore_company_id, company_id, segment_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **id** | **int**| Segment Item ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get(procore_company_id, company_id, segment_id, id, standard_cost_code_list_id=standard_cost_code_list_id)

Show Company Segment Item

Return details on a specific Company Segment Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    id = 56 # int | Segment Item ID
    standard_cost_code_list_id = 56 # int | Standard Cost Code List ID (required for cost codes only) (optional)

    try:
        # Show Company Segment Item
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get(procore_company_id, company_id, segment_id, id, standard_cost_code_list_id=standard_cost_code_list_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **id** | **int**| Segment Item ID | 
 **standard_cost_code_list_id** | **int**| Standard Cost Code List ID (required for cost codes only) | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch(procore_company_id, company_id, segment_id, id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request, standard_cost_code_list_id=standard_cost_code_list_id)

Update Company Segment Item

Update a specific Company Segment Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    id = 56 # int | Segment Item ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest | 
    standard_cost_code_list_id = 56 # int | Standard Cost Code List ID (required for cost codes only) (optional)

    try:
        # Update Company Segment Item
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch(procore_company_id, company_id, segment_id, id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request, standard_cost_code_list_id=standard_cost_code_list_id)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **id** | **int**| Segment Item ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest.md)|  | 
 **standard_cost_code_list_id** | **int**| Standard Cost Code List ID (required for cost codes only) | [optional] 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request)

Create Company Segment Item

Create a Company Segment Item.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest | 

    try:
        # Create Company Segment Item
        api_response = api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch**
> rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request)

Update All Company Segment Items

Update All Segment Items with the same attributes. The endpoint currently handles updating status (deactivating or reactivating) for segment items and their children.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    segment_id = 56 # int | Segment ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest | 

    try:
        # Update All Company Segment Items
        api_instance.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch(procore_company_id, company_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest.md)|  | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete(procore_company_id, project_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request)

Bulk Delete Project Segment Items

Bulk Delete Project Segment Items

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest | 

    try:
        # Bulk Delete Project Segment Items
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete(procore_company_id, project_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDeleteRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-Status |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get**
> List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner] rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get(procore_company_id, project_id, segment_id, legacy_sub_job_id=legacy_sub_job_id, legacy_cost_code_id=legacy_cost_code_id, include_action_policy=include_action_policy, only_active_items=only_active_items, with_descendant_counts=with_descendant_counts, include_sub_job_cost_codes=include_sub_job_cost_codes, page=page, per_page=per_page)

List Project Segment Items

List Segment Items for a specific segment

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    legacy_sub_job_id = 56 # int | Used to filter legacy cost codes by sub job. Default will filter by project. (optional)
    legacy_cost_code_id = 56 # int |  (optional)
    include_action_policy = True # bool |  (optional)
    only_active_items = True # bool |  (optional)
    with_descendant_counts = True # bool |  (optional)
    include_sub_job_cost_codes = True # bool |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Segment Items
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get(procore_company_id, project_id, segment_id, legacy_sub_job_id=legacy_sub_job_id, legacy_cost_code_id=legacy_cost_code_id, include_action_policy=include_action_policy, only_active_items=only_active_items, with_descendant_counts=with_descendant_counts, include_sub_job_cost_codes=include_sub_job_cost_codes, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **legacy_sub_job_id** | **int**| Used to filter legacy cost codes by sub job. Default will filter by project. | [optional] 
 **legacy_cost_code_id** | **int**|  | [optional] 
 **include_action_policy** | **bool**|  | [optional] 
 **only_active_items** | **bool**|  | [optional] 
 **with_descendant_counts** | **bool**|  | [optional] 
 **include_sub_job_cost_codes** | **bool**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete**
> rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete(procore_company_id, project_id, segment_id, id, sub_job_id=sub_job_id)

Delete Project Segment Item

Delete a specific Project Segment Item.

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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    id = 56 # int | Segment Item ID
    sub_job_id = 56 # int | Sub Job ID (required for a sub job's cost codes only) (optional)

    try:
        # Delete Project Segment Item
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete(procore_company_id, project_id, segment_id, id, sub_job_id=sub_job_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **id** | **int**| Segment Item ID | 
 **sub_job_id** | **int**| Sub Job ID (required for a sub job&#39;s cost codes only) | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch(procore_company_id, project_id, segment_id, id, rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request)

Update Project Segment Item

Update a specific Project Segment Item. The ID of the record is subject to change under certain conditions, please store the response accordingly.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request import RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    id = 56 # int | Segment Item ID
    rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest() # RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest | 

    try:
        # Update Project Segment Item
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch(procore_company_id, project_id, segment_id, id, rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **id** | **int**| Segment Item ID | 
 **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest**](RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post**
> RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post(procore_company_id, project_id, segment_id, rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request)

Create Project Segment Item

Create a Project Segment Item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request import RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest() # RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest | 

    try:
        # Create Project Segment Item
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post(procore_company_id, project_id, segment_id, rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest**](RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch**
> rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch(procore_company_id, project_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request)

Update All Project Segment Items

Update All Segment Items with the same attributes. The endpoint currently handles updating status (deactivating or reactivating) for segment items and their children.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    segment_id = 56 # int | Segment ID
    rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request = procore_sdk.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest() # RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest | 

    try:
        # Update All Project Segment Items
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch(procore_company_id, project_id, segment_id, rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureSegmentItemsApi->rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **segment_id** | **int**| Segment ID | 
 **rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest.md)|  | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

