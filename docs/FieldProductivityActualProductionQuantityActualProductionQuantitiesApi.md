# procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_actual_production_quantities_bulk_create_post**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/actual_production_quantities/bulk_create | Bulk Create Actual Production Quantities
[**rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/actual_production_quantities/bulk_destroy | Bulk Destroy Actual Production Quantities
[**rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/actual_production_quantities/bulk_update | Bulk Update Actual Production Quantities
[**rest_v10_projects_project_id_actual_production_quantities_get**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_get) | **GET** /rest/v1.0/projects/{project_id}/actual_production_quantities | List all Actual Production Quantities
[**rest_v10_projects_project_id_actual_production_quantities_id_delete**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/actual_production_quantities/{id} | Delete Actual Production Quantity
[**rest_v10_projects_project_id_actual_production_quantities_id_get**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_id_get) | **GET** /rest/v1.0/projects/{project_id}/actual_production_quantities/{id} | Show Actual Production Quantity
[**rest_v10_projects_project_id_actual_production_quantities_id_patch**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/actual_production_quantities/{id} | Update Actual Production Quantity
[**rest_v10_projects_project_id_actual_production_quantities_ids_get**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_ids_get) | **GET** /rest/v1.0/projects/{project_id}/actual_production_quantities/ids | List of Actual Production Quantity Ids
[**rest_v10_projects_project_id_actual_production_quantities_post**](FieldProductivityActualProductionQuantityActualProductionQuantitiesApi.md#rest_v10_projects_project_id_actual_production_quantities_post) | **POST** /rest/v1.0/projects/{project_id}/actual_production_quantities | Create Actual Production Quantity


# **rest_v10_projects_project_id_actual_production_quantities_bulk_create_post**
> RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response rest_v10_projects_project_id_actual_production_quantities_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request=rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request)

Bulk Create Actual Production Quantities

This endpoint bulk creates a batch of Actual Production Quantities (APQ).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_create_post201_response import RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request import RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostRequest |  (optional)

    try:
        # Bulk Create Actual Production Quantities
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_bulk_create_post(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request=rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_actual_production_quantities_bulk_create_post_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePostRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Actual Production Quantities Created Succesfully |  -  |
**403** | User does not have permission to create Actual Production Quantities |  -  |
**422** | Error creating Actual Production Quantities |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete**
> RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request=rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request)

Bulk Destroy Actual Production Quantities

This endpoint bulk destroys a batch of Actual Production Quantities (APQ).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_create_post201_response import RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request import RestV10ProjectsProjectIdActualProductionQuantitiesBulkDestroyDeleteRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesBulkDestroyDeleteRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesBulkDestroyDeleteRequest |  (optional)

    try:
        # Bulk Destroy Actual Production Quantities
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request=rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_actual_production_quantities_bulk_destroy_delete_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesBulkDestroyDeleteRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkDestroyDeleteRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actual Production Quantities Destroyed Succesfully |  -  |
**403** | User does not have permission to destroy Actual Production Quantities |  -  |
**422** | Error destroy Actual Production Quantities |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch**
> RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request=rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request)

Bulk Update Actual Production Quantities

This endpoint bulk updates a batch of Actual Production Quantities (APQ).

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_create_post201_response import RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request import RestV10ProjectsProjectIdActualProductionQuantitiesBulkUpdatePatchRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesBulkUpdatePatchRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesBulkUpdatePatchRequest |  (optional)

    try:
        # Bulk Update Actual Production Quantities
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request=rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_actual_production_quantities_bulk_update_patch_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesBulkUpdatePatchRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkUpdatePatchRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response**](RestV10ProjectsProjectIdActualProductionQuantitiesBulkCreatePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actual Production Quantities Updated Succesfully |  -  |
**403** | User does not have permission to update Actual Production Quantities |  -  |
**422** | Error update Actual Production Quantities |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_get**
> List[RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner] rest_v10_projects_project_id_actual_production_quantities_get(procore_company_id, project_id, filters_unit_of_measure=filters_unit_of_measure, filters_updated_at=filters_updated_at, filters_timesheet_id=filters_timesheet_id, filters_crew_id=filters_crew_id, filters_location_id=filters_location_id, filters_date=filters_date, filters_id=filters_id, per_page=per_page, page=page)

List all Actual Production Quantities

Return a list of all Actual Production Quantities for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_unit_of_measure = 'filters_unit_of_measure_example' # str | Return item(s) with the specified unit of measure. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_timesheet_id = 'filters_timesheet_id_example' # str | Timesheet ID. Returns item(s) with the specified Timesheet ID. (optional)
    filters_crew_id = 'filters_crew_id_example' # str | Crew ID. Returns item(s) with the specified Crew ID. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_date = 'filters_date_example' # str | Returns item(s) within the specified ISO 8601 datetime range. (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    per_page = 56 # int | Elements per page (optional)
    page = 56 # int | Page (optional)

    try:
        # List all Actual Production Quantities
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_get(procore_company_id, project_id, filters_unit_of_measure=filters_unit_of_measure, filters_updated_at=filters_updated_at, filters_timesheet_id=filters_timesheet_id, filters_crew_id=filters_crew_id, filters_location_id=filters_location_id, filters_date=filters_date, filters_id=filters_id, per_page=per_page, page=page)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_unit_of_measure** | **str**| Return item(s) with the specified unit of measure. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_timesheet_id** | **str**| Timesheet ID. Returns item(s) with the specified Timesheet ID. | [optional] 
 **filters_crew_id** | **str**| Crew ID. Returns item(s) with the specified Crew ID. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_date** | **str**| Returns item(s) within the specified ISO 8601 datetime range. | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **page** | **int**| Page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner]**](RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_id_delete**
> RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_actual_production_quantities_id_delete(procore_company_id, project_id, id)

Delete Actual Production Quantity

Delete Actual Production Quantity.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Delete Actual Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_id_delete(procore_company_id, project_id, id)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actual Production Quantity delete |  -  |
**403** | User does not have permission to delete Actual Production Quantities |  -  |
**422** | Error deleting Actual Production Quantities |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_id_get**
> RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_actual_production_quantities_id_get(procore_company_id, project_id, id, rest_v10_projects_project_id_actual_production_quantities_id_get_request=rest_v10_projects_project_id_actual_production_quantities_id_get_request)

Show Actual Production Quantity

Return Actual Production Quantity detailed information.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_id_get_request import RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    rest_v10_projects_project_id_actual_production_quantities_id_get_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest |  (optional)

    try:
        # Show Actual Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_id_get(procore_company_id, project_id, id, rest_v10_projects_project_id_actual_production_quantities_id_get_request=rest_v10_projects_project_id_actual_production_quantities_id_get_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **rest_v10_projects_project_id_actual_production_quantities_id_get_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_id_patch**
> RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_actual_production_quantities_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_actual_production_quantities_id_get_request=rest_v10_projects_project_id_actual_production_quantities_id_get_request)

Update Actual Production Quantity

Update Actual Production Quantity associated with the specific Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_id_get_request import RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    rest_v10_projects_project_id_actual_production_quantities_id_get_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest |  (optional)

    try:
        # Update Actual Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_actual_production_quantities_id_get_request=rest_v10_projects_project_id_actual_production_quantities_id_get_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **rest_v10_projects_project_id_actual_production_quantities_id_get_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesIdGetRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actual Production Quantity updated |  -  |
**403** | User does not have permission to update Actual Production Quantities |  -  |
**422** | Error updating Actual Production Quantities |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_ids_get**
> List[int] rest_v10_projects_project_id_actual_production_quantities_ids_get(procore_company_id, project_id, filters_unit_of_measure=filters_unit_of_measure, filters_updated_at=filters_updated_at, filters_timesheet_id=filters_timesheet_id, filters_crew_id=filters_crew_id, filters_location_id=filters_location_id, filters_date=filters_date, per_page=per_page, page=page)

List of Actual Production Quantity Ids

Returns a list of Actual Production Quantity Ids.

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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_unit_of_measure = 'filters_unit_of_measure_example' # str | Return item(s) with the specified unit of measure. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_timesheet_id = 'filters_timesheet_id_example' # str | Timesheet ID. Returns item(s) with the specified Timesheet ID. (optional)
    filters_crew_id = 'filters_crew_id_example' # str | Crew ID. Returns item(s) with the specified Crew ID. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_date = 'filters_date_example' # str | Returns item(s) within the specified ISO 8601 datetime range. (optional)
    per_page = 56 # int | Elements per page (optional)
    page = 56 # int | Page (optional)

    try:
        # List of Actual Production Quantity Ids
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_ids_get(procore_company_id, project_id, filters_unit_of_measure=filters_unit_of_measure, filters_updated_at=filters_updated_at, filters_timesheet_id=filters_timesheet_id, filters_crew_id=filters_crew_id, filters_location_id=filters_location_id, filters_date=filters_date, per_page=per_page, page=page)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_ids_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_unit_of_measure** | **str**| Return item(s) with the specified unit of measure. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_timesheet_id** | **str**| Timesheet ID. Returns item(s) with the specified Timesheet ID. | [optional] 
 **filters_crew_id** | **str**| Crew ID. Returns item(s) with the specified Crew ID. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_date** | **str**| Returns item(s) within the specified ISO 8601 datetime range. | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **page** | **int**| Page | [optional] 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_actual_production_quantities_post**
> RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner rest_v10_projects_project_id_actual_production_quantities_post(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_post_request=rest_v10_projects_project_id_actual_production_quantities_post_request)

Create Actual Production Quantity

Create new Actual Production Quantity associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_get200_response_inner import RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_post_request import RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest
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
    api_instance = procore_sdk.FieldProductivityActualProductionQuantityActualProductionQuantitiesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_actual_production_quantities_post_request = procore_sdk.RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest() # RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest |  (optional)

    try:
        # Create Actual Production Quantity
        api_response = api_instance.rest_v10_projects_project_id_actual_production_quantities_post(procore_company_id, project_id, rest_v10_projects_project_id_actual_production_quantities_post_request=rest_v10_projects_project_id_actual_production_quantities_post_request)
        print("The response of FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityActualProductionQuantityActualProductionQuantitiesApi->rest_v10_projects_project_id_actual_production_quantities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_actual_production_quantities_post_request** | [**RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest**](RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest.md)|  | [optional] 

### Return type

[**RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner**](RestV10ProjectsProjectIdActualProductionQuantitiesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Actual Production Quantity Created Succesfully |  -  |
**403** | User does not have permission to create Actual Production Quantity |  -  |
**422** | Error creating Actual Production Quantity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

