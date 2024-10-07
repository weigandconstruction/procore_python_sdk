# procore_sdk.QualitySafetyFormsFormTemplatesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_form_templates_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_form_templates_get) | **GET** /rest/v1.0/companies/{company_id}/form_templates | List Company Form Templates
[**rest_v10_companies_company_id_form_templates_id_delete**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_form_templates_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/form_templates/{id} | Delete Company Form Template
[**rest_v10_companies_company_id_form_templates_id_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_form_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/form_templates/{id} | Show Company Form Template
[**rest_v10_companies_company_id_form_templates_id_patch**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_form_templates_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/form_templates/{id} | Update Company Form Template
[**rest_v10_companies_company_id_form_templates_post**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_form_templates_post) | **POST** /rest/v1.0/companies/{company_id}/form_templates | Create Company Form Template
[**rest_v10_companies_company_id_recycle_bin_form_templates_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_form_templates_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/form_templates | List Recycled Company Form Templates
[**rest_v10_companies_company_id_recycle_bin_form_templates_id_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_form_templates_id_get) | **GET** /rest/v1.0/companies/{company_id}/recycle_bin/form_templates/{id} | Show Recycled Company Form Template
[**rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch) | **PATCH** /rest/v1.0/companies/{company_id}/recycle_bin/form_templates/{id}/restore | Restore Company Form Template
[**rest_v10_projects_project_id_form_templates_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_projects_project_id_form_templates_get) | **GET** /rest/v1.0/projects/{project_id}/form_templates | List Company Form Templates from Project
[**rest_v10_projects_project_id_form_templates_id_get**](QualitySafetyFormsFormTemplatesApi.md#rest_v10_projects_project_id_form_templates_id_get) | **GET** /rest/v1.0/projects/{project_id}/form_templates/{id} | Show Company Form Template from Project


# **rest_v10_companies_company_id_form_templates_get**
> List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner] rest_v10_companies_company_id_form_templates_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)

List Company Form Templates

Returns a collection of Form Templates for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Company Form Templates
        api_response = api_instance.rest_v10_companies_company_id_form_templates_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

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
**403** | User does not have permission to view Form Templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_form_templates_id_delete**
> rest_v10_companies_company_id_form_templates_id_delete(procore_company_id, id, company_id)

Delete Company Form Template

Delete a Company Form Template

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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Delete Company Form Template
        api_instance.rest_v10_companies_company_id_form_templates_id_delete(procore_company_id, id, company_id)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
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
**204** | Form Template deleted successfully |  -  |
**403** | User does not have permission to delete the Form Template |  -  |
**404** | Form Template does not exist |  -  |
**422** | Error deleting Form Template |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_form_templates_id_get**
> RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner rest_v10_companies_company_id_form_templates_id_get(procore_company_id, id, company_id)

Show Company Form Template

Returns the details for a specified Company Form Template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Company Form Template
        api_response = api_instance.rest_v10_companies_company_id_form_templates_id_get(procore_company_id, id, company_id)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

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
**403** | User does not have permission to view the Form Template |  -  |
**404** | Form Template does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_form_templates_id_patch**
> RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner rest_v10_companies_company_id_form_templates_id_patch(procore_company_id, id, company_id, body86)

Update Company Form Template

Update a Company Form Template

### Example


```python
import procore_sdk
from procore_sdk.models.body86 import Body86
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    company_id = 56 # int | Unique identifier for the company.
    body86 = procore_sdk.Body86() # Body86 | 

    try:
        # Update Company Form Template
        api_response = api_instance.rest_v10_companies_company_id_form_templates_id_patch(procore_company_id, id, company_id, body86)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body86** | [**Body86**](Body86.md)|  | 

### Return type

[**RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form Template updated successfully |  -  |
**403** | User does not have permission to update the Form Template |  -  |
**404** | Form Template does not exist |  -  |
**422** | Error updating Form Template |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_form_templates_post**
> RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner rest_v10_companies_company_id_form_templates_post(procore_company_id, company_id, form_template, fillable_pdf)

Create Company Form Template

Create a new Company Form Template

### Example


```python
import procore_sdk
from procore_sdk.models.form_template import FormTemplate
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    form_template = procore_sdk.FormTemplate() # FormTemplate | 
    fillable_pdf = None # bytearray | Form Template's Fillable PDF. To upload a fillable PDF you must upload the entire payload as `multipart/form-data` content-type and specify each parameter as form-data together with `fillable_pdf` as files.

    try:
        # Create Company Form Template
        api_response = api_instance.rest_v10_companies_company_id_form_templates_post(procore_company_id, company_id, form_template, fillable_pdf)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_form_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **form_template** | [**FormTemplate**](FormTemplate.md)|  | 
 **fillable_pdf** | **bytearray**| Form Template&#39;s Fillable PDF. To upload a fillable PDF you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;fillable_pdf&#x60; as files. | 

### Return type

[**RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Form Template created successfully |  -  |
**403** | User does not have permission to create a Form Template |  -  |
**422** | Error creating Form Template |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_recycle_bin_form_templates_get**
> List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner] rest_v10_companies_company_id_recycle_bin_form_templates_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)

List Recycled Company Form Templates

Returns a collection of Recycled Form Templates for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Company Form Templates
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_form_templates_get(procore_company_id, company_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_recycle_bin_form_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_recycle_bin_form_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  |
**401** | Unauthorized |  -  |
**403** | User does not have permission to view Form Templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_recycle_bin_form_templates_id_get**
> RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner rest_v10_companies_company_id_recycle_bin_form_templates_id_get(procore_company_id, id, company_id)

Show Recycled Company Form Template

Returns the details for a specified recycled Company Form Template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Show Recycled Company Form Template
        api_response = api_instance.rest_v10_companies_company_id_recycle_bin_form_templates_id_get(procore_company_id, id, company_id)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_recycle_bin_form_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_recycle_bin_form_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
 **company_id** | **int**| Unique identifier for the company. | 

### Return type

[**RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

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
**403** | User does not have permission to view the Form Template |  -  |
**404** | Form Template does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch**
> rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch(procore_company_id, id, company_id)

Restore Company Form Template

Restores the specified Form Template from Recycle Bin.

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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    company_id = 56 # int | Unique identifier for the company.

    try:
        # Restore Company Form Template
        api_instance.rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch(procore_company_id, id, company_id)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_form_templates_get**
> List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner] rest_v10_projects_project_id_form_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)

List Company Form Templates from Project

Returns a collection of Company Form Templates for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Company Form Templates from Project
        api_response = api_instance.rest_v10_projects_project_id_form_templates_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_projects_project_id_form_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_projects_project_id_form_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner]**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

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
**403** | User does not have permission to view Form Templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_form_templates_id_get**
> RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner rest_v10_projects_project_id_form_templates_id_get(procore_company_id, id, project_id)

Show Company Form Template from Project

Returns the details for a specified Company Form Template

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_form_templates_get200_response_inner import RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormTemplatesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Company Form Template ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Company Form Template from Project
        api_response = api_instance.rest_v10_projects_project_id_form_templates_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyFormsFormTemplatesApi->rest_v10_projects_project_id_form_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormTemplatesApi->rest_v10_projects_project_id_form_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Company Form Template ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner**](RestV10ProjectsProjectIdFormTemplatesGet200ResponseInner.md)

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
**403** | User does not have permission to view the Form Template |  -  |
**404** | Form Template does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

