# procore_sdk.QualitySafetyIncidentsWitnessStatementsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_witness_statements_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_incidents_witness_statements_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/witness_statements | List Witness Statements
[**rest_v10_projects_project_id_incidents_witness_statements_id_delete**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_incidents_witness_statements_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/witness_statements/{id} | Destroy Witness Statement
[**rest_v10_projects_project_id_incidents_witness_statements_id_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_incidents_witness_statements_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/witness_statements/{id} | Show Witness Statement
[**rest_v10_projects_project_id_incidents_witness_statements_id_patch**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_incidents_witness_statements_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/witness_statements/{id} | Update Witness Statement
[**rest_v10_projects_project_id_incidents_witness_statements_post**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_incidents_witness_statements_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/witness_statements | Create Witness Statement
[**rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/witness_statements | List Recycled Witness Statements
[**rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/witness_statements/{id} | Show Recycled Witness Statement
[**rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/witness_statements/{id}/restore | Retrieve Recycled Witness Statement
[**rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get) | **GET** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/witness_statements | List Recycled Witness Statements
[**rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get) | **GET** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/witness_statements/{id} | Show Recycled Witness Statement
[**rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch**](QualitySafetyIncidentsWitnessStatementsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch) | **PATCH** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/witness_statements/{id}/restore | Retrieve Recycled Witness Statement


# **rest_v10_projects_project_id_incidents_witness_statements_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner] rest_v10_projects_project_id_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort)

List Witness Statements

Returns a list of Witness Statements for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Witness Statements for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_date_received = '2013-10-20' # date | Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. (optional)
    filters_witness_id = [56] # List[int] | Return item(s) with the specified Witness (Party) ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Witness Statements
        api_response = api_instance.rest_v10_projects_project_id_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Witness Statements for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_date_received** | **date**| Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. | [optional] 
 **filters_witness_id** | [**List[int]**](int.md)| Return item(s) with the specified Witness (Party) ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_witness_statements_id_delete**
> rest_v10_projects_project_id_incidents_witness_statements_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Witness Statement

Sends the specified Witness Statement to the Recycle Bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Witness Statement
        api_instance.rest_v10_projects_project_id_incidents_witness_statements_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_incidents_witness_statements_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner rest_v10_projects_project_id_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Witness Statement

Returns the specified Witness Statement

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Witness Statement
        api_response = api_instance.rest_v10_projects_project_id_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_witness_statements_id_patch**
> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner rest_v10_projects_project_id_incidents_witness_statements_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_witness_statements_id_patch_request, incident_id=incident_id)

Update Witness Statement

Updates the specified Witness Statement

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_witness_statements_id_patch_request import RestV10ProjectsProjectIdIncidentsWitnessStatementsIdPatchRequest
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    rest_v10_projects_project_id_incidents_witness_statements_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsWitnessStatementsIdPatchRequest() # RestV10ProjectsProjectIdIncidentsWitnessStatementsIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Update Witness Statement
        api_response = api_instance.rest_v10_projects_project_id_incidents_witness_statements_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_witness_statements_id_patch_request, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **rest_v10_projects_project_id_incidents_witness_statements_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsWitnessStatementsIdPatchRequest**](RestV10ProjectsProjectIdIncidentsWitnessStatementsIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_incidents_witness_statements_post**
> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner rest_v10_projects_project_id_incidents_witness_statements_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_witness_statements_post_request)

Create Witness Statement

Creates a Witness Statement.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_witness_statements_post_request import RestV10ProjectsProjectIdIncidentsWitnessStatementsPostRequest
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_witness_statements_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsWitnessStatementsPostRequest() # RestV10ProjectsProjectIdIncidentsWitnessStatementsPostRequest | 

    try:
        # Create Witness Statement
        api_response = api_instance.rest_v10_projects_project_id_incidents_witness_statements_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_witness_statements_post_request)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_incidents_witness_statements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_witness_statements_post_request** | [**RestV10ProjectsProjectIdIncidentsWitnessStatementsPostRequest**](RestV10ProjectsProjectIdIncidentsWitnessStatementsPostRequest.md)|  | 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort, page=page, per_page=per_page)

List Recycled Witness Statements

Returns a list of Recycled Witness Statements for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Witness Statements for a given Incident. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_date_received = '2013-10-20' # date | Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. (optional)
    filters_witness_id = [56] # List[int] | Return item(s) with the specified Witness (Party) ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Recycled Witness Statements
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort, page=page, per_page=per_page)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Witness Statements for a given Incident. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_date_received** | **date**| Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. | [optional] 
 **filters_witness_id** | [**List[int]**](int.md)| Return item(s) with the specified Witness (Party) ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Witness Statement

Returns a specific Recycled Witness Statement

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Witness Statement
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Witness Statement

Retrieves a specific Recycled Witness Statement from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Witness Statement
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v10_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner] rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort)

List Recycled Witness Statements

Returns a list of Recycled Witness Statements for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Witness Statements for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_date_received = '2013-10-20' # date | Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. (optional)
    filters_witness_id = [56] # List[int] | Return item(s) with the specified Witness (Party) ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Witness Statements
        api_response = api_instance.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_date_received=filters_date_received, filters_witness_id=filters_witness_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Witness Statements for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_date_received** | **date**| Return item(s) within the specified date received date range. This assumes the dates provided are in the project time zone. | [optional] 
 **filters_witness_id** | [**List[int]**](int.md)| Return item(s) with the specified Witness (Party) ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Witness Statement

Returns a specific Recycled Witness Statement

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Witness Statement
        api_response = api_instance.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsWitnessStatementsApi->rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch**
> rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Witness Statement

Retrieves a specific Recycled Witness Statement from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsWitnessStatementsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Witness Statement ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Witness Statement
        api_instance.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsWitnessStatementsApi->rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Witness Statement ID | 
 **incident_id** | **int**| Incident ID | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

