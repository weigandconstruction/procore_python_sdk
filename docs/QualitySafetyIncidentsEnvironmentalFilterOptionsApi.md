# procore_sdk.QualitySafetyIncidentsEnvironmentalFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get**](QualitySafetyIncidentsEnvironmentalFilterOptionsApi.md#rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals/filter_options/affected_companies | Get Affected Company Filter Options
[**rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get**](QualitySafetyIncidentsEnvironmentalFilterOptionsApi.md#rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals/filter_options/environmental_types | Get Environmental Type Filter Options
[**rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get**](QualitySafetyIncidentsEnvironmentalFilterOptionsApi.md#rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals/filter_options/managed_equipment | Get Managed Equipment Filter Options
[**rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get**](QualitySafetyIncidentsEnvironmentalFilterOptionsApi.md#rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/environmentals/filter_options/work_activities | Get Work Activity Filter Options


# **rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get(procore_company_id, project_id)

Get Affected Company Filter Options

Returns affected companies in use for filtering environmental records

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Affected Company Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_affected_companies_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get**
> List[RestV10ProjectsProjectIdIncidentsInjuriesFilterOptionsAffectedBodyPartsGet200ResponseInner] rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get(procore_company_id, project_id)

Get Environmental Type Filter Options

Returns environmental types in use for filtering environmental records

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Environmental Type Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_environmental_types_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get(procore_company_id, project_id)

Get Managed Equipment Filter Options

Returns managed equipment in use for filtering environmental records

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Managed Equipment Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_managed_equipment_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get(procore_company_id, project_id)

Get Work Activity Filter Options

Returns work activities in use for filtering environmental records

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
    api_instance = procore_sdk.QualitySafetyIncidentsEnvironmentalFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Work Activity Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsEnvironmentalFilterOptionsApi->rest_v10_projects_project_id_incidents_environmentals_filter_options_work_activities_get: %s\n" % e)
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

