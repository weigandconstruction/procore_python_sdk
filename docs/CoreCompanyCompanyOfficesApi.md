# procore_sdk.CoreCompanyCompanyOfficesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_offices_get**](CoreCompanyCompanyOfficesApi.md#rest_v10_offices_get) | **GET** /rest/v1.0/offices | List company offices
[**rest_v10_offices_id_delete**](CoreCompanyCompanyOfficesApi.md#rest_v10_offices_id_delete) | **DELETE** /rest/v1.0/offices/{id} | Delete a company office
[**rest_v10_offices_id_get**](CoreCompanyCompanyOfficesApi.md#rest_v10_offices_id_get) | **GET** /rest/v1.0/offices/{id} | Show company office
[**rest_v10_offices_id_patch**](CoreCompanyCompanyOfficesApi.md#rest_v10_offices_id_patch) | **PATCH** /rest/v1.0/offices/{id} | Update company office
[**rest_v10_offices_post**](CoreCompanyCompanyOfficesApi.md#rest_v10_offices_post) | **POST** /rest/v1.0/offices | Create company office


# **rest_v10_offices_get**
> List[Office1] rest_v10_offices_get(procore_company_id, company_id, page=page, per_page=per_page, view=view)

List company offices

Returns a collection of Offices associated to a Company

### Example


```python
import procore_sdk
from procore_sdk.models.office1 import Office1
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
    api_instance = procore_sdk.CoreCompanyCompanyOfficesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    view = 'view_example' # str | The view determines which fields are returned. 'normal' returns id, address, city, country_code, division, fax, logo, name, phone, state_code, and zip.  'extended' additionally returns main_office. (optional)

    try:
        # List company offices
        api_response = api_instance.rest_v10_offices_get(procore_company_id, company_id, page=page, per_page=per_page, view=view)
        print("The response of CoreCompanyCompanyOfficesApi->rest_v10_offices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyOfficesApi->rest_v10_offices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **view** | **str**| The view determines which fields are returned. &#39;normal&#39; returns id, address, city, country_code, division, fax, logo, name, phone, state_code, and zip.  &#39;extended&#39; additionally returns main_office. | [optional] 

### Return type

[**List[Office1]**](Office1.md)

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

# **rest_v10_offices_id_delete**
> rest_v10_offices_id_delete(procore_company_id, id, company_id)

Delete a company office

Deletes an Office associated to a Company.

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
    api_instance = procore_sdk.CoreCompanyCompanyOfficesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the office
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete a company office
        api_instance.rest_v10_offices_id_delete(procore_company_id, id, company_id)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyOfficesApi->rest_v10_offices_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the office | 
 **company_id** | **int**| Unique identifier for the company. | 

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

# **rest_v10_offices_id_get**
> Office1 rest_v10_offices_id_get(procore_company_id, id, company_id, view=view)

Show company office

Returns information about an Office associated to a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.office1 import Office1
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
    api_instance = procore_sdk.CoreCompanyCompanyOfficesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the office
    company_id = 56 # int | Unique identifier for the company.
    view = 'view_example' # str | Response schema to use (optional)

    try:
        # Show company office
        api_response = api_instance.rest_v10_offices_id_get(procore_company_id, id, company_id, view=view)
        print("The response of CoreCompanyCompanyOfficesApi->rest_v10_offices_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyOfficesApi->rest_v10_offices_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the office | 
 **company_id** | **int**| Unique identifier for the company. | 
 **view** | **str**| Response schema to use | [optional] 

### Return type

[**Office1**](Office1.md)

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

# **rest_v10_offices_id_patch**
> Office1 rest_v10_offices_id_patch(procore_company_id, id, body110)

Update company office

Updates an Office associated to a Company.  #### Uploading logo To upload an office logo you must upload whole payload as `multipart/form-data` content-type and specify each parameter as form-data together with `office[logo]` as file.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.body110 import Body110
from procore_sdk.models.office1 import Office1
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
    api_instance = procore_sdk.CoreCompanyCompanyOfficesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the office
    body110 = procore_sdk.Body110() # Body110 | 

    try:
        # Update company office
        api_response = api_instance.rest_v10_offices_id_patch(procore_company_id, id, body110)
        print("The response of CoreCompanyCompanyOfficesApi->rest_v10_offices_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyOfficesApi->rest_v10_offices_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the office | 
 **body110** | [**Body110**](Body110.md)|  | 

### Return type

[**Office1**](Office1.md)

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

# **rest_v10_offices_post**
> Office1 rest_v10_offices_post(procore_company_id, body110)

Create company office

Creates an Office associated to a Company.  #### Uploading logo To upload an office logo you must upload whole payload as `multipart/form-data` content-type and specify each parameter as form-data together with `office[logo]` as file.  #### Country and State codes The `country_code` and `state_code` parameter values must conform to the ISO-3166 Alpha-2 specification. See [Working with Country Codes](/documentation/country-codes) for additional information.

### Example


```python
import procore_sdk
from procore_sdk.models.body110 import Body110
from procore_sdk.models.office1 import Office1
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
    api_instance = procore_sdk.CoreCompanyCompanyOfficesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body110 = procore_sdk.Body110() # Body110 | 

    try:
        # Create company office
        api_response = api_instance.rest_v10_offices_post(procore_company_id, body110)
        print("The response of CoreCompanyCompanyOfficesApi->rest_v10_offices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyCompanyOfficesApi->rest_v10_offices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body110** | [**Body110**](Body110.md)|  | 

### Return type

[**Office1**](Office1.md)

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

