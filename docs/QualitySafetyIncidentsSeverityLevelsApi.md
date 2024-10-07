# procore_sdk.QualitySafetyIncidentsSeverityLevelsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_severity_levels_get**](QualitySafetyIncidentsSeverityLevelsApi.md#rest_v10_companies_company_id_incidents_severity_levels_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/severity_levels | List Incident Severity Levels
[**rest_v10_companies_company_id_incidents_severity_levels_id_get**](QualitySafetyIncidentsSeverityLevelsApi.md#rest_v10_companies_company_id_incidents_severity_levels_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{id} | Show Incident Severity Level
[**rest_v10_companies_company_id_incidents_severity_levels_id_patch**](QualitySafetyIncidentsSeverityLevelsApi.md#rest_v10_companies_company_id_incidents_severity_levels_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{id} | Update Incident Severity Level


# **rest_v10_companies_company_id_incidents_severity_levels_get**
> List[SeverityLevel] rest_v10_companies_company_id_incidents_severity_levels_get(procore_company_id, company_id, page=page, per_page=per_page, filters_email_trigger=filters_email_trigger, filters_id=filters_id, filters_push_notification_trigger=filters_push_notification_trigger, filters_updated_at=filters_updated_at, sort=sort)

List Incident Severity Levels

Return a list of all Incident Severity Levels associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.severity_level import SeverityLevel
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
    api_instance = procore_sdk.QualitySafetyIncidentsSeverityLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_email_trigger = 'filters_email_trigger_example' # str | Return item(s) set to trigger email notifications. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_push_notification_trigger = 'filters_push_notification_trigger_example' # str | Return item(s) set to trigger push notifications. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Incident Severity Levels
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_get(procore_company_id, company_id, page=page, per_page=per_page, filters_email_trigger=filters_email_trigger, filters_id=filters_id, filters_push_notification_trigger=filters_push_notification_trigger, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_email_trigger** | **str**| Return item(s) set to trigger email notifications. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_push_notification_trigger** | **str**| Return item(s) set to trigger push notifications. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[SeverityLevel]**](SeverityLevel.md)

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

# **rest_v10_companies_company_id_incidents_severity_levels_id_get**
> SeverityLevel rest_v10_companies_company_id_incidents_severity_levels_id_get(procore_company_id, company_id, id)

Show Incident Severity Level

Returns the specified Incident Severity Level.

### Example


```python
import procore_sdk
from procore_sdk.models.severity_level import SeverityLevel
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
    api_instance = procore_sdk.QualitySafetyIncidentsSeverityLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Incident Severity Level ID

    try:
        # Show Incident Severity Level
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Incident Severity Level ID | 

### Return type

[**SeverityLevel**](SeverityLevel.md)

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

# **rest_v10_companies_company_id_incidents_severity_levels_id_patch**
> SeverityLevel rest_v10_companies_company_id_incidents_severity_levels_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_severity_levels_id_patch_request)

Update Incident Severity Level

Updates a specified Incident Severity Level.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_incidents_severity_levels_id_patch_request import RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequest
from procore_sdk.models.severity_level import SeverityLevel
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
    api_instance = procore_sdk.QualitySafetyIncidentsSeverityLevelsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Incident Severity Level ID
    rest_v10_companies_company_id_incidents_severity_levels_id_patch_request = procore_sdk.RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequest() # RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequest | 

    try:
        # Update Incident Severity Level
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_id_patch(procore_company_id, company_id, id, rest_v10_companies_company_id_incidents_severity_levels_id_patch_request)
        print("The response of QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsSeverityLevelsApi->rest_v10_companies_company_id_incidents_severity_levels_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Incident Severity Level ID | 
 **rest_v10_companies_company_id_incidents_severity_levels_id_patch_request** | [**RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequest**](RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequest.md)|  | 

### Return type

[**SeverityLevel**](SeverityLevel.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

