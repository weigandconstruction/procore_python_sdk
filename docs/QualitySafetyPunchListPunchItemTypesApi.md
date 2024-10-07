# procore_sdk.QualitySafetyPunchListPunchItemTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_punch_item_types_get**](QualitySafetyPunchListPunchItemTypesApi.md#rest_v10_punch_item_types_get) | **GET** /rest/v1.0/punch_item_types | List punch item types
[**rest_v10_punch_item_types_id_delete**](QualitySafetyPunchListPunchItemTypesApi.md#rest_v10_punch_item_types_id_delete) | **DELETE** /rest/v1.0/punch_item_types/{id} | Delete Punch Item Type
[**rest_v10_punch_item_types_id_get**](QualitySafetyPunchListPunchItemTypesApi.md#rest_v10_punch_item_types_id_get) | **GET** /rest/v1.0/punch_item_types/{id} | Show Punch Item Type
[**rest_v10_punch_item_types_id_patch**](QualitySafetyPunchListPunchItemTypesApi.md#rest_v10_punch_item_types_id_patch) | **PATCH** /rest/v1.0/punch_item_types/{id} | Update Punch Item type
[**rest_v10_punch_item_types_post**](QualitySafetyPunchListPunchItemTypesApi.md#rest_v10_punch_item_types_post) | **POST** /rest/v1.0/punch_item_types | Create Punch Item Type


# **rest_v10_punch_item_types_get**
> List[PunchItemType1] rest_v10_punch_item_types_get(procore_company_id, project_id, page=page, per_page=per_page)

List punch item types

Return a list of all Punch Item Types on a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item_type1 import PunchItemType1
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List punch item types
        api_response = api_instance.rest_v10_punch_item_types_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[PunchItemType1]**](PunchItemType1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_item_types_id_delete**
> rest_v10_punch_item_types_id_delete(procore_company_id, id, project_id)

Delete Punch Item Type

Delete the specified Punch Item Type.

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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item Type
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Punch Item Type
        api_instance.rest_v10_punch_item_types_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item Type | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_item_types_id_get**
> PunchItemType1 rest_v10_punch_item_types_id_get(procore_company_id, id, project_id)

Show Punch Item Type

Return detail on the specified Punch Item Type.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item_type1 import PunchItemType1
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item Type
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Punch Item Type
        api_response = api_instance.rest_v10_punch_item_types_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item Type | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**PunchItemType1**](PunchItemType1.md)

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

# **rest_v10_punch_item_types_id_patch**
> PunchItemType1 rest_v10_punch_item_types_id_patch(procore_company_id, id, punch_item_type_body)

Update Punch Item type

Update the specified Punch Item Type.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item_type1 import PunchItemType1
from procore_sdk.models.punch_item_type_body import PunchItemTypeBody
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the Punch Item Type
    punch_item_type_body = procore_sdk.PunchItemTypeBody() # PunchItemTypeBody | 

    try:
        # Update Punch Item type
        api_response = api_instance.rest_v10_punch_item_types_id_patch(procore_company_id, id, punch_item_type_body)
        print("The response of QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the Punch Item Type | 
 **punch_item_type_body** | [**PunchItemTypeBody**](PunchItemTypeBody.md)|  | 

### Return type

[**PunchItemType1**](PunchItemType1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_punch_item_types_post**
> PunchItemType1 rest_v10_punch_item_types_post(procore_company_id, punch_item_type_body)

Create Punch Item Type

Create a new Punch Item Type.

### Example


```python
import procore_sdk
from procore_sdk.models.punch_item_type1 import PunchItemType1
from procore_sdk.models.punch_item_type_body import PunchItemTypeBody
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
    api_instance = procore_sdk.QualitySafetyPunchListPunchItemTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    punch_item_type_body = procore_sdk.PunchItemTypeBody() # PunchItemTypeBody | 

    try:
        # Create Punch Item Type
        api_response = api_instance.rest_v10_punch_item_types_post(procore_company_id, punch_item_type_body)
        print("The response of QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyPunchListPunchItemTypesApi->rest_v10_punch_item_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **punch_item_type_body** | [**PunchItemTypeBody**](PunchItemTypeBody.md)|  | 

### Return type

[**PunchItemType1**](PunchItemType1.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

