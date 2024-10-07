# procore_sdk.QualitySafetyIncidentsPropertyDamageFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get**](QualitySafetyIncidentsPropertyDamageFilterOptionsApi.md#rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages/filter_options/affected_companies | Get Affected Company Filter Options
[**rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get**](QualitySafetyIncidentsPropertyDamageFilterOptionsApi.md#rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages/filter_options/managed_equipment | Get Managed Equipment Filter Options
[**rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get**](QualitySafetyIncidentsPropertyDamageFilterOptionsApi.md#rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages/filter_options/responsible_companies | Get Responsible Company Filter Options
[**rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get**](QualitySafetyIncidentsPropertyDamageFilterOptionsApi.md#rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get) | **GET** /rest/v1.0/projects/{project_id}/incidents/property_damages/filter_options/work_activities | Get Work Activity Filter Options


# **rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get(procore_company_id, project_id)

Get Affected Company Filter Options

Returns affected companies in use for filtering property damages

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamageFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Affected Company Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_affected_companies_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get(procore_company_id, project_id)

Get Managed Equipment Filter Options

Returns managed equipment in use for filtering property damages

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamageFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Managed Equipment Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_managed_equipment_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get(procore_company_id, project_id)

Get Responsible Company Filter Options

Returns responsible companies in use for filtering property damages

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamageFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Responsible Company Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_responsible_companies_get: %s\n" % e)
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

# **rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get**
> List[RestV10ProjectsProjectIdIncidentsPropertyDamagesFilterOptionsAffectedCompaniesGet200ResponseInner] rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get(procore_company_id, project_id)

Get Work Activity Filter Options

Returns work activities in use for filtering property damages

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
    api_instance = procore_sdk.QualitySafetyIncidentsPropertyDamageFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Get Work Activity Filter Options
        api_response = api_instance.rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get(procore_company_id, project_id)
        print("The response of QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsPropertyDamageFilterOptionsApi->rest_v10_projects_project_id_incidents_property_damages_filter_options_work_activities_get: %s\n" % e)
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

