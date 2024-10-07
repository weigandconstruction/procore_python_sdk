# procore_sdk.QualitySafetyIncidentsActionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_actions_get**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_incidents_actions_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/actions | List Actions
[**rest_v10_projects_project_id_incidents_actions_id_delete**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_incidents_actions_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/actions/{id} | Destroy Action
[**rest_v10_projects_project_id_incidents_actions_id_get**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_incidents_actions_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/actions/{id} | Show Action
[**rest_v10_projects_project_id_incidents_actions_id_patch**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_incidents_actions_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/actions/{id} | Update Action
[**rest_v10_projects_project_id_incidents_actions_post**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_incidents_actions_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/actions | Create Action
[**rest_v10_projects_project_id_recycle_bin_incidents_actions_get**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_actions_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/actions | List Recycled Actions
[**rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/actions/{id} | Show Recycled Action
[**rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch**](QualitySafetyIncidentsActionsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/actions/{id}/restore | Retrieve Recycled Action
[**rest_v11_projects_project_id_recycle_bin_incidents_actions_get**](QualitySafetyIncidentsActionsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_actions_get) | **GET** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/actions | List Recycled Actions
[**rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get**](QualitySafetyIncidentsActionsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get) | **GET** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/actions/{id} | Show Recycled Action
[**rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch**](QualitySafetyIncidentsActionsApi.md#rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch) | **PATCH** /rest/v1.1/projects/{project_id}/recycle_bin/incidents/actions/{id}/restore | Retrieve Recycled Action


# **rest_v10_projects_project_id_incidents_actions_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner] rest_v10_projects_project_id_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort)

List Actions

Returns a list of Actions for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Actions for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Actions
        api_response = api_instance.rest_v10_projects_project_id_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Actions for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_actions_id_delete**
> rest_v10_projects_project_id_incidents_actions_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Action

Sends the specified Action to the Recycle Bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Action
        api_instance.rest_v10_projects_project_id_incidents_actions_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
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

# **rest_v10_projects_project_id_incidents_actions_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner rest_v10_projects_project_id_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Action

Returns the specified Action

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Action
        api_response = api_instance.rest_v10_projects_project_id_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_actions_id_patch**
> RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner rest_v10_projects_project_id_incidents_actions_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_actions_id_patch_request, incident_id=incident_id, run_configurable_validations=run_configurable_validations)

Update Action

Updates the specified Action

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_actions_id_patch_request import RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    rest_v10_projects_project_id_incidents_actions_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest() # RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Update Action
        api_response = api_instance.rest_v10_projects_project_id_incidents_actions_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_actions_id_patch_request, incident_id=incident_id, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
 **rest_v10_projects_project_id_incidents_actions_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest**](RestV10ProjectsProjectIdIncidentsActionsIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_actions_post**
> RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner rest_v10_projects_project_id_incidents_actions_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_actions_post_request, run_configurable_validations=run_configurable_validations)

Create Action

Creates an Action.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_actions_post_request import RestV10ProjectsProjectIdIncidentsActionsPostRequest
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_actions_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsActionsPostRequest() # RestV10ProjectsProjectIdIncidentsActionsPostRequest | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Create Action
        api_response = api_instance.rest_v10_projects_project_id_incidents_actions_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_actions_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_incidents_actions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_actions_post_request** | [**RestV10ProjectsProjectIdIncidentsActionsPostRequest**](RestV10ProjectsProjectIdIncidentsActionsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_actions_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort, per_page=per_page, page=page)

List Recycled Actions

Returns a list of Recycled Actions for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Actions for a given Incident. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)
    per_page = 56 # int | Elements per page (optional)
    page = 56 # int | Page (optional)

    try:
        # List Recycled Actions
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort, per_page=per_page, page=page)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_recycle_bin_incidents_actions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_recycle_bin_incidents_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Actions for a given Incident. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **page** | **int**| Page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Action

Returns a specific Recycled Action

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Action
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Action

Retrieves a specific Recycled Action from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Action
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
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

# **rest_v11_projects_project_id_recycle_bin_incidents_actions_get**
> List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner] rest_v11_projects_project_id_recycle_bin_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort)

List Recycled Actions

Returns a list of Recycled Actions for a given project (or Incident, if incident_id is present).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Actions for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Actions
        api_response = api_instance.rest_v11_projects_project_id_recycle_bin_incidents_actions_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v11_projects_project_id_recycle_bin_incidents_actions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v11_projects_project_id_recycle_bin_incidents_actions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Actions for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner]**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get**
> RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Action

Returns a specific Recycled Action

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_actions_get200_response_inner import RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Action
        api_response = api_instance.rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsActionsApi->rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner**](RestV11ProjectsProjectIdRecycleBinIncidentsActionsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch**
> rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Action

Retrieves a specific Recycled Action from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsActionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Action ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Action
        api_instance.rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsActionsApi->rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Action ID | 
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

