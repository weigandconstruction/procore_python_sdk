# procore_sdk.QualitySafetyIncidentsEnvironmentalsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_environmentals_get**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_incidents_environmentals_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals | List Environmentals
[**rest_v10_projects_project_id_incidents_environmentals_id_delete**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_incidents_environmentals_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/environmentals/{id} | Destroy Environmental
[**rest_v10_projects_project_id_incidents_environmentals_id_get**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_incidents_environmentals_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals/{id} | Show Environmental
[**rest_v10_projects_project_id_incidents_environmentals_id_patch**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_incidents_environmentals_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/environmentals/{id} | Update Environmental
[**rest_v10_projects_project_id_incidents_environmentals_post**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_incidents_environmentals_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/environmentals | Create Environmental
[**rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/environmentals | List Recycled Environmentals
[**rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/environmentals/{id} | Show Recycled Environmental
[**rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch**](QualitySafetyIncidentsEnvironmentalsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/environmentals/{id}/restore | Retrieve Environmental


# **rest_v10_projects_project_id_incidents_environmentals_get**
> List[IncidentNormalAllOfEnvironmentalsInner] rest_v10_projects_project_id_incidents_environmentals_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_environmental_type_id=filters_environmental_type_id, filters_query=filters_query, sort=sort)

List Environmentals

Returns a list of Environmental records for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Environmentals for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_environmental_type_id = [56] # List[int] | Return item(s) with the specified Environmental Type ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Environmentals
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_environmental_type_id=filters_environmental_type_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Environmentals for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_environmental_type_id** | [**List[int]**](int.md)| Return item(s) with the specified Environmental Type ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[IncidentNormalAllOfEnvironmentalsInner]**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_incidents_environmentals_id_delete**
> rest_v10_projects_project_id_incidents_environmentals_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Environmental

Sends the specified Environmental record to the Recycle Bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Environmental ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Environmental
        api_instance.rest_v10_projects_project_id_incidents_environmentals_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Environmental ID | 
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

# **rest_v10_projects_project_id_incidents_environmentals_id_get**
> IncidentNormalAllOfEnvironmentalsInner rest_v10_projects_project_id_incidents_environmentals_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Environmental

Returns the specified Environmental record

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Environmental ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Environmental
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Environmental ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**IncidentNormalAllOfEnvironmentalsInner**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_incidents_environmentals_id_patch**
> IncidentNormalAllOfEnvironmentalsInner rest_v10_projects_project_id_incidents_environmentals_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_environmentals_id_patch_request, incident_id=incident_id)

Update Environmental

Updates the Environmental record

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_environmentals_id_patch_request import RestV10ProjectsProjectIdIncidentsEnvironmentalsIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Environmental ID
    rest_v10_projects_project_id_incidents_environmentals_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsEnvironmentalsIdPatchRequest() # RestV10ProjectsProjectIdIncidentsEnvironmentalsIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Update Environmental
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_environmentals_id_patch_request, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Environmental ID | 
 **rest_v10_projects_project_id_incidents_environmentals_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsEnvironmentalsIdPatchRequest**](RestV10ProjectsProjectIdIncidentsEnvironmentalsIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**IncidentNormalAllOfEnvironmentalsInner**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_incidents_environmentals_post**
> IncidentNormalAllOfEnvironmentalsInner rest_v10_projects_project_id_incidents_environmentals_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_environmentals_post_request)

Create Environmental

Creates an Environmental record.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_environmentals_post_request import RestV10ProjectsProjectIdIncidentsEnvironmentalsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_environmentals_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsEnvironmentalsPostRequest() # RestV10ProjectsProjectIdIncidentsEnvironmentalsPostRequest | 

    try:
        # Create Environmental
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_environmentals_post_request)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_incidents_environmentals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_environmentals_post_request** | [**RestV10ProjectsProjectIdIncidentsEnvironmentalsPostRequest**](RestV10ProjectsProjectIdIncidentsEnvironmentalsPostRequest.md)|  | 

### Return type

[**IncidentNormalAllOfEnvironmentalsInner**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get**
> List[IncidentNormalAllOfEnvironmentalsInner] rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_environmental_type_id=filters_environmental_type_id, filters_query=filters_query, sort=sort)

List Recycled Environmentals

Returns a list of Recycled Environmentals for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Environmentals for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_environmental_type_id = [56] # List[int] | Return item(s) with the specified Environmental Type ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Environmentals
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_environmental_type_id=filters_environmental_type_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_recycle_bin_incidents_environmentals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Environmentals for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_environmental_type_id** | [**List[int]**](int.md)| Return item(s) with the specified Environmental Type ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[IncidentNormalAllOfEnvironmentalsInner]**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get**
> IncidentNormalAllOfEnvironmentalsInner rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Environmental

Returns specified Recycled Environmental record

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal_all_of_environmentals_inner import IncidentNormalAllOfEnvironmentalsInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Environmental ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Environmental
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Environmental ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**IncidentNormalAllOfEnvironmentalsInner**](IncidentNormalAllOfEnvironmentalsInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Environmental

Retrieves specified Recycled Environmental from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Environmental ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Environmental
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalsApi->rest_v10_projects_project_id_recycle_bin_incidents_environmentals_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Environmental ID | 
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

