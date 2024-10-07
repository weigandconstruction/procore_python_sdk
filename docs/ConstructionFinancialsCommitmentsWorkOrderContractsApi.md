# procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_work_order_contracts_get**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_get) | **GET** /rest/v1.0/work_order_contracts | List work order contracts
[**rest_v10_work_order_contracts_id_delete**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_id_delete) | **DELETE** /rest/v1.0/work_order_contracts/{id} | Delete work order contract
[**rest_v10_work_order_contracts_id_get**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_id_get) | **GET** /rest/v1.0/work_order_contracts/{id} | Show work order contract
[**rest_v10_work_order_contracts_id_patch**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_id_patch) | **PATCH** /rest/v1.0/work_order_contracts/{id} | Update work order contract
[**rest_v10_work_order_contracts_post**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_post) | **POST** /rest/v1.0/work_order_contracts | Create work order contract
[**rest_v10_work_order_contracts_sync_patch**](ConstructionFinancialsCommitmentsWorkOrderContractsApi.md#rest_v10_work_order_contracts_sync_patch) | **PATCH** /rest/v1.0/work_order_contracts/sync | Sync work order contracts


# **rest_v10_work_order_contracts_get**
> List[RestV10WorkOrderContractsGet200ResponseInner] rest_v10_work_order_contracts_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_include_deleted=filters_include_deleted, filters_origin_id=filters_origin_id)

List work order contracts

Return a list of all Work Order Contracts of a specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner import RestV10WorkOrderContractsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies how much information to show for each work order contract. The compact view is returned by default. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Work Order Contract status. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)

    try:
        # List work order contracts
        api_response = api_instance.rest_v10_work_order_contracts_get(procore_company_id, project_id, view=view, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_include_deleted=filters_include_deleted, filters_origin_id=filters_origin_id)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies how much information to show for each work order contract. The compact view is returned by default. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_status** | **str**| Return item(s) with the specified Work Order Contract status. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 

### Return type

[**List[RestV10WorkOrderContractsGet200ResponseInner]**](RestV10WorkOrderContractsGet200ResponseInner.md)

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

# **rest_v10_work_order_contracts_id_delete**
> rest_v10_work_order_contracts_id_delete(procore_company_id, id, project_id)

Delete work order contract

Delete a specified Work Order Contract.

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete work order contract
        api_instance.rest_v10_work_order_contracts_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_id_get**
> RestV10WorkOrderContractsPost201Response rest_v10_work_order_contracts_id_get(procore_company_id, id, project_id)

Show work order contract

Return a Work Order Contract.  ### Special notes (Tiers)  The visibility of Change Order Packages, Potential Change Orders & Change Order Requests depends on the number of tiers defined in the Work Order Contract as follows:  1-tier: Change Order Packages  2-tier: Change Order Packages, Potential Change Orders  3-tier: Change Order Packages, Change Order Requests, Potential Change Orders

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_work_order_contracts_post201_response import RestV10WorkOrderContractsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show work order contract
        api_response = api_instance.rest_v10_work_order_contracts_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10WorkOrderContractsPost201Response**](RestV10WorkOrderContractsPost201Response.md)

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

# **rest_v10_work_order_contracts_id_patch**
> RestV10WorkOrderContractsPost201Response rest_v10_work_order_contracts_id_patch(procore_company_id, id, body, run_configurable_validations=run_configurable_validations)

Update work order contract

Update a specified Work Order Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body import Body
from procore_sdk.models.rest_v10_work_order_contracts_post201_response import RestV10WorkOrderContractsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body = procore_sdk.Body() # Body | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update work order contract
        api_response = api_instance.rest_v10_work_order_contracts_id_patch(procore_company_id, id, body, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body** | [**Body**](Body.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10WorkOrderContractsPost201Response**](RestV10WorkOrderContractsPost201Response.md)

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
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_work_order_contracts_post**
> RestV10WorkOrderContractsPost201Response rest_v10_work_order_contracts_post(procore_company_id, body, run_configurable_validations=run_configurable_validations)

Create work order contract

Create a Work Order Contract.

### Example


```python
import procore_sdk
from procore_sdk.models.body import Body
from procore_sdk.models.rest_v10_work_order_contracts_post201_response import RestV10WorkOrderContractsPost201Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body = procore_sdk.Body() # Body | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create work order contract
        api_response = api_instance.rest_v10_work_order_contracts_post(procore_company_id, body, run_configurable_validations=run_configurable_validations)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body** | [**Body**](Body.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10WorkOrderContractsPost201Response**](RestV10WorkOrderContractsPost201Response.md)

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

# **rest_v10_work_order_contracts_sync_patch**
> RestV10WorkOrderContractsSyncPatch200Response rest_v10_work_order_contracts_sync_patch(procore_company_id, body1)

Sync work order contracts

This endpoint creates or updates a batch of Work Order Contracts. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.body1 import Body1
from procore_sdk.models.rest_v10_work_order_contracts_sync_patch200_response import RestV10WorkOrderContractsSyncPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsWorkOrderContractsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body1 = procore_sdk.Body1() # Body1 | 

    try:
        # Sync work order contracts
        api_response = api_instance.rest_v10_work_order_contracts_sync_patch(procore_company_id, body1)
        print("The response of ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsWorkOrderContractsApi->rest_v10_work_order_contracts_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body1** | [**Body1**](Body1.md)|  | 

### Return type

[**RestV10WorkOrderContractsSyncPatch200Response**](RestV10WorkOrderContractsSyncPatch200Response.md)

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

