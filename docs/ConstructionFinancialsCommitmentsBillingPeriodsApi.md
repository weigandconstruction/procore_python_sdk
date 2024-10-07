# procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_billing_periods_get**](ConstructionFinancialsCommitmentsBillingPeriodsApi.md#rest_v10_projects_project_id_billing_periods_get) | **GET** /rest/v1.0/projects/{project_id}/billing_periods | List billing periods
[**rest_v10_projects_project_id_billing_periods_id_delete**](ConstructionFinancialsCommitmentsBillingPeriodsApi.md#rest_v10_projects_project_id_billing_periods_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/billing_periods/{id} | Delete billing period
[**rest_v10_projects_project_id_billing_periods_id_get**](ConstructionFinancialsCommitmentsBillingPeriodsApi.md#rest_v10_projects_project_id_billing_periods_id_get) | **GET** /rest/v1.0/projects/{project_id}/billing_periods/{id} | Show Billing Period for Project
[**rest_v10_projects_project_id_billing_periods_id_patch**](ConstructionFinancialsCommitmentsBillingPeriodsApi.md#rest_v10_projects_project_id_billing_periods_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/billing_periods/{id} | Update billing period
[**rest_v10_projects_project_id_billing_periods_post**](ConstructionFinancialsCommitmentsBillingPeriodsApi.md#rest_v10_projects_project_id_billing_periods_post) | **POST** /rest/v1.0/projects/{project_id}/billing_periods | Create billing period


# **rest_v10_projects_project_id_billing_periods_get**
> List[BillingPeriod] rest_v10_projects_project_id_billing_periods_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_status=filters_status)

List billing periods

Return a list of all Billing Periods of a specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.billing_period import BillingPeriod
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Billing Period status. (optional)

    try:
        # List billing periods
        api_response = api_instance.rest_v10_projects_project_id_billing_periods_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_status=filters_status)
        print("The response of ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_get: %s\n" % e)
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
 **filters_status** | **str**| Return item(s) with the specified Billing Period status. | [optional] 

### Return type

[**List[BillingPeriod]**](BillingPeriod.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_billing_periods_id_delete**
> rest_v10_projects_project_id_billing_periods_id_delete(procore_company_id, project_id, id)

Delete billing period

Delete a specified Billing Period

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Billing Period ID

    try:
        # Delete billing period
        api_instance.rest_v10_projects_project_id_billing_periods_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Billing Period ID | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_billing_periods_id_get**
> BillingPeriod rest_v10_projects_project_id_billing_periods_id_get(procore_company_id, project_id, id)

Show Billing Period for Project

Return information for a Billing Period

### Example


```python
import procore_sdk
from procore_sdk.models.billing_period import BillingPeriod
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Billing Period ID

    try:
        # Show Billing Period for Project
        api_response = api_instance.rest_v10_projects_project_id_billing_periods_id_get(procore_company_id, project_id, id)
        print("The response of ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Billing Period ID | 

### Return type

[**BillingPeriod**](BillingPeriod.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_billing_periods_id_patch**
> BillingPeriod rest_v10_projects_project_id_billing_periods_id_patch(procore_company_id, project_id, id, body142)

Update billing period

Update a specified Billing Period

### Example


```python
import procore_sdk
from procore_sdk.models.billing_period import BillingPeriod
from procore_sdk.models.body142 import Body142
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Billing Period ID
    body142 = procore_sdk.Body142() # Body142 | 

    try:
        # Update billing period
        api_response = api_instance.rest_v10_projects_project_id_billing_periods_id_patch(procore_company_id, project_id, id, body142)
        print("The response of ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Billing Period ID | 
 **body142** | [**Body142**](Body142.md)|  | 

### Return type

[**BillingPeriod**](BillingPeriod.md)

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

# **rest_v10_projects_project_id_billing_periods_post**
> BillingPeriod rest_v10_projects_project_id_billing_periods_post(procore_company_id, project_id, body142)

Create billing period

Create a Billing Period

### Example


```python
import procore_sdk
from procore_sdk.models.billing_period import BillingPeriod
from procore_sdk.models.body142 import Body142
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsBillingPeriodsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body142 = procore_sdk.Body142() # Body142 | 

    try:
        # Create billing period
        api_response = api_instance.rest_v10_projects_project_id_billing_periods_post(procore_company_id, project_id, body142)
        print("The response of ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsBillingPeriodsApi->rest_v10_projects_project_id_billing_periods_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body142** | [**Body142**](Body142.md)|  | 

### Return type

[**BillingPeriod**](BillingPeriod.md)

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

