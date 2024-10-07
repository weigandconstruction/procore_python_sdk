# procore_sdk.QualitySafetyIncidentsNearMissesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_near_misses_get**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_incidents_near_misses_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/near_misses | List Near Misses
[**rest_v10_projects_project_id_incidents_near_misses_id_delete**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_incidents_near_misses_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/near_misses/{id} | Destroy Near Miss
[**rest_v10_projects_project_id_incidents_near_misses_id_get**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_incidents_near_misses_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/near_misses/{id} | Show Near Miss
[**rest_v10_projects_project_id_incidents_near_misses_id_patch**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_incidents_near_misses_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/near_misses/{id} | Update Near Miss
[**rest_v10_projects_project_id_incidents_near_misses_post**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_incidents_near_misses_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/near_misses | Create Near Miss
[**rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/near_misses | List Recycled Near Misses
[**rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/near_misses/{id} | Show Recycled Near Miss
[**rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch**](QualitySafetyIncidentsNearMissesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/near_misses/{id}/restore | Retrieve Recycled Near Miss


# **rest_v10_projects_project_id_incidents_near_misses_get**
> List[RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner] rest_v10_projects_project_id_incidents_near_misses_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_query=filters_query, sort=sort)

List Near Misses

Returns a list of Near Misses for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Near Misses for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_affected_company_id = [56] # List[int] | Array of Company IDs. Returns item(s) with the specified affected Company IDs. (optional)
    filters_affected_party_id = [56] # List[int] | Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. (optional)
    filters_affected_person_id = [56] # List[int] | Array of Person IDs. Returns item(s) with the specified affected Person IDs. (optional)
    filters_harm_source_id = [56] # List[int] | Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. (optional)
    filters_work_activity_id = [56] # List[int] | Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Near Misses
        api_response = api_instance.rest_v10_projects_project_id_incidents_near_misses_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Near Misses for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_affected_company_id** | [**List[int]**](int.md)| Array of Company IDs. Returns item(s) with the specified affected Company IDs. | [optional] 
 **filters_affected_party_id** | [**List[int]**](int.md)| Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. | [optional] 
 **filters_affected_person_id** | [**List[int]**](int.md)| Array of Person IDs. Returns item(s) with the specified affected Person IDs. | [optional] 
 **filters_harm_source_id** | [**List[int]**](int.md)| Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. | [optional] 
 **filters_work_activity_id** | [**List[int]**](int.md)| Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_near_misses_id_delete**
> rest_v10_projects_project_id_incidents_near_misses_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Near Miss

Sends Near Miss to the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Near Miss ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Near Miss
        api_instance.rest_v10_projects_project_id_incidents_near_misses_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Near Miss ID | 
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

# **rest_v10_projects_project_id_incidents_near_misses_id_get**
> RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner rest_v10_projects_project_id_incidents_near_misses_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Near Miss

Returns specific Near Miss

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Near Miss ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Near Miss
        api_response = api_instance.rest_v10_projects_project_id_incidents_near_misses_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Near Miss ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_near_misses_id_patch**
> RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner rest_v10_projects_project_id_incidents_near_misses_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_near_misses_id_patch_request, incident_id=incident_id)

Update Near Miss

Update a Near Miss' attributes

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_id_patch_request import RestV10ProjectsProjectIdIncidentsNearMissesIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Near Miss ID
    rest_v10_projects_project_id_incidents_near_misses_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsNearMissesIdPatchRequest() # RestV10ProjectsProjectIdIncidentsNearMissesIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Update Near Miss
        api_response = api_instance.rest_v10_projects_project_id_incidents_near_misses_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_near_misses_id_patch_request, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Near Miss ID | 
 **rest_v10_projects_project_id_incidents_near_misses_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsNearMissesIdPatchRequest**](RestV10ProjectsProjectIdIncidentsNearMissesIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_near_misses_post**
> RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner rest_v10_projects_project_id_incidents_near_misses_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_near_misses_post_request)

Create Near Miss

Creates a Near Miss record.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_post_request import RestV10ProjectsProjectIdIncidentsNearMissesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_near_misses_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsNearMissesPostRequest() # RestV10ProjectsProjectIdIncidentsNearMissesPostRequest | 

    try:
        # Create Near Miss
        api_response = api_instance.rest_v10_projects_project_id_incidents_near_misses_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_near_misses_post_request)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_incidents_near_misses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_near_misses_post_request** | [**RestV10ProjectsProjectIdIncidentsNearMissesPostRequest**](RestV10ProjectsProjectIdIncidentsNearMissesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get**
> List[RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_query=filters_query, sort=sort, page=page, per_page=per_page)

List Recycled Near Misses

Returns a list of Recycled Near Misses for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Near Misses for a given Incident. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_affected_company_id = [56] # List[int] | Array of Company IDs. Returns item(s) with the specified affected Company IDs. (optional)
    filters_affected_party_id = [56] # List[int] | Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. (optional)
    filters_affected_person_id = [56] # List[int] | Array of Person IDs. Returns item(s) with the specified affected Person IDs. (optional)
    filters_harm_source_id = [56] # List[int] | Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. (optional)
    filters_work_activity_id = [56] # List[int] | Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Recycled Near Misses
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_query=filters_query, sort=sort, page=page, per_page=per_page)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_recycle_bin_incidents_near_misses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Near Misses for a given Incident. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_affected_company_id** | [**List[int]**](int.md)| Array of Company IDs. Returns item(s) with the specified affected Company IDs. | [optional] 
 **filters_affected_party_id** | [**List[int]**](int.md)| Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. | [optional] 
 **filters_affected_person_id** | [**List[int]**](int.md)| Array of Person IDs. Returns item(s) with the specified affected Person IDs. | [optional] 
 **filters_harm_source_id** | [**List[int]**](int.md)| Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. | [optional] 
 **filters_work_activity_id** | [**List[int]**](int.md)| Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get**
> RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Near Miss

Returns a specific Recycled Near Miss

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_near_misses_get200_response_inner import RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Near Miss ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Near Miss
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Near Miss ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsNearMissesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Near Miss

Retrieves a specific Recycled Near Miss from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsNearMissesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Near Miss ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Near Miss
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsNearMissesApi->rest_v10_projects_project_id_recycle_bin_incidents_near_misses_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Near Miss ID | 
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

