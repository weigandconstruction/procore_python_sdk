# procore_sdk.QualitySafetyObservationsProjectObservationTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_observation_types_get**](QualitySafetyObservationsProjectObservationTypesApi.md#rest_v10_projects_project_id_observation_types_get) | **GET** /rest/v1.0/projects/{project_id}/observation_types | List Project Observation Types
[**rest_v10_projects_project_id_observation_types_id_delete**](QualitySafetyObservationsProjectObservationTypesApi.md#rest_v10_projects_project_id_observation_types_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/observation_types/{id} | Delete Project Observation Type
[**rest_v10_projects_project_id_observation_types_id_patch**](QualitySafetyObservationsProjectObservationTypesApi.md#rest_v10_projects_project_id_observation_types_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/observation_types/{id} | Update Project Observation Type
[**rest_v10_projects_project_id_observation_types_post**](QualitySafetyObservationsProjectObservationTypesApi.md#rest_v10_projects_project_id_observation_types_post) | **POST** /rest/v1.0/projects/{project_id}/observation_types | Create Project Observation Type


# **rest_v10_projects_project_id_observation_types_get**
> List[ProjectObservationType] rest_v10_projects_project_id_observation_types_get(procore_company_id, project_id, page=page, per_page=per_page)

List Project Observation Types

Return a list of all Project Observation Types associated with a Project.

### Example


```python
import procore_sdk
from procore_sdk.models.project_observation_type import ProjectObservationType
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
    api_instance = procore_sdk.QualitySafetyObservationsProjectObservationTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Project Observation Types
        api_response = api_instance.rest_v10_projects_project_id_observation_types_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[ProjectObservationType]**](ProjectObservationType.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_observation_types_id_delete**
> rest_v10_projects_project_id_observation_types_id_delete(procore_company_id, project_id, id)

Delete Project Observation Type

Deletes a Project Observation Type.

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
    api_instance = procore_sdk.QualitySafetyObservationsProjectObservationTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Project Observation Type ID

    try:
        # Delete Project Observation Type
        api_instance.rest_v10_projects_project_id_observation_types_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Project Observation Type ID | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_observation_types_id_patch**
> ProjectObservationType rest_v10_projects_project_id_observation_types_id_patch(procore_company_id, project_id, id, project_observation_type_create_body1)

Update Project Observation Type

Updates a Project Observation Type.

### Example


```python
import procore_sdk
from procore_sdk.models.project_observation_type import ProjectObservationType
from procore_sdk.models.project_observation_type_create_body1 import ProjectObservationTypeCreateBody1
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
    api_instance = procore_sdk.QualitySafetyObservationsProjectObservationTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Project Observation Type ID
    project_observation_type_create_body1 = procore_sdk.ProjectObservationTypeCreateBody1() # ProjectObservationTypeCreateBody1 | 

    try:
        # Update Project Observation Type
        api_response = api_instance.rest_v10_projects_project_id_observation_types_id_patch(procore_company_id, project_id, id, project_observation_type_create_body1)
        print("The response of QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Project Observation Type ID | 
 **project_observation_type_create_body1** | [**ProjectObservationTypeCreateBody1**](ProjectObservationTypeCreateBody1.md)|  | 

### Return type

[**ProjectObservationType**](ProjectObservationType.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_observation_types_post**
> ProjectObservationType rest_v10_projects_project_id_observation_types_post(procore_company_id, project_id, project_observation_type_create_body)

Create Project Observation Type

Creates a Project Observation Type with the specified name/parent_id

### Example


```python
import procore_sdk
from procore_sdk.models.project_observation_type import ProjectObservationType
from procore_sdk.models.project_observation_type_create_body import ProjectObservationTypeCreateBody
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
    api_instance = procore_sdk.QualitySafetyObservationsProjectObservationTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    project_observation_type_create_body = procore_sdk.ProjectObservationTypeCreateBody() # ProjectObservationTypeCreateBody | 

    try:
        # Create Project Observation Type
        api_response = api_instance.rest_v10_projects_project_id_observation_types_post(procore_company_id, project_id, project_observation_type_create_body)
        print("The response of QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyObservationsProjectObservationTypesApi->rest_v10_projects_project_id_observation_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **project_observation_type_create_body** | [**ProjectObservationTypeCreateBody**](ProjectObservationTypeCreateBody.md)|  | 

### Return type

[**ProjectObservationType**](ProjectObservationType.md)

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

