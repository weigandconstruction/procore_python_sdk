# procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderPackagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_change_order_packages_get**](ConstructionFinancialsChangeOrdersChangeOrderPackagesApi.md#rest_v10_change_order_packages_get) | **GET** /rest/v1.0/change_order_packages | List Change Order Packages
[**rest_v10_change_order_packages_id_get**](ConstructionFinancialsChangeOrdersChangeOrderPackagesApi.md#rest_v10_change_order_packages_id_get) | **GET** /rest/v1.0/change_order_packages/{id} | Show Change Order Package
[**rest_v10_change_order_packages_id_patch**](ConstructionFinancialsChangeOrdersChangeOrderPackagesApi.md#rest_v10_change_order_packages_id_patch) | **PATCH** /rest/v1.0/change_order_packages/{id} | Update Change Order Package
[**rest_v10_change_order_packages_post**](ConstructionFinancialsChangeOrdersChangeOrderPackagesApi.md#rest_v10_change_order_packages_post) | **POST** /rest/v1.0/change_order_packages | Create Change Order Package


# **rest_v10_change_order_packages_get**
> List[RestV10ChangeOrderPackagesGet200ResponseInner] rest_v10_change_order_packages_get(procore_company_id, project_id, contract_id=contract_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_reviewed_at=filters_reviewed_at, filters_due_date=filters_due_date, filters_include_deleted=filters_include_deleted, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, filters_signed_change_order_received_date=filters_signed_change_order_received_date, page=page, per_page=per_page)

List Change Order Packages

List Change Order Packages.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_packages_get200_response_inner import RestV10ChangeOrderPackagesGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_reviewed_at = 'filters_reviewed_at_example' # str | Returns item(s) reviewed within the specified ISO 8601 datetime range. (optional)
    filters_due_date = 'filters_due_date_example' # str | Returns item(s) due within the specified ISO 8601 datetime range. (optional)
    filters_include_deleted = 'filters_include_deleted_example' # str | Use 'only' for only deleted resources. Use 'with' for deleted and undeleted resources. (optional)
    filters_invoiced_date = 'filters_invoiced_date_example' # str | Returns item(s) invoiced within the specified ISO 8601 datetime range. (optional)
    filters_paid_date = 'filters_paid_date_example' # str | Returns item(s) paid within the specified ISO 8601 datetime range. (optional)
    filters_signed_change_order_received_date = 'filters_signed_change_order_received_date_example' # str | Return item(s) with a signed change order received date within the specified ISO 8601 date range. (optional)
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Change Order Packages
        api_response = api_instance.rest_v10_change_order_packages_get(procore_company_id, project_id, contract_id=contract_id, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_reviewed_at=filters_reviewed_at, filters_due_date=filters_due_date, filters_include_deleted=filters_include_deleted, filters_invoiced_date=filters_invoiced_date, filters_paid_date=filters_paid_date, filters_signed_change_order_received_date=filters_signed_change_order_received_date, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_reviewed_at** | **str**| Returns item(s) reviewed within the specified ISO 8601 datetime range. | [optional] 
 **filters_due_date** | **str**| Returns item(s) due within the specified ISO 8601 datetime range. | [optional] 
 **filters_include_deleted** | **str**| Use &#39;only&#39; for only deleted resources. Use &#39;with&#39; for deleted and undeleted resources. | [optional] 
 **filters_invoiced_date** | **str**| Returns item(s) invoiced within the specified ISO 8601 datetime range. | [optional] 
 **filters_paid_date** | **str**| Returns item(s) paid within the specified ISO 8601 datetime range. | [optional] 
 **filters_signed_change_order_received_date** | **str**| Return item(s) with a signed change order received date within the specified ISO 8601 date range. | [optional] 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ChangeOrderPackagesGet200ResponseInner]**](RestV10ChangeOrderPackagesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | User does not have correct permissions. |  -  |
**403** | User does not have correct permissions. |  -  |
**404** | Specified Contract does not exists or User does not have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_packages_id_get**
> RestV10ChangeOrderPackagesIdGet200Response rest_v10_change_order_packages_id_get(procore_company_id, id, project_id, contract_id=contract_id)

Show Change Order Package

Show Change Order Package

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_packages_id_get200_response import RestV10ChangeOrderPackagesIdGet200Response
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.
    contract_id = 56 # int | Contract ID (optional)

    try:
        # Show Change Order Package
        api_response = api_instance.rest_v10_change_order_packages_id_get(procore_company_id, id, project_id, contract_id=contract_id)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **contract_id** | **int**| Contract ID | [optional] 

### Return type

[**RestV10ChangeOrderPackagesIdGet200Response**](RestV10ChangeOrderPackagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User does not have correct permissions. |  -  |
**403** | User does not have correct permissions. |  -  |
**404** | Specified Contract does not exists or User does not have access to it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_packages_id_patch**
> RestV10ChangeOrderPackagesIdGet200Response rest_v10_change_order_packages_id_patch(procore_company_id, id, rest_v10_change_order_packages_id_patch_request)

Update Change Order Package

Update Change Order Package

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_packages_id_get200_response import RestV10ChangeOrderPackagesIdGet200Response
from procore_sdk.models.rest_v10_change_order_packages_id_patch_request import RestV10ChangeOrderPackagesIdPatchRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    rest_v10_change_order_packages_id_patch_request = procore_sdk.RestV10ChangeOrderPackagesIdPatchRequest() # RestV10ChangeOrderPackagesIdPatchRequest | 

    try:
        # Update Change Order Package
        api_response = api_instance.rest_v10_change_order_packages_id_patch(procore_company_id, id, rest_v10_change_order_packages_id_patch_request)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **rest_v10_change_order_packages_id_patch_request** | [**RestV10ChangeOrderPackagesIdPatchRequest**](RestV10ChangeOrderPackagesIdPatchRequest.md)|  | 

### Return type

[**RestV10ChangeOrderPackagesIdGet200Response**](RestV10ChangeOrderPackagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unable to update Change Order Package due to errors. |  -  |
**403** | User does not have correct permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_change_order_packages_post**
> RestV10ChangeOrderPackagesPost201Response rest_v10_change_order_packages_post(procore_company_id, rest_v10_change_order_packages_post_request)

Create Change Order Package

Create Change Order Package

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_change_order_packages_post201_response import RestV10ChangeOrderPackagesPost201Response
from procore_sdk.models.rest_v10_change_order_packages_post_request import RestV10ChangeOrderPackagesPostRequest
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
    api_instance = procore_sdk.ConstructionFinancialsChangeOrdersChangeOrderPackagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    rest_v10_change_order_packages_post_request = procore_sdk.RestV10ChangeOrderPackagesPostRequest() # RestV10ChangeOrderPackagesPostRequest | 

    try:
        # Create Change Order Package
        api_response = api_instance.rest_v10_change_order_packages_post(procore_company_id, rest_v10_change_order_packages_post_request)
        print("The response of ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsChangeOrdersChangeOrderPackagesApi->rest_v10_change_order_packages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **rest_v10_change_order_packages_post_request** | [**RestV10ChangeOrderPackagesPostRequest**](RestV10ChangeOrderPackagesPostRequest.md)|  | 

### Return type

[**RestV10ChangeOrderPackagesPost201Response**](RestV10ChangeOrderPackagesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Unable to create Change Order Package due to errors. |  -  |
**403** | User does not have correct permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

