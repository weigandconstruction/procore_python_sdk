# procore_sdk.ProjectManagementDailyLogWeatherLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_weather_logs_conditions_get**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_conditions_get) | **GET** /rest/v1.0/projects/{project_id}/weather_logs/conditions | List Accepted Weather Conditions
[**rest_v10_projects_project_id_weather_logs_get**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_get) | **GET** /rest/v1.0/projects/{project_id}/weather_logs | List Weather Logs
[**rest_v10_projects_project_id_weather_logs_id_delete**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/weather_logs/{id} | Delete Weather Log
[**rest_v10_projects_project_id_weather_logs_id_get**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/weather_logs/{id} | Show Weather Logs
[**rest_v10_projects_project_id_weather_logs_id_patch**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/weather_logs/{id} | Update Weather Log
[**rest_v10_projects_project_id_weather_logs_post**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v10_projects_project_id_weather_logs_post) | **POST** /rest/v1.0/projects/{project_id}/weather_logs | Create Weather Log
[**rest_v11_projects_project_id_daily_logs_weather_logs_get**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v11_projects_project_id_daily_logs_weather_logs_get) | **GET** /rest/v1.1/projects/{project_id}/daily_logs/weather_logs | List Weather Logs
[**rest_v11_projects_project_id_daily_logs_weather_logs_id_delete**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v11_projects_project_id_daily_logs_weather_logs_id_delete) | **DELETE** /rest/v1.1/projects/{project_id}/daily_logs/weather_logs/{id} | Delete Weather Log
[**rest_v11_projects_project_id_daily_logs_weather_logs_id_get**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v11_projects_project_id_daily_logs_weather_logs_id_get) | **GET** /rest/v1.1/projects/{project_id}/daily_logs/weather_logs/{id} | Show Weather Log
[**rest_v11_projects_project_id_daily_logs_weather_logs_id_patch**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v11_projects_project_id_daily_logs_weather_logs_id_patch) | **PATCH** /rest/v1.1/projects/{project_id}/daily_logs/weather_logs/{id} | Update Weather Log
[**rest_v11_projects_project_id_daily_logs_weather_logs_post**](ProjectManagementDailyLogWeatherLogsApi.md#rest_v11_projects_project_id_daily_logs_weather_logs_post) | **POST** /rest/v1.1/projects/{project_id}/daily_logs/weather_logs | Create Weather Log


# **rest_v10_projects_project_id_weather_logs_conditions_get**
> RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response rest_v10_projects_project_id_weather_logs_conditions_get(procore_company_id, project_id)

List Accepted Weather Conditions

Returns accepted weather conditions for the sky, ground, temperature, calamity, and wind categories. This is a deprecated endpoint, please use [Weather Conditions](weather-conditions#list-accepted-weather-conditions)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_conditions_get200_response import RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Accepted Weather Conditions
        api_response = api_instance.rest_v10_projects_project_id_weather_logs_conditions_get(procore_company_id, project_id)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response**](RestV10ProjectsProjectIdWeatherLogsConditionsGet200Response.md)

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

# **rest_v10_projects_project_id_weather_logs_get**
> List[RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner] rest_v10_projects_project_id_weather_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, page=page, per_page=per_page)

List Weather Logs

Returns all Weather Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Weather Logs
        api_response = api_instance.rest_v10_projects_project_id_weather_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner]**](RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_weather_logs_id_delete**
> rest_v10_projects_project_id_weather_logs_id_delete(procore_company_id, project_id, id)

Delete Weather Log

Delete single Weather Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Use log date as your ID. Format YYYYMMDD ie:20161108

    try:
        # Delete Weather Log
        api_instance.rest_v10_projects_project_id_weather_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Use log date as your ID. Format YYYYMMDD ie:20161108 | 

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
**400** | Can not delete due to errors |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_weather_logs_id_get**
> RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner rest_v10_projects_project_id_weather_logs_id_get(procore_company_id, project_id, id, log_date=log_date)

Show Weather Logs

Returns single Weather Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Use log date as your ID. Format YYYYMMDD ie:20161108
    log_date = '2013-10-20' # date | Log date of specific log desired in YYYY-MM-DD format (This will override ID as log Date) (optional)

    try:
        # Show Weather Logs
        api_response = api_instance.rest_v10_projects_project_id_weather_logs_id_get(procore_company_id, project_id, id, log_date=log_date)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Use log date as your ID. Format YYYYMMDD ie:20161108 | 
 **log_date** | **date**| Log date of specific log desired in YYYY-MM-DD format (This will override ID as log Date) | [optional] 

### Return type

[**RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner**](RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_weather_logs_id_patch**
> RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner rest_v10_projects_project_id_weather_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_weather_logs_post_request)

Update Weather Log

Update single Weather Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_post_request import RestV10ProjectsProjectIdWeatherLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Use log date as your ID. Format YYYYMMDD ie:20161108
    rest_v10_projects_project_id_weather_logs_post_request = procore_sdk.RestV10ProjectsProjectIdWeatherLogsPostRequest() # RestV10ProjectsProjectIdWeatherLogsPostRequest | 

    try:
        # Update Weather Log
        api_response = api_instance.rest_v10_projects_project_id_weather_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_weather_logs_post_request)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Use log date as your ID. Format YYYYMMDD ie:20161108 | 
 **rest_v10_projects_project_id_weather_logs_post_request** | [**RestV10ProjectsProjectIdWeatherLogsPostRequest**](RestV10ProjectsProjectIdWeatherLogsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner**](RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_weather_logs_post**
> RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner rest_v10_projects_project_id_weather_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_weather_logs_post_request)

Create Weather Log

Creates single Weather Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_get200_response_inner import RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_weather_logs_post_request import RestV10ProjectsProjectIdWeatherLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_weather_logs_post_request = procore_sdk.RestV10ProjectsProjectIdWeatherLogsPostRequest() # RestV10ProjectsProjectIdWeatherLogsPostRequest | 

    try:
        # Create Weather Log
        api_response = api_instance.rest_v10_projects_project_id_weather_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_weather_logs_post_request)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v10_projects_project_id_weather_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_weather_logs_post_request** | [**RestV10ProjectsProjectIdWeatherLogsPostRequest**](RestV10ProjectsProjectIdWeatherLogsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner**](RestV10ProjectsProjectIdWeatherLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_daily_logs_weather_logs_get**
> List[RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner] rest_v11_projects_project_id_daily_logs_weather_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)

