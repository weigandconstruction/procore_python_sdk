# procore_sdk.ProjectManagementDailyLogWeatherConditionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_daily_logs_weather_conditions_get**](ProjectManagementDailyLogWeatherConditionsApi.md#rest_v10_projects_project_id_daily_logs_weather_conditions_get) | **GET** /rest/v1.0/projects/{project_id}/daily_logs/weather_conditions | List Accepted Weather Conditions


# **rest_v10_projects_project_id_daily_logs_weather_conditions_get**
> RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response rest_v10_projects_project_id_daily_logs_weather_conditions_get(procore_company_id, project_id)

List Accepted Weather Conditions

Returns accepted weather conditions for the sky, ground, temperature, calamity, and wind categories.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_daily_logs_weather_conditions_get200_response import RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherConditionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Accepted Weather Conditions
        api_response = api_instance.rest_v10_projects_project_id_daily_logs_weather_conditions_get(procore_company_id, project_id)
        print("The response of ProjectManagementDailyLogWeatherConditionsApi->rest_v10_projects_project_id_daily_logs_weather_conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherConditionsApi->rest_v10_projects_project_id_daily_logs_weather_conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response**](RestV10ProjectsProjectIdDailyLogsWeatherConditionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

