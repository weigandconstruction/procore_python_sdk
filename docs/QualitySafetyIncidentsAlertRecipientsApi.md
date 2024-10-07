# procore_sdk.QualitySafetyIncidentsAlertRecipientsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get**](QualitySafetyIncidentsAlertRecipientsApi.md#rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{severity_level_id}/alert_recipients | List Incident Alert Recipients
[**rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete**](QualitySafetyIncidentsAlertRecipientsApi.md#rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{severity_level_id}/alert_recipients/{id} | Delete Incident Alert Recipient
[**rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get**](QualitySafetyIncidentsAlertRecipientsApi.md#rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get) | **GET** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{severity_level_id}/alert_recipients/{id} | Show Incident Alert Recipient
[**rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch**](QualitySafetyIncidentsAlertRecipientsApi.md#rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/incidents/severity_levels/{severity_level_id}/alert_recipients/{id} | Update existing or create a new Incident Alert Recipient.


# **rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get**
> List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy] rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get(procore_company_id, company_id, severity_level_id, page=page, per_page=per_page, sort=sort)

List Incident Alert Recipients

Return a list of all Incident Alert Recipients associated with the specified Company and Incident Severity Level.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
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
    api_instance = procore_sdk.QualitySafetyIncidentsAlertRecipientsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    severity_level_id = 56 # int | Incident Severity Level ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Incident Alert Recipients
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get(procore_company_id, company_id, severity_level_id, page=page, per_page=per_page, sort=sort)
        print("The response of QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **severity_level_id** | **int**| Incident Severity Level ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete**
> rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete(procore_company_id, company_id, severity_level_id, id)

Delete Incident Alert Recipient

Deletes an Incident Alert Recipient.

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
    api_instance = procore_sdk.QualitySafetyIncidentsAlertRecipientsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    severity_level_id = 56 # int | Incident Severity Level ID
    id = 1 # int | Incident Alert Recipient's User ID

    try:
        # Delete Incident Alert Recipient
        api_instance.rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete(procore_company_id, company_id, severity_level_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **severity_level_id** | **int**| Incident Severity Level ID | 
 **id** | **int**| Incident Alert Recipient&#39;s User ID | 

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

# **rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get**
> RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get(procore_company_id, company_id, severity_level_id, id)

Show Incident Alert Recipient

Returns the specified Incident Alert Recipient.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
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
    api_instance = procore_sdk.QualitySafetyIncidentsAlertRecipientsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    severity_level_id = 56 # int | Incident Severity Level ID
    id = 1 # int | Incident Alert Recipient's User ID

    try:
        # Show Incident Alert Recipient
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get(procore_company_id, company_id, severity_level_id, id)
        print("The response of QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **severity_level_id** | **int**| Incident Severity Level ID | 
 **id** | **int**| Incident Alert Recipient&#39;s User ID | 

### Return type

[**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md)

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

# **rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch**
> RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch(procore_company_id, company_id, severity_level_id, id)

Update existing or create a new Incident Alert Recipient.

Finds an exisiting Incident Alert Recipient or creates one with the specified User.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
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
    api_instance = procore_sdk.QualitySafetyIncidentsAlertRecipientsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    severity_level_id = 56 # int | Incident Severity Level ID
    id = 1 # int | Incident Alert Recipient's User ID

    try:
        # Update existing or create a new Incident Alert Recipient.
        api_response = api_instance.rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch(procore_company_id, company_id, severity_level_id, id)
        print("The response of QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyIncidentsAlertRecipientsApi->rest_v10_companies_company_id_incidents_severity_levels_severity_level_id_alert_recipients_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **severity_level_id** | **int**| Incident Severity Level ID | 
 **id** | **int**| Incident Alert Recipient&#39;s User ID | 

### Return type

[**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md)

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

