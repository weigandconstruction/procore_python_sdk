# procore_sdk.QualitySafetyIncidentsInjuriesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_injuries_get**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_incidents_injuries_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/injuries | List Injuries
[**rest_v10_projects_project_id_incidents_injuries_id_delete**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_incidents_injuries_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/incidents/injuries/{id} | Destroy Injury
[**rest_v10_projects_project_id_incidents_injuries_id_get**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_incidents_injuries_id_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/injuries/{id} | Show Injury
[**rest_v10_projects_project_id_incidents_injuries_id_patch**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_incidents_injuries_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/incidents/injuries/{id} | Update Injury
[**rest_v10_projects_project_id_incidents_injuries_post**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_incidents_injuries_post) | **POST** /rest/v1.0/projects/{project_id}/incidents/injuries | Create Injury
[**rest_v10_projects_project_id_recycle_bin_incidents_injuries_get**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_injuries_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/injuries | List Recycled Injuries
[**rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/injuries/{id} | Show Recycled Injury
[**rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch**](QualitySafetyIncidentsInjuriesApi.md#rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/incidents/injuries/{id}/restore | Retrieve Recycled Injury


# **rest_v10_projects_project_id_incidents_injuries_get**
> List[RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner] rest_v10_projects_project_id_incidents_injuries_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_recordable=filters_recordable, filters_affected_body_part=filters_affected_body_part, filters_affliction_type_id=filters_affliction_type_id, filters_body_part_id=filters_body_part_id, filters_filing_type=filters_filing_type, filters_query=filters_query, sort=sort)

List Injuries

Returns a list of Injuries for a given project.  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Injuries for a given Incident. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_affected_company_id = [56] # List[int] | Array of Company IDs. Returns item(s) with the specified affected Company IDs. (optional)
    filters_affected_party_id = [56] # List[int] | Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. (optional)
    filters_affected_person_id = [56] # List[int] | Array of Person IDs. Returns item(s) with the specified affected Person IDs. (optional)
    filters_harm_source_id = [56] # List[int] | Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. (optional)
    filters_work_activity_id = [56] # List[int] | Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_recordable = True # bool | Return item(s) that are recordable. (optional)
    filters_affected_body_part = ['filters_affected_body_part_example'] # List[str] | Return item(s) with any of the specified Affected Body Parts. (optional)
    filters_affliction_type_id = 56 # int | Return item(s) with the specified Affliction Type IDs (optional)
    filters_body_part_id = [56] # List[int] | Return item(s) with the specified Body Part IDs (optional)
    filters_filing_type = ['filters_filing_type_example'] # List[str] | Return item(s) with the specified filing types. The `recordable` filing_type filter value is deprecated. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Injuries
        api_response = api_instance.rest_v10_projects_project_id_incidents_injuries_get(procore_company_id, project_id, incident_id=incident_id, page=page, per_page=per_page, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_recordable=filters_recordable, filters_affected_body_part=filters_affected_body_part, filters_affliction_type_id=filters_affliction_type_id, filters_body_part_id=filters_body_part_id, filters_filing_type=filters_filing_type, filters_query=filters_query, sort=sort)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Injuries for a given Incident. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_affected_company_id** | [**List[int]**](int.md)| Array of Company IDs. Returns item(s) with the specified affected Company IDs. | [optional] 
 **filters_affected_party_id** | [**List[int]**](int.md)| Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. | [optional] 
 **filters_affected_person_id** | [**List[int]**](int.md)| Array of Person IDs. Returns item(s) with the specified affected Person IDs. | [optional] 
 **filters_harm_source_id** | [**List[int]**](int.md)| Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. | [optional] 
 **filters_work_activity_id** | [**List[int]**](int.md)| Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_recordable** | **bool**| Return item(s) that are recordable. | [optional] 
 **filters_affected_body_part** | [**List[str]**](str.md)| Return item(s) with any of the specified Affected Body Parts. | [optional] 
 **filters_affliction_type_id** | **int**| Return item(s) with the specified Affliction Type IDs | [optional] 
 **filters_body_part_id** | [**List[int]**](int.md)| Return item(s) with the specified Body Part IDs | [optional] 
 **filters_filing_type** | [**List[str]**](str.md)| Return item(s) with the specified filing types. The &#x60;recordable&#x60; filing_type filter value is deprecated. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_injuries_id_delete**
> rest_v10_projects_project_id_incidents_injuries_id_delete(procore_company_id, project_id, id, incident_id=incident_id)

Destroy Injury

Sends Injury to the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Injury ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Destroy Injury
        api_instance.rest_v10_projects_project_id_incidents_injuries_id_delete(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Injury ID | 
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

# **rest_v10_projects_project_id_incidents_injuries_id_get**
> RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner rest_v10_projects_project_id_incidents_injuries_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Injury

Returns a specific Injury  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Injury ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Injury
        api_response = api_instance.rest_v10_projects_project_id_incidents_injuries_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Injury ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_injuries_id_patch**
> RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner rest_v10_projects_project_id_incidents_injuries_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_injuries_id_patch_request, incident_id=incident_id, run_configurable_validations=run_configurable_validations)

Update Injury

Update an Injury's attributes  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_id_patch_request import RestV10ProjectsProjectIdIncidentsInjuriesIdPatchRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Injury ID
    rest_v10_projects_project_id_incidents_injuries_id_patch_request = procore_sdk.RestV10ProjectsProjectIdIncidentsInjuriesIdPatchRequest() # RestV10ProjectsProjectIdIncidentsInjuriesIdPatchRequest | 
    incident_id = 56 # int | Incident ID (optional)
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Update Injury
        api_response = api_instance.rest_v10_projects_project_id_incidents_injuries_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_incidents_injuries_id_patch_request, incident_id=incident_id, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Injury ID | 
 **rest_v10_projects_project_id_incidents_injuries_id_patch_request** | [**RestV10ProjectsProjectIdIncidentsInjuriesIdPatchRequest**](RestV10ProjectsProjectIdIncidentsInjuriesIdPatchRequest.md)|  | 
 **incident_id** | **int**| Incident ID | [optional] 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_injuries_post**
> RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner rest_v10_projects_project_id_incidents_injuries_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_injuries_post_request, run_configurable_validations=run_configurable_validations)

Create Injury

Creates an Injury record.  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_post_request import RestV10ProjectsProjectIdIncidentsInjuriesPostRequest
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_incidents_injuries_post_request = procore_sdk.RestV10ProjectsProjectIdIncidentsInjuriesPostRequest() # RestV10ProjectsProjectIdIncidentsInjuriesPostRequest | 
    run_configurable_validations = True # bool | Whether or not Configurable validations from the Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. (optional)

    try:
        # Create Injury
        api_response = api_instance.rest_v10_projects_project_id_incidents_injuries_post(procore_company_id, project_id, rest_v10_projects_project_id_incidents_injuries_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_incidents_injuries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_incidents_injuries_post_request** | [**RestV10ProjectsProjectIdIncidentsInjuriesPostRequest**](RestV10ProjectsProjectIdIncidentsInjuriesPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| Whether or not Configurable validations from the Injury Configurable Field Set should be run (default: false). See (https://developers.procore.com/reference/configurable-field-sets#list-project-configurable-field-sets) for a list of Configurable validations enabled on this project. | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_injuries_get**
> List[RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_incidents_injuries_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_recordable=filters_recordable, filters_affected_body_part=filters_affected_body_part, filters_affliction_type_id=filters_affliction_type_id, filters_filing_type=filters_filing_type, filters_query=filters_query, sort=sort, page=page, per_page=per_page)

List Recycled Injuries

Returns a list of Recycled Injuries for a given project (or Incident, if incident_id is present).  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    incident_id = 56 # int | Incident ID. When provided, the list will be scoped to only the Recycled Injuries for a given Incident.  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_affected_company_id = [56] # List[int] | Array of Company IDs. Returns item(s) with the specified affected Company IDs. (optional)
    filters_affected_party_id = [56] # List[int] | Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. (optional)
    filters_affected_person_id = [56] # List[int] | Array of Person IDs. Returns item(s) with the specified affected Person IDs. (optional)
    filters_harm_source_id = [56] # List[int] | Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. (optional)
    filters_work_activity_id = [56] # List[int] | Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. (optional)
    filters_managed_equipment_id = 56 # int | Return item(s) with the specified Managed Equipment ID. (optional)
    filters_recordable = True # bool | Return item(s) that are recordable. (optional)
    filters_affected_body_part = ['filters_affected_body_part_example'] # List[str] | Return item(s) with any of the specified Affected Body Parts. (optional)
    filters_affliction_type_id = [56] # List[int] | Return item(s) with the specified Affliction Type IDs (optional)
    filters_filing_type = ['filters_filing_type_example'] # List[str] | Return item(s) with the specified filing types. The `recordable` filing_type filter value is deprecated. (optional)
    filters_query = 'filters_query_example' # str | Return item(s) containing query (optional)
    sort = 'sort_example' # str |  (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Recycled Injuries
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_injuries_get(procore_company_id, project_id, incident_id=incident_id, filters_created_at=filters_created_at, filters_affected_company_id=filters_affected_company_id, filters_affected_party_id=filters_affected_party_id, filters_affected_person_id=filters_affected_person_id, filters_harm_source_id=filters_harm_source_id, filters_work_activity_id=filters_work_activity_id, filters_managed_equipment_id=filters_managed_equipment_id, filters_recordable=filters_recordable, filters_affected_body_part=filters_affected_body_part, filters_affliction_type_id=filters_affliction_type_id, filters_filing_type=filters_filing_type, filters_query=filters_query, sort=sort, page=page, per_page=per_page)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_recycle_bin_incidents_injuries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_recycle_bin_incidents_injuries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **incident_id** | **int**| Incident ID. When provided, the list will be scoped to only the Recycled Injuries for a given Incident.  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_affected_company_id** | [**List[int]**](int.md)| Array of Company IDs. Returns item(s) with the specified affected Company IDs. | [optional] 
 **filters_affected_party_id** | [**List[int]**](int.md)| Array of Affected Party IDs. Returns item(s) with the specified Affected Party IDs. | [optional] 
 **filters_affected_person_id** | [**List[int]**](int.md)| Array of Person IDs. Returns item(s) with the specified affected Person IDs. | [optional] 
 **filters_harm_source_id** | [**List[int]**](int.md)| Array of Harm Source IDs. Returns item(s) with the specified Harm Source IDs. | [optional] 
 **filters_work_activity_id** | [**List[int]**](int.md)| Array of Work Activity IDs. Returns item(s) with the specified Work Activity IDs. | [optional] 
 **filters_managed_equipment_id** | **int**| Return item(s) with the specified Managed Equipment ID. | [optional] 
 **filters_recordable** | **bool**| Return item(s) that are recordable. | [optional] 
 **filters_affected_body_part** | [**List[str]**](str.md)| Return item(s) with any of the specified Affected Body Parts. | [optional] 
 **filters_affliction_type_id** | [**List[int]**](int.md)| Return item(s) with the specified Affliction Type IDs | [optional] 
 **filters_filing_type** | [**List[str]**](str.md)| Return item(s) with the specified filing types. The &#x60;recordable&#x60; filing_type filter value is deprecated. | [optional] 
 **filters_query** | **str**| Return item(s) containing query | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get**
> RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get(procore_company_id, project_id, id, incident_id=incident_id)

Show Recycled Injury

Returns a specific Recycled Injury  NOTE: The afflictions and affected_body_part keys are deprecated. Please disregard and use the affected_body_parts and affliction_type keys as documented below.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Injury ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Show Recycled Injury
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get(procore_company_id, project_id, id, incident_id=incident_id)
        print("The response of QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Injury ID | 
 **incident_id** | **int**| Incident ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner**](RestV10ProjectsProjectIdIncidentsInjuriesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch**
> rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)

Retrieve Recycled Injury

Retrieves a specific Injury from the recycle bin

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
    api_instance = procore_sdk.QualitySafetyIncidentsInjuriesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Injury ID
    incident_id = 56 # int | Incident ID (optional)

    try:
        # Retrieve Recycled Injury
        api_instance.rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch(procore_company_id, project_id, id, incident_id=incident_id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsInjuriesApi->rest_v10_projects_project_id_recycle_bin_incidents_injuries_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Injury ID | 
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

