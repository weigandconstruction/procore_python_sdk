# procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_prime_change_order_batches_get**](ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi.md#rest_v10_projects_project_id_prime_change_order_batches_get) | **GET** /rest/v1.0/projects/{project_id}/prime_change_order_batches | Show All Prime Change Order Batches
[**rest_v10_projects_project_id_prime_change_order_batches_id_delete**](ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi.md#rest_v10_projects_project_id_prime_change_order_batches_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/prime_change_order_batches/{id} | Delete Prime Change Order Batch
[**rest_v10_projects_project_id_prime_change_order_batches_id_get**](ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi.md#rest_v10_projects_project_id_prime_change_order_batches_id_get) | **GET** /rest/v1.0/projects/{project_id}/prime_change_order_batches/{id} | Show Prime Change Order Batch
[**rest_v10_projects_project_id_prime_change_order_batches_id_patch**](ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi.md#rest_v10_projects_project_id_prime_change_order_batches_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/prime_change_order_batches/{id} | Update Prime Change Order Batch
[**rest_v10_projects_project_id_prime_change_order_batches_post**](ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi.md#rest_v10_projects_project_id_prime_change_order_batches_post) | **POST** /rest/v1.0/projects/{project_id}/prime_change_order_batches | Create Prime Change Order Batch


# **rest_v10_projects_project_id_prime_change_order_batches_get**
> RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200Response rest_v10_projects_project_id_prime_change_order_batches_get(procore_company_id, project_id, sort=sort, filters_id=filters_id, filters_change_order_id=filters_change_order_id, filters_contract_id=filters_contract_id)

Show All Prime Change Order Batches

Returns all Prime Change Order Batches for the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_prime_change_order_batches_get200_response import RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    sort = 'sort_example' # str | Direction (asc/desc) can be controlled by the presence or absence of '-' before the sort parameter. (optional)
    filters_id = 56 # int | Filter results by Change Order Batch ID (optional)
    filters_change_order_id = 56 # int | Filter results by Change Order ID (optional)
    filters_contract_id = 56 # int | Filter results by Contract ID (optional)

    try:
        # Show All Prime Change Order Batches
        api_response = api_instance.rest_v10_projects_project_id_prime_change_order_batches_get(procore_company_id, project_id, sort=sort, filters_id=filters_id, filters_change_order_id=filters_change_order_id, filters_contract_id=filters_contract_id)
        print("The response of ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **sort** | **str**| Direction (asc/desc) can be controlled by the presence or absence of &#39;-&#39; before the sort parameter. | [optional] 
 **filters_id** | **int**| Filter results by Change Order Batch ID | [optional] 
 **filters_change_order_id** | **int**| Filter results by Change Order ID | [optional] 
 **filters_contract_id** | **int**| Filter results by Contract ID | [optional] 

### Return type

[**RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200Response**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_prime_change_order_batches_id_delete**
> rest_v10_projects_project_id_prime_change_order_batches_id_delete(procore_company_id, id, project_id)

Delete Prime Change Order Batch

Delete the specified Prime Change Order Batch.

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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Change Order Batch
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Prime Change Order Batch
        api_instance.rest_v10_projects_project_id_prime_change_order_batches_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Change Order Batch | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_prime_change_order_batches_id_get**
> RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response rest_v10_projects_project_id_prime_change_order_batches_id_get(procore_company_id, id, project_id)

Show Prime Change Order Batch

Show the details of the Prime Change Order Batch.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_prime_change_order_batches_post201_response import RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Change Order Batch
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Prime Change Order Batch
        api_response = api_instance.rest_v10_projects_project_id_prime_change_order_batches_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Change Order Batch | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_prime_change_order_batches_id_patch**
> RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response rest_v10_projects_project_id_prime_change_order_batches_id_patch(procore_company_id, id, project_id, body48, run_configurable_validations=run_configurable_validations)

Update Prime Change Order Batch

Update the specified Prime Change Order Batch.

### Example


```python
import procore_sdk
from procore_sdk.models.body48 import Body48
from procore_sdk.models.rest_v10_projects_project_id_prime_change_order_batches_post201_response import RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Prime Change Order Batch
    project_id = 56 # int | Unique identifier for the project.
    body48 = procore_sdk.Body48() # Body48 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Prime Change Order Batch
        api_response = api_instance.rest_v10_projects_project_id_prime_change_order_batches_id_patch(procore_company_id, id, project_id, body48, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Prime Change Order Batch | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body48** | [**Body48**](Body48.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_prime_change_order_batches_post**
> RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response rest_v10_projects_project_id_prime_change_order_batches_post(procore_company_id, project_id, body47, run_configurable_validations=run_configurable_validations)

Create Prime Change Order Batch

Create a new Prime Change Order Batch.

### Example


```python
import procore_sdk
from procore_sdk.models.body47 import Body47
from procore_sdk.models.rest_v10_projects_project_id_prime_change_order_batches_post201_response import RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body47 = procore_sdk.Body47() # Body47 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Prime Change Order Batch
        api_response = api_instance.rest_v10_projects_project_id_prime_change_order_batches_post(procore_company_id, project_id, body47, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersPrimeChangeOrderBatchesApi->rest_v10_projects_project_id_prime_change_order_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body47** | [**Body47**](Body47.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

