# procore_sdk.QualitySafetyFormsFormsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_forms_get**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_forms_get) | **GET** /rest/v1.0/projects/{project_id}/forms | List Forms on a project
[**rest_v10_projects_project_id_forms_id_delete**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_forms_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/forms/{id} | Delete Form
[**rest_v10_projects_project_id_forms_id_get**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_forms_id_get) | **GET** /rest/v1.0/projects/{project_id}/forms/{id} | Show Form
[**rest_v10_projects_project_id_forms_id_patch**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_forms_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/forms/{id} | Update Form
[**rest_v10_projects_project_id_forms_post**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_forms_post) | **POST** /rest/v1.0/projects/{project_id}/forms | Create Form
[**rest_v10_projects_project_id_recycle_bin_forms_get**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_recycle_bin_forms_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/forms | List Recycled Project Forms
[**rest_v10_projects_project_id_recycle_bin_forms_id_get**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_recycle_bin_forms_id_get) | **GET** /rest/v1.0/projects/{project_id}/recycle_bin/forms/{id} | Show Recycled Project Form
[**rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch**](QualitySafetyFormsFormsApi.md#rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch) | **PATCH** /rest/v1.0/projects/{project_id}/recycle_bin/forms/{id}/restore | Restore Project Form
[**rest_v11_projects_project_id_forms_get**](QualitySafetyFormsFormsApi.md#rest_v11_projects_project_id_forms_get) | **GET** /rest/v1.1/projects/{project_id}/forms | List Forms on a project


# **rest_v10_projects_project_id_forms_get**
> List[RestV11ProjectsProjectIdFormsGet200ResponseInner] rest_v10_projects_project_id_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_form_template_id=filters_form_template_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, sort=sort)

List Forms on a project

Return a list of all Forms from a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_form_template_id = [56] # List[int] | Array of Form Template IDs. Return item(s) associated with the specified Form Template IDs. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Forms on a project
        api_response = api_instance.rest_v10_projects_project_id_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_form_template_id=filters_form_template_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_form_template_id** | [**List[int]**](int.md)| Array of Form Template IDs. Return item(s) associated with the specified Form Template IDs. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdFormsGet200ResponseInner]**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Forms listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_forms_id_delete**
> rest_v10_projects_project_id_forms_id_delete(procore_company_id, project_id, id)

Delete Form

Delete the specified Form.

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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Form ID

    try:
        # Delete Form
        api_instance.rest_v10_projects_project_id_forms_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Form ID | 

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
**200** | Form deleted successfully |  -  |
**403** | User does not have permission to delete Form |  -  |
**404** | Form not found |  -  |
**500** | Error deleting Form |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_forms_id_get**
> RestV11ProjectsProjectIdFormsGet200ResponseInner rest_v10_projects_project_id_forms_id_get(procore_company_id, project_id, id)

Show Form

Return detailed information on the specified Form.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Form ID

    try:
        # Show Form
        api_response = api_instance.rest_v10_projects_project_id_forms_id_get(procore_company_id, project_id, id)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Form ID | 

### Return type

[**RestV11ProjectsProjectIdFormsGet200ResponseInner**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form shown successfully |  -  |
**403** | User does not have permission to view Form |  -  |
**404** | Form not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_forms_id_patch**
> RestV11ProjectsProjectIdFormsGet200ResponseInner rest_v10_projects_project_id_forms_id_patch(procore_company_id, project_id, id, body83, send_emails=send_emails)

Update Form

Update the specified Form.

### Example


```python
import procore_sdk
from procore_sdk.models.body83 import Body83
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Form ID
    body83 = procore_sdk.Body83() # Body83 | 
    send_emails = True # bool | Designates whether or not emails will be sent (default false) (optional)

    try:
        # Update Form
        api_response = api_instance.rest_v10_projects_project_id_forms_id_patch(procore_company_id, project_id, id, body83, send_emails=send_emails)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Form ID | 
 **body83** | [**Body83**](Body83.md)|  | 
 **send_emails** | **bool**| Designates whether or not emails will be sent (default false) | [optional] 

### Return type

[**RestV11ProjectsProjectIdFormsGet200ResponseInner**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form updated successfully |  -  |
**400** | Error updating Form |  -  |
**403** | User does not have permission to update Form |  -  |
**404** | Form not found |  -  |
**422** | Error updating Form |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_forms_post**
> RestV11ProjectsProjectIdFormsGet200ResponseInner rest_v10_projects_project_id_forms_post(procore_company_id, project_id, body81)

Create Form

Create a new Form associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body81 import Body81
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body81 = procore_sdk.Body81() # Body81 | 

    try:
        # Create Form
        api_response = api_instance.rest_v10_projects_project_id_forms_post(procore_company_id, project_id, body81)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_forms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body81** | [**Body81**](Body81.md)|  | 

### Return type

[**RestV11ProjectsProjectIdFormsGet200ResponseInner**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Form created successfully |  -  |
**400** | Error updating Form |  -  |
**403** | User does not have permission to create Form |  -  |
**422** | Error creating Form |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_forms_get**
> List[RestV11ProjectsProjectIdFormsGet200ResponseInner] rest_v10_projects_project_id_recycle_bin_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)

List Recycled Project Forms

Returns a collection of Recycled Forms for a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled Project Forms
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_get: %s\n" % e)
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

[**List[RestV11ProjectsProjectIdFormsGet200ResponseInner]**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

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
**403** | User does not have permission to view Forms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_forms_id_get**
> RestV11ProjectsProjectIdFormsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_forms_id_get(procore_company_id, id, project_id)

Show Recycled Project Form

Returns the details for a specified recycled Project Form

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Project Form ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Recycled Project Form
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_forms_id_get(procore_company_id, id, project_id)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Project Form ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV11ProjectsProjectIdFormsGet200ResponseInner**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

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
**403** | User does not have permission to view the Form |  -  |
**404** | Form does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch**
> RestV11ProjectsProjectIdFormsGet200ResponseInner rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch(procore_company_id, id, project_id)

Restore Project Form

Restores the specified Form from Recycle Bin.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Project Form ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Restore Project Form
        api_response = api_instance.rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch(procore_company_id, id, project_id)
        print("The response of QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v10_projects_project_id_recycle_bin_forms_id_restore_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Project Form ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV11ProjectsProjectIdFormsGet200ResponseInner**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_projects_project_id_forms_get**
> List[RestV11ProjectsProjectIdFormsGet200ResponseInner] rest_v11_projects_project_id_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_form_template_id=filters_form_template_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, sort=sort)

List Forms on a project

Return a list of all Forms from a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_projects_project_id_forms_get200_response_inner import RestV11ProjectsProjectIdFormsGet200ResponseInner
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
    api_instance = procore_sdk.QualitySafetyFormsFormsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_created_by_id = [56] # List[int] | Returns item(s) created by the specified User IDs. (optional)
    filters_form_template_id = [56] # List[int] | Array of Form Template IDs. Return item(s) associated with the specified Form Template IDs. (optional)
    filters_search = 'filters_search_example' # str | Returns item(s) matching the specified search query string. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List Forms on a project
        api_response = api_instance.rest_v11_projects_project_id_forms_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_created_by_id=filters_created_by_id, filters_form_template_id=filters_form_template_id, filters_search=filters_search, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, sort=sort)
        print("The response of QualitySafetyFormsFormsApi->rest_v11_projects_project_id_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyFormsFormsApi->rest_v11_projects_project_id_forms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_created_by_id** | [**List[int]**](int.md)| Returns item(s) created by the specified User IDs. | [optional] 
 **filters_form_template_id** | [**List[int]**](int.md)| Array of Form Template IDs. Return item(s) associated with the specified Form Template IDs. | [optional] 
 **filters_search** | **str**| Returns item(s) matching the specified search query string. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**List[RestV11ProjectsProjectIdFormsGet200ResponseInner]**](RestV11ProjectsProjectIdFormsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Forms listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

