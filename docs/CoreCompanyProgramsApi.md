# procore_sdk.CoreCompanyProgramsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_programs_get**](CoreCompanyProgramsApi.md#rest_v10_companies_company_id_programs_get) | **GET** /rest/v1.0/companies/{company_id}/programs | List programs
[**rest_v10_companies_company_id_programs_id_delete**](CoreCompanyProgramsApi.md#rest_v10_companies_company_id_programs_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/programs/{id} | Delete program
[**rest_v10_companies_company_id_programs_id_get**](CoreCompanyProgramsApi.md#rest_v10_companies_company_id_programs_id_get) | **GET** /rest/v1.0/companies/{company_id}/programs/{id} | Show program
[**rest_v10_companies_company_id_programs_id_patch**](CoreCompanyProgramsApi.md#rest_v10_companies_company_id_programs_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/programs/{id} | Update program
[**rest_v10_companies_company_id_programs_post**](CoreCompanyProgramsApi.md#rest_v10_companies_company_id_programs_post) | **POST** /rest/v1.0/companies/{company_id}/programs | Create program


# **rest_v10_companies_company_id_programs_get**
> List[Program] rest_v10_companies_company_id_programs_get(procore_company_id, company_id, page=page, per_page=per_page)

List programs

Return a list of Programs associated to the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.program import Program
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
    api_instance = procore_sdk.CoreCompanyProgramsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List programs
        api_response = api_instance.rest_v10_companies_company_id_programs_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Program]**](Program.md)

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

# **rest_v10_companies_company_id_programs_id_delete**
> rest_v10_companies_company_id_programs_id_delete(procore_company_id, company_id, id)

Delete program

Delete the specified Program.

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
    api_instance = procore_sdk.CoreCompanyProgramsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the program

    try:
        # Delete program
        api_instance.rest_v10_companies_company_id_programs_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the program | 

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

# **rest_v10_companies_company_id_programs_id_get**
> RestV10CompaniesCompanyIdProgramsPost201Response rest_v10_companies_company_id_programs_id_get(procore_company_id, company_id, id)

Show program

Show detail on the specified Program.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_programs_post201_response import RestV10CompaniesCompanyIdProgramsPost201Response
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
    api_instance = procore_sdk.CoreCompanyProgramsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the program

    try:
        # Show program
        api_response = api_instance.rest_v10_companies_company_id_programs_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the program | 

### Return type

[**RestV10CompaniesCompanyIdProgramsPost201Response**](RestV10CompaniesCompanyIdProgramsPost201Response.md)

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

# **rest_v10_companies_company_id_programs_id_patch**
> RestV10CompaniesCompanyIdProgramsPost201Response rest_v10_companies_company_id_programs_id_patch(procore_company_id, company_id, id, body43)

Update program

Update the specified Program.

### Example


```python
import procore_sdk
from procore_sdk.models.body43 import Body43
from procore_sdk.models.rest_v10_companies_company_id_programs_post201_response import RestV10CompaniesCompanyIdProgramsPost201Response
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
    api_instance = procore_sdk.CoreCompanyProgramsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the program
    body43 = procore_sdk.Body43() # Body43 | 

    try:
        # Update program
        api_response = api_instance.rest_v10_companies_company_id_programs_id_patch(procore_company_id, company_id, id, body43)
        print("The response of CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the program | 
 **body43** | [**Body43**](Body43.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdProgramsPost201Response**](RestV10CompaniesCompanyIdProgramsPost201Response.md)

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

# **rest_v10_companies_company_id_programs_post**
> RestV10CompaniesCompanyIdProgramsPost201Response rest_v10_companies_company_id_programs_post(procore_company_id, company_id, body43)

Create program

Create a new Program in the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body43 import Body43
from procore_sdk.models.rest_v10_companies_company_id_programs_post201_response import RestV10CompaniesCompanyIdProgramsPost201Response
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
    api_instance = procore_sdk.CoreCompanyProgramsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body43 = procore_sdk.Body43() # Body43 | 

    try:
        # Create program
        api_response = api_instance.rest_v10_companies_company_id_programs_post(procore_company_id, company_id, body43)
        print("The response of CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProgramsApi->rest_v10_companies_company_id_programs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body43** | [**Body43**](Body43.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdProgramsPost201Response**](RestV10CompaniesCompanyIdProgramsPost201Response.md)

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

