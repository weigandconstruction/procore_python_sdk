# procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get**](QualitySafetyIncidentsIncidentFilterOptionsApi.md#rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/filter_options/contributing_behaviors | Get Contributing Behavior Filter Options
[**rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get**](QualitySafetyIncidentsIncidentFilterOptionsApi.md#rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/filter_options/contributing_conditions | Get Contributing Condition Filter Options
[**rest_v10_projects_project_id_incidents_filter_options_hazards_get**](QualitySafetyIncidentsIncidentFilterOptionsApi.md#rest_v10_projects_project_id_incidents_filter_options_hazards_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/filter_options/hazards | Get Hazard Filter Options
[**rest_v10_projects_project_id_incidents_filter_options_locations_get**](QualitySafetyIncidentsIncidentFilterOptionsApi.md#rest_v10_projects_project_id_incidents_filter_options_locations_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/filter_options/locations | Get Location Filter Options
[**rest_v10_projects_project_id_incidents_filter_options_statuses_get**](QualitySafetyIncidentsIncidentFilterOptionsApi.md#rest_v10_projects_project_id_incidents_filter_options_statuses_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/filter_options/statuses | Get Status Filter Options


# **rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get(procore_company_id, project_id)

Get Contributing Behavior Filter Options

Returns contributing behaviors in use for filtering incidents

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Contributing Behavior Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_contributing_behaviors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get(procore_company_id, project_id)

Get Contributing Condition Filter Options

Returns contributing conditions in use for filtering incidents

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Contributing Condition Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_contributing_conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_filter_options_hazards_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_filter_options_hazards_get(procore_company_id, project_id)

Get Hazard Filter Options

Returns hazards in use for filtering incidents

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Hazard Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_filter_options_hazards_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_hazards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_hazards_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_filter_options_locations_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_filter_options_locations_get(procore_company_id, project_id)

Get Location Filter Options

Returns locations in use for filtering incidents

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get200_response_inner import RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Location Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_filter_options_locations_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_incidents_filter_options_statuses_get**
> List[RestV10ProjectsProjectIdIncidentsInjuriesFilterOptionsAffectedBodyPartsGet200ResponseInner] rest_v10_projects_project_id_incidents_filter_options_statuses_get(procore_company_id, project_id)

Get Status Filter Options

Returns available statuses for filtering incidents

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_incidents_injuries_filter_options_affected_body_parts_get200_response_inner import RestV10ProjectsProjectIdIncidentsInjuriesFilterOptionsAffectedBodyPartsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Status Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_filter_options_statuses_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentFilterOptionsApi->rest_v10_projects_project_id_incidents_filter_options_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdIncidentsInjuriesFilterOptionsAffectedBodyPartsGet200ResponseInner]**](RestV10ProjectsProjectIdIncidentsInjuriesFilterOptionsAffectedBodyPartsGet200ResponseInner.md)

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

