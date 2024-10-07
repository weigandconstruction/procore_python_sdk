# procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_budgeted_production_quantities_get**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_get) | **GET** /rest/v1.0/projects/{project_id}/budgeted_production_quantities | List all Project Budgeted Production Quantities
[**rest_v10_projects_project_id_budgeted_production_quantities_id_delete**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/budgeted_production_quantities/{id} | Delete a Budgeted Production Quantity
[**rest_v10_projects_project_id_budgeted_production_quantities_id_get**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_id_get) | **GET** /rest/v1.0/projects/{project_id}/budgeted_production_quantities/{id} | Show a Budgeted Production Quantity
[**rest_v10_projects_project_id_budgeted_production_quantities_id_patch**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/budgeted_production_quantities/{id} | Update a Budgeted Production Quantity
[**rest_v10_projects_project_id_budgeted_production_quantities_ids_get**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_ids_get) | **GET** /rest/v1.0/projects/{project_id}/budgeted_production_quantities/ids | List all Project Budgeted Production Quantity IDs
[**rest_v10_projects_project_id_budgeted_production_quantities_post**](FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi.md#rest_v10_projects_project_id_budgeted_production_quantities_post) | **POST** /rest/v1.0/projects/{project_id}/budgeted_production_quantities | Create a new Budgeted Production Quantity


# **rest_v10_projects_project_id_budgeted_production_quantities_get**
> List[RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner] rest_v10_projects_project_id_budgeted_production_quantities_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List all Project Budgeted Production Quantities

Return a list of all Budgeted Production Quantities with details for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all Project Budgeted Production Quantities
        api_response = api_instance.rest_v10_projects_project_id_budgeted_production_quantities_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner]**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budgeted_production_quantities_id_delete**
> rest_v10_projects_project_id_budgeted_production_quantities_id_delete(procore_company_id, project_id, id, budgeted_production_quantity_body)

Delete a Budgeted Production Quantity

Deleting a Budgeted Production Quantity associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.budgeted_production_quantity_body import BudgetedProductionQuantityBody
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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Budgeted Production Quantity
    budgeted_production_quantity_body = procore_sdk.BudgetedProductionQuantityBody() # BudgetedProductionQuantityBody | 

    try:
        # Delete a Budgeted Production Quantity
        api_instance.rest_v10_projects_project_id_budgeted_production_quantities_id_delete(procore_company_id, project_id, id, budgeted_production_quantity_body)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Budgeted Production Quantity | 
 **budgeted_production_quantity_body** | [**BudgetedProductionQuantityBody**](BudgetedProductionQuantityBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budgeted Production Quantity Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budgeted_production_quantities_id_get**
> RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_budgeted_production_quantities_id_get(procore_company_id, project_id, id)

Show a Budgeted Production Quantity

Show a Budgeted Production Quantity associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Budgeted Production Quantity

    try:
        # Show a Budgeted Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_budgeted_production_quantities_id_get(procore_company_id, project_id, id)
        print("The response of FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Budgeted Production Quantity | 

### Return type

[**RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budgeted Production Quantity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budgeted_production_quantities_id_patch**
> RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_budgeted_production_quantities_id_patch(procore_company_id, project_id, id, budgeted_production_quantity_body)

Update a Budgeted Production Quantity

Updating a Budgeted Production Quantity associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.budgeted_production_quantity_body import BudgetedProductionQuantityBody
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Id of the Budgeted Production Quantity
    budgeted_production_quantity_body = procore_sdk.BudgetedProductionQuantityBody() # BudgetedProductionQuantityBody | 

    try:
        # Update a Budgeted Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_budgeted_production_quantities_id_patch(procore_company_id, project_id, id, budgeted_production_quantity_body)
        print("The response of FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Id of the Budgeted Production Quantity | 
 **budgeted_production_quantity_body** | [**BudgetedProductionQuantityBody**](BudgetedProductionQuantityBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budgeted Production Quantity Updated |  -  |
**422** | Error updating a Budgeted Production Quantity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budgeted_production_quantities_ids_get**
> List[int] rest_v10_projects_project_id_budgeted_production_quantities_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List all Project Budgeted Production Quantity IDs

Return a list of all Budgeted Production Quantity IDs with details for a specified Project.

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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List all Project Budgeted Production Quantity IDs
        api_response = api_instance.rest_v10_projects_project_id_budgeted_production_quantities_ids_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_ids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

**List[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_budgeted_production_quantities_post**
> RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_budgeted_production_quantities_post(procore_company_id, project_id, budgeted_production_quantity_body)

Create a new Budgeted Production Quantity

Create a new Budgeted Production Quantity associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.budgeted_production_quantity_body import BudgetedProductionQuantityBody
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    budgeted_production_quantity_body = procore_sdk.BudgetedProductionQuantityBody() # BudgetedProductionQuantityBody | 

    try:
        # Create a new Budgeted Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_budgeted_production_quantities_post(procore_company_id, project_id, budgeted_production_quantity_body)
        print("The response of FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityBudgetedProductionQuantitiesBudgetedProductionQuantitiesApi->rest_v10_projects_project_id_budgeted_production_quantities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **budgeted_production_quantity_body** | [**BudgetedProductionQuantityBody**](BudgetedProductionQuantityBody.md)|  | 

### Return type

[**RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Budgeted Production Quantity Created Succesfully |  -  |
**422** | Error creating a Budgeted Production Quantity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

