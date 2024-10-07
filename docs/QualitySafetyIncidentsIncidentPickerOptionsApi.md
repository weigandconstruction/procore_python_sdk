# procore_sdk.QualitySafetyIncidentsIncidentPickerOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_affected_body_parts_get**](QualitySafetyIncidentsIncidentPickerOptionsApi.md#rest_v10_companies_company_id_incidents_affected_body_parts_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/affected_body_parts | Get Affected Body Parts
[**rest_v10_companies_company_id_incidents_filing_types_get**](QualitySafetyIncidentsIncidentPickerOptionsApi.md#rest_v10_companies_company_id_incidents_filing_types_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/filing_types | Get Filing Types
[**rest_v10_companies_company_id_incidents_statuses_get**](QualitySafetyIncidentsIncidentPickerOptionsApi.md#rest_v10_companies_company_id_incidents_statuses_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/statuses | Get Incident Statuses
[**rest_v10_companies_company_id_incidents_units_of_measure_get**](QualitySafetyIncidentsIncidentPickerOptionsApi.md#rest_v10_companies_company_id_incidents_units_of_measure_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/units_of_measure | Get Units of Measure


# **rest_v10_companies_company_id_incidents_affected_body_parts_get**
> List[AffectedBodyPart] rest_v10_companies_company_id_incidents_affected_body_parts_get(procore_company_id, company_id)

Get Affected Body Parts

Returns objects containing the display label and server value of affected body parts that are available when creating or updating injuries

### Example


```python
import procore_sdk
from procore_sdk.models.affected_body_part import AffectedBodyPart
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentPickerOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Get Affected Body Parts
        api_response = api_instance.rest_v10_companies_company_id_incidents_affected_body_parts_get(procore_company_id, company_id)
        print("The response of QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_affected_body_parts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_affected_body_parts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[AffectedBodyPart]**](AffectedBodyPart.md)

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

# **rest_v10_companies_company_id_incidents_filing_types_get**
> List[FilingType] rest_v10_companies_company_id_incidents_filing_types_get(procore_company_id, company_id)

Get Filing Types

Returns objects containing the display label and server value of filing types that are available when creating or updating injuries

### Example


```python
import procore_sdk
from procore_sdk.models.filing_type import FilingType
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentPickerOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Get Filing Types
        api_response = api_instance.rest_v10_companies_company_id_incidents_filing_types_get(procore_company_id, company_id)
        print("The response of QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_filing_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_filing_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[FilingType]**](FilingType.md)

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

# **rest_v10_companies_company_id_incidents_statuses_get**
> List[IncidentStatus] rest_v10_companies_company_id_incidents_statuses_get(procore_company_id, company_id)

Get Incident Statuses

Returns objects containing the display label and server value of statuses that are available when creating or updating incidents

### Example


```python
import procore_sdk
from procore_sdk.models.incident_status import IncidentStatus
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentPickerOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Get Incident Statuses
        api_response = api_instance.rest_v10_companies_company_id_incidents_statuses_get(procore_company_id, company_id)
        print("The response of QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_statuses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_statuses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[IncidentStatus]**](IncidentStatus.md)

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

# **rest_v10_companies_company_id_incidents_units_of_measure_get**
> List[IncidentUnitOfMeasure] rest_v10_companies_company_id_incidents_units_of_measure_get(procore_company_id, company_id)

Get Units of Measure

Returns objects containing the display label and server value of units of measure that are available when creating or updating incident's environmental records

### Example


```python
import procore_sdk
from procore_sdk.models.incident_unit_of_measure import IncidentUnitOfMeasure
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
    api_instance = procore_sdk.QualitySafetyIncidentsIncidentPickerOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Get Units of Measure
        api_response = api_instance.rest_v10_companies_company_id_incidents_units_of_measure_get(procore_company_id, company_id)
        print("The response of QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_units_of_measure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsIncidentPickerOptionsApi->rest_v10_companies_company_id_incidents_units_of_measure_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**List[IncidentUnitOfMeasure]**](IncidentUnitOfMeasure.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

