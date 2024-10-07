# procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_pdf_template_configs_get**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_get) | **GET** /rest/v1.0/companies/{company_id}/pdf_template_configs | List PDF template configs
[**rest_v10_companies_company_id_pdf_template_configs_id_delete**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/pdf_template_configs/{id} | Delete PDF Template Config
[**rest_v10_companies_company_id_pdf_template_configs_id_get**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_id_get) | **GET** /rest/v1.0/companies/{company_id}/pdf_template_configs/{id} | Return a PDF Template Config
[**rest_v10_companies_company_id_pdf_template_configs_id_patch**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/pdf_template_configs/{id} | Update a PDF Template Config
[**rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch) | **PATCH** /rest/v1.0/companies/{company_id}/pdf_template_configs/{id}/update_default_project | Update a PDF Template Config
[**rest_v10_companies_company_id_pdf_template_configs_post**](PDFsPDFTemplateConfigsPDFTemplateConfigsApi.md#rest_v10_companies_company_id_pdf_template_configs_post) | **POST** /rest/v1.0/companies/{company_id}/pdf_template_configs | Create PDF Template Config


# **rest_v10_companies_company_id_pdf_template_configs_get**
> List[RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner] rest_v10_companies_company_id_pdf_template_configs_get(procore_company_id, company_id, page=page, per_page=per_page, filters_record_generic_tool_id=filters_record_generic_tool_id, filters_project_id=filters_project_id, filters_template_name=filters_template_name, filters_only_parent=filters_only_parent, scope=scope)

List PDF template configs

Returns a list of PDF template configs

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_pdf_template_configs_get200_response_inner import RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner
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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_record_generic_tool_id = 56 # int | Return item(s) with the specified Generic Tool ID. (optional)
    filters_project_id = 56 # int | Return item(s) with the Project ID. (optional)
    filters_template_name = 'filters_template_name_example' # str | Return item(s) with provided template_name. (optional)
    filters_only_parent = True # bool | Return only parent records. (optional)
    scope = 'scope_example' # str | Return only scoped records. (optional)

    try:
        # List PDF template configs
        api_response = api_instance.rest_v10_companies_company_id_pdf_template_configs_get(procore_company_id, company_id, page=page, per_page=per_page, filters_record_generic_tool_id=filters_record_generic_tool_id, filters_project_id=filters_project_id, filters_template_name=filters_template_name, filters_only_parent=filters_only_parent, scope=scope)
        print("The response of PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_record_generic_tool_id** | **int**| Return item(s) with the specified Generic Tool ID. | [optional] 
 **filters_project_id** | **int**| Return item(s) with the Project ID. | [optional] 
 **filters_template_name** | **str**| Return item(s) with provided template_name. | [optional] 
 **filters_only_parent** | **bool**| Return only parent records. | [optional] 
 **scope** | **str**| Return only scoped records. | [optional] 

### Return type

[**List[RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner]**](RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_pdf_template_configs_id_delete**
> rest_v10_companies_company_id_pdf_template_configs_id_delete(procore_company_id, company_id, id)

Delete PDF Template Config

Delete PDF Template Config

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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | PDF Template Configs ID

    try:
        # Delete PDF Template Config
        api_instance.rest_v10_companies_company_id_pdf_template_configs_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| PDF Template Configs ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_pdf_template_configs_id_get**
> RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner rest_v10_companies_company_id_pdf_template_configs_id_get(procore_company_id, company_id, id)

Return a PDF Template Config

Return a PDF Template Config

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_pdf_template_configs_get200_response_inner import RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner
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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | PDF Template Configs ID

    try:
        # Return a PDF Template Config
        api_response = api_instance.rest_v10_companies_company_id_pdf_template_configs_id_get(procore_company_id, company_id, id)
        print("The response of PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| PDF Template Configs ID | 

### Return type

[**RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner**](RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner.md)

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

# **rest_v10_companies_company_id_pdf_template_configs_id_patch**
> RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner rest_v10_companies_company_id_pdf_template_configs_id_patch(procore_company_id, company_id, id, body49)

Update a PDF Template Config

Update a PDF Template Config

### Example


```python
import procore_sdk
from procore_sdk.models.body49 import Body49
from procore_sdk.models.rest_v10_companies_company_id_pdf_template_configs_get200_response_inner import RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner
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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | PDF Template Configs ID
    body49 = procore_sdk.Body49() # Body49 | 

    try:
        # Update a PDF Template Config
        api_response = api_instance.rest_v10_companies_company_id_pdf_template_configs_id_patch(procore_company_id, company_id, id, body49)
        print("The response of PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| PDF Template Configs ID | 
 **body49** | [**Body49**](Body49.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner**](RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch**
> RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch(procore_company_id, company_id, id, body49)

Update a PDF Template Config

Update a PDF Template Config

### Example


```python
import procore_sdk
from procore_sdk.models.body49 import Body49
from procore_sdk.models.rest_v10_companies_company_id_pdf_template_configs_get200_response_inner import RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner
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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the PDF Template Config
    body49 = procore_sdk.Body49() # Body49 | 

    try:
        # Update a PDF Template Config
        api_response = api_instance.rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch(procore_company_id, company_id, id, body49)
        print("The response of PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_id_update_default_project_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the PDF Template Config | 
 **body49** | [**Body49**](Body49.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner**](RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_pdf_template_configs_post**
> RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner rest_v10_companies_company_id_pdf_template_configs_post(procore_company_id, company_id, body49)

Create PDF Template Config

Create new PDF Template Config for a specified company

### Example


```python
import procore_sdk
from procore_sdk.models.body49 import Body49
from procore_sdk.models.rest_v10_companies_company_id_pdf_template_configs_get200_response_inner import RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner
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
    api_instance = procore_sdk.PDFsPDFTemplateConfigsPDFTemplateConfigsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body49 = procore_sdk.Body49() # Body49 | 

    try:
        # Create PDF Template Config
        api_response = api_instance.rest_v10_companies_company_id_pdf_template_configs_post(procore_company_id, company_id, body49)
        print("The response of PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsPDFTemplateConfigsPDFTemplateConfigsApi->rest_v10_companies_company_id_pdf_template_configs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body49** | [**Body49**](Body49.md)|  | 

### Return type

[**RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner**](RestV10CompaniesCompanyIdPdfTemplateConfigsGet200ResponseInner.md)

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

