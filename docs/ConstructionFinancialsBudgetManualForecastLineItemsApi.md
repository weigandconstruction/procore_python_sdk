# procore_sdk.ConstructionFinancialsBudgetManualForecastLineItemsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_manual_forecast_line_items_get**](ConstructionFinancialsBudgetManualForecastLineItemsApi.md#rest_v10_projects_project_id_manual_forecast_line_items_get) | **GET** /rest/v1.0/projects/{project_id}/manual_forecast_line_items | List Manual Forecast Line Items
[**rest_v10_projects_project_id_manual_forecast_line_items_id_delete**](ConstructionFinancialsBudgetManualForecastLineItemsApi.md#rest_v10_projects_project_id_manual_forecast_line_items_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/manual_forecast_line_items/{id} | Delete A Manual Forecast Line Item
[**rest_v10_projects_project_id_manual_forecast_line_items_id_patch**](ConstructionFinancialsBudgetManualForecastLineItemsApi.md#rest_v10_projects_project_id_manual_forecast_line_items_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/manual_forecast_line_items/{id} | Update A Manual Forecast Line Item
[**rest_v10_projects_project_id_manual_forecast_line_items_post**](ConstructionFinancialsBudgetManualForecastLineItemsApi.md#rest_v10_projects_project_id_manual_forecast_line_items_post) | **POST** /rest/v1.0/projects/{project_id}/manual_forecast_line_items | Create A Manual Forecast Line Item


# **rest_v10_projects_project_id_manual_forecast_line_items_get**
> List[RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner] rest_v10_projects_project_id_manual_forecast_line_items_get(procore_company_id, project_id)

List Manual Forecast Line Items

Returns a list of Manual Forecast Line Items on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_get200_response_inner import RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetManualForecastLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Manual Forecast Line Items
        api_response = api_instance.rest_v10_projects_project_id_manual_forecast_line_items_get(procore_company_id, project_id)
        print("The response of ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner]**](RestV10ProjectsProjectIdManualForecastLineItemsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_manual_forecast_line_items_id_delete**
> rest_v10_projects_project_id_manual_forecast_line_items_id_delete(procore_company_id, project_id, id, rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request)

Delete A Manual Forecast Line Item

Delete a manual forecast line item for a budget line item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request import RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetManualForecastLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Unique identifier for the manual forecast line item.
    rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request = procore_sdk.RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest() # RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest | 

    try:
        # Delete A Manual Forecast Line Item
        api_instance.rest_v10_projects_project_id_manual_forecast_line_items_id_delete(procore_company_id, project_id, id, rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Unique identifier for the manual forecast line item. | 
 **rest_v10_projects_project_id_manual_forecast_line_items_id_delete_request** | [**RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest**](RestV10ProjectsProjectIdManualForecastLineItemsIdDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The manual forecast line item has been deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_manual_forecast_line_items_id_patch**
> RestV10ProjectsProjectIdManualForecastLineItemsPost201Response rest_v10_projects_project_id_manual_forecast_line_items_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_manual_forecast_line_items_post_request)

Update A Manual Forecast Line Item

Update a manual forecast line item for a budget line item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_post201_response import RestV10ProjectsProjectIdManualForecastLineItemsPost201Response
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_post_request import RestV10ProjectsProjectIdManualForecastLineItemsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetManualForecastLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Unique identifier for the manual forecast line item.
    rest_v10_projects_project_id_manual_forecast_line_items_post_request = procore_sdk.RestV10ProjectsProjectIdManualForecastLineItemsPostRequest() # RestV10ProjectsProjectIdManualForecastLineItemsPostRequest | 

    try:
        # Update A Manual Forecast Line Item
        api_response = api_instance.rest_v10_projects_project_id_manual_forecast_line_items_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_manual_forecast_line_items_post_request)
        print("The response of ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Unique identifier for the manual forecast line item. | 
 **rest_v10_projects_project_id_manual_forecast_line_items_post_request** | [**RestV10ProjectsProjectIdManualForecastLineItemsPostRequest**](RestV10ProjectsProjectIdManualForecastLineItemsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdManualForecastLineItemsPost201Response**](RestV10ProjectsProjectIdManualForecastLineItemsPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_manual_forecast_line_items_post**
> RestV10ProjectsProjectIdManualForecastLineItemsPost201Response rest_v10_projects_project_id_manual_forecast_line_items_post(procore_company_id, project_id, rest_v10_projects_project_id_manual_forecast_line_items_post_request)

Create A Manual Forecast Line Item

Create a manual forecast line item for a budget line item

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_post201_response import RestV10ProjectsProjectIdManualForecastLineItemsPost201Response
from procore_sdk.models.rest_v10_projects_project_id_manual_forecast_line_items_post_request import RestV10ProjectsProjectIdManualForecastLineItemsPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsBudgetManualForecastLineItemsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_manual_forecast_line_items_post_request = procore_sdk.RestV10ProjectsProjectIdManualForecastLineItemsPostRequest() # RestV10ProjectsProjectIdManualForecastLineItemsPostRequest | 

    try:
        # Create A Manual Forecast Line Item
        api_response = api_instance.rest_v10_projects_project_id_manual_forecast_line_items_post(procore_company_id, project_id, rest_v10_projects_project_id_manual_forecast_line_items_post_request)
        print("The response of ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsBudgetManualForecastLineItemsApi->rest_v10_projects_project_id_manual_forecast_line_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_manual_forecast_line_items_post_request** | [**RestV10ProjectsProjectIdManualForecastLineItemsPostRequest**](RestV10ProjectsProjectIdManualForecastLineItemsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdManualForecastLineItemsPost201Response**](RestV10ProjectsProjectIdManualForecastLineItemsPost201Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

