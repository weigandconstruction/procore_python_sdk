# procore_sdk.CoreCostCodesSubJobsCostCodesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_cost_codes_copy_from_standard_list_post**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_copy_from_standard_list_post) | **POST** /rest/v1.0/cost_codes/copy_from_standard_list | Copy from Standard Cost Code List
[**rest_v10_cost_codes_copy_subset_from_standard_list_post**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_copy_subset_from_standard_list_post) | **POST** /rest/v1.0/cost_codes/copy_subset_from_standard_list | Copy Subset from Standard Cost Code List
[**rest_v10_cost_codes_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_get) | **GET** /rest/v1.0/cost_codes | List Cost Codes
[**rest_v10_cost_codes_id_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_id_get) | **GET** /rest/v1.0/cost_codes/{id} | Show Cost Code
[**rest_v10_cost_codes_id_patch**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_id_patch) | **PATCH** /rest/v1.0/cost_codes/{id} | Update Cost Code
[**rest_v10_cost_codes_post**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_post) | **POST** /rest/v1.0/cost_codes | Create Cost Code
[**rest_v10_cost_codes_sync_patch**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_cost_codes_sync_patch) | **PATCH** /rest/v1.0/cost_codes/sync | Sync Cost Codes
[**rest_v10_standard_cost_code_lists_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_code_lists_get) | **GET** /rest/v1.0/standard_cost_code_lists | List Standard Cost Code Lists
[**rest_v10_standard_cost_code_lists_id_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_code_lists_id_get) | **GET** /rest/v1.0/standard_cost_code_lists/{id} | Show Standard Cost Code List
[**rest_v10_standard_cost_code_lists_id_patch**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_code_lists_id_patch) | **PATCH** /rest/v1.0/standard_cost_code_lists/{id} | Update Standard Cost Code List
[**rest_v10_standard_cost_code_lists_post**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_code_lists_post) | **POST** /rest/v1.0/standard_cost_code_lists | Create Standard Cost Code List
[**rest_v10_standard_cost_codes_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_get) | **GET** /rest/v1.0/standard_cost_codes | List Standard Cost Codes
[**rest_v10_standard_cost_codes_id_delete**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_id_delete) | **DELETE** /rest/v1.0/standard_cost_codes/{id} | Delete Standard Cost Code
[**rest_v10_standard_cost_codes_id_get**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_id_get) | **GET** /rest/v1.0/standard_cost_codes/{id} | Show Standard Cost Code
[**rest_v10_standard_cost_codes_id_patch**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_id_patch) | **PATCH** /rest/v1.0/standard_cost_codes/{id} | Update Standard Cost Code
[**rest_v10_standard_cost_codes_post**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_post) | **POST** /rest/v1.0/standard_cost_codes | Create Standard Cost Code
[**rest_v10_standard_cost_codes_sync_patch**](CoreCostCodesSubJobsCostCodesApi.md#rest_v10_standard_cost_codes_sync_patch) | **PATCH** /rest/v1.0/standard_cost_codes/sync | Sync Standard Cost Codes


# **rest_v10_cost_codes_copy_from_standard_list_post**
> List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner] rest_v10_cost_codes_copy_from_standard_list_post(procore_company_id, body99)

Copy from Standard Cost Code List

Copy Cost Codes from Standard Cost Code List.

### Example