List Weather Logs

Returns all Weather Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired. Use together with end_date to specify a date range. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired. Use together with start_date to specify a date range. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY (optional)
    filters_status = 'filters_status_example' # str | Filter on log status (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Weather Logs
        api_response = api_instance.rest_v11_projects_project_id_daily_logs_weather_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_status=filters_status, filters_created_by_id=filters_created_by_id, page=page, per_page=per_page)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Date of specific logs desired. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY | [optional] 
 **start_date** | **date**| Start date of specific logs desired. Use together with end_date to specify a date range. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY | [optional] 
 **end_date** | **date**| End date of specific logs desired. Use together with start_date to specify a date range. Example formats YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, DD/MM/YYYY | [optional] 
 **filters_status** | **str**| Filter on log status | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner]**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_daily_logs_weather_logs_id_delete**
> rest_v11_projects_project_id_daily_logs_weather_logs_id_delete(procore_company_id, project_id, id)

Delete Weather Log

Delete single Weather Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Weather Log ID

    try:
        # Delete Weather Log
        api_instance.rest_v11_projects_project_id_daily_logs_weather_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Weather Log ID | 

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
**400** | Can not delete due to errors |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_daily_logs_weather_logs_id_get**
> RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner rest_v11_projects_project_id_daily_logs_weather_logs_id_get(procore_company_id, project_id, id)

Show Weather Log

Returns single Weather Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Weather Log ID

    try:
        # Show Weather Log
        api_response = api_instance.rest_v11_projects_project_id_daily_logs_weather_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Weather Log ID | 

### Return type

[**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.md)

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

# **rest_v11_projects_project_id_daily_logs_weather_logs_id_patch**
> RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner rest_v11_projects_project_id_daily_logs_weather_logs_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_daily_logs_weather_logs_post_request, run_configurable_validations=run_configurable_validations)

Update Weather Log

Update single Weather Log.  #### See - [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request import RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Weather Log ID
    rest_v11_projects_project_id_daily_logs_weather_logs_post_request = procore_sdk.RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest() # RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Weather Log
        api_response = api_instance.rest_v11_projects_project_id_daily_logs_weather_logs_id_patch(procore_company_id, project_id, id, rest_v11_projects_project_id_daily_logs_weather_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Weather Log ID | 
 **rest_v11_projects_project_id_daily_logs_weather_logs_post_request** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest**](RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_daily_logs_weather_logs_post**
> RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner rest_v11_projects_project_id_daily_logs_weather_logs_post(procore_company_id, project_id, rest_v11_projects_project_id_daily_logs_weather_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Weather Log

Creates single Weather Log.  #### See - [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_get200_response_inner import RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner
from procore_sdk.models.rest_v11_projects_project_id_daily_logs_weather_logs_post_request import RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogWeatherLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v11_projects_project_id_daily_logs_weather_logs_post_request = procore_sdk.RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest() # RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Weather Log
        api_response = api_instance.rest_v11_projects_project_id_daily_logs_weather_logs_post(procore_company_id, project_id, rest_v11_projects_project_id_daily_logs_weather_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogWeatherLogsApi->rest_v11_projects_project_id_daily_logs_weather_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v11_projects_project_id_daily_logs_weather_logs_post_request** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest**](RestV11ProjectsProjectIdDailyLogsWeatherLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

