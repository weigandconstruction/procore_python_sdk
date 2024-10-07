# procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_line_item_types_get**](ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi.md#rest_v10_line_item_types_get) | **GET** /rest/v1.0/line_item_types | List Line Item Types
[**rest_v10_line_item_types_id_get**](ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi.md#rest_v10_line_item_types_id_get) | **GET** /rest/v1.0/line_item_types/{id} | Show Line Item Type
[**rest_v10_line_item_types_id_patch**](ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi.md#rest_v10_line_item_types_id_patch) | **PATCH** /rest/v1.0/line_item_types/{id} | Update Line Item Type
[**rest_v10_line_item_types_post**](ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi.md#rest_v10_line_item_types_post) | **POST** /rest/v1.0/line_item_types | Create Line Item Type
[**rest_v10_line_item_types_sync_patch**](ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi.md#rest_v10_line_item_types_sync_patch) | **PATCH** /rest/v1.0/line_item_types/sync | Sync Line Item Types


# **rest_v10_line_item_types_get**
> List[LineItemType1] rest_v10_line_item_types_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id)

List Line Item Types

Return a list of all defined Line Item Types. See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.line_item_type1 import LineItemType1
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company. You must supply either a company_id or project_id.
    project_id = 56 # int | Unique identifier for the project. You must supply either a company_id or project_id.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID (optional)

    try:
        # List Line Item Types
        api_response = api_instance.rest_v10_line_item_types_get(procore_company_id, company_id, project_id, page=page, per_page=per_page, filters_origin_id=filters_origin_id)
        print("The response of ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. You must supply either a company_id or project_id. | 
 **project_id** | **int**| Unique identifier for the project. You must supply either a company_id or project_id. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_origin_id** | **str**| Origin ID | [optional] 

### Return type

[**List[LineItemType1]**](LineItemType1.md)

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

# **rest_v10_line_item_types_id_get**
> LineItemType1 rest_v10_line_item_types_id_get(procore_company_id, id, company_id)

Show Line Item Type

Return detailed information for a specified Line Item Type.

### Example


```python
import procore_sdk
from procore_sdk.models.line_item_type1 import LineItemType1
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Line Item Type
        api_response = api_instance.rest_v10_line_item_types_id_get(procore_company_id, id, company_id)
        print("The response of ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**LineItemType1**](LineItemType1.md)

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

# **rest_v10_line_item_types_id_patch**
> LineItemType1 rest_v10_line_item_types_id_patch(procore_company_id, id, body73)

Update Line Item Type

Update a Line Item Type.

### Example


```python
import procore_sdk
from procore_sdk.models.body73 import Body73
from procore_sdk.models.line_item_type1 import LineItemType1
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    body73 = procore_sdk.Body73() # Body73 | 

    try:
        # Update Line Item Type
        api_response = api_instance.rest_v10_line_item_types_id_patch(procore_company_id, id, body73)
        print("The response of ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **body73** | [**Body73**](Body73.md)|  | 

### Return type

[**LineItemType1**](LineItemType1.md)

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

# **rest_v10_line_item_types_post**
> LineItemType1 rest_v10_line_item_types_post(procore_company_id, body73)

Create Line Item Type

Create a new Line Item Type (e.g. L2 for Labor).

### Example


```python
import procore_sdk
from procore_sdk.models.body73 import Body73
from procore_sdk.models.line_item_type1 import LineItemType1
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body73 = procore_sdk.Body73() # Body73 | 

    try:
        # Create Line Item Type
        api_response = api_instance.rest_v10_line_item_types_post(procore_company_id, body73)
        print("The response of ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body73** | [**Body73**](Body73.md)|  | 

### Return type

[**LineItemType1**](LineItemType1.md)

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

# **rest_v10_line_item_types_sync_patch**
> RestV10LineItemTypesSyncPatch200Response rest_v10_line_item_types_sync_patch(procore_company_id, line_item_type_sync_body)

Sync Line Item Types

This endpoint creates or updates a batch of Line Item Types. See [Using Sync Actions](/documentation/using-sync-actions) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.line_item_type_sync_body import LineItemTypeSyncBody
from procore_sdk.models.rest_v10_line_item_types_sync_patch200_response import RestV10LineItemTypesSyncPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    line_item_type_sync_body = procore_sdk.LineItemTypeSyncBody() # LineItemTypeSyncBody | 

    try:
        # Sync Line Item Types
        api_response = api_instance.rest_v10_line_item_types_sync_patch(procore_company_id, line_item_type_sync_body)
        print("The response of ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsLineItemTypesCostTypesApi->rest_v10_line_item_types_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **line_item_type_sync_body** | [**LineItemTypeSyncBody**](LineItemTypeSyncBody.md)|  | 

### Return type

[**RestV10LineItemTypesSyncPatch200Response**](RestV10LineItemTypesSyncPatch200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