```python
import procore_sdk
from procore_sdk.models.body99 import Body99
from procore_sdk.models.rest_v10_projects_project_id_timesheets_scoped_cost_codes_get200_response_inner import RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body99 = procore_sdk.Body99() # Body99 | 

    try:
        # Copy from Standard Cost Code List
        api_response = api_instance.rest_v10_cost_codes_copy_from_standard_list_post(procore_company_id, body99)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_copy_from_standard_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_copy_from_standard_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body99** | [**Body99**](Body99.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cost Codes were copied successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_cost_codes_copy_subset_from_standard_list_post**
> RestV10CostCodesCopySubsetFromStandardListPost201Response rest_v10_cost_codes_copy_subset_from_standard_list_post(procore_company_id, rest_v10_cost_codes_copy_subset_from_standard_list_post_request=rest_v10_cost_codes_copy_subset_from_standard_list_post_request)

Copy Subset from Standard Cost Code List

Copy a subset of Cost Codes from Standard Cost Code List.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post201_response import RestV10CostCodesCopySubsetFromStandardListPost201Response
from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post_request import RestV10CostCodesCopySubsetFromStandardListPostRequest
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_cost_codes_copy_subset_from_standard_list_post_request = procore_sdk.RestV10CostCodesCopySubsetFromStandardListPostRequest() # RestV10CostCodesCopySubsetFromStandardListPostRequest |  (optional)

    try:
        # Copy Subset from Standard Cost Code List
        api_response = api_instance.rest_v10_cost_codes_copy_subset_from_standard_list_post(procore_company_id, rest_v10_cost_codes_copy_subset_from_standard_list_post_request=rest_v10_cost_codes_copy_subset_from_standard_list_post_request)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_copy_subset_from_standard_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_copy_subset_from_standard_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_cost_codes_copy_subset_from_standard_list_post_request** | [**RestV10CostCodesCopySubsetFromStandardListPostRequest**](RestV10CostCodesCopySubsetFromStandardListPostRequest.md)|  | [optional] 

### Return type

[**RestV10CostCodesCopySubsetFromStandardListPost201Response**](RestV10CostCodesCopySubsetFromStandardListPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | All of the Standard Cost Codes in the subset were copied successfully |  -  |
**207** | Only part of the Standard Cost Codes subset was copied successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_cost_codes_get**
> List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner] rest_v10_cost_codes_get(procore_company_id, project_id, sub_job_id=sub_job_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id, view=view)

List Cost Codes

Returns a list of Cost Codes.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_timesheets_scoped_cost_codes_get200_response_inner import RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    sub_job_id = 56 # int | Unique identifier for the Sub Job (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. (optional)

    try:
        # List Cost Codes
        api_response = api_instance.rest_v10_cost_codes_get(procore_company_id, project_id, sub_job_id=sub_job_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **sub_job_id** | **int**| Unique identifier for the Sub Job | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md)

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

# **rest_v10_cost_codes_id_get**
> Extended rest_v10_cost_codes_id_get(procore_company_id, id, project_id, sub_job_id=sub_job_id)

Show Cost Code

Returns details on a specific Cost Code.

### Example


```python
import procore_sdk
from procore_sdk.models.extended import Extended
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the Cost Code
    project_id = 56 # int | Unique identifier for the project.
    sub_job_id = 56 # int | Unique identifier for the Sub Job (optional)

    try:
        # Show Cost Code
        api_response = api_instance.rest_v10_cost_codes_id_get(procore_company_id, id, project_id, sub_job_id=sub_job_id)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the Cost Code | 
 **project_id** | **int**| Unique identifier for the project. | 
 **sub_job_id** | **int**| Unique identifier for the Sub Job | [optional] 

### Return type

[**Extended**](Extended.md)

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

# **rest_v10_cost_codes_id_patch**
> Extended rest_v10_cost_codes_id_patch(procore_company_id, id, body98)

Update Cost Code

Update a specific Cost Code.

### Example


```python
import procore_sdk
from procore_sdk.models.body98 import Body98
from procore_sdk.models.extended import Extended
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the Cost Code
    body98 = procore_sdk.Body98() # Body98 | 

    try:
        # Update Cost Code
        api_response = api_instance.rest_v10_cost_codes_id_patch(procore_company_id, id, body98)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the Cost Code | 
 **body98** | [**Body98**](Body98.md)|  | 

### Return type

[**Extended**](Extended.md)

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

# **rest_v10_cost_codes_post**
> Extended rest_v10_cost_codes_post(procore_company_id, body98)

Create Cost Code

Create a new Cost Code.

### Example


```python
import procore_sdk
from procore_sdk.models.body98 import Body98
from procore_sdk.models.extended import Extended
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body98 = procore_sdk.Body98() # Body98 | 

    try:
        # Create Cost Code
        api_response = api_instance.rest_v10_cost_codes_post(procore_company_id, body98)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body98** | [**Body98**](Body98.md)|  | 

