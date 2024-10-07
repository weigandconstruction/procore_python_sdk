# procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch**](ConstructionFinancialsWorkBreakdownStructureCodesApi.md#rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_breakdown_structure/wbs_codes/bulk_create | Bulk Create WBS codes
[**rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get**](ConstructionFinancialsWorkBreakdownStructureCodesApi.md#rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get) | **GET** /rest/v1.0/projects/{project_id}/work_breakdown_structure/wbs_codes | List Project WBS codes
[**rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch**](ConstructionFinancialsWorkBreakdownStructureCodesApi.md#rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_breakdown_structure/wbs_codes/{id} | Update a WBS code
[**rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post**](ConstructionFinancialsWorkBreakdownStructureCodesApi.md#rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post) | **POST** /rest/v1.0/projects/{project_id}/work_breakdown_structure/wbs_codes | Create a WBS Code
[**rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch**](ConstructionFinancialsWorkBreakdownStructureCodesApi.md#rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch) | **PATCH** /rest/v1.0/projects/{project_id}/work_breakdown_structure/wbs_codes/update_all | Bulk update WBS codes


# **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch**
> RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch(procore_company_id, project_id, wbs_code_bulk_create)

Bulk Create WBS codes

Bulk Create WBS codes using the specified segments. If the combination of segments matches an existing WBS Code, the existing code will be updated with the description provided.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch201_response import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response
from procore_sdk.models.wbs_code_bulk_create import WbsCodeBulkCreate
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    wbs_code_bulk_create = procore_sdk.WbsCodeBulkCreate() # WbsCodeBulkCreate | 

    try:
        # Bulk Create WBS codes
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch(procore_company_id, project_id, wbs_code_bulk_create)
        print("The response of ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_bulk_create_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **wbs_code_bulk_create** | [**WbsCodeBulkCreate**](WbsCodeBulkCreate.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesBulkCreatePatch201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get**
> List[RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner] rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get(procore_company_id, project_id, can_select_divisions=can_select_divisions, required_segments=required_segments, filters_status=filters_status, filters_updated_at=filters_updated_at, scope=scope, query=query, page=page, per_page=per_page)

List Project WBS codes

All Work Breakdown Structure codes for a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    can_select_divisions = True # bool | If true, will include WBS Codes with division segment items. Default is true. (optional)
    required_segments = ['required_segments_example'] # List[str] |  (optional)
    filters_status = ['filters_status_example'] # List[str] | Filter results to only return codes with the included statuses. Options are 'active' or 'inactive'. Defaults to returning all results. (optional)
    filters_updated_at = '2023-04-07T09:00:00Z...2023-04-07T17:00:00Z' # str | Filter results to only return codes that were updated within the range of the two specified ISO 8601 timestamps separated by the ... delimiter. (optional)
    scope = 'budget_code' # str | Filter results to only return codes that match the specified WBS scope. (optional)
    query = 'concrete' # str | Searches the WBS code and description values and returns results sorted in descending order of relevance to the search query. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project WBS codes
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get(procore_company_id, project_id, can_select_divisions=can_select_divisions, required_segments=required_segments, filters_status=filters_status, filters_updated_at=filters_updated_at, scope=scope, query=query, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **can_select_divisions** | **bool**| If true, will include WBS Codes with division segment items. Default is true. | [optional] 
 **required_segments** | [**List[str]**](str.md)|  | [optional] 
 **filters_status** | [**List[str]**](str.md)| Filter results to only return codes with the included statuses. Options are &#39;active&#39; or &#39;inactive&#39;. Defaults to returning all results. | [optional] 
 **filters_updated_at** | **str**| Filter results to only return codes that were updated within the range of the two specified ISO 8601 timestamps separated by the ... delimiter. | [optional] 
 **scope** | **str**| Filter results to only return codes that match the specified WBS scope. | [optional] 
 **query** | **str**| Searches the WBS code and description values and returns results sorted in descending order of relevance to the search query. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner]**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch**
> RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch_request)

Update a WBS code

Update a WBS Code with new custom description or status.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch_request import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | WBS Code ID
    rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesIdPatchRequest() # RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesIdPatchRequest | 

    try:
        # Update a WBS code
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| WBS Code ID | 
 **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_id_patch_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesIdPatchRequest**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesIdPatchRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post**
> RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request)

Create a WBS Code

Create a new WBS code using the specified segments.  If the combination of segments matches an existing WBS Code, the existing code will be updated with the description provided.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest() # RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest | 

    try:
        # Create a WBS Code
        api_response = api_instance.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request)
        print("The response of ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch**
> rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch_request)

Bulk update WBS codes

Bulk update WBS Codes with the same status.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch_request import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesUpdateAllPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsWorkBreakdownStructureCodesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch_request = procore_sdk.RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesUpdateAllPatchRequest() # RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesUpdateAllPatchRequest | 

    try:
        # Bulk update WBS codes
        api_instance.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch(procore_company_id, project_id, rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsWorkBreakdownStructureCodesApi->rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_update_all_patch_request** | [**RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesUpdateAllPatchRequest**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesUpdateAllPatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

