# procore_sdk.QualitySafetyIncidentsPropertyDamagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_property_damages_get**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_incidents_property_damages_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages | List Property Damages
[**rest_v10_projects_project_id_incidents_property_damages_id_delete**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_incidents_property_damages_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/property_damages/{id} | Destroy Property Damage
[**rest_v10_projects_project_id_incidents_property_damages_id_get**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_incidents_property_damages_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages/{id} | Show Property Damage
[**rest_v10_projects_project_id_incidents_property_damages_id_patch**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_incidents_property_damages_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/property_damages/{id} | Update Property Damage
[**rest_v10_projects_project_id_incidents_property_damages_post**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_incidents_property_damages_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/property_damages | Create Property Damage
[**rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/property_damages | List Recycled Property Damages
[**rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/property_damages/{id} | Show Recycled Property Damage
[**rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch**](QualitySafetyIncidentsPropertyDamagesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/property_damages/{id}/restore | Retrieve Property Damage


# **rest_v10_projects_project_id_incidents_property_damages_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner] rest_v10_projects_project_id_incidents_property_damages_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_responsible_company_id=filters_responsible_company_id, filters_query=filters_query, sort=sort)

List Property Damages

Returns a list of Property Damage records for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Property Damages for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_responsible_company_id = [56] # List[int] | Return item(s) with the specified Vendor ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Property Damages
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_responsible_company_id=filters_responsible_company_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Property Damages for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_responsible_company_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_property_damages_id_delete**
> rest_v10_projects_project_id_incidents_property_damages_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Property Damage

Sends the specified Property Damage record to the Recycle Bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Property Damage ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Property Damage
        api_instance.rest_v10_projects_project_id_incidents_property_damages_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Property Damage ID | 
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

# **rest_v10_projects_project_id_incidents_property_damages_id_get**
> RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner rest_v10_projects_project_id_incidents_property_damages_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Property Damage

Returns the specified Property Damage record

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Property Damage ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Property Damage
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Property Damage ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_property_damages_id_patch**
> RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner rest_v10_projects_project_id_incidents_property_damages_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_property_damages_id_patch_request, incident_id=incident_id)

Update Property Damage

Updates the specified Property Damage record

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_id_patch_request import RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Property Damage ID
    rest_v10_projects_project_id_incidents_property_damages_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest() # RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Update Property Damage
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_property_damages_id_patch_request, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Property Damage ID | 
 **rest_v10_projects_project_id_incidents_property_damages_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest**](RestV10ProjectsProjectIdIncidentsPropertyDamagesIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_property_damages_post**
> RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner rest_v10_projects_project_id_incidents_property_damages_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_property_damages_post_request)

Create Property Damage

Creates a Property Damage record.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_post_request import RestV10ProjectsProjectIdIncidentsPropertyDamagesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_property_damages_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsPropertyDamagesPostRequest() # RestV10ProjectsProjectIdIncidentsPropertyDamagesPostRequest | 

    try:
        # Create Property Damage
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_property_damages_post_request)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_incidents_property_damages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_property_damages_post_request** | [**RestV10ProjectsProjectIdIncidentsPropertyDamagesPostRequest**](RestV10ProjectsProjectIdIncidentsPropertyDamagesPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_responsible_company_id=filters_responsible_company_id, filters_query=filters_query, sort=sort)

List Recycled Property Damages

Returns a list of Recycled Property Damages for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Property Damages for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_responsible_company_id = [56] # List[int] | Return item(s) with the specified Vendor ID. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing search query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Property Damages
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_responsible_company_id=filters_responsible_company_id, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_recycle_bin_incidents_property_damages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Property Damages for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_responsible_company_id** | [**List[int]**](int.md)| Return item(s) with the specified Vendor ID. | [optional] 
 **filters_query** | **str**| Return item(s) containing search query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get**
> RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Property Damage

Returns specified Recycled Property Damage record

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Property Damage ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Property Damage
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Property Damage ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsPropertyDamagesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Property Damage

Retrieves specified Recycled Property Damage from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Property Damage ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Property Damage
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamagesApi->rest_v10_projects_project_id_recycle_bin_incidents_property_damages_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Property Damage ID | 
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