### Return type

[**Extended**](Extended.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_cost_codes_sync_patch**
> ArrayOfCostCodes rest_v10_cost_codes_sync_patch(procore_company_id, project_id, cost_code_sync_body, sub_job_id=sub_job_id)

Sync Cost Codes

This endpoint creates or updates a batch of Cost Codes. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_cost_codes import ArrayOfCostCodes
from procore_sdk.models.cost_code_sync_body import CostCodeSyncBody
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    cost_code_sync_body = procore_sdk.CostCodeSyncBody() # CostCodeSyncBody | 
    sub_job_id = 56 # int | Unique identifier for the Sub Job (optional)

    try:
        # Sync Cost Codes
        api_response = api_instance.rest_v10_cost_codes_sync_patch(procore_company_id, project_id, cost_code_sync_body, sub_job_id=sub_job_id)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_cost_codes_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **cost_code_sync_body** | [**CostCodeSyncBody**](CostCodeSyncBody.md)|  | 
 **sub_job_id** | **int**| Unique identifier for the Sub Job | [optional] 

### Return type

[**ArrayOfCostCodes**](ArrayOfCostCodes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Cost Codes |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_standard_cost_code_lists_get**
> List[StandardCostCodeList] rest_v10_standard_cost_code_lists_get(procore_company_id, company_id, page=page, per_page=per_page)

List Standard Cost Code Lists

Return a list of all Standard Cost Code Lists at the Company level. Deprecation Note: Please find the replacement endpoint in the Work Breakdown Structure documents. This endpoint will be replaced with the List Company WBS Segment Item Lists Endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.standard_cost_code_list import StandardCostCodeList
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Standard Cost Code Lists
        api_response = api_instance.rest_v10_standard_cost_code_lists_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[StandardCostCodeList]**](StandardCostCodeList.md)

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

# **rest_v10_standard_cost_code_lists_id_get**
> StandardCostCodeList2 rest_v10_standard_cost_code_lists_id_get(procore_company_id, id, company_id)

Show Standard Cost Code List

Return detailed information on a Standard Cost Code List at the Company level.

### Example


```python
import procore_sdk
from procore_sdk.models.standard_cost_code_list2 import StandardCostCodeList2
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the Standard Cost Code
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Standard Cost Code List
        api_response = api_instance.rest_v10_standard_cost_code_lists_id_get(procore_company_id, id, company_id)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the Standard Cost Code | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**StandardCostCodeList2**](StandardCostCodeList2.md)

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

# **rest_v10_standard_cost_code_lists_id_patch**
> StandardCostCodeList3 rest_v10_standard_cost_code_lists_id_patch(procore_company_id, id, body101)

Update Standard Cost Code List

Update a Standard Cost Code List at the Company level.

### Example


```python
import procore_sdk
from procore_sdk.models.body101 import Body101
from procore_sdk.models.standard_cost_code_list3 import StandardCostCodeList3
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Unique identifier for the Standard Cost Code
    body101 = procore_sdk.Body101() # Body101 | 

    try:
        # Update Standard Cost Code List
        api_response = api_instance.rest_v10_standard_cost_code_lists_id_patch(procore_company_id, id, body101)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Unique identifier for the Standard Cost Code | 
 **body101** | [**Body101**](Body101.md)|  | 

### Return type

[**StandardCostCodeList3**](StandardCostCodeList3.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_standard_cost_code_lists_post**
> StandardCostCodeList2 rest_v10_standard_cost_code_lists_post(procore_company_id, body100)

Create Standard Cost Code List

Create a new Standard Cost Code List at the Company level.

### Example


```python
import procore_sdk
from procore_sdk.models.body100 import Body100
from procore_sdk.models.standard_cost_code_list2 import StandardCostCodeList2
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body100 = procore_sdk.Body100() # Body100 | 

    try:
        # Create Standard Cost Code List
        api_response = api_instance.rest_v10_standard_cost_code_lists_post(procore_company_id, body100)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_code_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body100** | [**Body100**](Body100.md)|  | 

### Return type

[**StandardCostCodeList2**](StandardCostCodeList2.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_standard_cost_codes_get**
> List[StandardCostCode] rest_v10_standard_cost_codes_get(procore_company_id, company_id, standard_cost_code_list_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id, view=view)

List Standard Cost Codes

Return a list of all Standard Cost Codes in a specified Standard Cost Code list.

### Example


```python
import procore_sdk
from procore_sdk.models.standard_cost_code import StandardCostCode
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    standard_cost_code_list_id = 56 # int | Standard Cost Code List ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    view = 'view_example' # str | The 'default' view only returns id and standard_cost_code_list_id. The 'compact' view also includes origin_id. The 'extended' view includes the more complete list of attributes shown below. The 'extended' view is used when no value is passed in for this parameter. (optional)

    try:
        # List Standard Cost Codes
        api_response = api_instance.rest_v10_standard_cost_codes_get(procore_company_id, company_id, standard_cost_code_list_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **standard_cost_code_list_id** | **int**| Standard Cost Code List ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **view** | **str**| The &#39;default&#39; view only returns id and standard_cost_code_list_id. The &#39;compact&#39; view also includes origin_id. The &#39;extended&#39; view includes the more complete list of attributes shown below. The &#39;extended&#39; view is used when no value is passed in for this parameter. | [optional] 

### Return type

[**List[StandardCostCode]**](StandardCostCode.md)

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

# **rest_v10_standard_cost_codes_id_delete**
> StandardCostCode rest_v10_standard_cost_codes_id_delete(procore_company_id, id, company_id)

Delete Standard Cost Code

Delete a Standard Cost Code for ERP integrated companies and standard cost code lists. Deprecation Note: Please find the replacement endpoint in the Work Breakdown Structure documents. This endpoint will be replaced with the Delete Company Segment Item Endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.standard_cost_code import StandardCostCode
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete Standard Cost Code
        api_response = api_instance.rest_v10_standard_cost_codes_id_delete(procore_company_id, id, company_id)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**StandardCostCode**](StandardCostCode.md)

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

# **rest_v10_standard_cost_codes_id_get**
> StandardCostCode rest_v10_standard_cost_codes_id_get(procore_company_id, id, company_id, standard_cost_code_list_id, view=view)

Show Standard Cost Code

Return information about a Standard Cost Code from a specified Standard Cost Code list.

### Example


```python
import procore_sdk
from procore_sdk.models.standard_cost_code import StandardCostCode
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    company_id = 56 # int | Unique identifier for the company.
    standard_cost_code_list_id = 56 # int | The ID of the Standard Cost Code List
    view = 'view_example' # str | The 'default' view only returns id and standard_cost_code_list_id. The 'compact' view also includes origin_id. The 'extended' view includes the more complete list of attributes shown below. The 'extended' view is used when no value is passed in for this parameter. (optional)

    try:
        # Show Standard Cost Code
        api_response = api_instance.rest_v10_standard_cost_codes_id_get(procore_company_id, id, company_id, standard_cost_code_list_id, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **standard_cost_code_list_id** | **int**| The ID of the Standard Cost Code List | 
 **view** | **str**| The &#39;default&#39; view only returns id and standard_cost_code_list_id. The &#39;compact&#39; view also includes origin_id. The &#39;extended&#39; view includes the more complete list of attributes shown below. The &#39;extended&#39; view is used when no value is passed in for this parameter. | [optional] 

### Return type

[**StandardCostCode**](StandardCostCode.md)

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

# **rest_v10_standard_cost_codes_id_patch**
> StandardCostCode rest_v10_standard_cost_codes_id_patch(procore_company_id, id, body103, view=view)

Update Standard Cost Code

Update a Standard Cost Code.

### Example


```python
import procore_sdk
from procore_sdk.models.body103 import Body103
from procore_sdk.models.standard_cost_code import StandardCostCode
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body103 = procore_sdk.Body103() # Body103 | 
    view = 'view_example' # str | The 'default' view only returns id and standard_cost_code_list_id. The 'compact' view also includes origin_id. The 'extended' view includes the more complete list of attributes shown below. The 'extended' view is used when no value is passed in for this parameter. (optional)

    try:
        # Update Standard Cost Code
        api_response = api_instance.rest_v10_standard_cost_codes_id_patch(procore_company_id, id, body103, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body103** | [**Body103**](Body103.md)|  | 
 **view** | **str**| The &#39;default&#39; view only returns id and standard_cost_code_list_id. The &#39;compact&#39; view also includes origin_id. The &#39;extended&#39; view includes the more complete list of attributes shown below. The &#39;extended&#39; view is used when no value is passed in for this parameter. | [optional] 

### Return type

[**StandardCostCode**](StandardCostCode.md)

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

# **rest_v10_standard_cost_codes_post**
> StandardCostCode rest_v10_standard_cost_codes_post(procore_company_id, body102, view=view)

Create Standard Cost Code

Create a new Standard Cost Code.

### Example


```python
import procore_sdk
from procore_sdk.models.body102 import Body102
from procore_sdk.models.standard_cost_code import StandardCostCode
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body102 = procore_sdk.Body102() # Body102 | 
    view = 'view_example' # str | The 'default' view only returns id and standard_cost_code_list_id. The 'compact' view also includes origin_id. The 'extended' view includes the more complete list of attributes shown below. The 'extended' view is used when no value is passed in for this parameter. (optional)

    try:
        # Create Standard Cost Code
        api_response = api_instance.rest_v10_standard_cost_codes_post(procore_company_id, body102, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body102** | [**Body102**](Body102.md)|  | 
 **view** | **str**| The &#39;default&#39; view only returns id and standard_cost_code_list_id. The &#39;compact&#39; view also includes origin_id. The &#39;extended&#39; view includes the more complete list of attributes shown below. The &#39;extended&#39; view is used when no value is passed in for this parameter. | [optional] 

### Return type

[**StandardCostCode**](StandardCostCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_standard_cost_codes_sync_patch**
> RestV10StandardCostCodesSyncPatch200Response rest_v10_standard_cost_codes_sync_patch(procore_company_id, standard_cost_code_sync_body, view=view)

Sync Standard Cost Codes

This endpoint creates or updates a batch of Standard Cost Codes. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_standard_cost_codes_sync_patch200_response import RestV10StandardCostCodesSyncPatch200Response
from procore_sdk.models.standard_cost_code_sync_body import StandardCostCodeSyncBody
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
    api_instance = procore_sdk.CoreCostCodesSubJobsCostCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    standard_cost_code_sync_body = procore_sdk.StandardCostCodeSyncBody() # StandardCostCodeSyncBody | 
    view = 'view_example' # str | The 'default' view only returns id and standard_cost_code_list_id. The 'compact' view also includes origin_id. The 'extended' view includes the more complete list of attributes shown below. The 'extended' view is used when no value is passed in for this parameter. (optional)

    try:
        # Sync Standard Cost Codes
        api_response = api_instance.rest_v10_standard_cost_codes_sync_patch(procore_company_id, standard_cost_code_sync_body, view=view)
        print("The response of CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCostCodesSubJobsCostCodesApi->rest_v10_standard_cost_codes_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **standard_cost_code_sync_body** | [**StandardCostCodeSyncBody**](StandardCostCodeSyncBody.md)|  | 
 **view** | **str**| The &#39;default&#39; view only returns id and standard_cost_code_list_id. The &#39;compact&#39; view also includes origin_id. The &#39;extended&#39; view includes the more complete list of attributes shown below. The &#39;extended&#39; view is used when no value is passed in for this parameter. | [optional] 

### Return type

[**RestV10StandardCostCodesSyncPatch200Response**](RestV10StandardCostCodesSyncPatch200Response.md)

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
**413** | Payload Too Large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

