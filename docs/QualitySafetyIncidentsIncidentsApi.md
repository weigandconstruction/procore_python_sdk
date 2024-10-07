# procore_sdk.QualitySafetyIncidentsIncidentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_get**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_incidents_get) | **GET** /rest/v1.0/projects/{project_id}/incidents | List Incidents
[**rest_v10_projects_project_id_incidents_id_delete**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_incidents_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/{id} | Delete Incident
[**rest_v10_projects_project_id_incidents_id_get**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_incidents_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/{id} | Show Incident
[**rest_v10_projects_project_id_incidents_id_patch**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_incidents_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/{id} | Update Incident
[**rest_v10_projects_project_id_incidents_post**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_incidents_post) | **POST** /rest/v1.0/projects/{project_id}/incidents | Create Incident
[**rest_v10_projects_project_id_recycle_bin_incidents_get**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents | List Recycled Incidents
[**rest_v10_projects_project_id_recycle_bin_incidents_id_get**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/{id} | Show Recycled Incident
[**rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch**](QualitySafetyIncidentsIncidentsApi.md#rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/{id}/restore | Retrieve Recycled Incident


# **rest_v10_projects_project_id_incidents_get**
> List[IncidentCompact] rest_v10_projects_project_id_incidents_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_event_date=filters_event_date, filters_location_id=filters_location_id, filters_status=filters_status, filters_contributing_behavior_id=filters_contributing_behavior_id, filters_contributing_condition_id=filters_contributing_condition_id, filters_hazard_id=filters_hazard_id, filters_time_unknown=filters_time_unknown, filters_recordable=filters_recordable, filters_query=filters_query, sort=sort)

List Incidents

Returns a list of Incidents for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_compact import IncidentCompact
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 1000 # int | Number of items returned per page (Min: 1, Max: 1000). Defaults to 1000 when parameter is not provided. (optional) (default to 1000)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_event_date = '2013-10-20' # date | Returns item(s) with an event date within the specified ISO 8601 datetime range. (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_contributing_behavior_id = [56] # List[int] | Contributing Behavior ID. Returns item(s) with the specified Contributing Behavior ID. (optional)
    filters_contributing_condition_id = [56] # List[int] | Contributing Condition ID. Returns item(s) with the specified Contributing Condition ID. (optional)
    filters_hazard_id = [56] # List[int] | Hazard ID. Returns item(s) with the specified Hazard ID. (optional)
    filters_time_unknown = False # bool | If true, returns item(s) where the time of Incident occurrence is unknown. (optional) (default to False)
    filters_recordable = True # bool | Return item(s) that are recordable. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query. Searchable fields include Incident title, Creator, Witness Statement, Incident Action description, Incident Action Type, Contributing Behavior, Contributing Condition, Hazard, and Location. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Incidents
        api_response = api_instance.rest_v10_projects_project_id_incidents_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_event_date=filters_event_date, filters_location_id=filters_location_id, filters_status=filters_status, filters_contributing_behavior_id=filters_contributing_behavior_id, filters_contributing_condition_id=filters_contributing_condition_id, filters_hazard_id=filters_hazard_id, filters_time_unknown=filters_time_unknown, filters_recordable=filters_recordable, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Number of items returned per page (Min: 1, Max: 1000). Defaults to 1000 when parameter is not provided. | [optional] [default to 1000]
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_event_date** | **date**| Returns item(s) with an event date within the specified ISO 8601 datetime range. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_contributing_behavior_id** | [**List[int]**](int.md)| Contributing Behavior ID. Returns item(s) with the specified Contributing Behavior ID. | [optional] 
 **filters_contributing_condition_id** | [**List[int]**](int.md)| Contributing Condition ID. Returns item(s) with the specified Contributing Condition ID. | [optional] 
 **filters_hazard_id** | [**List[int]**](int.md)| Hazard ID. Returns item(s) with the specified Hazard ID. | [optional] 
 **filters_time_unknown** | **bool**| If true, returns item(s) where the time of Incident occurrence is unknown. | [optional] [default to False]
 **filters_recordable** | **bool**| Return item(s) that are recordable. | [optional] 
 **filters_query** | **str**| Return item(s) containing query. Searchable fields include Incident title, Creator, Witness Statement, Incident Action description, Incident Action Type, Contributing Behavior, Contributing Condition, Hazard, and Location. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[IncidentCompact]**](IncidentCompact.md)

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

# **rest_v10_projects_project_id_incidents_id_delete**
> rest_v10_projects_project_id_incidents_id_delete(procore_company_id, project_id, id)

Delete Incident

Sends Incident to the Recycle Bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Incident ID

    try:
        # Delete Incident
        api_instance.rest_v10_projects_project_id_incidents_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Incident ID | 

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_incidents_id_get**
> IncidentNormal rest_v10_projects_project_id_incidents_id_get(procore_company_id, project_id, id)

Show Incident

Returns the specified Incident.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal import IncidentNormal
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Incident ID

    try:
        # Show Incident
        api_response = api_instance.rest_v10_projects_project_id_incidents_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Incident ID | 

### Return type

[**IncidentNormal**](IncidentNormal.md)

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

# **rest_v10_projects_project_id_incidents_id_patch**
> IncidentNormal rest_v10_projects_project_id_incidents_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_post_request, run_configurable_validations=run_configurable_validations)

Update Incident

Updates the specified Incident.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal import IncidentNormal
from procore_sdk.models.rest_v10_projects_project_id_incidents_post_request import RestV10ProjectsProjectIdIncidentsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Incident ID
    rest_v10_projects_project_id_incidents_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsPostRequest() # RestV10ProjectsProjectIdIncidentsPostRequest | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Update Incident
        api_response = api_instance.rest_v10_projects_project_id_incidents_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Incident ID | 
 **rest_v10_projects_project_id_incidents_post_request** | [**RestV10ProjectsProjectIdIncidentsPostRequest**](RestV10ProjectsProjectIdIncidentsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**IncidentNormal**](IncidentNormal.md)

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

# **rest_v10_projects_project_id_incidents_post**
> IncidentNormal rest_v10_projects_project_id_incidents_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_post_request, run_configurable_validations=run_configurable_validations)

Create Incident

Creates an Incident in a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal import IncidentNormal
from procore_sdk.models.rest_v10_projects_project_id_incidents_post_request import RestV10ProjectsProjectIdIncidentsPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsPostRequest() # RestV10ProjectsProjectIdIncidentsPostRequest | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Create Incident
        api_response = api_instance.rest_v10_projects_project_id_incidents_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_incidents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_post_request** | [**RestV10ProjectsProjectIdIncidentsPostRequest**](RestV10ProjectsProjectIdIncidentsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Incident/Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**IncidentNormal**](IncidentNormal.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_get**
> List[IncidentCompact] rest_v10_projects_project_id_recycle_bin_incidents_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_event_date=filters_event_date, filters_location_id=filters_location_id, filters_status=filters_status, filters_contributing_behavior_id=filters_contributing_behavior_id, filters_contributing_condition_id=filters_contributing_condition_id, filters_hazard_id=filters_hazard_id, filters_time_unknown=filters_time_unknown, filters_recordable=filters_recordable, filters_query=filters_query, sort=sort)

List Recycled Incidents

Returns a list of Recycled Incidents for a given project.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_compact import IncidentCompact
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_event_date = '2013-10-20' # date | Returns item(s) with an event date within the specified ISO 8601 datetime range. (optional)
    filters_location_id = [56] # List[int] | Return item(s) with the specified Location IDs. (optional)
    filters_status = ['filters_status_example'] # List[str] | Returns item(s) matching the specified status value. (optional)
    filters_contributing_behavior_id = [56] # List[int] | Contributing Behavior ID. Returns item(s) with the specified Contributing Behavior ID. (optional)
    filters_contributing_condition_id = [56] # List[int] | Contributing Condition ID. Returns item(s) with the specified Contributing Condition ID. (optional)
    filters_hazard_id = [56] # List[int] | Hazard ID. Returns item(s) with the specified Hazard ID. (optional)
    filters_time_unknown = False # bool | If true, returns item(s) where the time of Incident occurrence is unknown. (optional) (default to False)
    filters_recordable = True # bool | Return item(s) that are recordable. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query. Searchable fields include Incident title, Creator, Witness Statement, Incident Action description, Incident Action Type, Contributing Behavior, Contributing Condition, Hazard, and Location. (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Recycled Incidents
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_event_date=filters_event_date, filters_location_id=filters_location_id, filters_status=filters_status, filters_contributing_behavior_id=filters_contributing_behavior_id, filters_contributing_condition_id=filters_contributing_condition_id, filters_hazard_id=filters_hazard_id, filters_time_unknown=filters_time_unknown, filters_recordable=filters_recordable, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_recycle_bin_incidents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_recycle_bin_incidents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_event_date** | **date**| Returns item(s) with an event date within the specified ISO 8601 datetime range. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Return item(s) with the specified Location IDs. | [optional] 
 **filters_status** | [**List[str]**](str.md)| Returns item(s) matching the specified status value. | [optional] 
 **filters_contributing_behavior_id** | [**List[int]**](int.md)| Contributing Behavior ID. Returns item(s) with the specified Contributing Behavior ID. | [optional] 
 **filters_contributing_condition_id** | [**List[int]**](int.md)| Contributing Condition ID. Returns item(s) with the specified Contributing Condition ID. | [optional] 
 **filters_hazard_id** | [**List[int]**](int.md)| Hazard ID. Returns item(s) with the specified Hazard ID. | [optional] 
 **filters_time_unknown** | **bool**| If true, returns item(s) where the time of Incident occurrence is unknown. | [optional] [default to False]
 **filters_recordable** | **bool**| Return item(s) that are recordable. | [optional] 
 **filters_query** | **str**| Return item(s) containing query. Searchable fields include Incident title, Creator, Witness Statement, Incident Action description, Incident Action Type, Contributing Behavior, Contributing Condition, Hazard, and Location. | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[IncidentCompact]**](IncidentCompact.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_id_get**
> IncidentNormal rest_v10_projects_project_id_recycle_bin_incidents_id_get(procore_company_id, project_id, id)

Show Recycled Incident

Returns the specified Recycled Incident.

### Example


```python
import procore_sdk
from procore_sdk.models.incident_normal import IncidentNormal
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Incident ID

    try:
        # Show Recycled Incident
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_recycle_bin_incidents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_recycle_bin_incidents_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Incident ID | 

### Return type

[**IncidentNormal**](IncidentNormal.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch(procore_company_id, project_id, id)

Retrieve Recycled Incident

Retrieves the specified Incident from Recycle Bin.

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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Incident ID

    try:
        # Retrieve Recycled Incident
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentsApi->rest_v10_projects_project_id_recycle_bin_incidents_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Incident ID | 

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

